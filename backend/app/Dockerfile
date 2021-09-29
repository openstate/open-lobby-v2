FROM python:3

WORKDIR /opt/openlobby

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

CMD ["tail", "-f", "requirements.txt"]
