# Notes about Flask....

## How it works

The 'runner.py' will execute the 'run' function. This function will start the app; this should open a localhost port. After that, we can control web traffic. For specific types of requests, we can view the request data and package our dyanamic webpage response. You are welcome to reference my old project to see an example of this working.

## myGymClub.db database reference

The myGymClub.db generated currently includes the table(s):

User_Record:
    username (TEXT) -> Username of the user
    password (TEXT) -> Password of the user 
    isAdmin (INTEGER) -> Number that's either 0 or 1 signaling if a user is an admin or not

## Project Reference

https://github.com/milkchocolatejr/Home-Listing-and-Price-Explorer/tree/main

The files are named similarly. This is a larger scale example of Flask at work from CS 480.