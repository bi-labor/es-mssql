# Exercise 5: Import the books and ratings datasets using Integration Services

1. Create two new tables in the database to store the books and ratings contents. Design the tables such that they map to the columns in the CSV.

   > :memo: Put the SQL code that creates the tables into two separate files `exercise-5\ex5_create_table_books.sql` and `exercise-5\ex5_create_table_ratings.sql`. There should be a single sql command ("create table") in each. Please do _not_ include the database names in the commands.

1. Create a new ETL process to import the books and ratings datasets. Open the provided empty Integration Services project for this exercise, and perform the modifications in place.

   > :memo: The ETL process should be edited in solution `exercise-5\ex5_integration_services.sln`.

   - Import the **ISBN** from the books as **string**.
   - You will need to **filter for duplicate ISBNs** among the books dataset, as we did before. Make sure to use case insensitive comparison for the duplicate filter.
   - Make sure to import the **image URLs** from the books data file.
   - Remember to extend the length of the imported columns in the flat file connection settings (**_OutputColumnWidth_**) for the fields; **1000 characters** should be sufficient.
   - The **ratings** dataset contains invalid values. The ratings data file contains lines where the value is **0**. These should be skipped using a **Conditional split** component.
   - It is best to separate the two CSV import into a different _data flow_ within the same _control flow_ process.

   > :memo: Include proof of the successful imports by taking two screenshots of the database table contents after successful execution of the ETL process as `exercise-5\ex5_table_screenshot_books.png` and `exercise-5\ex5_table_screenshot_ratings.png`. Please make sure that the screenshots are taken such that both **include the database name** (which is your Neptun code) from the _Object explorer_ window!

## Next exercise

Next is [exercise 6](exercise6.md).
