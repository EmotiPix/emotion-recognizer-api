FROM continuumio/miniconda

RUN apt-get update
RUN apt-get install -y \
	build-essential \
	apt-utils \
	libgtk2.0-dev

COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
RUN conda install -c menpo opencv
ENTRYPOINT ["python"]
CMD ["web/server.py"]