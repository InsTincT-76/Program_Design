from movie import Movie

movies = (
    Movie("No Time to Die", "James Bond has left active service", "Daniel Craig", "Ana de Armas", "Rami Malek", "Thriller", 7.4),
    Movie("The Last Letter from Your Lover", "A pair of interwovwn stories set in the past and present", "Shaileen woodley", "Joe Alwyn", "Wendy Nottingham", "Romance", 6.7),
    Movie("Passing", "Passing, follows the unexpected reunion of two high school friends", "Tessa Thompson", "Ruth Negga", "Andre Holland", "Drama", 6.6),
    Movie("Last Night in Soho", "An aspiring fashion designer is mysteriously able to enter the 1960s", "Thomasin Mckenzie", "Anya Taylor-Joy", "Matt Smith", "Mystery", 7.2)

)


print("***  Movie Listings  ***")


while True:
    command = input("(L)ist all movies, get a movie (D)etails, or (Q)uit: ").strip().lower()
    
    if command == "q":
        break
    
    elif command == "l":
         for movie in movies:
            movie.display()
            
            
    elif command == "d":
        title = input("Enter Movie name:  ").strip().lower()
        for movie in movies:
            if movie.is_match(title):
                movie.display()
                
                
    else:
        print("Invalid command")
        
print("Goodbye")