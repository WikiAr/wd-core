
import requests

session = requests.Session()
url = "https://query.wikidata.org/bigdata/namespace/wdq/sparql?query=LIMIT%205000&format=JSON"
req = session.get(url)
json1 = {}
try:
    json1 = req.json()
except Exception as e:
    json1 = {}
    #---
    print( '<<lightred>> Traceback (most recent call last):' )
    e = str(e)
    if e.find('java.util.concurrent') != -1 : e = "java.util.concurrent"
    print( "<<lightred>> Exception:%s." % e )
    print( 'CRITICAL:' )
#---
# list of all compression extensions
false_ex = ['.bz2', '.gz', '.xz', '.lzma', '.lz', '.zst', '.br', '.7z', '.rar', '.zip', '.tar', '.tar.gz', '.tar.bz2', '.tar.xz', '.tar.lzma', '.tar.lz', '.tar.zst', '.tar.7z', '.tar.rar', '.tar.zip']
#---
filepath = './sdsd.zip'
#---
test = any(filepath.endswith(ext) for ext in false_ex)
if test:
    print( '<<lightred>> File is compressed.:%s' % str(test) )
#---
if filepath.endswith(tuple(false_ex)):
    print( '<<lightred>> File er' )
#---