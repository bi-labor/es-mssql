# Microsoft SQL Server Business Intelligence

This laboratory's goal is to practice the usage of Microsoft SQL Server products in business intelligence scenarios. Through the exercises, you will familiarize yourself with Microsoft SQL Server's usage as a data warehouse, Integration Services as an ETL tool, and Reporting Services for report generation.

## Pre-requisites

You need to following tools to complete this laboratory:

- PC with Windows. You can also use a VM at <https://cloud.bme.hu>, see details [here](bme-cloud-vm-usage.md).
- Microsoft SQL Server. Express edition is sufficient, or _localdb_ installed along with Visual Studio is also fine
- [SQL Server Management Studio](https://docs.microsoft.com/en-us/sql/ssms/download-sql-server-management-studio-ssms)
- Microsoft Visual Studio 2022. The community version is sufficient. 
- [SQL Server Integration Services Projects extension](https://marketplace.visualstudio.com/items?itemName=SSIS.MicrosoftDataToolsIntegrationServices).
- PowerBI Desktop
- A GitHub account and a git tool

## Material to review before the laboratory

- The expected mode of submitting your work, as detailed [here](../GitHub.md).
- The material covered in course _Business intelligence_ related to the topic, including, but not limited to
    - The demo material covered during the semester (<https://github.com/peekler/Business-Intelligence-Demos/tree/master/MSSQL-BI>)
    - The [short introduction](bi-software-intro.md) to using these software. This guide provides solutions to a few typical issues too, feel free to refer to this guide.
- SQL Integration Services [tutorial](https://docs.microsoft.com/en-us/sql/integration-services/ssis-how-to-create-an-etl-package)

## Task overview

We have a webshop that sells books. Our goal is to understand our users and find out which are the best books we should market more. We have the users of the webshop, the books, and user-given ratings of these books. We already exported these data in the form of CSV files. We will use Microsoft SQL Server as a data warehouse, Integration Services as the ETL tool, and PowerBI to present our insights in a visual form.

The model of our approach looks like the following.

![Overview of the process](images/process-overview2.png)

## Grading

Exercises 1 & 2 help you prepare the environment. Starting with exercise 3, **each exercise is worth one grade when completed successfully**. For an exercise to count as _successful_ you must finish _all_ its subtasks successfully. (E.g. if you complete exercises 3 and 4 successfully, but there is an error in exercise 5, and you did not complete exercise 6, the resulting grade will be 3.)
