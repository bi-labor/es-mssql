# Exercise 5: _Elasticsearch_ queries

The purpose of this exercise is to try out the search and aggregation capabilities of _Elasticsearch_.

> :information_source: All of the following queries are sent to the `salaries/_search` endpoint with a `GET` method. This means that the first row in _Kibana_ will be `GET salaries/_search` for all of them. Therefore, the following examples will only contain the query JSON.

![Kibana query parts](./images/kibana-query-parts.png)

## `SELECT *` in _Elasticsearch_

Issue the following query.

```json
{
  "query": { "match_all": {} },
  "from": 0,
  "size": 10,
  "sort": [ "_doc" ]
}
```

* `query`: This provides the filter for the query. Think of the `WHERE` clause in _SQL_.

* `from` and `size`: These can be used for paging results. It is important to note that there is no way to query **all** documents using _Elasticsearch_. If you omit the `size` value, it defaults to **10**.

* `sort`: This can be used to sort the results.

## a) Who are the top **5** workers with the best salaries?

The following query answers our question.

```json
{
  "query": { "match_all": {} },
  "size": 5,
  "sort": [
    { "salary": { "order": "desc" } }
  ]
}
```

The only difference between this query and the previous one is that we want only **5** documents, and we changed the `sort` order to be by the `salary` values.

> :memo: Save the query JSON as `exercise-5\a.json`.

## b) Who are the top **5** five workers at _McDonalds_ aged between **18** and **30** with the best salaries?

```json
{
  "query": { 
    "bool": {
      "must": { "match_all": {} },
      "filter": [
        { "range": { "age": { "gte": 18, "lte": 30} } },
        { "term": { "company": "McDonalds" } }
      ]
    }
  },
  "size": 5,
  "sort": [
    { "salary": { "order": "desc" } }
  ]
}
```

The difference between this query and the previous one is that we have to apply some filters to the results.

* The `age` must be between **18** and **30**.
* The `company` must be _McDonalds_.

> :memo: Save the query JSON as `exercise-5\b.json`.

## c) Are there more men or women working for these companies? Is there a difference between the average salaries?

We have to use aggregations to answer these questions. We can use the following query.

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

This query first groups the documents by the `gender` value and then calculates the average of the `salary` values in them.

> :memo: Save the query JSON as `exercise-5\c.json`.

## d) What is the answer to the previous question in different age groups?

To answer this question we can mostly reuse the previous query. The only thing we have to change is to add a `range` aggregation to create age buckets before doing the grouping by the `gender` value.

```json
{
  "size": 0,
  "aggs": {
    "group_by_age": {
      "range": {
        "field": "age",
        "ranges": [
          { "from": 20, "to": 30 },
          { "from": 30, "to": 40 },
          { "from": 40, "to": 50 },
          { "from": 50, "to": 60 },
          { "from": 60, "to": 70 }
        ]
      },
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
  }
}
```

> :memo: Save the query JSON as `exercise-5\d.json`.

## Next exercise

Next is [exercise 6](exercise6.md).