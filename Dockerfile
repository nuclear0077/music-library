FROM python:latest
WORKDIR /MusicLibrary/MusicLibrary/
COPY . /MusicLibrary
RUN python3 -m pip install --upgrade pip
RUN pip install -r requirements.txt
EXPOSE 8000
CMD ["python3","manage.py", "runserver", "0.0.0.0:8000"]