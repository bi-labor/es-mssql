import elasticsearch
import es_common


def main():
    # Ensure that ES is available
    es_common.ensure_elasticsearch_available(60)

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
    with open('/tmp/evaluator/data/salaries_sample.json', 'r') as f:
        es.index(index='salaries', doc_type='_doc', body=f.read())

    # Index the remaining documents
    with open('/tmp/evaluator/data/salaries.json', 'r') as f:
        es.bulk(body=f.read())

    # Flush the changes to disk
    es.indices.flush()

    print('Index and documents created successfully')


if __name__ == "__main__":
    main()
