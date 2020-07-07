# Microsoft SQL Server Business Intelligence

## Goal

The goal of this laboratory is to practice the usage of Microsoft SQL Server products in business intelligence scenarios. Through the exercises you will familiarize yourself with the usage of Microsoft SQL Server as a data warehouse, Integration Services as an ETL tool and Reporting Services for report generation.

## Pre-requisites

You need to following tools to complete this laboratory:

- PC with Windows
  - You can also use a VM at <https://cloud.bme.hu>, see details [here](bme-cloud-vm-usage.md).
- Microsoft SQL Server
  - Express edition is sufficient, or _localdb_ installed along with Visual Studio is also fine
- [SQL Server Management Studio](https://docs.microsoft.com/en-us/sql/ssms/download-sql-server-management-studio-ssms)
- Microsoft Visual Studio 2017 / 2019
  - Community version is sufficient
- Integration Services and Report Server Project support for Visual Studio
  - Visual Studio 2017: [SQL Server Data Tools](https://docs.microsoft.com/en-us/sql/ssdt/download-sql-server-data-tools-ssdt?view=sql-server-2017#install-analysis-services-integration-services-and-reporting-services-tools)
  - Visual Studio 2019:
    - [Microsoft Reporting Services Projects extension](https://marketplace.visualstudio.com/items?itemName=ProBITools.MicrosoftReportProjectsforVisualStudio)
    - [SQL Server Integration Services Projects extension](https://marketplace.visualstudio.com/items?itemName=SSIS.SqlServerIntegrationServicesProjects)
    - It is recommended that these extension are kept [up to date](https://docs.microsoft.com/en-us/visualstudio/extensibility/how-to-update-a-visual-studio-extension?view=vs-2019).
- A GitHub account and a git tool

## Material to review before the laboratory

- The expected mode of submitting your work, as detailed [here](GitHub-usage.md).
- The material covered in course _Business intelligence_ related to the topic, including, but not limited to
  - The demo material covered during the semester (<https://github.com/peekler/Business-Intelligence-Demos/tree/master/MSSQL-BI>)
  - The [short introduction](mssql-bi-software-intro.md) to using these software
- SQL Integration Services [tutorial](https://docs.microsoft.com/en-us/sql/integration-services/ssis-how-to-create-an-etl-package)
- SQL Reporting Services [tutorial](https://docs.microsoft.com/en-us/sql/reporting-services/create-a-basic-table-report-ssrs-tutorial)

## Submitting your solution

To complete this laboratory you are required to solve exercises and submit your work through GitHub. The detailed description of the process of submission is detailed [here](GitHub-usage.md). Deadline: you must complete and submit your solution no later than **TBD**.

While completing your exercises, please include the scripts, packages, projects, etc. in your submission. A starter submission is provided to you. Fill in the missing pieces there.

> The exercises all highlight the `path` where you should put your solution. **Please follow these guidelines.** The submissions are checked automatically, and files and folders not adhering to the prescribed structure are not graded.

## Task overview

We have a webshop that sells books. Our goal is to understand our users, and find out which are the best books we should market more. We have the users of the webshop, the books, and user-given ratings of these books. We already exported these data in the form of CSV files. We will use Microsoft SQL Server as a data warehouse, Integration Services as the ETL tool, and Reporting Services to present our insights in a visual form.

The model of our approach looks like the following.

![Overview of the process](images/exercise/process-overview.svg)

## Grading

Exercises 1 & 2 help you prepare the environment. Starting with exercise 3, **each exercise is worth one grade when completed successfully**. In order for an exercise to count as _successful_ you must finish _all_ its subtasks successfully. (E.g. if you complete exercises 3, 4 successfully, but there is an error in exercise 5, and you did not complete exercise 6, the resulting grade will be 3.)

**You will receive an automatic feedback in GitHub when submitting your solution.** This feedback includes a "total", which is the number of successfully completed exercises; this is a preliminary grade, and it is subject to change by the instructor.

**Your solution is expected to work in this automated evaluation environment**. Please take extra care following the exercise guidelines. The automated feedback will let you know if there is some error in your submission; you are required to fix these. The evaluation uses _GitHub Actions_. You have access to all the logs and the detailed result of every evaluation on the GitHub web interface. [This guide](GitHub-Actions-usage.md) helps you understand where to look for them.

## Exercises

Start with [Exercise 1 here](exercise1.md).
