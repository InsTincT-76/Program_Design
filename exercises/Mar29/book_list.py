
FILE_NAME = "exercises/Mar29/books.txt"


def write_books(books):
    with open(FILE_NAME,"w") as file:
        for book in books:
            file.write(book + "\n")
            
            
def read_books():
    books=[]
    with open(FILE_NAME) as file:
        for line in file:
            line=line.replace("\n","").strip()
            books.append(line)
            
    return books



def list_books(books):
    for i in range(len(books)):
        print(f"{i+1}. {books[i]}")
        
       
       
def add_book(books):
    book = input("Book: ").strip()
    books.append(book)
    write_books(books)
    print(f"{book} was added.")
    return books

def delete_book(books):
    index = int(input("Enter book number:  ")) - 1
    
    if index < 0 or index >= len(books):
        print(f"Sorry, valid numbers are between 1 and {len(books)}")
        
        
    else:
        book = books.pop(index)
        write_books(books)
        print(f"{book} was deleted")
    return books
        
        
        
while True:
    command = input("Enter (L)ist, (A)dd, (D)elete, or (Q)uit:  ").lower().strip()
    books = read_books()

    
    if command=="l":
        list_books(books)
    
    elif command =="a":
        books = add_book(books)
        
        
    elif command =="d":
        books = delete_book(books)
        
    elif command =="q":
        break
    
    else:
        print("Invalid command, try again.")
        
print("Goodbye")