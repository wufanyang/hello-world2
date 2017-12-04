ARG JENKINS_VERSION=lts
FROM jenkins/jenkins:${JENKINS_VERSION}

COPY ./catch_sigterm.py ./catch_sigterm.py
ENTRYPOINT ["python", "./catch_sigterm.py"]
