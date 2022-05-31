from flask import Flask
from neo4j import GraphDatabase
import csv

# establish the connection
with open("connector.txt") as con:
    data = csv.reader(con, delimiter = ",")
    for i in data:
        user = i[0]
        pwd = i[1]
        uri = i[2]
driver = GraphDatabase.driver(uri=uri, auth = (user,pwd))
session = driver.session()

# # flask api
# api = Flask(__name__)
#
# @api.route('/')
# def create_course(name, id):
#     query = """
#     CREATE (n:Course{NAME:$name, ID:$id})
#     """



# first we need to truncate the xml-file?
q1 = """
CALL apoc.load.xml("toy.xml","/INSERTCOURSES/*") YIELD value AS cs 
WITH cs, 
[x IN cs._children WHERE x._type="CS_NAME" | x._text] as name,
[x IN cs._children WHERE x._type="CS_DESC_LONG" | x._text] as descr, 
[x IN cs._children WHERE x._type="CS_ID" | x._text] as cid
MERGE (c:Course{cid:cid[0]}) 
SET c.Name=name[0],
c.descr = descr[0] ;
"""

session.run(q1)