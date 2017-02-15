import json
import os.path


if not os.path.exists('data.txt'):
    print('Database file doesn\'t exist! You have to run SecondTask.py script to create the file!')
else:
    print('Enter any query string:')
    query_string = input()

    all_movies = []
    query_movies = []
    with open('data.txt', 'r') as database_file:
        all_movies = json.load(database_file)

    for m in all_movies:
        if query_string.lower() in str(m['title']).lower():
            query_movies.append(m)

    print('Result of the query:')
    if len(query_movies) != 0:
        print('{} movie(s):'.format(len(query_movies)))
        for m in query_movies:
            print(m['title'])
    else:
        print('Nothing')