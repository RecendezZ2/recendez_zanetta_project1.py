# # BOOK COLLECTION MANAGER
# # Stores details about book and calculates inventory


# step 1
# diplay welcome mesage
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
print("This program tracks an individual collection of books and  calculates their total inventory value.\n")


# -delclaring a variable for author name, total pages, copies in stock and the price per book using the input function so users can write their dynamic response 
# Each input() returns a string, making it able to  convert # inputs to int or a float
author_name = input("Enter the author's name: ")
total_pages = int(input("Enter the total number of pages: "))
copies_in_stock = int(input("Enter the number of copies in stock: "))
price_per_book = float(input("Enter the price per book: $"))


#assigning the price per book multiplyed by the copies in stock to get the toql invengtory value
# Multiply price per book by number of copies to get total inventory value
total_inventory_value = price_per_book * copies_in_stock


# --- Display formatted summary with all attributes and calculated result ---
# Using f-strings  to insert variables and expressions directly into a string making it dynamic
# :.2f formats currency values to show exactly 2 decimal places
print("\nBOOK SUMMARY ")
print(f"Author: {author_name}")
print(f"Total pages: {total_pages}")
print(f"Copies in stock: {copies_in_stock}")
print(f"Price per book: ${price_per_book:.2f}")
print(f"Total inventory value: ${total_inventory_value:.2f}")
print("==================================")