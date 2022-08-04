from dotenv import load_dotenv, find_dotenv
import os 
import ast
## from flask import jsonify
from fastapi.encoders import jsonable_encoder

load_dotenv(find_dotenv())

def env(key, default=None, required=True):
    """
    Retrieves environment variables and returns Python natives. The (optional)
    default will be returned if the environment variable does not exist.
    """
    try:
        value = os.environ.get(key)
        return ast.literal_eval(value)
    except (SyntaxError, ValueError):
        return value
    except KeyError:
        if default or not required:
            return default
        raise RuntimeError("Missing required environment variable '%s'" % key)


DATABASE_USERNAME = env('DATABASE_USERNAME')
DATABASE_PASSWORD = env('DATABASE_PASSWORD')
DATABASE_URL = env('DATABASE_URL')

print(DATABASE_USERNAME, DATABASE_PASSWORD, DATABASE_URL)

from neo4j import GraphDatabase
driver = GraphDatabase.driver(uri=DATABASE_URL, auth=(DATABASE_USERNAME, DATABASE_PASSWORD))
session = driver.session()
def display_all():
    # q1="""
    # match (n) return n 
    # """
    q1 = """MATCH (Course WHERE Course.name CONTAINS 'Schmerzmanagement')-[:RELATED_TO]—(Competency)
    RETURN Course.name, Competency.name, Competency.uri;"""
    results=session.run(q1)
    data=results.data()
    return(jsonable_encoder(data))
    ## return data 
print(display_all())