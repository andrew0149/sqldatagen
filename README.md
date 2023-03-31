# SQL Data Gen

A little script that will help you generate some sample data for your SQL database.

## Why this exists

At university, I had a course that included a couple of projects that needed to use PostgreSQL. Lector gave us links to online tools that we could use to generate sample data for our databases but I really didn't like any of them cause they didn't truly work the way I needed. So I decided to write this tool to probably use it in my future projects and let you use it.

## Getting started

1) Clone or download repository
2) You must have **python3** installed to use **sqldatagen**, so install it if you haven't already
3) Enter the repository directory
4) Install the required python packages with
`pip3 install -r requirements.txt`

Now you can finally run the script!

## How to use

### Usage:
### `$ python3 sqldatagen.py`

After running that command you'll get access to CLI which will grant you an oppotunity to choose the amount of rows you'll need in your table, the names of columns, and datatypes for them.

After generation you will be asked a delimiter for .CSV file to use, and the name for that file.

Finally, the script will suggest a preview of 10 rows of the table you've generated.

### Currently available datatypes:
+ **Autoincrement** - integer numbers from starting with start index 
+ **Integer** - random integer numbers from the interval
+ **Float** - random float numbers from the interval with the specified accuracy 
+ **List element** - random lines from the specified .txt file
+ **Name** - random names from `lists/names.txt`
+ **Surname** - random surnames from `lists/surnames.txt`
+ **Full name** - random full names which are made up by concatenating names from `lists/names.txt` and surnames from `lists/surnames.txt`
+ **Phone number** - random phone numbers of specified mask
+ **Date** - random date from interval
+ **Date with timestamp** - random timestamp from interval

