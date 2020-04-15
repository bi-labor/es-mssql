# Microsoft SQL Server Business Intelligence

## Goal

The goal of this laboratory is to practice the usage of Microsoft SQL Server products in business intelligence scenarios. Through the exercises you will familiarize yourself with the usage of Microsoft SQL Server as a data warehouse, Integration Services as an ETL tool and Reporting Services for report generation.

## Pre-requisites

You need to following tools to complete this laboratory:

- PC with Windows
  - You can also use a VM at <https://cloud.bme.hu>. A prepared VM template is available in the "Smallville" datacenter with name "BI laboratory MSSQL". You can use this template to create a VM that has all the necessary software installed. If you do not have access to the template, please request it via email from the instructor. Please note, that altough being installed already, you may need to [log into Visual Studio](https://visualstudio.microsoft.com/vs/support/community-edition-expired-buy-license/) with a Microsoft account (e.g. your @edu.bme.hu account).
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
  - The short introduction to using these software in [mssql-bi-software-intro.md](mssql-bi-software-intro.md)
- SQL Integration Services [tutorial](https://docs.microsoft.com/en-us/sql/integration-services/ssis-how-to-create-an-etl-package)
- SQL Reporting Services [tutorial](https://docs.microsoft.com/en-us/sql/reporting-services/create-a-basic-table-report-ssrs-tutorial)

## Submitting your solution

To complete this laboratory you are required to solve exercises and submit your work through GitHub. The detailed description of the process of submission is detailed [here](GitHub-usage.md). Deadline: you must complete and submit your solution no later than **April ~~20~~ 30, 2020, 23:59 CET**.

While completing your exercises, please include the scripts, packages, projects, etc. in your submission. A starter submission is provided to you. Fill in the missing pieces there.

> The exercises all highlight the `path` where you should put your solution. **Please follow these guidelines.** The submissions are checked automatically, and files and folders not adhering to the prescribed structure are not graded.

## Task overview

We have a webshop that sells books. Our goal is to understand our users, and find out which are the best books we should market more. We have the users of the webshop, the books, and user-given ratings of these books. We already exported these data in the form of CSV files. We will use Microsoft SQL Server as a data warehouse, Integration Services as the ETL tool, and Reporting Services to present our insights in a visual form.

The model of our approach looks like the following.

![Overview of the process](images/exercise/process-overview.svg)

## Grading

Follow the exercises in order. The result will be graded as follows.

- For a sufficient grade (2) you must complete exercise 2 and 3. Exercise 3 must run to completion, but it may work incorrectly (e.g. import less data, or skip the duplicate search, etc).
- For a satisfactory grade (3) exercise 3 must work correctly.
- For a good grade (4) exercise 4 should be completed without errors.
- For a very good grade (5) all exercises should be completed without errors.

## Exercises

Start with [Exercise 1 here](exercise1.md).
