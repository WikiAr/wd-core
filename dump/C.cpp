#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <unordered_map>
#include <json/json.h>
#include <ctime>

std::string jsonname = "dumps/claims.json";

std::unordered_map<std::string, int> tab = {
    {"done", 0},
    {"len_of_all_properties", 0},
    {"items_0_claims", 0},
    {"items_1_claims", 0},
    {"items_no_P31", 0},
    {"All_items", 0},
    {"all_claims_2020", 0},
};

void workondata() {
    std::clock_t t1 = std::clock();
    std::string filename = "/mnt/nfs/dumps-clouddumps1002.wikimedia.org/other/wikibase/wikidatawiki/latest-all.json.bz2";
    if (!std::ifstream(filename)) {
        std::cout << "file " << filename << " not found" << std::endl;
        return;
    }
    std::ifstream fileeee(filename, std::ios::binary);
    std::string line;

    int done = 0;

    while (std::getline(fileeee, line)) {
        line = line.substr(0, line.size() - 1);

        if (line[0] != '{' || line[line.size() - 1] != '}') {
            continue;
        }

        tab["All_items"] += 1;

        Json::Value json1;
        Json::Reader reader;
        reader.parse(line, json1);
        Json::Value claimse = json1["claims"];

        if (claimse.size() == 0) {
            tab["items_0_claims"] += 1;
            continue;
        }

        if (claimse.size() == 1) {
            tab["items_1_claims"] += 1;
        }

        if (!claimse.isMember("P31")) {
            tab["items_no_P31"] += 1;
            continue;
        }

        Json::Value claims_to_work = claimse.getMemberNames();

        for (const auto& P31 : claims_to_work) {
            if (tab["Main_Table"].find(P31.asString()) == tab["Main_Table"].end()) {
                tab["Main_Table"][P31.asString()] = {
                    {"props", {}},
                    {"lenth_of_usage", 0},
                    {"lenth_of_claims_for_property", 0},
                };
            }

            tab["Main_Table"][P31.asString()]["lenth_of_usage"] += 1;
            tab["all_claims_2020"] += claimse[P31].size();

            for (const auto& claim : claimse[P31]) {
                tab["Main_Table"][P31.asString()]["lenth_of_claims_for_property"] += 1;

                Json::Value datavalue = claim["mainsnak"]["datavalue"];
                std::string ttype = datavalue["type"].asString();

                if (ttype == "wikibase-entityid") {
                    std::string idd = datavalue["value"]["id"].asString();
                    if (idd != "") {
                        if (tab["Main_Table"][P31.asString()]["props"].find(idd) == tab["Main_Table"][P31.asString()]["props"].end()) {
                            tab["Main_Table"][P31.asString()]["props"][idd] = 0;
                        }
                        tab["Main_Table"][P31.asString()]["props"][idd] += 1;
                    }
                }
            }
        }

        tab["done"] = done;
    }

    std::ofstream outfile(jsonname);
    outfile << tab;
    outfile.close();
}
