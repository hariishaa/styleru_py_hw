import json
import os.path


if not os.path.exists('data.txt'):
    print('Database file doesn\'t exist! You have to run SecondTask.py script to create the file!')
else:
    print('Enter the precise movie name:')
    movie_name = input()

    all_movies = []
    with open('data.txt', 'r') as database_file:
        all_movies = json.load(database_file)

    base_movie = None
    for m in all_movies:
        if movie_name.lower() == str(m['title']).lower():
            base_movie = m
            all_movies.remove(m)
            break

    if base_movie is not None:
        recommended_movies = []
        # рекоммендация по году выпуска
        for m in all_movies:
            if (str(base_movie['release_date']))[:4] == (str(m['release_date']))[:4]:
                recommended_movies.append(m)

        print('Recommended movie(s):')
        if len(recommended_movies) != 0:
            for m in recommended_movies:
                print(m['title'])
        else:
            print('Nothing')
    else:
        print('Oops! The entered movie name hasn\'t been found in database!')