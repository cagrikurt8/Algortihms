import pandas as pd


movies_dframe = pd.read_csv('movies.csv', names=['Movie', 'Rating'])
movies_dict = movies_dframe.to_dict('split')

"""
Bubble Sort

for i in range(1, len(movies_dict['data'])):
    for j in range(1, len(movies_dict['data'])):
        curr_rating = movies_dict['data'][j - 1][1]
        next_rating = movies_dict['data'][j][1]

        if curr_rating > next_rating:
            movies_dict['data'][j - 1], movies_dict['data'][j] = movies_dict['data'][j], movies_dict['data'][j - 1]
"""


def merge_sort(data):
    if len(data) > 1:

        r = len(data)//2
        L = data[:r]
        M = data[r:]

        merge_sort(L)
        merge_sort(M)

        i = j = k = 0

        while i < len(L) and j < len(M):
            if L[i][1] < M[j][1]:
                data[k] = L[i]
                i += 1
            else:
                data[k] = M[j]
                j += 1
            k += 1

        while i < len(L):
            data[k] = L[i]
            i += 1
            k += 1

        while j < len(M):
            data[k] = M[j]
            j += 1
            k += 1


def binary_search(movies):
    low = 0
    high = len(movies['data']) - 1

    while low <= high:
        middle = high + low // 2

        if movies['data'][middle][1] == 6:
            lower_bound = middle - 1
            upper_bound = middle + 1

            while movies['data'][lower_bound - 1][1] == 6.0:
                lower_bound -= 1

            while movies['data'][upper_bound + 1][1] == 6.0:
                upper_bound += 1

            for idx in range(lower_bound, upper_bound):
                movie = movies['data'][idx][0]
                rating = movies['data'][idx][1]
                print(f"{movie} - {rating}")
            break

        elif movies['data'][middle][1] > 6:
            high = middle - 1

        elif movies['data'][middle][1] < 6:
            low = middle + 1


merge_sort(movies_dict['data'])
binary_search(movies_dict)
