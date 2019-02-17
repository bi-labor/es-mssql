import elasticsearch
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


def main():
    # Ensure that ES is available
    ensure_elasticsearch_available(90)

    # Connect to ES and wait for it to initialize
    es = elasticsearch.Elasticsearch()
    es.ping()

    # Create the 'salaries' index
    es.indices.create(
        index='salaries',
        body={
            'settings': {
                'number_of_shards': 1,
                'number_of_replicas': 0
            },
            'mappings': {
                '_doc': {
                    'properties': {
                        'gender': {'type': 'keyword'},
                        'address.state': {'type': 'keyword'},
                        'company': {'type': 'keyword'},
                        'hired': {
                            'type': 'date',
                            'format': 'MM/dd/yyyy'
                        }
                    }
                }
            }
        })

    # Index the sample document
    with open('/tmp/init/salaries_sample.json', 'r') as f:
        es.index(index='salaries', doc_type='_doc', body=f.read())

    # Index the remaining documents
    with open('/tmp/init/salaries.json', 'r') as f:
        es.bulk(body=f.read())

    # Flush the changes to disk
    es.indices.flush()

    print('Index and documents created successfully')


if __name__ == "__main__":
    main()

