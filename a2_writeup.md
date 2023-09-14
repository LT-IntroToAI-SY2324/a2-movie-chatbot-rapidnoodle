# Assignment 2 - Write UP

## Description
This assignment is about learning and applying the while loop and iterating through multiple lists at a time.  We also will discuss how we match things in chatbots in order to extract what a user is trying to find.  Next assignment we will work with data bases and how we can extract information from them.

## What to complete
1. Go through the notes.py file w/ Mr. Berg
2. Complete `a2.py`, Mr. Berg will walk everyone through the process
3. Make sure you pass all asserts in `a2.py`
4. Complete the reflection problems below
5. Push your code to github for grading

## Reflection Questions
1. What was difficult for you while completing the match function?
I found it difficult writing the functionality for the '%' pattern case because it could return a multitude of words or none at all.
This means that I had to write specific cases for each condition, but I commented each section, so the code doesn't look too messy.

2. Explain how you could use the match function for extracting information from a movie database.
I could retrieve movies with Robert Downey Jr (or any actor) playing in it from a database with the pattern of
['what', 'movies', 'have', '%', 'in', 'it'] and a source of ['what', 'movies', 'have', 'robert', 'downey', 'jr', 'in', 'it'].
I would insert this information into my match function and extract the actor to call an API and retrieve movies with that actor in it.
