"""
Smid csv i elasticsearch
"""
import csv
import json
from timeit import default_timer as timer

from elasticsearch import Elasticsearch

ES = Elasticsearch([{"host": "localhost", "port": 9200}])
FNAMES = ["a", "b", "c", "d"]
START = timer()
# with open("/home/niels/t_mikro_ny.csv") as f:
#    READER = csv.DictReader(f, fieldnames=FNAMES, delimiter="|")
#    i = 0
#    for r in READER:
#        i += 1
#        item = json.dumps(r)
#        ES.index(index="newidx", doc_type="items", id=i, body=item)
#        if (i % 10000) == 0:
#            print(i)
#        # Vi har ikke hele dagen
#        if i == 1_000_000:
#            break
# print(f"timing index: {timer() - START}")

# print(ES.get(index="newidx", doc_type="items", id=5))
# print(ES.search(index="newidx", body={"query": {"match": {"b": "0287/99-2"}}}))
# print(ES.search(index="newidx", body={"query": {"prefix": {"d": "nævo"}}}))
# print(ES.search(index="newidx", body={"query": {"regexp": {"d": ".*[ben|mal]ign.*"}}}))
