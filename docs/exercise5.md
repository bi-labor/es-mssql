# Exercise 5: Import the books and ratings datasets using Integration Services

Your task is to import the remaining two CSV files using Integration Services into the database.

1. Create two new tables in the database to store the books and ratings contents. Design the tables such that they map to the columns in the CSV.

   Put the SQL code that creates the tables into two separate files `ex5_books.sql` and `ex5_ratings.sql`.

   > There should be a single sql command ("create table") in each file. Please do _not_ include the database name in the commands and do _not_ include any `go` command in them either.

1. Create a new ETL process to import the books and ratings datasets. Open the provided empty Integration Services project in `ex5.sln`, and perform the modifications in place.

   - Import the **ISBN** from the books as **string**.
   - Prefix the **book titles** with your Neptun code.
   - You will need to **filter for duplicate ISBNs** among the books dataset, as we did before. Make sure to use case insensitive comparison for the duplicate filter.
   - Make sure to import the **image URLs** from the books data file.
   - Remember to extend the length of the imported columns in the flat file connection settings (**_OutputColumnWidth_**) for the fields; **1000 characters** should be sufficient.
   - The **ratings** dataset contains invalid values: there are rows where the value is **0**. These should be skipped using a **Conditional split** component.
   - It is best to separate the two CSV import into different _data flows_ within the same _control flow_ process.

1. Include proof of the successful imports by taking two screenshots of the **database table contents** after successful execution of the ETL process as `ex5_books.png` and `ex5_ratings.png`.

   Please make sure that the screenshot is taken such that both

   - include the database name (which is your Neptun code) from the _Object explorer_ window,
   - contain sample rows to verify the result of the ETL process,
   - contain the date and time when the screenshot was taken (e.g. including the clock form the Start menu)
   - and include the name of the machine you are working on (e.g. execute a `whoami` command from the command prompt).

## Next exercise

Next is [exercise 6](exercise6.md).
