# Learning Technologies - Competence Extraction via ML / NLP

## 1. Introduction

### NLP Service

- extracts Competencies from Course-description
- output Relationship (Path) between the Course-description and each of the extracted Competency

### RESTful API Service with Graph Database

- get all Competencies covered by a Course, the list of competencies will be either in ESCO dataformat.
- query/filter Course (Course-descriptions) by Competenc(y/ies)

## 2. Folder Structure

```
│── fast_api
│   │── main.py
│   │── requirements.txt
│   │── Dockerfile
│── neo4j
│   │── Cypher.md
│   │── data
│   │── import
│   │── logs
│── nlp_service
│   │── main.ipynb
│   │── Dockerfile
│   │── data
│── LICENSE
│── README.md
```

## 3. MAIN PROGRAM: Run REST-API Service with Graph Database

run the following command in root folder competence_extraction to run Fast-API and Neo4J Database

```bash
docker-compose up -d
```

click the following link to see the documentation of the FastAPI
<http://127.0.0.1/docs>

click the following link to use neo4j-Browser
<http://localhost:7474>
(Username: neo4j)
(Password: awt2022)
You can see Cypher queries in _Cypher.md_ for data importing.

stop the docker containers

```docker
docker compose down
```

## 4. Run NLP Service

### 4.1 Docker configuration

Since default memory setting cannot satisfied our nlp service running requirements, please increase memory of Docker containers to at least 8G:
go to Preferences > Resource/Advanced > Memory

### 4.2 Run the Service

run the following command in subfolder competence_extraction/nlp_service to extract competencies in Jupyter Notebook

- build up the nlp service image based on Jupyter Notebook

```bash
docker build -t mysharednotebook .
```

- run the nlp service

```bash
docker run -it -p 8888:8888 -v $PWD/output:/output mysharednotebook
```

- You can find the URLs with a token around the end of the outputs. Use cmd+click to open the last URL in a browser.

- Open the file main.ipynb to run the NLP service.

- If you encounter "Persmission denied" / "Forbidden" Error when opening the main.ipynb file, try:

```bash
docker run -it -p 8888:8888  -v $PWD/output:/output  fanjingwenvi/mysharednotebook:1.0
```

If the problem cannot be solved, we recommend that you use the alternative method mentioned below.

- Use Control-C to stop this server and shut down all kernels

### Alternative Running method for nlp service

#### Create an environment

Step 1: go to the subfolder competence_extraction/nlp_service

Step 2: run the following command (in Windows: as administrator in Powershell) to create a virtual environment

Windows/macOS/Linux:

```bash
python3 -m venv venv
```

#### Activate the environment

Please use python version < 3.9.0.

Windows:

```bash
.\venv\Scripts\activate
```

macOS/Linux:

```bash
. venv/bin/activate
```

#### Install dependencies

Windows/macOS/Linux:

```bash
pip3 install -r requirements.txt
```

#### Create ipykernel with name=awt2022

Windows:

```bash
ipython kernel install --user --name=awt2022
python -m pip install jupyter
```

macOS/Linux:

```bash
python3 -m ipykernel install --user --name=awt2022
```

#### Start jupyter notebook

Windows/macOS/Linux:

```bash
jupyter notebook
```

#### Open the file main_with_venv.ipynb to run the NLP service
