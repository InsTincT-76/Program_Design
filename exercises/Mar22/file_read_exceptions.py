def getMovies():
    movies=[]
    try:
        with open("exercises/Mar22/movies.txt") as file:
            for line in file:
                movie = line.replace("\n", "")
                movies.append(movie)
    except FileNotFoundError:
        print("File could not be located")
        
        
    return movies



print("*** Awesome movie program ***")
movies = getMovies()

for movie in movies:
    print(movie)