# database
> This is a Class I made for using sqlite3. And I wanted to get a better understanding of OOP.

## Table of Contents
* [General Info](#general-information)
* [Technologies Used](#technologies-used)
* [Features](#features)
* [Usage](#usage)
* [Project Status](#project-status)
* [Acknowledgements](#acknowledgements)


## General Information
- Has the features I used the most in sqlite3.
- Helps me not have to duplicte lines of code for connecting to sqlite.


## Technologies Used
- Python 3.9.9
- Sqlite3


## Features
- Querry data
- Add, Edit, Update, Search and Delete records in sqlite.
- Add, Edit, Update, Copy and Delete Tables in sqlite.


## Usage
Database object:

`database = 'Test.db'`

Connect to a table:

`table_name = 'test_table'`

`connect = Database(database, table_name)`

Querry the data:

`data = connect.querry()`


## Project Status
Project is: _complete_. I'm sure there is more to add, but not for any of my needs.


## Acknowledgements
- [Object Oriented Programming with Python - Full Course for Beginners](https://youtu.be/Ej_02ICOIgs).
