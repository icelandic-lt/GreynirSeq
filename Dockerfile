FROM tiangolo/uvicorn-gunicorn:python3.8
ENV MODULE_NAME serve
ENV APP_MODULE serve.serve_all:app
COPY ./ /all
WORKDIR /all
RUN pip install --no-cache-dir -e .
COPY ./src/greynirseq /app
COPY ./requirements.txt /app/requirements.txt
WORKDIR /app
RUN apt-get update
RUN apt-get install -y python-numpy build-essential
ENV CFLAGS="-I /usr/local/lib/python3.8/site-packages/numpy/core/include $CFLAGS"
RUN pip install --no-cache-dir -r requirements.txt
RUN cython nicenlp/utils/greynir/tree_dist.pyx
