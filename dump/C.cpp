#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <unordered_map>
#include <boost/filesystem.hpp>
#include <bzlib.h>
#include <nlohmann/json.hpp>

using json = nlohmann::json;

std::string filename = "/mnt/nfs/dumps-clouddumps1002.wikimedia.org/other/wikibase/wikidatawiki/latest-all.json.bz2";
std::string jsonname = "dumps/claims.json";

struct Property {
    std::unordered_map<std::string, int> props;
    int length_of_usage = 0;
    int length_of_claims_for_property = 0;
};

std::unordered_map<std::string, Property> Main_Table;
int done = 0;
int len_of_all_properties = 0;
int items_0_claims = 0;
int items_1_claims = 0;
int items_no_P31 = 0;
int All_items = 0;
int all_claims_2020 = 0;

void workondata() {
    if (!boost::filesystem::exists(filename)) {
        std::cout << "File " << filename << " not found" << std::endl;
        return;
    }

    FILE* file = fopen(filename.c_str(), "rb");
    int bzerror;
    BZFILE* bzf = BZ2_bzReadOpen(&bzerror, file, 0, 0, NULL, 0);
    char buf[4096];

    while (BZ2_bzRead(&bzerror, bzf, buf, sizeof(buf)) > 0) {
        std::string line(buf);
        line = line.substr(0, line.find_last_not_of(",\n") + 1);

        if (line.front() != '{' || line.back() != '}')
            continue;

        All_items++;

        json json1 = json::parse(line);
        auto claims = json1.value("claims", json::object());

        if (claims.empty()) {
            items_0_claims++;
            continue;
        }

        if (claims.size() == 1)
            items_1_claims++;

        if (claims.find("P31") == claims.end()) {
            items_no_P31++;
            continue;
        }

        for (auto& [P31, claim_array] : claims.items()) {
            if (Main_Table.find(P31) == Main_Table.end())
                Main_Table[P31] = Property();

            Main_Table[P31].length_of_usage++;
            all_claims_2020 += claim_array.size();

            for (auto& claim : claim_array) {
                Main_Table[P31].length_of_claims_for_property++;

                auto datavalue = claim.value("mainsnak", json::object()).value("datavalue", json::object());
                auto ttype = datavalue.value("type", "");

                if (ttype == "wikibase-entityid") {
                    auto idd = datavalue.value("value", json::object()).value("id", "");
                    if (!idd.empty()) {
                        Main_Table[P31].props[idd]++;
                    }
                }
            }
        }

        done++;
    }

    BZ2_bzReadClose(&bzerror, bzf);
    fclose(file);

    json tab = {
        {"done", done},
        {"len_of_all_properties", len_of_all_properties},
        {"items_0_claims", items_0_claims},
        {"items_1_claims", items_1_claims},
        {"items_no_P31", items_no_P31},
        {"All_items", All_items},
        {"all_claims_2020", all_claims_2020},
        {"Main_Table", Main_Table}
    };

    std::ofstream outfile(jsonname);
    outfile << tab.dump(4);
    outfile.close();
}

int main() {
    workondata();
    return 0;
}
