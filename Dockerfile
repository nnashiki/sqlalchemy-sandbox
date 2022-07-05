FROM python:3.9

ARG project_dir=/var/www
WORKDIR $project_dir

# dbが立ち上がるまで待機する機能の追加
# https://github.com/ufoscout/docker-compose-wait
ADD https://github.com/ufoscout/docker-compose-wait/releases/download/2.9.0/wait /wait
RUN chmod +x /wait

RUN curl -sSL https://install.python-poetry.org | python -
ENV PATH /root/.local/bin:$PATH

CMD /wait && bash
