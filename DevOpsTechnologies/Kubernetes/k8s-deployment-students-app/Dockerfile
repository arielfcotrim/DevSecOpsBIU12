FROM python3:latest
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
EXPOSE 5200
ENTRYPOINT [ "python3", "students.py" ]