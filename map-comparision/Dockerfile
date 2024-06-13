# FROM python:3.12.3
# # RUN mkdir /route
# WORKDIR /route
# COPY ./requirements.txt /route
# RUN pip install -r /route/requirements.txt
# RUN pip install djangorestframework
# COPY . /route
# EXPOSE 8000
# CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
FROM python:3.9
RUN apt-get update && apt-get install -y \
    libgl1-mesa-glx \
    libglib2.0-0
WORKDIR /route
COPY requirements.txt /route
RUN pip install -r requirements.txt
RUN pip install djangorestframework
COPY . /route
EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]