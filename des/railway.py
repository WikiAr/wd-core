#!/usr/bin/env python3
#
'''
from des.railway import railway_tables, work_railway#work_railway( item, P31, q='' )

python3 core8/pwb.py des/fam railway Q55678
python3 core8/pwb.py des/fam railway Q728937
python3 core8/pwb.py des/fam railway Q784159
python3 core8/pwb.py des/fam railway Q55488
'''
#
# ---
import sys
from wd_api import wd_desc
from API import himoBOT2

# ---
from des.ru_st_2_latin import make_en_label

# enlabel = make_en_label(labels, Add=False)
# ---
railway_tables = {
    "Q728937": {"ar": "خط سكة حديدية", "en": "railway line"},
    "Q55678": {"ar": "نقطة سكة حديدية", "en": "railway stop"},
    "Q784159": {"ar": "", "en": "passing loop"},
    "Q55488": {"ar": "محطة سكة حديدية", "en": "railway station"},
}


def Get_P_API_id(claims, P, onlyone=False):
    # ---
    list = []
    # ---
    for c in claims.get(P, {}):
        if (
            q := c.get('mainsnak', {})
            .get('datavalue', {})
            .get('value', {})
            .get('id')
        ):
            list.append(q)
            if onlyone:
                return q
    # ---
    return "" if onlyone else list


def work_railway(wditem, p31, q=""):
    # ---
    if "railway" not in sys.argv:
        return
    # ---
    if wditem == {}:
        wditem = himoBOT2.Get_Item_API_From_Qid(q)
    # ---
    q = wditem.get("q", "")
    # ---
    print(f'Make_railway_desc: q:{q}, [p31:{p31}]')
    # ---
    labels = wditem.get("labels", {})
    if labels.get("en", "") == "":
        print("item enlabel == ''")
        make_en_label(labels, q, Add=True)
    # ---
    Claims = wditem.get("claims", {})
    # ---
    if Claims == {}:
        Claims = himoBOT2.Get_Item_API_From_Qid(q).get("claims", {})
    # ---
    P17_qid = Get_P_API_id(Claims, 'P17', onlyone=True)  # Claims.get('P17',[{}])[0].get("mainsnak",{}).get("datavalue",{}).get("value",{}).get("id",'')
    P131_qid = Get_P_API_id(Claims, 'P131', onlyone=True)
    # ---
    p17_labels, p131_labels = {}, {}
    # ---
    if P17_qid != "":
        p17_labels = himoBOT2.Get_Item_API_From_Qid(P17_qid).get('labels', {})
    # ---
    if P131_qid != "":
        p131_labels = himoBOT2.Get_Item_API_From_Qid(P131_qid).get('labels', {})
    # ---
    to_do_descs = railway_tables.get(p31, {})
    # ---
    lang_format = {
        "ar": {1: "{} في {}", 2: "{} في {}، {}"},
        "en": {1: "{} in {}", 2: "{} in {}, {}"},
    }
    # ---
    if to_do_descs == {}:
        return
    # ---
    wditem_desc = wditem.get("descriptions", {})
    newdesc = {}
    # ---
    labs = {
        "p17": {"ar": p17_labels.get("ar", ""), "en": p17_labels.get("en", "")},
        "p131": {"ar": p131_labels.get("ar", ""), "en": p131_labels.get("en", "")},
    }
    # ---
    P31_list = Get_P_API_id(Claims, 'P31')
    # ---
    for lang, des in to_do_descs.items():
        if des == "":
            continue
        # ---
        org_desc = wditem_desc.get(lang, "")
        # ---
        if org_desc not in ["", des]:
            continue
        # ---
        p17_desc = labs["p17"].get(lang, "").split("(")[0].strip()
        # ---
        p131_desc = labs["p131"].get(lang, "").split("(")[0].strip()
        # ---
        if p17_desc == "" and p131_desc == "" and lang != "ar":
            continue
        # ---
        o1 = f", {p17_desc}"
        o2 = f"، {p17_desc}"
        o3 = f"({p17_desc})"
        # ---
        if p131_desc.endswith(o1):
            p131_desc = p131_desc.replace(o1, '')
        if p131_desc.endswith(o2):
            p131_desc = p131_desc.replace(o2, '')
        if p131_desc.endswith(o3):
            p131_desc = p131_desc.replace(o3, '')
        # ---
        # make new desc
        # ---
        desc_n = des
        if p17_desc != "":
            if p31 != 'Q728937' and 'Q728937' not in P31_list and p131_desc != "":
                desc_n = lang_format[lang][2].format(des, p131_desc, p17_desc)
            else:
                desc_n = lang_format[lang][1].format(des, p17_desc)
        # ---
        if desc_n != '':
            newdesc[lang] = {"language": lang, "value": desc_n}
            # ---
    # ---
    if not newdesc:
        print("nothing to add..")
        return
    # ---
    een = ['en-gb', 'en-ca']
    # ---
    # if newdesc.get("en"):
    # for o in een:
    # if not o in wditem_desc:
    # newdesc[o] = {"language": o, "value": newdesc["en"]["value"]}
    # ---
    wd_desc.work_api_desc(newdesc, q)
    # ---
    return ''


# ---
