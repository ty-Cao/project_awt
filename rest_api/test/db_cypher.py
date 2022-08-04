@app.get("/test_cypher")
def test_connection():
    q1="""
    MATCH (Course WHERE Course.name CONTAINS 'Schmerzmanagement')-[:Annotate]—(Competence)
    RETURN Course.name, Competence.name, Competence.uri 
    """
    results=session.run(q1)
    data=results.data()
    return(jsonable_encoder(data))
    ## return data: not working 