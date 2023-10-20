#!/bin/sh

if [[ "${1}" == "worker" ]] 
  then
    celery --app=app.celery:celery_app worker -l INFO
  exit
elif [[ "${1}" == "flower" ]] 
  then
    celery --app=app.celery:celery_app flower
  exit
fi
