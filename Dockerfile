FROM python:3.7-alpine

RUN apk add --no-cache \
   udev \
   chromium \
   chromium-chromedriver \

