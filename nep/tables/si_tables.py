"""
from nep.tables.si_tables import genders, MainTestTable, new_types, offsetbg, Qids_translate, Add_en_labels, Geo_List
"""
import sys
from des.places import placesTable
from desc_dicts.descraptions import DescraptionsTable, Qid_Descraptions
from desc_dicts.scientific_article_desc import Scientific_descraptions
from nep.tables.lists import others_list

# ---
genders = {
    "Q6581097": "male",
    "Q2449503": "male",  # transgender male
    "Q6581072": "female",
    "Q1052281": "female",  # transgender female
}
# ---
MainTestTable = {1: False}
# ---
new_types = {}
# ---
offsetbg = {1: 0}
# ---
for arg in sys.argv:
    # ---
    arg, _, value = arg.partition(":")
    # ---
    if arg.startswith("-"):
        arg = arg[1:]
    # ---
    if arg.lower() in ["offset", "off"]:
        print(f"offsetbg[1] = int({value})")
        offsetbg[1] = int(value)
# ---
Qids_translate = {
    "Q13442814 ": Scientific_descraptions,
    "Q21014462": DescraptionsTable["cell line"],
    "Q11173": DescraptionsTable["chemical compound"],
    # 'Q101352' : DescraptionsTable['family name'], # family name
    "Q3409032": DescraptionsTable["unisex given name"],
    "Q11879590": DescraptionsTable["female given name"],
    "Q12308941": DescraptionsTable["male given name"],
    "Q24046192": DescraptionsTable["Wikimedia category"],
    "Q4167836": DescraptionsTable["Wikimedia category"],
    "Q4167410": DescraptionsTable["Wikimedia disambiguation page"],
    "Q22808320": DescraptionsTable["Wikimedia disambiguation page"],
    "Q13406463": DescraptionsTable["Wikimedia list article"],
    "Q11266439": DescraptionsTable["Wikimedia template"],
    "Q11753321": DescraptionsTable["Wikimedia template"],
    "Q17633526": DescraptionsTable["Wikinews article"],
    "Q2467461": {"en": "academic department", "ar": "قسم أكاديمي"},
    "Q7187": DescraptionsTable["gene"],
    "Q7889": DescraptionsTable["video game"],
    "Q8054": DescraptionsTable["protein"],
    "Q21199": DescraptionsTable["natural number"],
    "Q24856": DescraptionsTable["film series"],
    "Q49008": DescraptionsTable["prime number"],
    "Q4502142": DescraptionsTable["visual artwork"],
    "Q6979593": DescraptionsTable["national association football team"],
    "Q10870555": DescraptionsTable["report"],
    "Q13100073": DescraptionsTable["village in China"],
    "Q19389637": DescraptionsTable["biographical article"],
    # space
}
# ---
for x, taba in Qid_Descraptions.items():
    Qids_translate[x] = taba
# ---
for qid1 in others_list:
    if qid1 not in Qids_translate:
        Qids_translate[qid1] = others_list[qid1]
# ---
Add_en_labels = {}
# ---
Add_en_labels[1] = True if "addenlabel" in sys.argv else False
# ---
Geo_List = list(placesTable.keys())
