# # BOOK COLLECTION MANAGER
# # Stores details about book and calculates inventory


# step 1
# display welcome message
# Welcome message 	print("Welcome to the Book Collection Manager!")
# step 2
# My program description
# print("This program tracks individual books...")
# step 3
# Four attributes with function input() author, pages, copies, & price
# 	data type used int() pages/copies, float() price
# step 4 
# Meaningful calculation 2+ attributes	used to make calculation total_inventory_value = price_per_book * copies_in_stock
# step 5
# Final print section with all values labeled
# step 6
#  use f-string	All five summary lines use f-strings
# Planning table comment- top of the file and using descriptive varible names author_name, total_pages, copies_in_stock, price_per_book
#   
# -----------------------------------

# Collection Theme: Book Collection Manager
# Item Name: Book
#
# Attribute         | Data Type  | Example Value
# ----------------- | ---------- | -------------
# author_name       | string     | J.R.R. Tolkien
# total_pages       | integer    | 310
# copies_in_stock   | integer    | 3
# price_per_book    | float      | 15.99
#
# Calculation       | Formula                    | Purpose
# ----------------- | -------------------------- | -------------------------
# total_inventory_value | price_per_book * copies_in_stock | Find total monetary value of all copies



# -print() fuction passes the string argument to show user the Welcome/display message
#
print("Welcome to Zanetta's Book Collection Manager!")
print("When your ready to start the compilers handy dandy robot will help you along the way")
print("This program tracks an individual collection of books and  calculates their total inventory value.\n")



# # -setting  a variable for author name, total pages, copies in stock and the price per book using the input function so users can write their dynamic response 
# # Each input() returns a string, making it able to  convert # inputs to int or a float
# author_name = input("May I ask you what the Authors name?")


# #assigning the price per book multiplied by the copies in stock to get the l inventory value
# # Multiply price per book by number of copies to get total inventory value
# total_inventory_value = price_per_book * copies_in_stock


# print("\nBOOK SUMMARY ")
# print(f"Author: {author_name}")
# print(f"Total pages: {total_pages}")
# print(f"Copies in stock: {copies_in_stock}")
# print(f"Price per book: ${price_per_book:.2f}")
# print(f"Total inventory value: ${total_inventory_value:.2f}")
# print("==================================")


# I had confused my self with this project. I was not understanding what python was or how it worked. It didn't register to me that its just the key fundamentals written with different syntax and its not a frontend language. Same fundamentals different syntax but both have static and dynamic codes that grabs data or interacts with the user. Defining a function/code block requires and : in Py and ; in Js. Basically python is all code alot of backend. 


# I am commenting out the code i have already written so I can rebuild this project
# using my normal workflow. Now that I better understand of Python if that is ok as you said not to delete anything we write just comment out.


#notes --
#slow down and read the instructions
#pseudocode 
#code test code 
#clean and comment 
#test 
#slow down and reread the instructions 

# ✅
# step one
# start
# 
# create an empty list called book-collection a book disctionary list
# render "welcome to worlds best book collection ever"
# render "this program will keep you in a trance by its wonderful algorithm that tracks books/calculates  total inventory"
#its going to run like an infinity loop REPEAT FOREVER duh duh duhn...

# ❌
# I re read the instructions and started my notes over  so i had to fix my code 
# ✅
#start step 1
#create a empty variable called book_collection = [] 
# def a function called book_menu() that will  display a organized list 
#                              
# book_menu()
#     print "--- Book Collection Menu ---"
# "1. Add a book"
#  "2. View all books"
# "3. Calculate inventory value"
# "4. Quit"
# input user choice 
# return user choice
 # ✅
 #step 2 
#create a function that will get the positive inter possible argument parameter situation 
#this is where i will create my if else condition that will check to see if the value is a whole number and not a float
#print 
#input 
#if value is not a whole then print nope enter a whole number
#elif value is > 0 print um u # > then 0
#elif return value 
#end if 
#end of this function

#  ❌✅
#step 3
#create a function that will show a valid decimal price greater then zero 
# use a while loop - check condition if true exectue keep running the code until its no true then you stop 
# book_collection = [] this is a global and i dont need it because It in my main function
#  Use try/except so the program does not crash
#  Ask the user for input using the prompt argument
# Convert the input into an integer using int()
#  If the number is less than or equal to 0
#   print an error message
# -Otherwise:
#   return the number
# If the user enters letters, decimals, or invalid data
#  Catch ValueError
# Print a message telling the user to enter a whole number
# ⬜️ 

# STEP 4: Create a function for a valid price
# Define a function called get_positive_price(prompt).
# Use a while True loop so the program continues asking
# until the user enters a valid price.
#
# Inside the loop:
#  Use try/except 
# -Ask the user for input using the prompt argument.
# - Convert the input into a float using float().
# - If the price is less than or equal to 0:
#   print an error message.
# - Otherwise:
#   return the price.
# If the user enters invalid text:
# - Catch ValueError.
# - Print an example such as 15.99.


# STEP 5: Create the add_book function
# Define a function called add_book(book_collection).
# Display a heading: "--- Add a Book ---"
# Ask the user for:
#  Book title
#  Author name
#  Total pages
#  Number of copies in stock
#  Price per book
#Use get_positive_integer() for:
#  Total pages
# -Copies in stock
#Use get_positive_price() for:
# Price per book
#Calculate the individual book inventory value:
# total_inventory_value = price_per_book * copies_in_stock
#Create a dictionary list called new_book
# Store all book information in the dictionary:
#  title
#  author_name
# total_pages
# copies_in_stock
#price_per_book
# total_inventory_value
#use append to add a bnook to the collection
# Append new_book to book_collection
# Print a success message
# Print the inventory value of the new book
# ✅
# STEP 6
#  Create the remove_book function
# Define a function called remove_book(book_collection, title_to_remove)
#
# Loop through every book dictionary in book_collection
#
# Compare the entered title with each saved book title
# lower() string method on both titles so capitalization does not matter
#If the titles match:
# Remove that book dictionary from book_collection
#  Return True to show that a book was removed
#If the loop finishes and no title matches----->
# Return False
#✅

# STEP 7
#  Create the display_books function
# Define a function called display_books(book_collection)
#Print a heading: "--- #1 Book Collection ---"
# Check whether book_collection is empty
# If the list length is 0
# - Print "close but no cigar"
# - Return so the rest of the function does not run.
#Otherwise
#  Use enumerate(book_collection, start=1) that zeros index but i can use any number so its going to start at uno
# for loop through each book dictionary index
#  Print the number of each book
# Print the author name
# Print the total pages
#  Print copies in stock
# print the price per book formatted to two decimal places
# print the book inventory value formatted to two decimal places
# using  in enumerate

# ✅
# STEP 8
# make the calculate_inventory_value function
# set a variable called calculate_inventory_value(book_collection).
#variable called total_value = 0.
#Loop through every book in book_collection.
# Add each book's total_inventory_value to total_value.
#inventory value
# 
#  ✅


# STEP 9
#  Create the main function
# Define a function called main()
#Create an empty book_collection list inside main()
# a welcome message
#short description of what the program does
#use a while True loop to keep the menu running until its stopped
#inside the loop:
# call show_menu()
# have the returned choice in a variable named choice
#Use if/elif statements to check the user's menu choice
#Otherwise
# print an nope invalid  
# Step 10 Start the program
# function call main() to start the program

#-------------------------------------------------------------------
✅
# 
# -----------------------------------
# Book Collection Manager
# Stores book details and calculates inventory value.
# -----------------------------------


# Collection Theme: Book Collection Manager
# Item Name: Book
#
# Attribute               | Data Type | Example Value
# ----------------------- | --------- | ----------------
# title                   | string    | The Hobbit
# author_name             | string    | J.R.R. Tolkien
# total_pages             | integer   | 310
# copies_in_stock         | integer   | 3
# price_per_book          | float     | 15.99
# total_inventory_value   | float     | 47.97
#
# Calculation:
# total_inventory_value = price_per_book * copies_in_stock

# ✅✅✅✅✅✅✅✅✅ 

#  defining a function called book show menu that will render input area for the user
def show_menu():
# print function with different  string options that moves the cursor to a start a new fresh line 
    print("\n---Hello, I am futuristic robot managing Zanetta's collection please choose from the options below,  ---")
    print("1 Add a book")
    print("2 Remove a book")
    print("3 View all books")
    print("4 Calculate inventory value")
    print("5 Quit")
# choice variable with the value of users choice 
    choice = input("Choose an option (1-5): ")
    # the return statement stops the code immediately with in the code block returns the value back to the function  and shows the choice to user
    return choice



# defining   functions  that gets a number greater then 0 using a while true. 
def get_positive_integer(prompt):
    #while true is an infinity loop that will run until its told to stop. 
    # break statement is needed to instantly stop the loops and execute the next line of code
    while True:
        #try: starting point of handling errors with out a crash its tries running the code, but if a specific error comes up  don't crash its just goes to the next next best thing its always has at least one except: block, creating a structure known as a try-except block where python will catch errors handle them and not crash 
        try:
            value = int(input(prompt))


#  if else  statement checks if the value is smaller then or equal to 0 print this else or otherwise stop the code and return the value
            if value <= 0:
                print("Please enter a number that is 0 or greater.")
            else:
                return value
# a ValueError happens when argument passed into the function is the correct data type but an invalid value for example if Im putting a test string of letters when there should be a number that is greater then 0
        except ValueError:
            print("Read out loud in robot voice--->🤖 You did not enter a valid number!!! Does not compute!!!.")



#  defining a function with a prompt as the  perameter will show to the user 

def get_positive_price(prompt):
    #while True is an infinity loop that will run until its told stop its break: is used to make the loop stop and run the next line of code
    while True:
        #  #try: starting point of handling errors straightly maken sure it does not crash. it tries running the code, but if a specific error comes up it wont  crash instead it moves on to the next best line of code.its always has at least one except: block, building a solid structure known as a try-except block here python will  catch the error  and moves on to the next working line of code all while not crashing 
        try: 
            
            price = float(input(prompt))


            if price < 0:
                print("Please enter a price that is 0 or greater.")
            else:
                return price


        except ValueError:
            print("Invalid input. Please enter a valid price, such as 15.99.")



# Add to the book's book collection dictionary list
def add_book(book_collection):
    print("\n--- Add a Book ---")


    title = input("Enter the book title: ")
    author_name = input("Enter the author's name: ")


    total_pages = get_positive_integer(
        "Enter the total number of pages front to back : "
    )


    copies_in_stock = get_positive_integer(
        "Enter the number of copies in stock both Hard Cover and Paper Back copies: "
    )


    price_per_book = get_positive_price(
        "Enter the price per book: $"
    )


    total_inventory_value = price_per_book * copies_in_stock

# creating a new book dictionary list
    new_book = {
        "title": title,
        "author_name": author_name,
        "total_pages": total_pages,
        "copies_in_stock": copies_in_stock,
        "price_per_book": price_per_book,
        "total_inventory_value": total_inventory_value
    }

# using the list method append() to add a new book to the list
    book_collection.append(new_book)


    print(f'\n"{title}" was successfully added to the collection. Way to go! ')
    print(f"Inventory value for this book: ${total_inventory_value:.2f}.")



# uses remove() to remove the first book whose title matches the input
# Returns True if a book was removed and False if no book was found.
def remove_book(book_collection, title_to_remove):
    for book in book_collection:
    #  lower()is Pystring method that returns a version of text where uppercase letters become lowercase letters only.
    #  if value is equal to value 
        if book["title"].lower() == title_to_remove.lower():
            #function block stating to remove book from the collection 
            book_collection.remove(book)

            #two return statements for the boolean result 
            return True


    return False



# a display_books function that uses the parameter of book_collection to display the books 
def display_books(book_collection):
    print("\n--- Book Collection ---")

# if length of book collection is == 0 
    if len(book_collection) == 0:
        print("There are no books in the collection.")
        #prevents the loops from continuing if there is no more books
        return

    #a for index loop that goes threw the books starting the count at 1 
    #in enumerate() is a for loop functions that  keeps track of items being looped threw and uses zero indexing but can be started at any number 
    for index, book in enumerate(book_collection, start=1):
        print("\n==================================")
        #formated string also know as f-string similar  to a temperate literal in js
        print(f"Book {index}")
        print(f"Title: {book['title']}")
        print(f"Author: {book['author_name']}")
        print(f"Total Pages: {book['total_pages']}")
        print(f"Copies in Stock: {book['copies_in_stock']}")
        print(f"Price per Book: ${book['price_per_book']:.2f}")
        print(
            f"Book Inventory Value: "
            f"${book['total_inventory_value']:.2f}"
        )


    print("==================================")



# Calculates and displays the total inventory value of all books.
def calculate_inventory_value(book_collection):
    total_value = 0


    for book in book_collection:
        total_value += book["total_inventory_value"]


    print("\n--- Inventory Value ---")
    print(f"Total collection inventory value: ${total_value:.2f}")



# Controls the program menu loop.
def main():
    # This empty list holds every book dictionary added during this session.
    book_collection = []


    print("THE Amazing Futuristic Book Collection Manager!")
    print("This program tracks books and calculates total inventory value.")


    # The menu keeps running until the user chooses option 5.
    while True:
        choice = show_menu()


        if choice == "1":
            add_book(book_collection)


        elif choice == "2":
            title_to_remove = input(
                " Enter the title of the book to remove: "
            )


            was_removed = remove_book(
                book_collection,
                title_to_remove
            )


            if was_removed:
                print(f'"{title_to_remove}" was removed successfully.')
            else:
                print(f'No book titled "{title_to_remove}" was found.')


        elif choice == "3":
            display_books(book_collection)


        elif choice == "4":
            calculate_inventory_value(book_collection)


        elif choice == "5":
            print("\nThank you for using the Book Collection Manager.")
            break


        else:
            print("\nInvalid choice. Please enter 1, 2, 3, 4, or 5.")



# function that starts the whole program
main()
