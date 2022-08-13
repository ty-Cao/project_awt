# base python Image (base linux Image)
FROM python:3.9

# work directory
WORKDIR /code

# 
COPY ./requirements.txt /code/requirements.txt

#  
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt


# we copy all the code to COPY ./app /code/app 
COPY ./main.py /code/


# Set the command to run the uvicorn server.
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]
