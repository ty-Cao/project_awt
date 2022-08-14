# Cypher Code for Database Operations

## 1. Import data into database

First you need to place the files(course_description_FOKUS.xml, skills_de.csv, relations.csv) in the neo4j/import folder. (You can find the file relations.csv in nlp_service/output after you run the file main.ipynb or main_with_venv.ipynb.)

### 1.1 import course descriptions

```Cypher
CALL apoc.load.xml('course_description_FOKUS.xml',"/DEFTISCAT/COURSETRANSACTIONS/INSERTCOURSES/*") YIELD value AS cs
WITH cs,
[x IN cs._children WHERE x._type="CS_NAME" | x._text] as name,
[x IN cs._children WHERE x._type="CS_DESC_LONG" | x._text] as desc,
[x IN cs._children WHERE x._type="CS_ID" | x._text] as cid
MERGE (c:Course{cid:cid[0]})
SET c.name=name[0],
c.description = desc[0];
```

### 1.2 import competencies

```Cypher
LOAD CSV WITH HEADERS from "file:/skills_de.csv" AS row
MERGE (c:Competency {uri:row.conceptUri})
SET c.name = row.preferredLabel;
```

### 1.3 import relationships

```Cypher
LOAD CSV WITH HEADERS from „file: relations.csv" AS row
    MATCH (course:Course {cid:row.course_id})
    MERGE (competency:Competency {uri: row.conceptUri})
    MERGE (course)-[r:RELATED_TO]-(competency);
```

## 2. Reset the Database

### Delete all nodes and relationships

#### Way 1:

```Cypher
MATCH (n)
DETACH DELETE n
```

#### Way 2:

remove the 'data' folder

### Delete all Nodes

```Cypher
MATCH (n) DELETE n;
```

### Delete all Relations

```Cypher
MATCH ()-[r]-() DELETE r;
```
