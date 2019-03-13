import json
import unittest


class KibanaTest(unittest.TestCase):

    def test_exercise_6_a(self):
        self.execute_test(6, 'a', 'histogram',
                          expected_aggs=[
                              ('metric', 'count'),
                              (
                                  'segment',
                                  'date_histogram',
                                  {
                                      'field': 'hired',
                                      'interval': 'M'
                                  }
                              )
                          ],
                          expected_filter=['range', 'hired'])

    def test_exercise_6_b(self):
        self.execute_test(6, 'b', 'pie',
                          expected_aggs=[
                              ('metric', 'count'),
                              (
                                  'segment',
                                  'terms',
                                  {'field': 'gender'}
                              ),
                              (
                                  'segment',
                                  'range',
                                  {'field': 'age'}
                              )
                          ])

    def test_exercise_6_c(self):
        self.execute_test(6, 'c', 'region_map',
                          expected_aggs=[
                              ('metric', 'count'),
                              (
                                  'segment',
                                  'terms',
                                  {'field': 'address.state'}
                              )
                          ])

    def test_exercise_8_a(self):
        self.execute_test(8, 'a', 'histogram',
                          expected_aggs=[
                              (
                                  'metric',
                                  'avg',
                                  {'field': 'age'}
                              ),
                              (
                                  'segment',
                                  'date_histogram',
                                  {
                                      'field': 'hired',
                                      'interval': 'y'
                                  }
                              ),
                              (
                                  'group',
                                  'terms',
                                  {'field': 'company'}
                              )
                          ])

    def test_exercise_8_b(self):
        self.execute_test(8, 'b', 'pie',
                          expected_aggs=[
                              ('metric', 'count'),
                              (
                                  'segment',
                                  'terms',
                                  {'field': 'company'}
                              )
                          ],
                          expected_filter=['query', 'match', 'address.state'])

    def test_exercise_8_c(self):
        self.execute_test(8, 'c', 'region_map',
                          expected_aggs=[
                              (
                                  'metric',
                                  'avg',
                                  {'field': 'salary'}
                              ),
                              (
                                  'segment',
                                  'terms',
                                  {'field': 'address.state'}
                              )
                          ],
                          expected_filter=['range', 'age'])

    def execute_test(self, exercise, sub, expected_type, expected_aggs, expected_filter=None):
        vis_state, filters = self.read_visualization('/tmp/solution/exercise-{}/{}.json'.format(exercise, sub))

        self.assertEqual(expected_type, vis_state['type'])
        self.assert_aggs(expected_aggs, vis_state['aggs'])
        self.assert_filter(expected_filter, filters)

    def read_visualization(self, filename):
        try:
            with open(filename, 'r') as file:
                visualization = json.load(file)[0]['_source']
                vis_state = json.loads(visualization['visState'])
                search_source = json.loads(visualization['kibanaSavedObjectMeta']['searchSourceJSON'])
                return vis_state, search_source['filter']
        except IOError:
            self.fail('Missing solution for exercise')

    def assert_aggs(self, expected_aggs, aggs):
        for expected_agg in expected_aggs:
            self.assertTrue(any(KibanaTest.is_same_agg(expected_agg, agg) for agg in aggs),
                            msg='Missing expected aggregation: {}'.format(expected_agg))

    @classmethod
    def is_same_agg(cls, expected_agg, agg):
        if agg['schema'] != expected_agg[0] or agg['type'] != expected_agg[1]:
            return False

        if len(expected_agg) == 3:
            if not agg.get('params'):
                return False

            for key, value in expected_agg[2].items():
                if agg['params'].get(key) != value:
                    return False

        return True

    def assert_filter(self, expected_filter, filters):
        if not expected_filter:
            self.assertEqual(len(filters), 0, msg='Visualization must not have a filter')
        else:
            self.assertTrue(len(filters) > 0, msg='Visualization must have a filter')

            current = filters[0]
            for part in expected_filter:
                current = current.get(part)
                self.assertTrue(current, msg='Missing filter type of field: {}'.format(part))


if __name__ == '__main__':
    unittest.main()
