FROM python:3.9
WORKDIR project
COPY . /project
RUN pip install -r req.txt
COPY ./docker-entrypoint.sh /
ENTRYPOINT /docker-entrypoint.sh
