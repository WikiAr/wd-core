tata = {
        "isRedirectPage":False,
        "exists":True,"from":"",
        "to":"",
        "title":"",
        "ns":"",
        "pageid":"",
        "langlinks":{},
        "templates":{},
        "wikibase_item":"",
        "q":""
        }
#---
tata2 = { x:z for x,z in tata.items()}
#---
tata["q"] = "qqqqqqqqqqqqqqqqqqqqqqq"
#---
print(f"{tata=}")
print(f"{tata2=}")