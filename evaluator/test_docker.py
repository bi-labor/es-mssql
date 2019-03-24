import common_test
import base64
import binascii
import hashlib
import unittest


class DockerTest(common_test.CommonTest):

    @classmethod
    def setUpClass(cls):
        with open('/tmp/solution/neptun.txt', 'r') as f:
            cls._neptun = f.read().strip()[:6].upper()

        assert cls._neptun, 'Missing NEPTUN code from neptun.txt'

    def test_exercise_2(self):
        self.execute_docker_test(2, '/usr/local/bin/python')

    def test_exercise_3(self):
        self.execute_docker_test(3, '/data/redis-server')

    def execute_docker_test(self, exercise, executable):
        self.execute_test(lambda: self.execute_docker_test_internal(exercise, executable), exercise)

    def execute_docker_test_internal(self, exercise, executable):
        neptun, secret_hash = self.read_secret('/tmp/solution/exercise-{}/secret.txt'.format(exercise))
        self.assertEqual(self._neptun, neptun,
                         msg='NEPTUN code mismatch: {} (neptun.txt) != {} (secret)'.format(self._neptun, neptun))

        expected_hash = DockerTest.calculate_hash(executable, self._neptun)
        self.assertEqual(expected_hash, secret_hash, msg='Incorrect secret')

    def read_secret(self, filename):
        try:
            with open(filename, 'r') as file:
                secret = file.read().strip()
                self.assertTrue(secret, msg='Missing solution for exercise')
                self.assertEqual(35, len(secret), msg='Invalid secret length')

                neptun_b64 = secret[:8]
                neptun_bytes = base64.b64decode(neptun_b64.encode('utf8'), validate=True)
                return neptun_bytes.decode('utf8'), secret[8:]
        except IOError:
            self.fail(msg='Missing solution for exercise')
        except binascii.Error:
            self.fail(msg='Invalid secret format')

    @classmethod
    def calculate_hash(cls, executable, neptun):
        seed = '{}_{}'.format(executable, neptun)
        seed_bytes = seed.encode('utf8')
        hash_bytes = hashlib.sha1(seed_bytes).digest()
        hash_base64 = base64.b64encode(hash_bytes)
        return hash_base64.decode('utf8').rstrip('=')


if __name__ == '__main__':
    unittest.main()
