import common_test
import elasticsearch
import es_common
import unittest


class ElasticsearchTest(common_test.CommonTest):

    @classmethod
    def setUpClass(cls):
        # Ensure that ES is available
        es_common.ensure_elasticsearch_available(60)

        # Connect to ES and wait for it to initialize
        cls._es = elasticsearch.Elasticsearch()
        cls._es.ping()

    def test_exercise_5_a(self):
        self.execute_query_test(5, 'a')

    def test_exercise_5_b(self):
        self.execute_query_test(5, 'b')

    def test_exercise_5_c(self):
        self.execute_aggregation_test(5, 'c', ['sterm', 'avg'])

    def test_exercise_5_d(self):
        self.execute_aggregation_test(5, 'd', ['range', 'sterm', 'avg'])

    def test_exercise_7_a(self):
        self.execute_query_test(7, 'a')

    def test_exercise_7_b(self):
        self.execute_query_test(7, 'b')

    def test_exercise_7_c(self):
        self.execute_aggregation_test(7, 'c', ['sterm', 'avg'])

    def execute_query_test(self, exercise, sub):
        self.execute_test(lambda: self.execute_query_test_internal(exercise, sub), exercise, sub)

    def execute_query_test_internal(self, exercise, sub):
        expected = self.get_query_result('./solutions/{}_{}.json'.format(exercise, sub))
        actual = self.get_query_result('/tmp/solution/exercise-{}/{}.json'.format(exercise, sub))
        self.assertEqual(len(expected), len(actual),
                         msg='Incorrect number of results for the query (should be {}, got {})'
                         .format(len(expected), len(actual)))
        self.assertEqual(expected, actual, msg='Incorrect results for query')

    def get_query_result(self, filename):
        result = self.execute_search(filename, is_aggregation=False)['hits']['hits']
        return [item['_source']['email'] for item in result]

    def execute_aggregation_test(self, exercise, sub, aggregations):
        self.execute_test(lambda: self.execute_aggregation_test_internal(exercise, sub, aggregations), exercise, sub)

    def execute_aggregation_test_internal(self, exercise, sub, aggregations):
        expected = self.get_aggregation_result('./solutions/{}_{}.json'.format(exercise, sub), aggregations)
        actual = self.get_aggregation_result('/tmp/solution/exercise-{}/{}.json'.format(exercise, sub),
                                             aggregations)
        self.assertEqual(expected, actual, msg='Incorrect results for aggregation')

    def get_aggregation_result(self, filename, aggregations):
        result = self.execute_search(filename, is_aggregation=True)
        return self.get_doc_counts(result['aggregations'], aggregations)

    def execute_search(self, filename, is_aggregation):
        try:
            with open(filename, 'r') as file:
                query = file.read()
                self.assertTrue(query, msg='Missing solution for exercise')
                return self._es.search(index='salaries', doc_type='_doc', body=query, typed_keys=is_aggregation)
        except IOError:
            self.fail(msg='Missing solution for exercise')
        except elasticsearch.exceptions.TransportError as e:
            self.fail(msg='Invalid query json (Elasticsearch response: {} - {})'.format(e.status_code, e.error))

    def get_doc_counts(self, result, aggregations):
        aggregation = aggregations[0]
        aggregation_key = ElasticsearchTest.get_aggregation_key(result, aggregation)
        self.assertTrue(aggregation_key, msg='The query does not have the proper aggregations')

        if len(aggregations) == 1:
            return result[aggregation_key]['value']
        else:
            buckets = result[aggregation_key]['buckets']
            buckets.sort(key=lambda b: b['key'])
            return [self.get_doc_counts(bucket, aggregations[1:]) for bucket in buckets]

    @classmethod
    def get_aggregation_key(cls, d, aggregation):
        return next((key for key in d.keys() if key.startswith(aggregation)), None)


if __name__ == '__main__':
    unittest.main()
