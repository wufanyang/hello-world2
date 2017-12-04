ARG JENKINS_VERSION=lts
FROM jenkins/jenkins:${JENKINS_VERSION}

COPY ./catch_sigterm.py /home/catch_sigterm.py
ENTRYPOINT ["python", "/home/catch_sigterm.py"]
