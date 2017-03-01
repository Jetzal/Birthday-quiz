"""
birthday.py
Author: <your name here>
Credit: <list sources used, if any>
Assignment:

Your program will ask the user the following questions, in this order:

1. Their name.
2. The name of the month they were born in (e.g. "September").
3. The year they were born in (e.g. "1962").
4. The day they were born on (e.g. "11").

If the user's birthday fell on October 31, then respond with:

  You were born on Halloween!

If the user's birthday fell on today's date, then respond with:

  Happy birthday!

Otherwise respond with a statement like this:

  Peter, you are a winter baby of the nineties.

Example Session

  Hello, what is your name? Eric
  Hi Eric, what was the name of the month you were born in? September
  And what year were you born in, Eric? 1972
  And the day? 11
  Eric, you are a fall baby of the stone age.
"""
from datetime import datetime
from calendar import month_name
todaymonth = datetime.today().month
todaydate = datetime.today().day

name =  ( input("Hello, what is your name?"))
month =  (input("Hi "+name+", what was the name of the month you were born in?"))
year =  ( input("And what year were you born in," +name+"?"))
day =  ( input("And the day?"))




if month == "January": 
    season= "winter"
if month == "Febuary":
     season= "winter"
if month == "March":
    season="spring"
if month == "April":
    season="spring"
if month == "May":
    season ="spring"
if month == "June":
    season="summer"
if month == "July":
    season="summer"
if month == "August":
    season="summer"
if month == "September":
    season="fall"
if month == "October":
    season="fall"
if month == "November":
    season="fall"
if month == "December":
     season="winter"
    
#Years from 1980-1989 are known as the eighties.

#Years from 1990-1999 are known as the nineties.

#Years from 2000 through today are known as the two thousands.

#Years prior to 1980 are known as the Stone Age.


if int(year) >= 2000:
    age="two thousands"
if int(year) >= 1990 and int(year) <=1999:
    age="nineties"
if int(year) >= 1980 and int(year) <= 1989:
    age="eighties"
if int(year) <= 1980:
    age="the Stone Age"
    
todaymonth = datetime.today().month
todaydate = datetime.today().day

TMONTH = month_name[todaymonth]

if month == TMONTH and day == int(todaydate):
    print("Happy birthday!")
elif month == "October" and day == "31":
    print("You were born on Halloween!")
else:
    print(""+name+", you are a "+season+" baby of the " +age+"")