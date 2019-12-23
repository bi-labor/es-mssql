import common_test
import json
import unittest


class KibanaTest(common_test.CommonTest):

    def test_exercise_6_a(self):
        self.execute_kibana_test(6, 'a', 'histogram',
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
        self.execute_kibana_test(6, 'b', 'pie',
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
        self.execute_kibana_test(6, 'c', 'region_map',
                                 expected_aggs=[
                                     ('metric', 'count'),
                                     (
                                         'segment',
                                         'terms',
                                         {'field': 'address.state'}
                                     )
                                 ])

    def test_exercise_8_a(self):
        self.execute_kibana_test(8, 'a', 'histogram',
                                 expected_aggs=[
                                     (
                                         'metric',
                                         'avg',
                                         {'field': 'age'}
                                     ),
                                     (
                                         ['segment', 'group'],
                                         'date_histogram',
                                         {
                                             'field': 'hired',
                                             'interval': 'y'
                                         }
                                     ),
                                     (
                                         ['group', 'segment'],
                                         ['terms', 'significant_terms'],
                                         {'field': 'company'}
                                     )
                                 ])

    def test_exercise_8_b(self):
        self.execute_kibana_test(8, 'b', 'pie',
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
        self.execute_kibana_test(8, 'c', 'region_map',
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

    def execute_kibana_test(self, exercise, sub, expected_type, expected_aggs, expected_filter=None):
        self.execute_test(
            lambda: self.execute_kibana_test_internal(exercise, sub, expected_type, expected_aggs, expected_filter),
            exercise,
            sub)

    def execute_kibana_test_internal(self, exercise, sub, expected_type, expected_aggs, expected_filter):
        try:
            vis_state, filters = self.read_visualization('/tmp/solution/exercise-{}/{}.json'.format(exercise, sub))

            self.assertEqual(expected_type, vis_state['type'],
                             msg='Incorrect visualization type (expected: {}, got: {}'
                             .format(expected_type, vis_state['type']))
            self.assert_filter(expected_filter, filters)
            self.assert_aggs(expected_aggs, vis_state['aggs'])
        except KeyError:
            self.fail(msg='Invalid export file')

    def read_visualization(self, filename):
        try:
            with open(filename, 'r') as file:
                export_json = file.read()
                self.assertTrue(export_json, msg='Missing solution for exercise')
                export = json.loads(export_json)
                self.assertIsInstance(export, list, msg='Invalid export file')
                self.assertEqual(1, len(export), msg='Export should contain exactly one visualization, got {}'
                                 .format(len(export)))

                visualization = export[0]['_source']
                vis_state = json.loads(visualization['visState'])
                search_source = json.loads(visualization['kibanaSavedObjectMeta']['searchSourceJSON'])
                return vis_state, search_source['filter']
        except IOError:
            self.fail(msg='Missing solution for exercise')
        except json.JSONDecodeError:
            self.fail(msg='Invalid export file')

    def assert_filter(self, expected_filter, filters):
        if not expected_filter:
            self.assertEqual(len(filters), 0, msg='Visualization must not have a filter')
        else:
            self.assertTrue(len(filters) > 0, msg='Missing filter for visualization')

            current = filters[0]
            for part in expected_filter:
                current = current.get(part)
                self.assertTrue(current, msg='Incorrect filter for visualization')

    def assert_aggs(self, expected_aggs, aggs):
        for expected_agg in expected_aggs:
            self.assertTrue(any(KibanaTest.is_same_agg(expected_agg, agg) for agg in aggs),
                            msg='Some aggregations in the visualization are missing or incorrect')

    @classmethod
    def is_same_agg(cls, expected_agg, agg):
        if not KibanaTest.check_agg_field(expected_agg[0], 'schema', agg):
            return False
        if not KibanaTest.check_agg_field(expected_agg[1], 'type', agg):
            return False

        if len(expected_agg) == 3:
            if not agg.get('params'):
                return False

            for key, value in expected_agg[2].items():
                if agg['params'].get(key) != value:
                    return False

        return True

    @classmethod
    def check_agg_field(cls, expected_field, key, agg):
        if isinstance(expected_field, list):
            if not agg[key] in expected_field:
                return False
        else:
            if agg[key] != expected_field:
                return False

        return True


if __name__ == '__main__':
    unittest.main()
