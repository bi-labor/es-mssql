# Exercise 4: Elasticsearch queries

The purpose of this exercise is to use the search and aggregation capabilities of _Elasticsearch_ to answer questions of the data imported previously.

!!! note "Query JSON"
    You will be requested to save the **query** JSON in the following exercises. The image below shows you what that means: the **VALID** JSON sent to Elasticsearch, **WITHOUT** the first line, and definitely **NOT** the result JSON that is on the right side in Kibana.

    ![Kibana query parts](images/kibana-query-parts.png)

!!! note "Search syntax"
    Please use the [search syntax](https://www.elastic.co/guide/en/elasticsearch/reference/current/search-your-data.html) of Elasticsearch that defines the criteria in JSON body. Do _not_ use the URL query method filtering.

All of the following queries are sent to the `salaries/_search` endpoint with a `GET` method. This means that the **first line in _Kibana Dev Tools_ will be `GET salaries/_search`** for all of them.

## "SELECT \*" in _Elasticsearch_

Issue the following query.

```json
{
  "query": { "match_all": {} },
  "from": 0,
  "size": 10,
  "sort": ["_doc"]
}
```

- `query`: This provides the filter for the query. Think of the `WHERE` clause in _SQL_.

- `from` and `size`: These can be used for paging results. It is important to note that there is no way to query **all** documents using _Elasticsearch_. If you omit the `size` value, it defaults to **10**.

- `sort`: This can be used to sort the results.

You do not have to save this query.

## a) Who are the top **5** workers with the best salaries?

Change the previous query:

- we need the first _5_, so the size will be _5_;
- the [sort](https://www.elastic.co/guide/en/elasticsearch/reference/current/search-request-body.html#_sort_values) has to be performed on field _salary_, for which use the following syntax:

  ```json
  {
    ...
    "sort": [{ "salary": { "order": "desc" } }]
  }
  ```

Execute this query and verify the results.

!!! example "SUBMISSION"
    Save the final query JSON as `ex4-a.json`.

## b) Who are the top **5** workers at _McDonalds_ aged between **18** and **30** with the best salaries?

Building on the previous query, replace the `query` with a [boolean query](https://www.elastic.co/guide/en/elasticsearch/reference/current/query-dsl-bool-query.html#query-dsl-bool-query) as follows:

```json
{
  "query": {
    "bool": {
      "must": { "match_all": {} },
      "filter": [
        { "range": { "age": { "gte": 18, "lte": 30 } } },
        { "term": { "company": "NEPTUN McDonalds" } }
      ]
    }
  },
  ...
}
```

The difference between this query and the previous one is that we have to apply some filters to the results.

- The `age` must be between **18** and **30**.
- The `company` must be _NEPTUN McDonalds_ prefixed with your Neptun code.

Execute this query and verify the results.

!!! example "SUBMISSION"
    Save the final query JSON as `ex4-b.json`.

## c) Are there more men or women working for these companies? Is there a difference between the average salaries?

We have to use [term aggregations](https://www.elastic.co/guide/en/elasticsearch/reference/current/search-aggregations-bucket-terms-aggregation.html) to answer these questions. We can use the following query.

```json
{
  "size": 0,
  "aggs": {
    "group_by_gender": {
      "terms": {
        "field": "gender"
      },
      "aggs": {
        "average_salary": {
          "avg": {
            "field": "salary"
          }
        }
      }
    }
  }
}
```

Specifying `"size": 0` means that we do not want any matching documents as we only need the aggregation results. (There are no search criteria specified here, but there could be.)

This query first groups the documents by the `gender` value and then calculates the average of the `salary` values within the groups.

!!! example "SUBMISSION"
    Based on the results, what is the average salary of women? Type your answer into `ex4-c.txt`. Include only the number and nothing else in this text file (e.g., `123.45`). Don't worry about decimal digits, the value will be rounded for comparison. (You do _not_ need to save the query JSON here.)
