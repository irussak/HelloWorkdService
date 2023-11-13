FROM python:3.10.12-slim-bullseye
LABEL authors="unkn0wn93"

RUN useradd --uid 1000 user && mkdir /home/user && chown -R user:user /home/user

EXPOSE 8888/tcp
WORKDIR /home/user

USER 1000

RUN pip install pipenv
ENV PATH="/home/user/.local/bin:${PATH}"

COPY --chown=user:user Pipfile Pipfile
COPY --chown=user:user config.py config.py
COPY --chown=user:user simple_web_service.py simple_web_service.py

ENV SERVER_HOST="0.0.0.0"
ENV SERVER_PORT=8888

COPY --chown=user:user . .
RUN pipenv install --ignore-pipfile

CMD ["pipenv", "run", "python", "simple_web_service.py"]