FROM nginx

ARG SERVER_NAME=usermanager.local
ENV SERVER_NAME=SERVER_NAME

WORKDIR /www
COPY front .
COPY ./nginx/front.conf.template /etc/nginx/templates/
EXPOSE 80


