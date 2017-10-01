#! /usr/bin/env python3
import psycopg2


# Cutting out the reusable statements and created one function
def connect(DBNAME="news"):
    try:
        # Connecting to the database
        db = psycopg2.connect(database=DBNAME)
        # Runing queries to get the results
        c = db.cursor()
        return db, c
    except Exception:
        print("You are not connected to your database.")


# Function for getting the most popular articles
def query_1():

    # Connecting to connect function
    db, c = connect()
    # Execute query_1
    c.execute("SELECT title, count(*) AS views FROM articles, log WHERE " +
              "articles.slug=substring(log.path FROM 10) GROUP BY " +
              "articles.title ORDER BY views DESC LIMIT 3")
    # Get the results from the cursor
    results = c.fetchall()
    # Prints the 1st Question
    print("\nWhat are the most popular three articles of all time?\n")
    # Prints out the results that we are requesting
    for results in results:
        print(" \"{:}\" -- {:} views".format(results[0], results[1]))
    # Close database
    db.close()
    # Return results


# Function for geting the most popular authors
def query_2():

    # Connecting to connect function
    db, c = connect()
    # Execute query_2
    c.execute("SELECT authors.name, count(*) AS views " +
              "FROM authors, articles, log " +
              "WHERE authors.id = articles.author " +
              "AND log.path = concat('/article/', articles.slug) " +
              "GROUP BY authors.name " +
              "ORDER BY views DESC;")
    # Get the results from the cursor
    results = c.fetchall()
    # Prints the 2nd Question
    print("\nWho are the most popular article authors of all time?\n")
    # Prints out the results that we are requesting
    for results in results:
        print(" {:} -- {:} views".format(results[0], results[1]))
    # Close database
    db.close()
    # Return results


# Function for getting the results of 1% or higher in lead errors
def query_3():

    # Connecting to connect function
    db, c = connect()
    # Execute query_3
    c.execute("SELECT to_char(time, 'FMMonth DD, YYYY'), round(100.0*" +
              "sum(case log.status when '404 NOT FOUND' then 1 else 0 " +
              "end)/count(log.status), 2) AS error FROM log GROUP BY " +
              "to_char(time, 'FMMonth DD, YYYY') ORDER BY error DESC " +
              "LIMIT 1")
    # Get the results from the cursor
    results = c.fetchall()
    # Prints the 3rd Question
    print("\nOn which days did more than 1% of requests lead to errors? \n")
    # Prints out the results that we are requesting
    for results in results:
        print(" {:} -- {:}% errors".format(results[0], results[1]))
    # Close database
    db.close()
    # Return results


# Main function
def main():
    # Prints the query_1
    query_1()
    # Prints the query_2
    query_2()
    # Prints the query_3
    query_3()


# Everything correct print results below
if __name__ == '__main__':

    # Calls the function main()
    main()
