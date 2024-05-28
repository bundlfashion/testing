FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt
EXPOSE 8080
COPY . . 
CMD ['python', 'app.py']
