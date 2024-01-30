# Exercise 6: Data Integration — Transformation practice

In the data folder can find a file called `BI_ZH.csv`, this file contains the midterm results of the subject from a previous year. The file does not contain the final grades, only the number of points. Your job is to create a Pentaho Data Integration Transformation to do the following:

1. Calculate the final grade based on the points (Grading was the following: **1** ... < 25 points, 25 <= **2** < 30, 30 <= **3** < 35, 35 <= **4** < 40, 40 <= ... **5**)
1. Create a final grouping for each individual grade (i.e. there were N students with grade 2, K students with grade 3...)
1. Save the output to a JSON file `ex6-excellents.json` if the student received a 5 as a grade.

!!! note ""
    Write your NEPTUN code after the _Number range_ step name!

When done, save the file with the following name: `ex6-transformation2.ktr`! 

A few tips for help:

- Use the _Number range_ block for associating the points to grades
- Set _Number of rows in a bloc_ to 0 in the JSON Output to avoid lines overwriting each other

!!! example "SUBMISSION"
    Save this file as `ex6-transformation2.ktr`

    Save the JSON as `ex6-excellents.json`

    Create a screenshot of the executed job flow and save it as `ex6-transformation2-flow.png`. Make sure that all the nodes including your Neptun code are visible on this screenshot.

    Create a screenshot of the beginning of the JSON file and save it as `ex6-excellents.png`