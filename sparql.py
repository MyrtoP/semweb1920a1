# Εάν η αναζήτηση είναι επιτυχής θα στέλνει δεύτερο ερώτημα (ένα μόνο) για να ανακτήσει τα ονόματα των συμπρωταγωνιστών του ηθοποιού και τα ονόματα των αντίστοιχων ταινιών.
from urllib.request import urlopen, Request
from urllib.parse import urlencode
import json


def sparql_select_query(query, endpoint):

    # params sent to server
    params = {'query': query}
    # create appropriate param string
    paramstr = urlencode(params)

    # create GET http request object with params appended
    req = Request(endpoint+paramstr)
    # request specific content type
    req.add_header('Accept', 'application/sparql-results+json')
    # dispatch request
    page = urlopen(req)

    # get response and close
    response = page.read().decode('utf-8')
    page.close()

    # convert to json object
    jso = json.loads(response)

    results = []
    # iterate over results
    for binding in jso['results']['bindings']:
        # for every column in binding
        result = {}
        for bname, bcontent in binding.items():
            result[bname] = bcontent['value']

        results.append(result)

    # return the list of result dicts
    return results


# define the endpoint
endpoint = "https://linkedmdb.lodbook.org/sparql?"

namestr = input('Give actor> ')

query = """
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX actor_name: <http://data.linkedmdb.org/resource/movie/actor_name>
PREFIX movie: <http://data.linkedmdb.org/resource/movie/>
SELECT ?actor WHERE {{
  ?actor a movie:actor .
  ?actor movie:actor_name "{}" .
}}
""".format(namestr)

# get results from endpoint
results = sparql_select_query(query, endpoint)

if results:

    actoruri = results[0]['actor']

    query = """
	PREFIX movie: <http://data.linkedmdb.org/resource/movie/>
	SELECT ?actorname ?filmname WHERE {{
	  ?film movie:actor <{name}> .
	  ?film movie:actor ?actor .
	  ?actor movie:actor_name ?actorname.
	  ?film rdfs:label ?filmname .
	  FILTER (?actor!=<{name}>)
	}}
	""".format(name=actoruri)

    # get results from endpoint
    results = sparql_select_query(query, endpoint)

    # process list of results here
    movies = {}
    for result in results:
        movies.setdefault(result['filmname'], []).append(result['actorname'])

    for movie, names in movies.items():
        print('{}:'.format(movie))
        for name in names:
            print('\t{}'.format(name))
