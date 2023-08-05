#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <bzlib.h>
#include <json-c/json.h>
#include <time.h>

#define LIMIT 900000000

char* Dump_Dir;
char* saveto;
int sections_done = 0;
int sections_false = 0;
int dump_done = 0;
char* jsonname;

struct Table {
    int done;
    int len_of_all_properties;
    int items_0_claims;
    int items_1_claims;
    int items_no_P31;
    int All_items;
    int all_claims_2020;
    struct Main_Table* main_table;
};

struct Main_Table {
    char* P31;
    struct Property* props;
    int length_of_usage;
    int length_of_claims_for_property;
};

struct Property {
    char* id;
    int count;
};

void workondata() {
    time_t t1;
    time(&t1);
    int diff = 20000;
    if (strstr("test", "test") != NULL) {
        diff = 1000;
    }
    char* filename = "/mnt/nfs/dumps-clouddumps1002.wikimedia.org/other/wikibase/wikidatawiki/latest-all.json.bz2";
    if (access(filename, F_OK) == -1) {
        printf("file %s not found\n", filename);
        return;
    }
    FILE* fileeee = fopen(filename, "r");
    int done2 = 0;
    int done = 0;
    int offset = 0;
    if (tab.done != 0) {
        offset = tab.done;
        printf("offset == %d\n", offset);
    }
    char line[1000];
    while (fgets(line, sizeof(line), fileeee)) {
        line[strcspn(line, "\n")] = 0;
        done += 1;
        if (offset != 0 && done < offset) {
            continue;
        }
        if (done % diff == 0 || done == 1000) {
            printf("%d : %f.\n", done, difftime(time(NULL), t1));
            time(&t1);
        }
        if (done2 == 5000000) {
            done2 = 1;
            log_dump();
        }
        if (tab.done > LIMIT) {
            break;
        }
        if (line[0] != '{' || line[strlen(line) - 1] != '}') {
            continue;
        }
        done2 += 1;
        tab.All_items += 1;
        if (strstr("printline", "printline") != NULL && tab.done % 1000 == 0) {
            printf("%s\n", line);
        }
        json_object* json1 = json_tokener_parse(line);
        json_object* claims = json_object_object_get(json1, "claims");
        int num_claims = json_object_object_length(claims);
        if (num_claims == 0) {
            tab.items_0_claims += 1;
            continue;
        }
        if (num_claims == 1) {
            tab.items_1_claims += 1;
        }
        json_object* P31 = json_object_object_get(claims, "P31");
        if (P31 == NULL) {
            tab.items_no_P31 += 1;
            continue;
        }
        json_object_object_foreach(claims, key, val) {
            if (strcmp(key, "P31") != 0) {
                continue;
            }
            json_object* props = json_object_object_get(val, "props");
            int num_props = json_object_object_length(props);
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
