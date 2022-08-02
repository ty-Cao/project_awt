import time

from neo4j import GraphDatabase
import csv

start = time.time()

# establish the connection
with open("connector.txt") as con:
    data = csv.reader(con, delimiter = ",")
    for i in data:
        user = i[0]
        pwd = i[1]
        uri = i[2]

driver = GraphDatabase.driver(uri=uri, auth=(user, pwd))
session = driver.session()

clear_all_relations = """
MATCH ()-[r]-() DELETE r;
"""

session.run(clear_all_relations)

for i in range(1,29):
    import_relation = """
    USING PERIODIC COMMIT 500
    LOAD CSV WITH HEADERS from "file:/benchmark/relations_part_""" + str(i) + """.csv" AS row
    MATCH (course:Course {cid:row.course_id})
    MERGE (competency:Competency {uri: row.conceptUri})
    MERGE (course)-[r:RELATED_TO]-(competency);
    """
# RETURN course.name, r, competency;
    session.run(import_relation)

end = time.time()
print(end-start)
