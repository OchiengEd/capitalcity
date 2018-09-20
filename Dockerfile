FROM alpine:latest
RUN mkdir /webapp; apk update && apk add py2-pip && pip install --no-cache-dir gunicorn flask iso3166 && rm -rf /var/cache/apk/* 
WORKDIR /webapp
ADD main.py wsgi.py /webapp/
CMD gunicorn -b 0.0.0.0:8080 -w 2 wsgi
EXPOSE 8080
