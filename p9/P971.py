#!/usr/bin/python
# -*- coding: utf-8 -*-
"""

إيجاد تسمية عربية من خلال قوالب 
geobox

"""
#
# (C) Ibrahem Qasim, 2022
#
#

#---
# start of himoAPI.py file
from API import himoAPI
#himoAPI.Claim_API2( item_numeric , property, id)
#himoAPI.Claim_API_With_Quall(q , pro ,numeric, quall_prop , quall_id)
#himoAPI.New_API(data2, summary)
#himoAPI.New_Mult_Des( q, data2, summary , ret )
#himoAPI.Des_API( Qid, desc , lang )
#himoAPI.Labels_API( Qid, desc , lang , False)
#himoAPI.Merge( q1, q2)
#himoAPI.Sitelink_API( Qid, title , wiki )
#---
categories = [
	"Q25072344",
	"Q25072345",
	"Q25072347",
	"Q25072722",
	"Q25072724",
	"Q25072725",
	"Q25072727",
	"Q25072729",
	"Q25072730",
	"Q25072731",
	"Q25073113",
	"Q25073755",
	"Q25073756",
	"Q25073757",
	"Q25074221",
	"Q25074662",
	"Q25074663",
	"Q25074664",
	"Q25074665",
	"Q25074667",
	"Q25074672",
	"Q25074709",
	"Q25074761",
	"Q25074762",
	"Q25074763",
	"Q25074764",
	"Q25074776",
	"Q25074779",
	"Q25075320",
	"Q25075322",
	"Q25075325",
	"Q25075472",
	"Q25075496",
	"Q25075534",
	"Q25075675",
	"Q25075676",
	"Q25075683",
	"Q25076126",
	"Q25076137",
	"Q25076260",
	"Q25076261",
	"Q25076429",
	"Q25076431",
	"Q25076432",
	"Q25076724",
	"Q25076995",
	"Q25077007",
	"Q25077031",
	"Q25077080",
	"Q25077104",
	"Q25077284",
	"Q25077778",
	"Q25077779",
	"Q25077780",
	"Q25077781",
	"Q25077782",
	"Q25077783",
	"Q25077784",
	"Q25077785",
	"Q25077787",
	"Q25077788",
	"Q25077790",
	"Q25077791",
	"Q25077792",
	"Q25077793",
	"Q25077795",
	"Q25077796",
	"Q25077797",
	"Q25077948",
	"Q25077950",
	"Q25077951",
	"Q25077952",
	"Q25077953",
	"Q25078247",
	"Q25078522",
	"Q25078606",
	"Q25078607",
	"Q25078754",
	"Q25079004",
	"Q25079196",
	"Q25079729",
	"Q25079733",
	"Q25079735",
	"Q25079739",
	"Q25079745",
	"Q25079816",
	"Q25079817",
	"Q25079819",
	"Q25079825",
	"Q25079826",
	"Q25079827",
	"Q25079828",
	"Q25079831",
	"Q25079834",
	"Q25079835",
	"Q25079837",
	"Q25079849",
	"Q25079912",
	"Q25096511",
	"Q25110140",
	"Q25149585",
	"Q25164934",
	"Q25168619",
	"Q25168621",
	"Q25168623",
	"Q25168627",
	"Q25169782",
	"Q25169811",
	"Q25170266",
	"Q25170486",
	"Q25170500",
	"Q25170501",
	"Q25170502",
	"Q25170504",
	"Q25170505",
	"Q25170507",
	"Q25171737",
	"Q25172419",
	"Q25172879",
	"Q25173263",
	"Q25174089",
	"Q25174123",
	"Q25182951",
	"Q25183594",
	"Q25183765",
	"Q25183770",
	"Q25184012",
	"Q25184078",
	"Q25186900",
	"Q25187215",
	"Q25187761",
	"Q25188251",
	"Q25188252",
	"Q25188254",
	"Q25188255",
	"Q25188256",
	"Q25188257",
	"Q25188258",
	"Q25188259",
	"Q25188260",
	"Q25188261",
	"Q25188262",
	"Q25188263",
	"Q25188264",
	"Q25188265",
	"Q25188266",
	"Q25188267",
	"Q25188268",
	"Q25188269",
	"Q25188270",
	"Q25188271",
	"Q25188272",
	"Q25188273",
	"Q25188274",
	"Q25188275",
	"Q25188276",
	"Q25188401",
	"Q25188962",
	"Q25188971",
	"Q25189012",
	"Q25189062",
	"Q25195331",
	"Q25208271",
	"Q25208275",
	"Q25211458",
	"Q25211549",
	"Q25211806",
	"Q25211807",
	"Q25211821",
	"Q25211876",
	"Q25211895",
	"Q25211899",
	"Q25216048",
	"Q25217518",
	"Q25218906",
	"Q25218907",
	"Q25218910",
	"Q25218925",
	"Q25218926",
	"Q25218957",
	"Q25218980",
	"Q25218982",
	"Q25218983",
	"Q25218984",
	"Q25219001",
	"Q25219007",
	"Q25219020",
	"Q25219025",
	"Q25219066",
	"Q25219693",
	"Q25219694",
	"Q25219780",
	"Q25220229",
	"Q25223436",
	"Q25223523",
	"Q25223526",
	"Q25225470",
	"Q25227822",
	"Q25227879",
	"Q25228079",
	"Q25228442",
	"Q25228499",
	"Q25228541",
	"Q25228562",
	"Q25228567",
	"Q25228628",
	"Q25228707",
	"Q25228711",
	"Q25228829",
	"Q25228838",
	"Q25228876",
	"Q25231239",
	"Q25231927",
	"Q25231928",
	"Q25231999",
	"Q25232360",
	"Q25232361",
	"Q25232374",
	"Q25232379",
	"Q25232380",
	"Q25232381",
	"Q25232383",
	"Q25233243",
	"Q25233323",
	"Q25233602",
	"Q25233621",
	"Q25233659",
	"Q25233695",
	"Q25233736",
	"Q25233991",
	"Q25234062",
	"Q25234228",
	"Q25234239",
	"Q25234241",
	"Q25234355",
	"Q25234412",
	"Q25234448",
	"Q25241867",
	"Q25241905",
	"Q25241907",
	"Q25242090",
	"Q25242194",
	"Q25243084",
	"Q25243253",
	"Q25243437",
	"Q25243439",
	"Q25243606",
	"Q25243608",
	"Q25243609",
	"Q25243852",
	"Q25243883",
	"Q25243926",
	"Q25243940",
	"Q25243942",
	"Q25243944",
	"Q25243945",
	"Q25243946",
	"Q25243947",
	"Q25244186",
	"Q25244187",
	"Q25244188",
	"Q25244189",
	"Q25244194",
	"Q25244202",
	"Q25244325",
	"Q25244457",
	"Q25250388",
	"Q25250407",
	"Q25250418",
	"Q25250446",
	"Q25250808",
	"Q25251209",
	"Q25251403",
	"Q25251420",
	"Q25251422",
	"Q25251442",
	"Q25251447",
	"Q25251468",
	"Q25251527",
	"Q25251535",
	"Q25251619",
	"Q25251667",
	"Q25251714",
	"Q25251818",
	"Q25251820",
	"Q25251847",
	"Q25251931",
	"Q25251933",
	"Q25251941",
	"Q25252000",
	"Q25263010",
	"Q25268205",
	"Q25268597",
	"Q25304014",
	"Q25304019",
	"Q25304026",
	"Q25304033",
	"Q25304189",
	"Q25304257",
	"Q25304268",
	"Q25304269",
	"Q25304319",
	"Q25304495",
	"Q25304537",
	"Q25304538",
	"Q25304814",
	"Q25305528",
	"Q25306046",
	"Q25306891",
	"Q25307155",
	"Q25307162",
	"Q25307174",
	"Q25307178",
	"Q25307205",
	"Q25307206",
	"Q25307207",
	"Q25307214",
	"Q25307221",
	"Q25307225",
	"Q25307226",
	"Q25307228",
	"Q25307232",
	"Q25307234",
	"Q25307236",
	"Q25307237",
	"Q25307252",
	"Q25307271",
	"Q25307273",
	"Q25307274",
	"Q25307278",
	"Q25307281",
	"Q25307283",
	"Q25307287",
	"Q25307290",
	"Q25307293",
	"Q25307296",
	"Q25307300",
	"Q25307304",
	"Q25307308",
	"Q25307309",
	"Q25307320",
	"Q25307322",
	"Q25307325",
	"Q25307342",
	"Q25307354",
	"Q25307386",
	"Q25307404",
	"Q25307412",
	"Q25307415",
	"Q25307416",
	"Q25307417",
	"Q25307423",
	"Q25307425",
	"Q25307440",
	"Q25307453",
	"Q25307459",
	"Q25307461",
	"Q25307466",
	"Q25307467",
	"Q25307488",
	"Q25307784",
	"Q25307837",
	"Q25307838",
	"Q25307839",
	"Q25307841",
	"Q25307842",
	"Q25307843",
	"Q25307908",
	"Q25307911",
	"Q25307923",
	"Q25307925",
	"Q25307932",
	"Q25307961",
	"Q25307963",
	"Q25307989",
	"Q25308067",
	"Q25308099",
	"Q25308115",
	"Q25308162",
	"Q25308164",
	"Q25308167",
	"Q25308190",
	"Q25308447",
	"Q25308519",
	"Q25309705",
	"Q25312821",
	"Q25313077",
	"Q25314761",
	"Q25315069",
	"Q25315114",
	"Q25315262",
	"Q25316676",
	"Q25316845",
	"Q25316890",
	"Q25317036",
	"Q25317108",
	"Q25317136",
	"Q25317139",
	"Q25317347",
	"Q25317351",
	"Q25317450",
	"Q25317461",
	"Q25317525",
	"Q25317531",
	"Q25317533",
	"Q25317543",
	"Q25317544",
	"Q25317554",
	"Q25317608",
	"Q25317621",
	"Q25317623",
	"Q25317838",
	"Q25317858",
	"Q25318020",
	"Q25318215",
	"Q25318282",
	"Q25318324",
	"Q25318488",
	"Q25318542",
	"Q25318747",
	"Q25318963",
	"Q25318983",
	"Q25319065",
	"Q25319334",
	"Q25319373",
	"Q25319416",
	"Q25319469",
	"Q25319560",
	"Q25319608",
	"Q25319621",
	"Q25319675",
	"Q25319698",
	"Q25319772",
	"Q25319800",
	"Q25319801",
	"Q25319802",
	"Q25319830",
	"Q25320022",
	"Q25320276",
	"Q25320283",
	"Q25320293",
	"Q25320353",
	"Q25320391",
	"Q25320742",
	"Q25321157",
	"Q25321314",
	"Q25321459",
	"Q25321468",
	"Q25321490",
	"Q25321510",
	"Q25321525",
	"Q25321535",
	"Q25321844",
	"Q25321894",
	"Q25321895",
	"Q25321922",
	"Q25321940",
	"Q25321944",
	"Q25321946",
	"Q25322216",
	"Q25324358",
	"Q25324454",
	"Q25324459",
	"Q25324675",
	"Q25324679",
	"Q25324752",
	"Q25325497",
	"Q25325557",
	"Q25325581",
	"Q25325619",
	"Q25325667",
	"Q25325855",
	"Q25325858",
	"Q25325878",
	"Q25325888",
	"Q25325934",
	"Q25325945",
	"Q25326007",
	"Q25326058",
	"Q25326071",
	"Q25326226",
	"Q25326251",
	"Q25326253",
	"Q25326329",
	"Q25327481",
	"Q25328895",
	"Q25328984",
	"Q25329020",
	"Q25329030",
	"Q25329410",
	"Q25329707",
	"Q25330081",
	"Q25330334",
	"Q25330508",
	"Q25330518",
	"Q25330520",
	"Q25330574",
	"Q25330817",
	"Q25330923",
	"Q25330992",
	"Q25331018",
	"Q25331072",
	"Q25331592",
	"Q25331696",
	"Q25331815",
	"Q25331846",
	"Q25332056",
	"Q25332115",
	"Q25332132",
	"Q25332136",
	"Q25332472",
	"Q25332816",
	"Q25333125",
	"Q25333147",
	"Q25333150",
	"Q25333152",
	"Q25333158",
	"Q25333159",
	"Q25333160",
	"Q25333162",
	"Q25333208",
	"Q25333225",
	"Q25333228",
	"Q25333231",
	"Q25333291",
	"Q25333292",
	"Q25333294",
	"Q25333295",
	"Q25333300",
	"Q25333316",
	"Q25333320",
	"Q25333466",
	"Q25333611",
	"Q25333758",
	"Q25334070",
	"Q25334071",
	"Q25334095",
	"Q25334334",
	"Q25334415",
	"Q25334585",
	"Q25334726",
	"Q25334727",
	"Q25334753",
	"Q25334783",
	"Q25334806",
	"Q25334927",
	"Q25334984",
	"Q25334985",
	"Q25334986",
	"Q25334987",
	"Q25334988",
	"Q25334989",
	"Q25335022",
	"Q25335026",
	"Q25335075",
	"Q25336077",
	"Q25336185",
	"Q25338593",
	"Q25338668",
	"Q25341033",
	"Q25341038",
	"Q25341056",
	"Q25341501",
	"Q25353159",
	"Q25353161",
	"Q25353181",
	"Q25353182",
	"Q25354755",
	"Q25354796",
	"Q25355287",
	"Q25355451",
	"Q25365576",
	"Q25366446",
	"Q25371228",
	"Q25371229",
	"Q25371230",
	"Q25371235",
	"Q25371241",
	"Q25371325",
	"Q25372496",
	"Q25372497",
	"Q25372499",
	"Q25967190",
	"Q25990698",
	"Q25997879",
	"Q25997882",
	"Q26037030",
	"Q26162250",
	"Q26209744",
	"Q26463130",
	"Q26463294",
	"Q26463323",
	"Q26463391",
	"Q26463408",
	"Q26463416",
	"Q26463418",
	"Q26463420",
	"Q26463421",
	"Q26700311",
	"Q26700318",
	"Q26714856",
	"Q26810982",
	"Q26857971",
	"Q26936780",
	"Q26936781",
	"Q26936782",
	"Q26972841",
	"Q26972929",
	"Q27070097",
	"Q27120499",
	"Q27144363",
	"Q27492092",
	"Q27500375",
	"Q27532176",
	"Q27543104",
	"Q27664219",
	"Q27671884",
	"Q27876313",
	"Q27876337",
	"Q27891504",
	"Q27899580",
	"Q27899585",
	"Q27920063",
	"Q27920183",
	"Q27973886",
	"Q27974511",
	"Q27978653",
	"Q27991619",
	"Q28007364",
	"Q28007393",
	"Q28016605",
	"Q28017608",
	"Q28017612",
	"Q28031348",
	"Q28031976",
	"Q28046081",
	"Q28046095",
	"Q28049968",
	"Q28055070",
	"Q28060461",
	"Q28060906",
	"Q28086063",
	"Q28097665",
	"Q28105175",
	"Q28105208",
	"Q28105242",
	"Q28105372",
	"Q28113845",
	"Q28125272",
	"Q28125311",
	"Q28191228",
	"Q28197284",
	"Q28197322",
	"Q28197325",
	"Q28197330",
	"Q28197350",
	"Q28197363",
	"Q28214556",
	"Q28315928",
	"Q28362445",
	"Q28399005",
	"Q28399291",
	"Q28399552",
	"Q28399757",
	"Q28400680",
	"Q28400998",
	"Q28420322",
	"Q28420466",
	"Q28420577",
	"Q28420595",
	"Q28420972",
	"Q28421282",
	"Q28422487",
	"Q28427756",
	"Q28430379",
	"Q28432074",
	"Q28432254",
	"Q28433295",
	"Q28433708",
	"Q28433710",
	"Q28433713",
	"Q28433715",
	"Q28433739",
	"Q28434196",
	"Q28434258",
	"Q28435719",
	"Q28436694",
	"Q28437117",
	"Q28438451",
	"Q28438590",
	"Q28439217",
	"Q28439946",
	"Q28439981",
	"Q28440351",
	"Q28440403",
	"Q28441487",
	"Q28442007",
	"Q28442020",
	"Q28442021",
	"Q28442022",
	"Q28442097",
	"Q28442098",
	"Q28442210",
	"Q28442346",
	"Q28442495",
	"Q28458723",
	"Q28458770",
	"Q28458772",
	"Q28458778",
	"Q28458795",
	"Q28458818",
	"Q28458819",
	"Q28458820",
	"Q28458821",
	"Q28458822",
	"Q28458823",
	"Q28458824",
	"Q28458860",
	"Q28458925",
	"Q28458935",
	"Q28458939",
	"Q28458943",
	"Q28458944",
	"Q28458952",
	"Q28458953",
	"Q28458960",
	"Q28458961",
	"Q28458972",
	"Q28458974",
	"Q28458975",
	"Q28458980",
	"Q28459088",
	"Q28459101",
	"Q28459102",
	"Q28459138",
	"Q28459140",
	"Q28459306",
	"Q28459329",
	"Q28459365",
	"Q28459374",
	"Q28459398",
	"Q28459406",
	"Q28459408",
	"Q28459416",
	"Q28459440",
	"Q28459448",
	"Q28459449",
	"Q28459450",
	"Q28459452",
	"Q28459453",
	"Q28459455",
	"Q28459456",
	"Q28459458",
	"Q28459564",
	"Q28459566",
	"Q28459570",
	"Q28459574",
	"Q28460060",
	"Q28460061",
	"Q28460064",
	"Q28460177",
	"Q28460222",
	"Q28460228",
	"Q28460288",
	"Q28460292",
	"Q28460293",
	"Q28460317",
	"Q28460339",
	"Q28460363",
	"Q28460373",
	"Q28460430",
	"Q28460559",
	"Q28460609",
	"Q28460718",
	"Q28460809",
	"Q28461018",
	"Q28461019",
	"Q28461049",
	"Q28461096",
	"Q28461113",
	"Q28461338",
	"Q28461547",
	"Q28462021",
	"Q28462022",
	"Q28462044",
	"Q28462064",
	"Q28462077",
	"Q28462157",
	"Q28462159",
	"Q28462421",
	"Q28463113",
	"Q28463232",
	"Q28463235",
	"Q28463238",
	"Q28463261",
	"Q28463406",
	"Q28463443",
	"Q28463444",
	"Q28463445",
	"Q28463447",
	"Q28463448",
	"Q28463450",
	"Q28463455",
	"Q28463456",
	"Q28463457",
	"Q28463458",
	"Q28463460",
	"Q28463461",
	"Q28463462",
	"Q28463463",
	"Q28463464",
	"Q28463466",
	"Q28463467",
	"Q28463470",
	"Q28463471",
	"Q28463472",
	"Q28463473",
	"Q28463474",
	"Q28463475",
	"Q28463531",
	"Q28463601",
	"Q28463602",
	"Q28463603",
	"Q28463604",
	"Q28463605",
	"Q28463606",
	"Q28463607",
	"Q28463609",
	"Q28463610",
	"Q28463611",
	"Q28463612",
	"Q28463613",
	"Q28463616",
	"Q28463632",
	"Q28463635",
	"Q28463636",
	"Q28463637",
	"Q28463638",
	"Q28463639",
	"Q28463640",
	"Q28463641",
	"Q28463642",
	"Q28463643",
	"Q28463645",
	"Q28463680",
	"Q28463682",
	"Q28463683",
	"Q28463684",
	"Q28463715",
	"Q28463716",
	"Q28463717",
	"Q28463718",
	"Q28463719",
	"Q28463720",
	"Q28463721",
	"Q28463722",
	"Q28463723",
	"Q28463724",
	"Q28463725",
	"Q28463726",
	"Q28463728",
	"Q28463729",
	"Q28463731",
	"Q28463732",
	"Q28463733",
	"Q28463734",
	"Q28463735",
	"Q28463736",
	"Q28463737",
	"Q28463759",
	"Q28463796",
	"Q28463853",
	"Q28463862",
	"Q28463867",
	"Q28463869",
	"Q28463872",
	"Q28463874",
	"Q28464107",
	"Q28464109",
	"Q28464116",
	"Q28464159",
	"Q28464161",
	"Q28466736",
	"Q28500580",
	"Q28545410",
	"Q28549595",
	"Q28549597",
	"Q28549609",
	"Q28600078",
	"Q28604487",
	"Q28604496",
	"Q28604502",
	"Q28604505",
	"Q28604552",
	"Q28604553",
	"Q28604555",
	"Q28604569",
	"Q28604739",
	"Q28604740",
	"Q28604742",
	"Q28604744",
	"Q28604745",
	"Q28604747",
	"Q28604748",
	"Q28604751",
	"Q28604787",
	"Q28604788",
	"Q28604811",
	"Q28604815",
	"Q28604820",
	"Q28604821",
	"Q28604822",
	"Q28604825",
	"Q28604829",
	"Q28604835",
	"Q28604838",
	"Q28604852",
	"Q28604853",
	"Q28604854",
	"Q28604855",
	"Q28604856",
	"Q28604857",
	"Q28658968",
	"Q28693097",
	"Q28725723",
	"Q28730580",
	"Q28736402",
	"Q28778521",
	"Q28778524",
	"Q28780731",
	"Q28791036",
	"Q28813827",
	"Q28813835",
	"Q28813842",
	"Q28813845",
	"Q28813851",
	"Q28813862",
	"Q28813888",
	"Q28813896",
	"Q28813899",
	"Q28813911",
	"Q28813915",
	"Q28813923",
	"Q28813925",
	"Q28813928",
	"Q28813938",
	"Q28813939",
	"Q28814049",
	"Q28814050",
	"Q28814053",
	"Q28834843",
	"Q28861641",
	"Q28862565",
	"Q28862599",
	"Q28862667",
	"Q28862705",
	"Q28869740",
	"Q28869805",
	"Q28873415",
	"Q28881058",
	"Q28900711",
	"Q28921130",
	"Q28923814",
	"Q28923824",
	"Q28923986",
	"Q28924566",
	"Q28927683",
	"Q28927762",
	"Q28927967",
	"Q28927970",
	"Q28928033",
	"Q28928036",
	"Q28928037",
	"Q28928042",
	"Q28928043",
	"Q28928044",
	"Q28928045",
	"Q28928046",
	"Q28928048",
	"Q28929786",
	"Q28929812",
	"Q28933629",
	"Q28933715",
	"Q28933725",
	"Q28933951",
	"Q28933987",
	"Q28933994",
	"Q28934009",
	"Q28946259",
	"Q28946277",
	"Q28946335",
	"Q28955924",
	"Q28971711",
	"Q29002753",
	"Q29002763",
	"Q29010873",
	"Q29014603",
	"Q29014635",
	"Q29016016",
	"Q29016713",
	"Q29016715",
	"Q29016716",
	"Q29043395",
	"Q29053183",
	"Q29110508",
	"Q29168042",
	"Q29203795",
	"Q29204106",
	"Q29205796",
	"Q29235178",
	"Q29263920",
	"Q29319583",
	"Q29342726",
	"Q29348138",
	"Q29366462",
	"Q29414154",
	"Q29414169",
	"Q29419795",
	"Q29440738",
	"Q29472518",
	"Q29510957",
	"Q29557227",
	"Q29570268",
	"Q29578372",
	"Q29578380",
	"Q29584163",
	"Q29587461",
	"Q29587519",
	"Q29587537",
	"Q29587540",
	"Q29587607",
	"Q29587612",
	"Q29587617",
	"Q29587622",
	"Q29587626",
	"Q29587668",
	"Q29587678",
	"Q29587801",
	"Q29587806",
	"Q29587853",
	"Q29587857",
	"Q29587859",
	"Q29587862",
	"Q29587866",
	"Q29587867",
	"Q29587868",
	"Q29587871",
	"Q29587874",
	"Q29587876",
	"Q29587880",
	"Q29587884",
	"Q29587886",
	"Q29587890",
	"Q29587893",
	"Q29587895",
	"Q29587899",
	"Q29587903",
	"Q29587912",
	"Q29587922",
	"Q29587925",
	"Q29587929",
	"Q29587930",
	"Q29587934",
	"Q29587937",
	"Q29587939",
	"Q29587944",
	"Q29587946",
	"Q29587949",
	"Q29587952",
	"Q29587954",
	"Q29587958",
	"Q29587960",
	"Q29587971",
	"Q29587985",
	"Q29587990",
	"Q29587997",
	"Q29587999",
	"Q29588003",
	"Q29588027",
	"Q29588032",
	"Q29588105",
	"Q29588107",
	"Q29588149",
	"Q29593270",
	"Q29593286",
	"Q29593300",
	"Q29593343",
	"Q29593354",
	"Q29593366",
	"Q29593375",
	"Q29593588",
	"Q29593614",
	"Q29593649",
	"Q29593655",
	"Q29593864",
	"Q29593889",
	"Q29593904",
	"Q29593931",
	"Q29594870",
	"Q29594902",
	"Q29595285",
	"Q29595359",
	"Q29595860",
	"Q29596436",
	"Q29596452",
	"Q29597179",
	"Q29597187",
	"Q29597188",
	"Q29597232",
	"Q29597340",
	"Q29597634",
	"Q29597754",
	"Q29597800",
	"Q29597903",
	"Q29597966",
	"Q29598772",
	"Q29598774",
	"Q29598935",
	"Q29599022",
	"Q29599061",
	"Q29599812",
	"Q29601965",
	"Q29602368",
	"Q29602583",
	"Q29602624",
	"Q29602657",
	"Q29602662",
	"Q29602667",
	"Q29602682",
	"Q29602687",
	"Q29612587",
	"Q29626263",
	"Q29628197",
	"Q29628200",
	"Q29628206",
	"Q29628210",
	"Q29628214",
	"Q29628217",
	"Q29628221",
	"Q29628224",
	"Q29628231",
	"Q29628234",
	"Q29628238",
	"Q29628241",
	"Q29628244",
	"Q29628247",
	"Q29628250",
	"Q29628254",
	"Q29628258",
	"Q29628262",
	"Q29628266",
	"Q29628270",
	"Q29628275",
	"Q29628277",
	"Q29628279",
	"Q29628282",
	"Q29628809",
	"Q29628826",
	"Q29629053",
	"Q29629339",
	"Q29630024",
	"Q29630959",
	"Q29631196",
	"Q29631359",
	"Q29648349",
	"Q29841588",
	"Q29849336",
	"Q29857420",
	"Q29857421",
	"Q29857424",
	"Q29857425",
	"Q29857429",
	"Q29857430",
	"Q29857433",
	"Q29857435",
	"Q29857471",
	"Q29857555",
	"Q29857557",
	"Q29857587",
	"Q29859297",
	"Q29859390",
	"Q29899261",
	"Q29900328",
	"Q29900348",
	"Q29901192",
	"Q29901487",
	"Q29901733",
	"Q29901892",
	"Q29901939",
	"Q29901967",
	"Q29901968",
	"Q29902022",
	"Q29902148",
	"Q29902157",
	"Q29902194",
	"Q29902202",
	"Q29902204",
	"Q29902205",
	"Q29902208",
	"Q29902210",
	"Q29902211",
	"Q29902213",
	"Q29902215",
	"Q29902308",
	"Q29902334",
	"Q29902336",
	"Q29902345",
	"Q29902348",
	"Q29902350",
	"Q29902351",
	"Q29902354",
	"Q29902356",
	"Q29902358",
	"Q29902360",
	"Q29902418",
	"Q29902439",
	"Q29902449",
	"Q29902457",
	"Q29902504",
	"Q29902515",
	"Q29902561",
	"Q29902572",
	"Q29902688",
	"Q29902689",
	"Q29902691",
	"Q29902807",
	"Q29902832",
	"Q29903012",
	"Q29903019",
	"Q29903020",
	"Q29903034",
	"Q29903038",
	"Q29903076",
	"Q29903084",
	"Q29903105",
	"Q29903114",
	"Q29903118",
	"Q29903120",
	"Q29903121",
	"Q29903124",
	"Q29903127",
	"Q29903128",
	"Q29903129",
	"Q29903133",
	"Q29903146",
	"Q29903149",
	"Q29903151",
	"Q29903152",
	"Q29903154",
	"Q29903156",
	"Q29903162",
	"Q29903191",
	"Q29903207",
	"Q29903208",
	"Q29903210",
	"Q29903211",
	"Q29903218",
	"Q29903234",
	"Q29903245",
	"Q29903247",
	"Q29903265",
	"Q29903267",
	"Q29903269",
	"Q29903271",
	"Q29903273",
	"Q29903275",
	"Q29916133",
	"Q29934296",
	"Q29974918",
	"Q29976803",
	"Q30000394",
	"Q30000437",
	"Q30000439",
	"Q30000454",
	"Q30000456",
	"Q30000459",
	"Q30000461",
	"Q30000464",
	"Q30000466",
	"Q30000469",
	"Q30000472",
	"Q30000475",
	"Q30000477",
	"Q30000480",
	"Q30000482",
	"Q30000487",
	"Q30000491",
	"Q30000493",
	"Q30000496",
	"Q30000499",
	"Q30000501",
	"Q30000502",
	"Q30000504",
	"Q30000505",
	"Q30000506",
	"Q30000507",
	"Q30000508",
	"Q30000509",
	"Q30000510",
	"Q30000512",
	"Q30000619",
	"Q30000702",
	"Q30000703",
	"Q30000704",
	"Q30000705",
	"Q30000706",
	"Q30000707",
	"Q30000708",
	"Q30000709",
	"Q30000710",
	"Q30000711",
	"Q30000712",
	"Q30000714",
	"Q30000715",
	"Q30000716",
	"Q30000717",
	"Q30000718",
	"Q30001107",
	"Q30001148",
	"Q30001149",
	"Q30001230",
	"Q30001465",
	"Q30001466",
	"Q30001478",
	"Q30001499",
	"Q30001593",
	"Q30003051",
	"Q30003126",
	"Q30003176",
	"Q30003713",
	"Q30003908",
	"Q30003949",
	"Q30003950",
	"Q30003951",
	"Q30004135",
	"Q30004140",
	"Q30004161",
	"Q30004171",
	"Q30004202",
	"Q30004682",
	"Q30005458",
	"Q30005459",
	"Q30005460",
	"Q30005461",
	"Q30005462",
	"Q30005463",
	"Q30005477",
	"Q30005844",
	"Q30005857",
	"Q30008272",
	"Q30016703",
	"Q30089799",
	"Q30089804",
	"Q30140748",
	"Q30140786",
	"Q30140803",
	"Q30150027",
	"Q30239188",
	"Q30239190",
	"Q30411028",
	"Q30542522",
	"Q30542822",
	"Q30582945",
	"Q30599943",
	"Q30602387",
	"Q30604929",
	"Q30633195",
	"Q30634055",
	"Q30634313",
	"Q30635127",
	"Q30635129",
	"Q30639376",
	"Q30639437",
	"Q30639597",
	"Q30639862",
	"Q30640126",
	"Q30640131",
	"Q30640498",
	"Q30640541",
	"Q30641340",
	"Q30642042",
	"Q30642376",
	"Q30642409",
	"Q30642852",
	"Q30643282",
	"Q30643329",
	"Q30643583",
	"Q30644404",
	"Q30644462",
	"Q30644554",
	"Q30645144",
	"Q30645153",
	"Q30645398",
	"Q30646055",
	"Q30646306",
	"Q30646712",
	"Q30646767",
	"Q30646774",
	"Q30646778",
	"Q30646814",
	"Q30646858",
	"Q30646933",
	"Q30646948",
	"Q30647246",
	"Q30647487",
	"Q30647542",
	"Q30647738",
	"Q30648045",
	"Q30648498",
	"Q30648658",
	"Q30648908",
	"Q30649059",
	"Q30649235",
	"Q30649297",
	"Q30649675",
	"Q30649711",
	"Q30649788",
	"Q30649800",
	"Q30649856",
	"Q30671907",
	"Q30674049",
	"Q30674157",
	"Q30674404",
	"Q30674460",
	"Q30675531",
	"Q30675970",
	"Q30677204",
	"Q30677491",
	"Q30677774",
	"Q30677787",
	"Q30677792",
	"Q30677798",
	"Q30677806",
	"Q30677825",
	"Q30677827",
	"Q30677835",
	"Q30677849",
	"Q30677926",
	"Q30678109",
	"Q30678258",
	"Q30678632",
	"Q30678733",
	"Q30678786",
	"Q30678788",
	"Q30678789",
	"Q30678790",
	"Q30678791",
	"Q30678792",
	"Q30678793",
	"Q30678794",
	"Q30678795",
	"Q30678796",
	"Q30678797",
	"Q30678799",
	"Q30678800",
	"Q30678801",
	"Q30678802",
	"Q30678803",
	"Q30678804",
	"Q30678805",
	"Q30678806",
	"Q30678807",
	"Q30678808",
	"Q30678809",
	"Q30678811",
	"Q30678812",
	"Q30678813",
	"Q30678814",
	"Q30678815",
	"Q30678817",
	"Q30678818",
	"Q30678820",
	"Q30678822",
	"Q30678824",
	"Q30678825",
	"Q30678827",
	"Q30678828",
	"Q30678829",
	"Q30678831",
	"Q30678832",
	"Q30678834",
	"Q30678835",
	"Q30678837",
	"Q30678840",
	"Q30678842",
	"Q30678843",
	"Q30678845",
	"Q30678847",
	"Q30678848",
	"Q30678849",
	"Q30678851",
	"Q30678852",
	"Q30678854",
	"Q30678855",
	"Q30678858",
	"Q30678859",
	"Q30678871",
	"Q30678875",
	"Q30678878"
	]
#---   
for q in categories:
	himoAPI.Claim_API2(q , 'P971', 'Q19360703')