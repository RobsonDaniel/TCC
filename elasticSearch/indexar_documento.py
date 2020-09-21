from elasticsearch import Elasticsearch

es = Elasticsearch("192.168.0.23:9200")

def indexar(nome_index, documento):
    indexacao = es.index(index=nome_index, body=documento)
    #indexacao = es.create(index='ssc', doc_type='_doc', body=documento, ignore=409)
    print(indexacao)
