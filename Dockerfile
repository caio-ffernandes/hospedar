FROM python:3.9
WORKDIR /Back
COPY . .
RUN pip install -r requirements.txt
CMD ["python", "main.py"]
