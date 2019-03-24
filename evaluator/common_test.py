import unittest


class CommonTest(unittest.TestCase):

    def execute_test(self, test_func, exercise, sub=None):
        self.longMessage = False
        sub_postfix = '.{}'.format(sub) if sub else ''
        exercise_name = '{}{}'.format(exercise, sub_postfix)
        try:
            test_func()

            print('###ahk#ARt$=fC3CpDg%mfK#testresult#exercise {}#passed'.format(exercise_name))
        except AssertionError as error:
            print('###ahk#ARt$=fC3CpDg%mfK#testresult#exercise {}#failed#{}'
                  .format(exercise_name, error))
            raise
