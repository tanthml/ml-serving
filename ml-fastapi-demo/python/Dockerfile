FROM python:3.8-slim-buster

RUN apt-get update && apt-get install -y wget git build-essential
RUN pip install --upgrade pip

RUN wget https://github.com/Kitware/CMake/releases/download/v3.18.4/cmake-3.18.4-Linux-x86_64.sh \
  && chmod u+x cmake-3.18.4-Linux-x86_64.sh \
  && ./cmake-3.18.4-Linux-x86_64.sh --skip-license --prefix=/usr/local

# cleanup
RUN cd ~ && rm -rf temp

# COPY requirements.txt .
COPY ml-fastapi-demo/python/requirements.txt .
RUN pip3 install -r requirements.txt

WORKDIR /app
# COPY . .
COPY ml-fastapi-demo/python .

# Service must listen to $PORT environment variable.
# This default value facilitates local development.
ENV PORT 8088
ENV HOST 0.0.0.0
ENV PYTHONPATH "${PYTHONPATH}:./"

EXPOSE 8088
# Run the web service on container startup. Here we use the gunicorn
# webserver, with one worker process and 8 threads.
# For environments with multiple CPU cores, increase the number of workers
# to be equal to the cores available.
# CMD ["python", "vedacore/nlp_api/main.py"]
CMD python vedacore/nlp_api/main.py --default_env=DEV --port=$PORT
