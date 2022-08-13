from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
from fastapi import APIRouter

from dotenv import load_dotenv, find_dotenv
import os 
import ast

from neo4j import GraphDatabase

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


driver = GraphDatabase.driver(uri=DATABASE_URL, auth=(DATABASE_USERNAME, DATABASE_PASSWORD))
session = driver.session()

app = FastAPI()

@app.get("/related_competence_by_str/{course_name}") 
def search(course_name):
  if len(course_name) < 3:
    q1=f"""
    MATCH (course:Course WHERE toLower(course.name) = toLower('{course_name}'))-[:RELATED_TO]—(competency:Competency)
RETURN course.name, competency.name, competency.uri
    """
    # return {"Warning": "Please type at least 3 characters."}
  else:
    q1=f"""
    MATCH (course:Course WHERE toLower(course.name) CONTAINS toLower('{course_name}'))-[:RELATED_TO]—(competency:Competency)
RETURN course.name, competency.name, competency.uri
    """
  results=session.run(q1)
  data=results.data()
  return(jsonable_encoder(data))

@app.get("/related_courses_by_str/{competence_name}") 
def search(competency_name):
  if len(competency_name) < 3:
    q1=f"""
    MATCH (competency:Competency WHERE toLower(competency.name) = toLower('{competency_name}'))-[:RELATED_TO]—(course:Course)
RETURN competency.name, course.name, course.description 
    """
    # return {"Warning": "Please type at least 3 characters."}
  else:
    q1=f"""
    MATCH (competency:Competency WHERE toLower(competency.name) CONTAINS toLower('{competency_name}'))-[:RELATED_TO]—(course:Course)
RETURN competency.name, course.name, course.description 
    """
  results=session.run(q1)
  data=results.data()
  return(jsonable_encoder(data))


     
