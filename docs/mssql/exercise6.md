# Exercise 6: Create a report listing the highest rated books

In this exercise, you are required to create a new report using Reporting Services. Create a report that lists the **top 10 highest rated books** in a table.

- The report should be edited in solution `ex6.sln` in file `books.rdl`.

- The top 10 books should be presented as a table displaying the title, author, publication year, average rating, and the cover image of the book (using the medium-sized image URL from the dataset).

- Use an _Image_ component from the toolbox. The image source should be _External_ to fetch it based on the URL.

- An SQL script should compute the average rating. Ignore any book that does not have at least 20 ratings.

    Include this sql script (a single `select` sql statement) in file `ex6.sql`.

    !!! note ""
        The file should contain a single sql query. Do not include the database name, and do not include any `go` command either.

- Make sure to calculate the rating appropriately: if the imported rating is of type integer, make sure to use decimal types when averaging the values!

- Add a title to the report, and include your Neptun code in the title.

- The final report should look similar to this (your results do not need to match exactly):

     ![Top books report](images/report-books.png)

!!! example "SUBMISSION"
    Include the **SQL query** in file `ex6.sql` and a screenshot of the **report** in file `ex6.png`.

    Please ensure that the screenshot displays all the relevant parts of the report (title, table with Neptun codes, ratings, cover images). See the sample above.
