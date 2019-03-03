import urllib.request
import time


def ensure_elasticsearch_available(timeout):
    available = False
    start = time.time()
    print('Connecting to Elasticsearch', end='')

    while time.time() - start < timeout:
        try:
            print('.', end='', flush=True)

            request = urllib.request.Request('http://localhost:9200/', method='HEAD')
            with urllib.request.urlopen(request, timeout=10) as response:
                if response.getcode() == 200:
                    available = True
                    break
        except:
            pass

        time.sleep(2)

    if available:
        print(' SUCCESS')
    else:
        print(' FAILED')
        exit(1)
