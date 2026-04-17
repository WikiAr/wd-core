""" """

import logging
import sys
from datetime import datetime
import json
from urllib.error import HTTPError, URLError
from SPARQLWrapper import JSON, SPARQLWrapper

logger = logging.getLogger(__name__)
menet = datetime.now().strftime("%Y-%b-%d  %H:%M:%S")


def get_query_data(query):
    """Retrieve query data from the Wikidata SPARQL endpoint.

    This function sends a SPARQL query to the Wikidata endpoint and
    retrieves the results in JSON format. It constructs a user agent string
    based on the Python version and uses the SPARQLWrapper library to handle
    the query execution. If an error occurs during the query process, it
    logs the exception for debugging purposes.

    Args:
        query (str): A SPARQL query string to be executed against the
            Wikidata database.

    Returns:
        dict: The data retrieved from the SPARQL query, formatted as a
            dictionary.
    """
    # TODO: https://www.wikidata.org/wiki/Wikidata:SPARQL_query_service/WDQS_graph_split/Rules#Scholarly_Articles

    # endpoint_url = "https://query-main.wikidata.org/sparql"
    endpoint_url = "https://query.wikidata.org/sparql"
    # ---
    user_agent = f"WDQS-example Python/{sys.version_info[0]}.{sys.version_info[1]}"
    # ---
    sparql = SPARQLWrapper(endpoint_url, agent=user_agent)
    # ---
    sparql.setQuery(query)
    sparql.setReturnFormat(JSON)
    sparql.setTimeout(30)
    # ---
    data = {}
    # ---
    try:
        data = sparql.query().convert()
    except (HTTPError, URLError, TimeoutError, ValueError, json.JSONDecodeError):
        logger.exception("wd_helps.get_query_data failed")
    # ---
    return data


def wd_sparql_generator_url(quary, returnq=False):
    """Generate a list of unique item identifiers from a SPARQL query.

    This function takes a SPARQL query as input, executes it to retrieve
    data, and extracts unique item identifiers from the results. It
    processes the results to filter and sort the identifiers, returning a
    list of those that start with 'Q'. The function also outputs the number
    of items found and the number of unique items appended.

    Args:
        quary (str): The SPARQL query string to be executed.
        returnq (bool?): A flag indicating whether to return the
            generated list of items. Defaults to False.

    Returns:
        list: A list of unique item identifiers extracted from the query results.
    """

    # ---
    logger.info(quary)
    # ---
    items = []
    qlist = []
    # ---
    json1 = get_query_data(quary)
    # ---
    if not json1:
        return items
    # ---
    bindings = json1.get("results", {}).get("bindings", [])
    # ---
    for result in bindings:
        q = "item" in result and result["item"]["value"].split("/entity/")[1]
        if q:
            qlist.append(q)
    # ---
    qlist.sort()
    # ---
    lenth2 = len(qlist)
    numb2 = 0
    # ---
    for q in qlist:
        if q.startswith("Q"):
            numb2 += 1
            items.append(q)
    # ---
    ss = f"{lenth2} items found, {len(items)} items append, {menet}"
    # ---
    logger.info(ss)
    # ---
    return items


def sparql_generator_url(quary, printq=False, add_date=True, key="", geterror=False, returndict=False, returnq=False):
    # ---
    if add_date:
        quary = f"{quary}\n#{str(menet)}"
    # ---
    if printq is True:
        logger.info(quary)
    # ---
    json1 = get_query_data(quary)
    # ---
    qlist = []
    qdict = {}
    # ---
    if not json1:
        return qlist
    # ---
    heads = json1.get("head", {}).get("vars", [])
    var = sorted(heads)
    # ---
    bindings = json1.get("results", {}).get("bindings", [])
    # ---
    # {"P2875ar": {'xml:lang': "ar", "type": "literal", "value": 'تصنيف:صفحات تستخدم خاصية P655'}, "label": {'xml:lang': "ar", "type": "literal", "value": 'المُترجِم'}, "en": {'xml:lang': "en", "type": "literal", "value": "translator"}, "prop": {"type": "literal", "value": "655"}, "type": {"type": "literal", "value": "WikibaseItem"}, "Description": {'xml:lang': "ar", "type": "literal", "value": 'شخص ينقل نصاً مكتوباً من لغة إلى أخرى'}}
    # ---
    numb = 0
    # ---
    for result in bindings:
        s = {}
        # ---
        for vv in var:
            s[vv] = result.get(vv, {}).get("value", "")
        # ---
        qlist.append(s)
    # ---
    if returndict:
        for result in bindings:
            # ---
            numb += 1
            iid = numb
            # ---
            if key and key in result:
                iid = result[key]["value"]
            # ---
            if iid not in qdict:
                qdict[iid] = {}
            # ---
            for vv in var:
                if vv not in qdict[iid]:
                    qdict[iid][vv] = []
                # ---
                if vv in result:
                    if result[vv]["value"] not in qdict[iid][vv]:
                        qdict[iid][vv].append(result[vv]["value"])
    # ---
    logger.info(f"#sparql_generator_url:<<lightgreen>> {len(qlist)} items found. {menet}")
    # ---
    if returndict:
        return qdict
    # ---
    return qlist


def sparql_generator_big_results(spq, offset=0, limit=5000, alllimit=0):
    """Generate a list of results from a SPARQL query with pagination support.

    This function executes a SPARQL query and retrieves results in batches,
    handling pagination through the use of offset and limit parameters. It
    continues to fetch results until either all results are retrieved or a
    specified limit is reached. The function constructs the query
    dynamically based on the provided parameters and appends the results to
    a list, which is returned at the end.

    Args:
        spq (str): The SPARQL query string to be executed.
        offset (int?): The starting point for results retrieval.
            Defaults to 0.
        limit (int?): The maximum number of results to retrieve
            in each batch. Defaults to 5000.
        alllimit (int?): The total number of results to retrieve.
            If set, the function will stop fetching results once this limit
            is reached. Defaults to 0 (no limit).

    Returns:
        list: A list containing the results retrieved from the SPARQL query.
    """

    # ---
    if limit == 0:
        limit = 5000
    # ---
    if alllimit > 0 and alllimit <= limit:
        limit = alllimit
    # ---
    qua = spq
    # ---
    New_List = []
    # ---
    Keep = True
    off_set = offset if offset != 0 else 0
    # ---
    logger.info(f'qua "{qua}"')
    # ---
    while Keep:
        # ---
        quarry = qua
        # ---
        if limit != 0:
            quarry = f"{quarry}\n limit {str(limit)}"
        # ---
        if off_set != 0:
            quarry = f"{quarry} offset {str(off_set)}"
        # ---
        logger.info(f'limit:"{limit}"\t offset:"{off_set}"')
        # ---
        generator = sparql_generator_url(quarry)
        # ---
        for x in generator:
            New_List.append(x)
        # ---
        off_set = int(off_set + limit)
        # ---
        if alllimit != 0:
            if off_set == alllimit or off_set > alllimit:
                logger.info("Keep = False 1 ")
                Keep = False
        # ---
        if not generator or generator == [] or "nokeep" in sys.argv:
            logger.info("Keep = False 2 ")
            Keep = False
        # ---
        if limit == 0:
            logger.info("Keep = False 3 ")
            Keep = False
    # ---
    return New_List
