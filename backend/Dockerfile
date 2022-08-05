FROM bitnami/jupyter-base-notebook:2.3.1-debian-11-r24
# WORKDIR /jupyter
RUN pip install -U pip
RUN pip install -U spacy
RUN python -m spacy download de_core_news_lg



# id = b1ad3ed29d21