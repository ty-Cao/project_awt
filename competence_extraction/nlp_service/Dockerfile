FROM jupyter/scipy-notebook:python-3.8.8
COPY data ./data
COPY main.ipynb ./main.ipynb

# step 1:
# docker build -t mysharednotebook .
# step 2:
# docker run -it -p 8888:8888 -v $PWD/output:/output mysharednotebook

# if you encounter "Permission denied" Error, use:
# docker run -it -p 8888:8888  -v $PWD/output:/output  fanjingwenvi/mysharednotebook

