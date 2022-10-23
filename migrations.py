########## E X E R C I S E S ##########
#
#  Exercise 1: Add a new column for saving the publish date.
#  Exercise 2: Add a route to run the migrations.
#  Exercise 3: Handle the runtime error while adding the new column.
#  Exercise 4: Add a publish date in the existing blog posts.
#
#  Bonus: Change the format of the date.
# 
# Homework 1: Add date when inserting new blog post 
#             In the file post_models.py
#             Inside insert_post(),
#             - Inside the existing insert query, add the column published_on.
#             
#             In the file views.py
#             - Import date class from the datetime module.
#             Inside new_post()
#             - In the post_data object, add another key published_on.
#             - Give a value of date.today() to the above key.
# 
# Homework 2: Show tags of each blog post.
#             In the file macros.html
#             Inside macro blog_post()
#              - Split the post.tags with , using the split function.
#              - Add a for loop, to go through above tags.
#              - Inside the for loop, add a span tag to show above tag.
#              - Style the above tag using the Bootstrap component.
#                https://getbootstrap.com/docs/5.1/components/badge/
#
############################################################
from datetime import date
from .connection import get_db

def add_publish_date():
    connection = get_db()
    sql = connection.cursor()
    sql.execute('''alter table BlogPosts
                     add published_on Text''')

def insert_dates():
    connection = get_db()
    sql = connection.cursor()
    
    sql.execute('''
    update BlogPosts
    set published_on=?
    where published_on is null
    ''', [date.today()])
    
    connection.commit()
