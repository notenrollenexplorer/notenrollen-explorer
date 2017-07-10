def dbp_request(search_term):
    from SPARQLWrapper import SPARQLWrapper
    import re

    with open('composer_request.sparql' ,'r') as f:
        query = f.read()

    query = query.replace("SEARCH_TERM", search_term)

    sparql = SPARQLWrapper("http://dbpedia.org/sparql")
    sparql.setQuery(query)
    try :
       result = sparql.query()
    except:
       print("request failed")

    xml=""

    for line in result:
        xml+=str(line)

    #clean xml from control sequences 
    #dirty hack since sub ignores escaped special chars by some reason
    xml=re.sub("^b'|'$","",xml).replace("\\n'b'","")

    return xml