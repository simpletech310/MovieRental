from os import system
import time
import ui.main as ui
import csv

def call_add_movie():
    ui.print_header()
    print('Add Movie')
    print()
    movie_title = input("Movie Title: ")
    movie_release_date = input("Movie Release Date: ")
    rating = input("Rating: ")
    number_of_units = input("How many do you have in stock?: ")

    fields = ['movie_title', 'movie_release_date', 'rating', 'number_of_units']
    rows = [[movie_title, movie_release_date, rating, number_of_units]]

    with open("data/movie.csv", 'a') as csvfile:
       # creating a csv writer object  
       csvwriter = csv.writer(csvfile) 

       if csvfile.tell() == 0:
           # writing the fields  
           csvwriter.writerow(fields)

       # writing the data rows  
       csvwriter.writerows(rows)
    
    system("clear")
    print("New movie added")
    time.sleep(3)

def call_edit_movie():
    pass

def call_find_movie():
    pass

def call_delete_movie():
    pass
