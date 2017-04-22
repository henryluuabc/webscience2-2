# -*- coding: utf-8 -*-
from whoosh.index import open_dir
from whoosh.fields import *
# from whoosh.qparser import QueryParser
from whoosh.qparser import MultifieldParser
import whoosh.index as index
from whoosh import scoring
import os
import argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-d', '--dir_index', help='path to index directory - default=indexdir', type=str, default="indexdir")
    parser.add_argument('-i', '--index_name', help='name of indexed file - default=data', type=str, default="data")
    parser.add_argument('-q', '--query', help='search data? - default=query', type=str, default="query")
    parser.add_argument('-l', '--limit', help= 'limit number of results - default=20', type=int, default=20)
    parsed = parser.parse_args()
    if not os.path.exists(parsed.dir_index):
        os.mkdir(parsed.dir_index)
    schema = Schema(url=ID(stored=True), title=TEXT(stored=True), content=TEXT(stored=True))
    ix = index.open_dir(parsed.dir_index, indexname=parsed.index_name)
    # weighting=scoring.TF_IDF()
    with ix.searcher(weighting=scoring.TF_IDF()) as searcher:
    	query = MultifieldParser(["title", "content"], ix.schema).parse(parsed.query)
    	results = searcher.search(query, limit=parsed.limit)
        print results
        for data in results:
           print data

if __name__ == '__main__':
   main()
