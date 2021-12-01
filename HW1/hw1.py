# CS210 Data Management for Data Science Project 1
# Umar Khattak and Aatif Sayed

# WILL NEED TO INSERT TEST FILE PATH INTO LINES 32, 55, AND 192

# Multiple values declared depend on previous files running with the test path file given)
# For example, read_ratings_data_dict = read_ratings_data("movieRatingSample.txt")
# read_ratings_data_dict is used as a parameter for other files

# Task 1.1

def read_ratings_data(f):
    array = []
    dictionary = {}

    with open (f, "r") as file:
        array = file.readlines()
    file.close()

    for i in range(len(array)):
        input = array[i][:-1].split("|")
        array[i] = [input[0], float(input[1])]
        
    for i in array:
        if i[0] not in dictionary:
            dictionary [i[0]] = []
        
        dictionary[i[0]].append(i[1])
    
    return dictionary 

read_ratings_data_dict = read_ratings_data("movieRatingSample.txt")
# INSERT PATH TO FILE IN ABOVE STRING, CURRENT FILE ABOVE IS THE TEST FILE GIVEN

# read_ratings_data_dict

# Task 1.2

def read_movie_genre(f):
    array = []
    dictionary  = {}
    
    with open (f, "r") as file:
        array = file.readlines()
    file.close()
    
    for i in range(len(array)):
        array[i] = array[i][:-1].split("|")
    
    for i in array:
        dictionary[i[2]] = i[0]
        
    return dictionary

read_movie_genre_dict = read_movie_genre("genreMovieSample.txt")
# INSERT PATH TO FILE IN ABOVE STRING, CURRENT FILE ABOVE IS THE TEST FILE GIVEN

# read_movie_genre_dict

# Task 2.1

def create_genre_dict(read_movie_genre_dict):
    dictionary = {}

    for i in read_movie_genre_dict.keys():
        x = read_movie_genre_dict[i]

        if not x in dictionary.keys():
            dictionary[x] = []

        dictionary[x].append(i);

    return dictionary
    
genre_to_movies_dict = create_genre_dict(read_movie_genre_dict)
# genre_to_movies_dict

# Task 2.2

def calculate_average_rating(read_ratings_data_dict):
    dictionary = {}

    for x in read_ratings_data_dict.keys():
        average = sum(read_ratings_data_dict[x])/len(read_ratings_data_dict[x])
        dictionary[x] = average

    return dictionary
    
avg_rating_dict = calculate_average_rating(read_ratings_data_dict)
# avg_rating_dict

# Task 3.1

def get_popular_movies(avg_rating_dict, n = 10):
    avg_rating_dict = dict(sorted(avg_rating_dict.items(), key=lambda item: -1*item[1]))
    length = len(avg_rating_dict)
    if length < n:
        return avg_rating_dict

    else:
        return dict(list(avg_rating_dict.items())[:n])
    
# get_popular_movies(avg_rating_dict, 10)

# Task 3.2

def filter_movies(avg_rating_dict, threshold_rating = 3):
    newDictionary = dict()

    for i, j in avg_rating_dict.items():
        if j >= threshold_rating:
            newDictionary[i] = j

    # indent here 
    return newDictionary

# filter_movies(avg_rating_dict, 3)

# Task 3.3

def get_popular_in_genre(genre, genre_to_movies_dict, avg_rating_dict, n = 5):
    dictionary = {}

    if(len(genre_to_movies_dict[genre]) < n):
        n = len(genre_to_movies_dict[genre])
        
    for i in genre_to_movies_dict[genre]:
        dictionary[i] = avg_rating_dict[i]
        
    newDictionary = get_popular_movies(dictionary, n)
    return newDictionary

# get_popular_in_genre("Action", genre_to_movies_dict, avg_rating_dict,5)

# Task 3.4

def get_genre_rating(genre, genre_to_movies_dict, avg_rating_dict):
    dictionary = {}
    x = 0
    y = 0

    for i in genre_to_movies_dict[genre]:
        x = x + avg_rating_dict[i]
        y = y + 1
        
    z = (x / y)
    dictionary[genre] = z
    return dictionary

# get_genre_rating("Action", genre_to_movies_dict, avg_rating_dict)

# Task 3.5

def genre_popularity(genre_to_movies_dict, avg_rating_dict, n=5):
    dictionary = {}
    #similar to get_popular_in_genre

    if(len(genre_to_movies_dict) < n):
        n = len(genre_to_movies_dict)
        
    for i in genre_to_movies_dict:
        dictionary[i] = get_genre_rating(i, genre_to_movies_dict, avg_rating_dict)[i]
        
    newDictionary = get_popular_movies(dictionary, n)
    return newDictionary

# genre_popularity(genre_to_movies_dict, avg_rating_dict, 5)

# Task 4.1

def read_user_rating(file):
    with open (file, "r") as file:
        array = file.readlines() 
        
    dictionary = {}

    for i in array: #declare dict outside
        arrayA = i.split("|")
        xVal = arrayA[0]
        yVal = arrayA[1]
        zVal = arrayA[2].replace("\n", "")
        if zVal not in dictionary:
            dictionary[zVal] = []
            dictionary[zVal].append((xVal, yVal))
        else:
            dictionary[zVal].append((xVal, yVal))

    return dictionary

# read_user_rating("movieRatingSample.txt")

read_user_ratings_dict = read_user_rating("movieRatingSample.txt")
# INSERT PATH TO FILE IN ABOVE STRING, CURRENT FILE ABOVE IS THE TEST FILE GIVEN

# read_user_ratings_dict

# Task 4.2

def get_user_genre(userId, read_user_ratings_dict, genre_to_movies_dict):
    dictionary = {}

    for i in read_user_ratings_dict[userId]:
        if(not genre_to_movies_dict[i[0]] in dictionary):
            dictionary[genre_to_movies_dict[i[0]]] = []
            dictionary[genre_to_movies_dict[i[0]]].append(float(i[1]))
        else:
            dictionary[genre_to_movies_dict[i[0]]].append(float(i[1]))

    newDictionary = calculate_average_rating(dictionary)
    finalDictionary = get_popular_movies(newDictionary, 1)
    result = list(finalDictionary.keys())[0]
    # return list(finalDictionary.keys())[0]
    return result

# get_user_genre(userId, read_user_ratings_dict, genre_to_movies_dict)

# Task 4.3

def recommend_movies(userId, read_user_ratings_dict, genre_to_movies_dict, avg_rating_dict):
    first_genre = get_user_genre(userId, read_user_ratings_dict, genre_to_movies_dict)
    genre = create_genre_dict(genre_to_movies_dict)
    genre = genre[first_genre]

    for i in genre:
        for tuple in read_user_ratings_dict[userId]:
            if i in tuple[0]:
                genre.remove(i)

    dictionary = {}

    for i in genre:
        dictionary[i] = avg_rating_dict[i]

    result = get_popular_movies(dictionary, 3)
    # return get_popular_movies(dictionary, 3)
    return result