# Microsoft SQL Server Business Intelligence

This laboratory's goal is to practice the usage of Microsoft SQL Server products in business intelligence scenarios. Through the exercises, you will familiarize yourself with the usage of Microsoft SQL Server as a data warehouse, Integration Services as an ETL tool, and Reporting Services for report generation.

## Pre-requisites

You need to following tools to complete this laboratory:

- PC with Windows. You can also use a VM at <https://cloud.bme.hu>, see details [here](bme-cloud-vm-usage.md).
- Microsoft SQL Server. Express edition is sufficient, or _localdb_ installed along with Visual Studio is also fine
- [SQL Server Management Studio](https://docs.microsoft.com/en-us/sql/ssms/download-sql-server-management-studio-ssms)
- Microsoft Visual Studio 2017 / 2019. The community version is sufficient.
- Integration Services and Report Server Project support for Visual Studio
    - Visual Studio 2017: [SQL Server Data Tools](https://docs.microsoft.com/en-us/sql/ssdt/download-sql-server-data-tools-ssdt?view=sql-server-2017#install-analysis-services-integration-services-and-reporting-services-tools)
    - Visual Studio 2019:
        - [Microsoft Reporting Services Projects extension](https://marketplace.visualstudio.com/items?itemName=ProBITools.MicrosoftReportProjectsforVisualStudio)
        - [SQL Server Integration Services Projects extension](https://marketplace.visualstudio.com/items?itemName=SSIS.SqlServerIntegrationServicesProjects). It is recommended that these extensions are kept [up to date](https://docs.microsoft.com/en-us/visualstudio/extensibility/how-to-update-a-visual-studio-extension?view=vs-2019).
- A GitHub account and a git tool

## Material to review before the laboratory

- The expected mode of submitting your work, as detailed [here](../GitHub.md).
- The material covered in course _Business intelligence_ related to the topic, including, but not limited to
    - The demo material covered during the semester (<https://github.com/peekler/Business-Intelligence-Demos/tree/master/MSSQL-BI>)
    - The [short introduction](bi-software-intro.md) to using these software. This guide provides solutions to a few typical issues too, feel free to refer to this guide.
- SQL Integration Services [tutorial](https://docs.microsoft.com/en-us/sql/integration-services/ssis-how-to-create-an-etl-package)
- SQL Reporting Services [tutorial](https://docs.microsoft.com/en-us/sql/reporting-services/create-a-basic-table-report-ssrs-tutorial)

## Task overview

We have a webshop that sells books. Our goal is to understand our users and find out which are the best books we should market more. We have the users of the webshop, the books, and user-given ratings of these books. We already exported these data in the form of CSV files. We will use Microsoft SQL Server as a data warehouse, Integration Services as the ETL tool, and Reporting Services to present our insights in a visual form.

The model of our approach looks like the following.

![Overview of the process](images/process-overview.svg)

## Grading

Exercises 1 & 2 help you prepare the environment. Starting with exercise 3, **each exercise is worth one grade when completed successfully**. For an exercise to count as _successful_ you must finish _all_ its subtasks successfully. (E.g. if you complete exercises 3, 4 successfully, but there is an error in exercise 5, and you did not complete exercise 6, the resulting grade will be 3.)
