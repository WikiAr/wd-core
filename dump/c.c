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
ect_length(props);
            for (int i = 0; i < num_props; i++) {
                json_object* prop = json_object_array_get_idx(props, i);
                const char* id = json_object_get_string(json_object_object_get(prop, "id"));
                int count = json_object_get_int(json_object_object_get(prop, "count"));
                if (tab.main_table == NULL) {
                    tab.main_table = malloc(sizeof(struct Main_Table));
                    tab.main_table->P31 = malloc(strlen(key) + 1);
                    strcpy(tab.main_table->P31, key);
                    tab.main_table->props = malloc(sizeof(struct Property));
                    tab.main_table->props->id = malloc(strlen(id) + 1);
                    strcpy(tab.main_table->props->id, id);
                    tab.main_table->props->count = count;
                    tab.main_table->length_of_usage = 1;
                    tab.main_table->length_of_claims_for_property = 1;
                } else {
                    int found = 0;
                    for (int j = 0; j < tab.len_of_all_properties; j++) {
                        if (strcmp(tab.main_table[j].P31, key) == 0) {
                            found = 1;
                            tab.main_table[j].length_of_usage += 1;
                            tab.main_table[j].length_of_claims_for_property += 1;
                            int found_prop = 0;
                            for (int k = 0; k < tab.main_table[j].length_of_claims_for_property; k++) {
                                if (strcmp(tab.main_table[j].props[k].id, id) == 0) {
                                    found_prop = 1;
                                    tab.main_table[j].props[k].count += count;
                                    break;
                                }
                            }
                            if (!found_prop) {
                                tab.main_table[j].props = realloc(tab.main_table[j].props, (tab.main_table[j].length_of_claims_for_property + 1) * sizeof(struct Property));
                                tab.main_table[j].props[tab.main_table[j].length_of_claims_for_property].id = malloc(strlen(id) + 1);
                                strcpy(tab.main_table[j].props[tab.main_table[j].length_of_claims_for_property].id, id);
                                tab.main_table[j].props[tab.main_table[j].length_of_claims_for_property].count = count;
                                tab.main_table[j].length_of_claims_for_property += 1;
                            }
                            break;
                        }
                    }
                    if (!found) {
                        tab.main_table = realloc(tab.main_table, (tab.len_of_all_properties + 1) * sizeof(struct Main_Table));
                        tab.main_table[tab.len_of_all_properties].P31 = malloc(strlen(key) + 1);
                        strcpy(tab.main_table[tab.len_of_all_properties].P31, key);
                        tab.main_table[tab.len_of_all_properties].props = malloc(sizeof(struct Property));
                        tab.main_table[tab.len_of_all_properties].props->id = malloc(strlen(id) + 1);
                        strcpy(tab.main_table[tab.len_of_all_properties].props->id, id);
                        tab.main_table[tab.len_of_all_properties].props->count = count;
                        tab.main_table[tab.len_of_all_properties].length_of_usage = 1;
                        tab.main_table[tab.len_of_all_properties].length_of_claims_for_property = 1;
                        tab.len_of_all_properties += 1;
                    }
                }
            }
        }
        tab.done = done;
    }
    fclose(fileeee);
    FILE* outfile = fopen(jsonname, "w");
    json_object* json_tab = json_object_new_object();
    json_object_object_add(json_tab, "done", json_object_new_int(tab.done));
    json_object_object_add(json_tab, "len_of_all_properties", json_object_new_int(tab.len_of_all_properties));
    json_object_object_add(json_tab, "items_0_claims", json_object_new_int(tab.items_0_claims));
    json_object_object_add(json_tab, "items_1_claims", json_object_new_int(tab.items_1_claims));
    json_object_object_add(json_tab, "items_no_P31", json_object_new_int(tab.items_no_P31));
    json_object_object_add(json_tab, "All_items", json_object_new_int(tab.All_items));
    json_object_object_add(json_tab, "all_claims_2020", json_object_new_int(tab.all_claims_2020));
    json_object* json_main_table = json_object_new_array();
    for (int i = 0; i < tab.len_of_all_properties; i++) {
        json_object* json_main_table_entry = json_object_new_object();
        json_object_object_add(json_main_table_entry, "P31", json_object_new_string(tab.main_table[i].P31));
        json_object* json_props = json_object_new_array();
        for (int j = 0; j < tab.main_table[i].length_of_claims_for_property; j++) {
            json_object* json_prop = json_object_new_object();
            json_object_object_add(json_prop, "id", json_object_new_string(tab.main_table[i].props[j].id));
            json_object_object_add(json_prop, "count", json_object_new_int(tab.main_table[i].props[j].count));
            json_object_array_add(json_props, json_prop);
        }
        json_object_object_add(json_main_table_entry, "props", json_props);
        json_object_object_add(json_main_table_entry, "length_of_usage", json_object_new_int(tab.main_table[i].length_of_usage));
        json_object_object_add(json_main_table_entry, "length_of_claims_for_property", json_object_new_int(tab.main_table[i].length_of_claims_for_property));
        json_object_array_add(json_main_table, json_main_table_entry);
    }
    json_object_object_add(json_tab, "Main_Table", json_main_table);
    fprintf(outfile, "%s", json_object_to_json_string(json_tab));
    fclose(outfile);
}

int main() {
    workondata();
    return 0;
