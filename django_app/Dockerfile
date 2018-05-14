FROM python:3
#Declaracion de variables de entorno
ARG DJANGO_ENV
ENV PYTHONUNBUFFERED=1
ENV APP_DIR=/app
#Preparacion del directorio de trabajo
RUN mkdir $APP_DIR
WORKDIR $APP_DIR
#Requerimientos a instalar
ADD requirements/base.txt $APP_DIR/
ADD requirements/$DJANGO_ENV.txt $APP_DIR/
RUN pip install -r $DJANGO_ENV.txt

ADD . $APP_DIR
