# Elasticsearch Business Intelligence

## Goal

The goal of this laboratory is to practice the usage of the _Docker_ virtualization technology and the _Elasticsearch_ and _Kibana_ systems.

Through the exercises you will familiarize yourself with the building of _Docker_ images as well as managing services consisting of multiple containers. You will also get hands on with _Elasticsearch_ queries and aggregations and try out some visualization tools provided by _Kibana_.

## Pre-requisites

You need the following tools to complete this laboratory:

* Docker Community Edition (CE)
  * Docker Desktop for Windows is available for download [here](https://hub.docker.com/editions/community/docker-ce-desktop-windows)

## Material to review before the laboratory

- The material covered in course _Business intelligence_ related to the topic, including, but not limited to
  - The demo material covered during the semester <https://github.com/peekler/Business-Intelligence-Demos/tree/master/ELK>
- Elasticsearch documentation
  - <https://www.elastic.co/guide/en/elasticsearch/reference/current/search.html>
  - <https://www.elastic.co/guide/en/elasticsearch/reference/current/search-aggregations.html>


## Submitting your solution

While completing your exercises, please include the scripts, packages, projects, etc. in your submission. A starter submission is provided to you. Fill in the missing pieces there.

> :memo: The exercises each highlight the `path` where you should put your solution. **Please follow these guidelines.** The submissions are checked automatically. Files and folders not adhering to the prescribed structure might be skipped, and you will get a worse grade.

## Grading

Follow the exercises in order. In order for an exercise to count as _completed_ you must finish **all** its subtasks successfully. The 3-hour laboratory class should be sufficient time to complete all exercises. The result will be graded as follows.

- For a sufficient grade (**2**) you must complete exercises **1** through **5**.
- For a satisfactory grade (**3**) exercise **6** should be completed as well.
- For a good grade (**4**) exercise **7** should be completed.
- For a very good grade (**5**) **all** exercises should be completed.

## Exercises

Start with [Exercise 1 here](exercise1.md).

## Finishing your work from home

If you weren't able to do all the exercises during the 3-hour laboratory class, you are welcome to finish them from home. If you decide to do that, however, you have to be aware of the following.

Due to how the _Docker Hub's_ rate limitations work, we have to use a private _Docker_ repository during the lab. You cannot use that from home, therefore you have to use the original _Docker_ images. The required modifications:

* [Exercise 2](exercise2.md), `Dockerfile`:

    * **From**: sydney.aut.bme.hu:5000/python:3.7.2-alpine
    * **To**: python:3.7.2-alpine

* [Exercise 3](exercise3.md), `docker-compose.yml`:

    * **From**: sydney.aut.bme.hu:5000/redis:5.0.3-alpine
    * **To**: redis:5.0.3-alpine

* [Exercise 4](exercise4.md), `docker-compose.yml`:

    * **From**: sydney.aut.bme.hu:5000/elasticsearch-oss:6.6.0
    * **To**: docker.elastic.co/elasticsearch/elasticsearch-oss:6.6.0

* [Exercise 4](exercise4.md), `docker-compose.yml`:

    * **From**: sydney.aut.bme.hu:5000/kibana-oss:6.6.0
    * **To**: docker.elastic.co/kibana/kibana-oss:6.6.0