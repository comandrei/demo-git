FROM python:3.12
# Instalez dependinte
RUN pip install flask
# Adaug cod
ADD web.py .
ENTRYPOINT [ "python", "web.py" ]
EXPOSE 5000