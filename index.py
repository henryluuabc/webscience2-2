# -*- coding: utf-8 -*-
import codecs
from whoosh.index import create_in
from whoosh.fields import *
from whoosh.qparser import QueryParser
import os
import argparse
from whoosh import index

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-d', '--dir_index', help='path to index directory - default=indexdir', type=str, default="indexdir")
    parser.add_argument('-i', '--index_name', help='name of index file - default=data', type=str, default="data")
    parser.add_argument('-f', '--file_name', help='path to data to get index - default=data.txt', type=str, default="data.txt")
    parsed = parser.parse_args()
    if not os.path.exists(parsed.dir_index):
        os.mkdir(parsed.dir_index)
    schema = Schema(url=ID(stored=True), title=TEXT(stored=True), content=TEXT(stored=True))
    ix = index.create_in(parsed.dir_index, schema, indexname=parsed.index_name)
    writer = ix.writer()
    print "Start indexing file ..."
    with codecs.open(parsed.file_name, 'rb', encoding='utf8') as f:
        for line_terminated in f:
            line = line_terminated.split("\t")
            writer.add_document(url=line[0], title=line[1], content=line[2])
    writer.commit()
if __name__ == '__main__':
   main()
