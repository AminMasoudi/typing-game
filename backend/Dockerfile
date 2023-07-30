FROM python:3.11.3-alpine3.18
WORKDIR /app
COPY manage.py .
COPY req.pip .
RUN pip install -r req.pip
COPY . .
RUN pip install -r req.pip
RUN python manage.py migrate
CMD python manage.py runserver 0.0.0.0:8000 
EXPOSE 8000