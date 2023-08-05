#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <bzlib.h>
#include <json-c/json.h>
#include <time.h>

#define MAX_LINE_LENGTH 1000

char* jsonname = "dumps/claims.json";

struct Table {
    int done;
    int len_of_all_properties;
    int items_0_claims;
    int items_1_claims;
    int items_no_P31;
    int All_items;
    int all_claims_2020;
    struct MainTable* main_table;
};

struct MainTable {
    struct Property* props;
    int length_of_usage;
    int length_of_claims_for_property;
};

struct Property {
    int count;
};

void workondata() {
    struct Table tab;
    tab.done = 0;
    tab.len_of_all_properties = 0;
    tab.items_0_claims = 0;
    tab.items_1_claims = 0;
    tab.items_no_P31 = 0;
    tab.All_items = 0;
    tab.all_claims_2020 = 0;
    tab.main_table = NULL;

    struct json_object* json;
    struct json_object* claims;
    struct json_object* claimse;
    struct json_object* mainsnak;
    struct json_object* datavalue;
    struct json_object* value;
    struct json_object* idd;

    char line[MAX_LINE_LENGTH];
    FILE* fileeee;
    const char* filename = "/mnt/nfs/dumps-clouddumps1002.wikimedia.org/other/wikibase/wikidatawiki/latest-all.json.bz2";
    if (!(fileeee = fopen(filename, "r"))) {
        printf("file %s <<lightred>> not found\n", filename);
        return;
    }

    while (fgets(line, MAX_LINE_LENGTH, fileeee)) {
        line[strcspn(line, "\n")] = 0;

        if (line[0] != '{' || line[strlen(line) - 1] != '}') {
            continue;
        }

        tab.All_items++;

        json = json_tokener_parse(line);
        json_object_object_get_ex(json, "claims", &claims);
        claimse = json_object_get_object(claims);

        if (json_object_object_length(claimse) == 0) {
            tab.items_0_claims++;
            continue;
        }

        if (json_object_object_length(claimse) == 1) {
            tab.items_1_claims++;
        }

        if (!json_object_object_get_ex(claimse, "P31", NULL)) {
            tab.items_no_P31++;
            continue;
        }

        json_object_object_foreach(claimse, key, val) {
            struct MainTable* main_table_entry;
            struct Property* prop_entry;

            if (!tab.main_table) {
                tab.main_table = malloc(sizeof(struct MainTable));
                tab.main_table->props = NULL;
                tab.main_table->length_of_usage = 0;
                tab.main_table->length_of_claims_for_property = 0;
            }

            if (!json_object_object_get_ex(tab.main_table, key, NULL)) {
                main_table_entry = malloc(sizeof(struct MainTable));
                main_table_entry->props = NULL;
                main_table_entry->length_of_usage = 0;
                main_table_entry->length_of_claims_for_property = 0;
                json_object_object_add(tab.main_table, key, main_table_entry);
            } else {
                main_table_entry = json_object_get_object(json_object_object_get(tab.main_table, key));
            }

            main_table_entry->length_of_usage++;
            tab.all_claims_2020 += json_object_array_length(val);

            json_object_array_foreach(val, idx, claim) {
                main_table_entry->length_of_claims_for_property++;

                json_object_object_get_ex(claim, "mainsnak", &mainsnak);
                json_object_object_get_ex(mainsnak, "datavalue", &datavalue);
                json_object_object_get_ex(datavalue, "type", &value);

                if (strcmp(json_object_get_string(value), "wikibase-entityid") == 0) {
                    json_object_object_get_ex(datavalue, "value", &value);
                    json_object_object_get_ex(value, "id", &idd);
                    const char* id_str = json_object_get_string(idd);

                    if (!json_object_object_get_ex(main_table_entry->props, id_str, NULL)) {
                        prop_entry = malloc(sizeof(struct Property));
                        prop_entry->count = 0;
                        json_object_object_add(main_table_entry->props, id_str, prop_entry);
                    } else {
                        prop_entry = json_object_get_object(json_object_object_get(main_table_entry->props, id_str));
                    }

                    prop_entry->count++;
                }
            }
        }

        tab.done++;
    }

    fclose(fileeee);

    FILE* outfile = fopen(jsonname, "w");
    if (outfile) {
        json_object_to_file_ext(jsonname, tab.main_table, JSON_C_TO_STRING_PRETTY);
        fclose(outfile);
    }

    free(tab.main_table);
}

int main() {
    workondata();
    return 0;
}
