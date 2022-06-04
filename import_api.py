from flask import Flask
from neo4j import GraphDatabase
import csv

# local import folder path: /Users/ty/Library/Application Support/Neo4j Desktop/Application/relate-data/dbmss/dbms-34cdcc30-5d6d-443c-b14a-3fa16d3c7c1d/import

# establish the connection
# with open("connector.txt") as con:
#     data = csv.reader(con, delimiter = ",")
#     for i in data:
#         user = i[0]
#         pwd = i[1]
#         uri = i[2]

user = "neo4j"
pwd = "passawt"
uri = "bolt://localhost:7687"
driver = GraphDatabase.driver(uri=uri, auth = (user,pwd))

# from neo4j import GraphDatabase
# import os
#
# db_host = os.environ.get('NEO4J_HOST', 'localhost')
# db_port = os.environ.get('NEO4J_PORT', '7687')
# driver = GraphDatabase.driver(f'neo4j://{db_host}:{db_port}')

session = driver.session()

# # flask api
# api = Flask(__name__)
#
# @api.route('/')
# def create_course(name, id):
#     query = """
#     CREATE (n:Course{NAME:$name, ID:$id})
#     """


clear_all = """
MATCH (n) DELETE n;
"""

# import_competence = """
# CALL apoc.periodic.iterate('
#     CALL apoc.load.csv(
#         "/toy_comp.csv",{skip:1,header:true,ignore:"name",
#         mapping:{uri:{type:"string"},preferredLabel:{name:"competence"}}
#         }) yield map as row return row
#         ','
#         MERGE (k:Competence{uri:row.conceptUri, name:row.competence})'
#         , {batchSize:1000, iterateList:true, parallel:true}
# );
# """


import_descriptions = """
CALL apoc.load.xml("toy.xml","/DEFTISCAT/COURSETRANSACTIONS/INSERTCOURSES/*") YIELD value AS cs
WITH cs,
[x IN cs._children WHERE x._type="CS_NAME" | x._text] as name,
[x IN cs._children WHERE x._type="CS_DESC_LONG" | x._text] as descr,
[x IN cs._children WHERE x._type="CS_ID" | x._text] as cid
MERGE (c:Course{cid:cid[0]})
SET c.Name=name[0],
c.descr = descr[0] ;
"""

import_competence = """
USING PERIODIC COMMIT 500
LOAD CSV WITH HEADERS from "file:/toy_comp.csv" AS row 
MERGE (c:Competence {uri:row.conceptUri})
SET c.name = row.preferredLabel ;
"""

session.run(clear_all)
session.run(import_competence)
session.run(import_descriptions)



