import base64
import hashlib
import unittest


def calculate_secret(executable, neptun):
    seed = '{}_{}'.format(executable, neptun)
    seed_bytes = seed.encode('utf8')
    hash_bytes = hashlib.sha1(seed_bytes).digest()
    hash_base64 = base64.b64encode(hash_bytes)
    return hash_base64.decode('utf8').rstrip('=')


class DockerTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        with open('/tmp/solution/neptun.txt', 'r') as f:
            cls._neptun = f.read()

        assert cls._neptun, 'Missing NEPTUN code from neptun.txt'

    def test_docker(self):
        expected = calculate_secret('/usr/local/bin/python', self._neptun)

        with open('/tmp/solution/exercise-2/secret.txt', 'r') as f:
            self.assertEqual(expected, f.read())

    def test_docker_compose(self):
        expected = calculate_secret('/data/redis-server', self._neptun)

        with open('/tmp/solution/exercise-3/secret.txt', 'r') as f:
            self.assertEqual(expected, f.read())


if __name__ == '__main__':
    unittest.main()
