# Notes about Flask....

## How it works

The 'runner.py' will execute the 'run' function. This function will start the app; this should open a localhost port. After that, we can control web traffic. For specific types of requests, we can view the request data and package our dyanamic webpage response. You are welcome to reference my old project to see an example of this working.

## myGymClub.db database reference

The myGymClub.db database generated currently includes the tables:

User_Records(username, password, isAdmin, experience):

    username - text not null

    password - text not null

    isAdmin - integer not null

    experience - integer not null

Goals(username, exercise_name, style, reps, rep_type, sets, frequency, freq_type, memo):

    username - text not null

    exercise_name - text not null

    style - text not null

        Habitual

        Progress

    reps - integer

    rep_type - string

        minutes

        miles

    sets - integer

    frequency - integer

    freq_type - text

        day, week, month

    memo - text (optional for user)


## Project Reference

https://github.com/milkchocolatejr/Home-Listing-and-Price-Explorer/tree/main

The files are named similarly. This is a larger scale example of Flask at work from CS 480.