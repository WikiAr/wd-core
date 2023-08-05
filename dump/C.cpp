#include <iostream>
#include <fstream>
#include <string>
#include <map>
#include <json/json.h>
#include <bzlib.h>
#include <ctime>

std::string jsonname = "dumps/claims.json";
std::map<std::string, int> tab = {
    {"done", 0},
    {"len_of_all_properties", 0},
    {"items_0_claims", 0},
    {"items_1_claims", 0},
    {"items_no_P31", 0},
    {"All_items", 0},
    {"all_claims_2020", 0},
};
void workondata()
{
    std::time_t t1 = std::time(nullptr);
    std::string filename = "/mnt/nfs/dumps-clouddumps1002.wikimedia.org/other/wikibase/wikidatawiki/latest-all.json.bz2";
    if (!std::ifstream(filename))
    {
        std::cout << "file " << filename << " not found" << std::endl;
        return;
    }
    BZFILE *fileeee = BZ2_bzopen(filename.c_str(), "r");
    char line[4096];
    int done = 0;
    while (BZ2_bzread(fileeee, line, sizeof(line)) > 0)
    {
        std::string lineStr(line);
        lineStr = lineStr.substr(0, lineStr.find_last_not_of("\n") + 1);
        if (!lineStr.starts_with("{") || !lineStr.ends_with("}"))
        {
            continue;
        }
        tab["All_items"] += 1;
        Json::Value json1;
        Json::Reader reader;
        reader.parse(lineStr, json1);
        Json::Value claimse = json1.get("claims", Json::Value());
        if (claimse.size() == 0)
        {
            tab["items_0_claims"] += 1;
            continue;
        }
        if (claimse.size() == 1)
        {
            tab["items_1_claims"] += 1;
        }
        if (!claimse.isMember("P31"))
        {
            tab["items_no_P31"] += 1;
            continue;
        }
        Json::Value claims_to_work = claimse.getMemberNames();
        for (const std::string &P31 : claims_to_work)
        {
            if (!tab["Main_Table"].count(P31))
            {
                tab["Main_Table"][P31] = 0;
            }
        }
    }
    BZ2_bzclose(fileeee);
}
