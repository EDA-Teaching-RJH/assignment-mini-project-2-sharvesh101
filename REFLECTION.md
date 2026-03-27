EENG4101 Fundamentals of Programming — Mini Project 2

I made a command-line inventory system for an electronics store. It lets you add,
remove, search and update products. All the data is saved to a CSV file so it
is not lost when you close the program.

I made a Product class and an Electronics class that inherits
from it. This came from the OOP workshops. Electronics uses super() to get the
shared attributes from Product.

I used the csv module to save and load products from inventory.csv.

I used try/except in my validators to catch bad input like
letters where a number is expected.
I also added a function to check the csv file exists in current path ot it creates one.

The hardest part was loading products back from the CSV correctly. Everything
comes back as a string so I had to convert price to float and quantity to int
manually.

I also created a function to make a random product ID 
I also had to make sure generated product IDs were unique by checking the
inventory before returning a new one, or it would break will acessing the data. 