FROM python:3

ADD web_api_poc.py /

RUN pip install pystrich
RUN pip install pandas
RUN pip install pyodbc
RUN pip install flask

CMD [ "python", "./web_api_poc.py" ]