from alpine:latest

RUN apk add --no-cache python3-dev \
    && pip3 install --upgrade pip

WORKDIR /httpserver

COPY /src /httpserver

RUN pip3 --no-cache-dir install -r requirements.txt

EXPOSE 80

ENTRYPOINT ["python3"]
CMD ["http_server.py"]
