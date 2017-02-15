import urllib.request
import urllib.parse
import json
import os.path


def load_json_data_from_url(base_url, url_params):
    url = '%s?%s' % (base_url, urllib.parse.urlencode(url_params))
    response = urllib.request.urlopen(url).read().decode('utf-8')
    return json.loads(response)

def make_tmdb_api_request(method, api_key, extra_params=None):
    extra_params = extra_params or {}
    url = 'https://api.themoviedb.org/3%s' % method
    params = {
        'api_key': api_key
    }
    params.update(extra_params)
    return load_json_data_from_url(url, params)


file_name = 'data.txt'
if not os.path.exists(file_name):
    movies = []
    try:
        #for i in range(1, 2):
        for i in range(1, 51):
            page_results = make_tmdb_api_request(method='/discover/movie', api_key='50343efe17481663862b837e642cb6d0',
                                                 extra_params={'page': i})['results']
            for m in page_results:
                movies.append(make_tmdb_api_request(method='/movie/{}'.format(m['id']), api_key='50343efe17481663862b837e642cb6d0'))
        with open(file_name, 'w') as database_file:
            json.dump(movies, database_file)
    except:
        print("Something went wrong!")
    else:
        print('Database file has been created successfully!')
else:
    print('Database file is already exists!')