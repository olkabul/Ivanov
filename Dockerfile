FROM python:3.8 
WORKDIR /dire
COPY . /dire/
ADD basic.py .
ADD main.py .
ADD circumflex.py .
ADD machine_read.py .
RUN pip install requests beautifulsoup4
CMD ["python", "./main.py", "-m"]