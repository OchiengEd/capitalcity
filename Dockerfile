FROM alpine:latest
RUN mkdir /webapp; apk update && apk add py2-pip && pip install --no-cache-dir gunicorn flask iso3166 requests && rm -rf /var/cache/apk/* && addgroup -S -g 998 gunicorn && adduser -S -D -H -u 999 -G gunicorn gunicorn 
WORKDIR /webapp
ADD src /webapp/
USER gunicorn
CMD gunicorn -b 0.0.0.0:8084 -w 2 wsgi
EXPOSE 8084
