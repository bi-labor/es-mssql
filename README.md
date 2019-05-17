# Microsoft SQL Server Business Intelligence

## Goal

The goal of this laboratory is to practice the usage of Microsoft SQL Server products in business intelligence scenarios. Through the exercises you will familiarize yourself with the usage of Microsoft SQL Server as a data warehouse, Integration Services as an ETL tool and Reporting Services for report generation.

## Pre-requisites

You need to following tools to complete this laboratory:

- Microsoft SQL Server (LocalDB installed with Visual Studio is sufficient)
- Microsoft SQL Server Management Studio (free to download)
- Visual Studio 2017
- Microsoft SQL Server Data Tools (standalone installer for VS2017, free to download)
- A GitHub account, and your favorite tools to work with Git.

## Material to review before the laboratory

- The material covered in course _Business intelligence_ related to the topic, including, but not limited to
  - The demo material covered during the semester (<https://github.com/peekler/Business-Intelligence-Demos/tree/master/MSSQL-BI>)
  - The short introduction to using these software in [mssql-bi-software-intro.md](mssql-bi-software-intro.md)
- Further tutorials are available at the following addresses:
  - <https://msdn.microsoft.com/en-us/library/ms169917(v=sql.120).aspx>
  - <https://msdn.microsoft.com/en-us/library/ms167305(v=sql.120).aspx>

## Submitting your solution

To complete this laboratory you are required to solve excercises and submit your work, as prescribed by the exercise descriptions. You may only submit your own work! Submitting a work that you did not create is considered cheating, and will be handled according to the code of studies ("TVSZ").

While completing your exercises, please include the scripts, packages, projects, etc. in your submission. A starter submission is provided to you. Fill in the missing pieces there.

> :memo: The exercises all highlight the `path` where you should put your solution. **Please follow these guidelines.** The submissions are checked automatically. Files and folders not adhering to the prescribed structure might be skipped, and you will get a worse grade.

## Task

We have a webshop that sells books. Our goal is to understand our users, and find out which are the best books we should market more. We have the users of the webshop, the books, and user-given ratings of these books. We already exported these data in the form of CSV files. We will use Microsoft SQL Server as a data warehouse, Integration Services as the ETL tool, and Reporting Services to present our insights in a visual form.

The model of our approach looks like the following.

![Overview of the process](images/exercise/process-overview.svg)

## Grading

Follow the exercises in order. The 3 hour laboratory class should be sufficient time to complete all exercises. The result will be graded as follows.

- For a sufficient grade (2) you must complete exercise 2 and 3. Exercise 3 must run to completion, but it may work incorrectly (e.g. import less data, or skip the duplicate search, etc).
- For a satisfactory grade (3) exercise 3 must work correctly.
- For a good grade (4) exercise 4 should be completed without errors.
- For a very good grade (5) all exercises should be completed without errors.

## Exercises

Start with [Exercise 1 here](exercise1.md).
