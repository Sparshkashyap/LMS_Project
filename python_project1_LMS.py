book=["harry potter","the vedass","bhagwat geeta","the pikachu","the inshoniga"]
isshued_book=[]

def display():
    global book
    for boo in range(len(book)):
        print(str(boo+1)+".",book[boo])

# display(book)
def addbook():
    books=input("Enter the book name which you are added in the library :")
    book.append(books)
    print()
    print("the book has been added in the library sucessfully!")



# addbook(books)
# print()
# print(book)
# print()

def delete_book():
    book_id=int(input("Enter the book id number which you are delete or rempove in the library:"))
    book.pop(book_id-1)
    print()
    print("The book has been deleted by the library successfully!")


#book_id=int(input("Enter the book id number which you are delete or rempove in the library:"))
# delete_book(book_id)
# print()
# print(book)


def isshu_book():
    book_id=int(input("Enter the book id which you are isshued :"))
    isshued_book.append(book[book_id-1])
    book.pop(book_id-1)
    print()
    print("The book has been isshued by the library successfully!")
print(f"Isshued book list :{isshued_book}")



def isshu_book_show():
    for boo in range(len(isshued_book)):
        print(str(boo+1)+".",isshued_book[boo])

    print("The list of the isshued book in front of you")    



# isshu_book(isshu_book_id)
# print()
# print(isshued_book)

def return_book():
    book_id=int(input("Enter the book id which you are returned :"))
    if len(isshued_book)<book_id:
        print("This book is not isshued by the library 'jo app vapas kar rahe ho'")
    else:
        book.append(isshued_book[book_id-1])
        isshued_book.pop(book_id-1)
        print()
        print("The book has been returned by the library successfully!")



# return_book(book_id)
# print()
# print(book)
while 1:
    print("============================RESTART==============================")
    print("1.Display all the books")
    print("2.Add a book")
    print("3.Remove or pop a book")
    print("4.Isshued a book")
    print("5.Show the all Isshued book list")
    print("6.Return a book")
    print("7.Exit")
    user=int(input("Enter your choice: "))
    print()
    #print("============================RESTART==============================")
    if user==1:
        display()
    elif user==2:
        addbook()
    elif user==3:
        delete_book()
    elif user==4:
        isshu_book()
    elif user==5:
        isshu_book_show()
    elif user==6:
        return_book()
    else:
        False
        break




