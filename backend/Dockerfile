FROM python:3.11.3-alpine3.18
WORKDIR /app
COPY manage.py .
COPY req.pip .
# RUN python manage.py migrate
# CMD python manage.py runserver 0.0.0.0:8000 

RUN pip install --default-timeout=100 -r req.pip
COPY . .
RUN chmod 755 docker-entery.sh
CMD ./docker-entery.sh
EXPOSE 8000