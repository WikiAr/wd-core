#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <map>
#include <boost/iostreams/filtering_streambuf.hpp>
#include <boost/iostreams/copy.hpp>
#include <boost/iostreams/filter/bzip2.hpp>
#include <nlohmann/json.hpp>

std::map<std::string, int> tab = {
    {"done", 0},
    {"len_of_all_properties", 0},
    {"items_0_claims", 0},
    {"items_1_claims", 0},
    {"items_no_P31", 0},
    {"All_items", 0},
    {"all_claims_2020", 0},
    // "Main_Table" will be handled separately
};

std::map<std::string, std::map<std::string, int>> main_table;

int dump_done = 0;

void log_dump() {
    dump_done++;
    std::cout << "log_dump %d done " << dump_done << std::endl;
    // JSON dump will be handled separately
}

void do_claims(nlohmann::json claims) {
    for (auto& el : claims.items()) {
        std::string p = el.key();
        if (main_table.find(p) == main_table.end()) {
            main_table[p] = {{"props", 0}, {"lenth_of_usage", 0}, {"lenth_of_claims_for_property", 0}};
        }

        main_table[p]["lenth_of_usage"]++;

        tab["all_claims_2020"] += claims[p].size();

        for (auto& claim : claims[p]) {
            main_table[p]["lenth_of_claims_for_property"]++;

            auto datavalue = claim["mainsnak"]["datavalue"];
            std::string ttype = datavalue["type"];

            if (ttype == "wikibase-entityid") {
                std::string idd = datavalue["value"]["id"];
                if (!idd.empty()) {
                    if (main_table[p]["props"].find(idd) == main_table[p]["props"].end()) {
                        main_table[p]["props"][idd] = 0;
                    }
                    main_table[p]["props"][idd]++;
                }
            }
        }
    }
}

void read_file() {
    std::string filename = "/mnt/nfs/dumps-clouddumps1002.wikimedia.org/other/wikibase/wikidatawiki/latest-all.json.bz2";

    std::ifstream file(filename, std::ios_base::in | std::ios_base::binary);
    if (!file) {
        std::cerr << "file " << filename << " not found" << std::endl;
        return;
    }

    std::cout << "read file: " << filename << std::endl;

    boost::iostreams::filtering_streambuf<boost::iostreams::input> inbuf;
    inbuf.push(boost::iostreams::bzip2_decompressor());
    inbuf.push(file);

    std::istream instream(&inbuf);
    std::string line;
    while (std::getline(instream, line)) {
        tab["done"]++;

        if (line.front() == '{' && line.back() == '}') {
            tab["All_items"]++;

            auto json1 = nlohmann::json::parse(line);
            auto claims = json1["claims"];

            if (claims.size() == 0) {
                tab["items_0_claims"]++;
            } else {
                if (claims.size() == 1) {
                    tab["items_1_claims"]++;
                }
                if (claims.find("P31") == claims.end()) {
                    tab["items_no_P31"]++;
                }
                do_claims(claims);
            }
        }
    }

    log_dump();
}

int main() {
    read_file();
    return 0;
}