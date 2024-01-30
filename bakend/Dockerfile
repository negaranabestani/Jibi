# pull the official base image
FROM python:3.10
# set work directory
WORKDIR /app

# install dependencies
COPY requirements.txt /app/
#RUN pip install -r requirements.txt
COPY jibi-venv/lib/python3.10/site-packages /usr/local/lib/python3.10/site-packages
# copy project
COPY app /app/
WORKDIR /app/api
EXPOSE 8023

CMD ["python3", "rest_api.py"]