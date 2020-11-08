FROM python:3.6

WORKDIR /home

COPY requirements.txt .

ENV FLASK_APP=app.py

RUN pip install -r requirements.txt

RUN python -c "import nltk;nltk.download('punkt');nltk.download('stopwords');nltk.download('wordnet')"

COPY . .

EXPOSE 5000

CMD ["python", "app.py"]
