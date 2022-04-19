class Movie:
    def __init__(self, title, description, actor1, actor2, actor3, genre, rating):
        self.title=title
        self.description=description
        self.actors=(actor1,actor2, actor3)
        self.genre=genre
        self.rating=rating
        
 
    def display(self):
     
        print(f"***{self.title}***")
        print(f"{self.description}")
        for actor in self.actors:
            print(f"Stars: - {actor}")
        print(f"Genre:{self.genre}")
        print(f"Rating:{self.rating} stars")
    
            
    def list_actors(self):
        for i in range(len(self.actors)):
            print(f"{i+1}. {self.answers[i]}")
        
        
    def is_match(self,title):
        if title == self.title.lower():
            return True
    
        return False
        
        

            
