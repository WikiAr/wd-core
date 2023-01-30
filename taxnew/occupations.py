#!/usr/bin/python
# -*- coding: utf-8 -*-
"""


"""
#
# (C) Ibrahem Qasim, 2022
#
#
translationsOccupations = {
			'~ alga':{'ar':'~ الطحالب'},
			'~ algae':{'ar':'~ الطحالب'},
			'~ amphibian':{'ar':'~ البرمائيات'},
			'~ amphibians':{'ar':'~ البرمائيات'},
			'~ annelid':{'ar':'~ الحلقيات'},
			'~ arachnid':{'ar':'~ العنكبيات'},
			'~ arachnids':{'ar':'~ العنكبيات'},
			'~ arthropods':{'ar':'~ المفصليات'},
			'~ bird':{'ar':'~ الطيور'},
			'~ birds':{'ar':'~ الطيور'},
			'~ brachiopods':{'ar':'~ ذوات القوائم الذراعية'},
			'~ bryozoan':{'ar':'~ المرجانيات'},
			'~ bryozoans':{'ar':'~ المرجانيات'},
			'~ chordates':{'ar':'~ الحبليات'},
			'~ cnidarian':{'ar':'~ القراصات'},
			'~ cnidarians':{'ar':'~ القراصات'},
			'~ crustacean':{'ar':'~ القشريات'},
			'~ crustaceans':{'ar':'~ القشريات'},
			'~ ctenophore':{'ar':'~ الممشطيات'},
			'~ echinoderm':{'ar':'~ الشوكيات'},
			'~ echinoderms':{'ar':'~ الشوكيات'},
			'~ entoprocts':{'ar':'~ داخليات الشرج'},
			'~ fish':{'ar':'~ الأسماك'},
			'~ fishes':{'ar':'~ الأسماك'},
			'~ fungi':{'ar':'~ الفطريات'},
			'~ fungus':{'ar':'~ الفطريات'},
			'~ gastrotrichs':{'ar':'~ شعريات البطن'},
			'~ insect':{'ar':'~ الحشرات'},
			'~ insects':{'ar':'~ الحشرات'},
			'~ mammal':{'ar':'~ الثدييات'},
			'~ mammals':{'ar':'~ الثدييات'},
			'~ mollusc':{'ar':'~ الرخويات'},
			'~ molluscs':{'ar':'~ الرخويات'},
			'~ myriapod':{'ar':'~ كثيرات الأرجل'},
			'~ myriapods':{'ar':'~ كثيرات الأرجل'},
			'~ plant':{'ar':'~ النباتات'},
			'~ plants':{'ar':'~ النباتات'},
			'~ prokaryote':{'ar':'~ بدائيات النوى'},
			'~ prokaryotes':{'ar':'~ بدائيات النوى'},
			'~ reptile':{'ar':'~ الزواحف'},
			'~ reptiles':{'ar':'~ الزواحف'},
			'~ rotifers':{'ar':'~ الدوارات'},
			'~ sea spiders':{'ar':'~ العناكب البحرية'},
			'~ sponge':{'ar':'~ الإسفنجيات'},
			'~ sponges':{'ar':'~ الإسفنجيات'},
			'~ trilobites':{'ar':'~ ثلاثية الفصوص'},
			'~ virus':{'ar':'~ الفيروسات'},
			'~ waterbears':{'ar':'~ دب الماء'},
			'~ worm':{'ar':'~ الديدان'},
			'~ worms':{'ar':'~ الديدان'},
    }
"""
def translationsOccupations(query):
  wikidatasite=pywikibot.Site('wikidata','wikidata') 
  generator=pg.WikidataSPARQLPageGenerator(query,site=wikidatasite)
  for wd in generator:
    wd.get(get_redirect=True)
    yield wd"""