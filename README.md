# Business Intelligence Laboratory exercises

![Build docs](https://github.com/bi-labor/es-mssql/workflows/Build%20docs/badge.svg?branch=master)

This repository contains laboratory exercises for the following course topics:

- Elasticsearch laboratory
- Microsoft SQL Server Business Intelligence laboratory

The exercise documentation is build with MkDocs and published on GitHub Pages at <https://bi-labor.github.io/es-mssql/>

#### Render website locally

1. Open a PowerShell console at the repository root

1. `docker run -it --rm -p 8000:8000 -v ${PWD}:/docs squidfunk/mkdocs-material:6.2.2`

1. Open <http://localhost:8000> in a browser

1. Edit the Markdown and it will trigger automatic update in the browser
