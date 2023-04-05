#!/usr/bin/env python

#-----------------------------------------------------------------------
# database.py
# Author: Bob Dondero
#-----------------------------------------------------------------------

from sqlite3 import connect
from contextlib import closing

#-----------------------------------------------------------------------

_DATABASE_URL = 'file:penny.sqlite?mode=ro'

_DATABASE_URL = 'file:geonames.sqlite?mode=ro'

def search(author):

    books = []

    with connect(_DATABASE_URL, uri=True) as connection:

        with closing(connection.cursor()) as cursor:

            # query_str = "SELECT author, title, price FROM books "
            # query_str += "WHERE author LIKE ?"
            # cursor.execute(query_str, [author+'%'])

            # row = cursor.fetchone()
            # while row is not None:
            #     book = Book(str(row[0]), str(row[1]), float(row[2]))
            #     books.append(book)
            #     row = cursor.fetchone()

            # make a query retrieves information about all cities with names that begin with the current value. We want city, country, and timezone. The schema is CREATE TABLE country ( countrycode char(2) NOT NULL, countryname varchar(200) NOT NULL, PRIMARY KEY (countrycode) ); CREATE TABLE geonames ( geonameid int(10) NOT NULL default '0', `name` varchar(200) NOT NULL default '', countrycode char(2) NOT NULL, `population` bigint(11) default '0', timezone varchar(40), PRIMARY KEY (`geonameid`) FOREIGN KEY (countrycode) REFERENCES country(countrycode) ;

            cities = []

            # build the query string (return geonames.name, geonames.timezone, country.countryname) ). Use JOIN 
            query_str = "SELECT geonames.name, country.countryname, geonames.timezone FROM geonames JOIN country ON geonames.countrycode = country.countrycode WHERE LOWER(geonames.name) LIKE ?"
            cursor.execute(query_str, [author+'%'])

            # fetch the first row
            row = cursor.fetchone()
            # while there are rows to fetch
            while row is not None:
                # print(cities)
                # add the city to the list of cities
                cities.append((str(row[0]), str(row[1]), str(row[2])))
                # fetch the next row
                row = cursor.fetchone()

            # build the secoind query string (return geonames.name, geonames.timezone, country.countryname) ). Use JOIN. It's similar to the previous string but we do the where statement on the countryname instead of the city name
            query_str = "SELECT geonames.name, country.countryname, geonames.timezone FROM geonames JOIN country ON geonames.countrycode = country.countrycode WHERE LOWER(country.countryname) LIKE ?"
            cursor.execute(query_str, [author+'%'])

            # fetch the first row
            row = cursor.fetchone()
            # while there are rows to fetch
            while row is not None:
                # print(cities)
                # add the city to the list of cities
                cities.append((str(row[0]), str(row[1]), str(row[2])))
                # fetch the next row
                row = cursor.fetchone()

            # return cities


    return cities




    # return books

#-----------------------------------------------------------------------

# For testing:

def _test():
    books = search('Kernighan')
    for book in books:
        print(book.get_author())
        print(book.get_title())
        print(book.get_price())
        print()

if __name__ == '__main__':
    _test()
