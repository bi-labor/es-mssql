# Exercise 6: Create a report listing the highest rated books

In this exercise you are required to create a new report using Reporting Services.

1. Create a report that lists the **top 10 highest rated books** in a table.

   The report should be edited in solution `ex6.sln` in file `books.rdl`.

   - The top 10 books should be presented as a table displaying the title, author, publication year, average rating, and the cover image of the book (using the medium sized image URL from the dataset).

   - Use an _Image_ component from the toolbox. The image source should be _External_ in order to fetch it based on the URL.

   - The average rating should be computed by an SQL script. Ignore any book that does not have at least 20 ratings.

     Include this sql script (a single `select` sql statement) in file `ex6.sql`.

     > The file should contain a single sql query. Do not include the database name, and do not include any `go` command either.

   - Make sure to calculate the rating appropriately: if the imported rating is of type integer, make sure to use decimal types when averaging the values!

   - Add a title to the report, and include your neptun code in the title.

   - The final report should look similar to this (your results do not need to match exactly):

     ![Top books report](images/exercise/report-books.png)

2. Include a screenshot of the **report** in file `ex6.png`.

   Please make sure that the screenshot is taken such that it

   - includes entire window of Visual Studio, not just the report preview,
   - contains the date and time when the screenshot was taken (e.g. including the clock form the Start menu)
   - and includes the name of the machine you are working on (e.g. execute a `whoami` command from the command prompt).

## Submit your solution

See instructions in [exercise 1](exercise1.md) to submit your solution.
