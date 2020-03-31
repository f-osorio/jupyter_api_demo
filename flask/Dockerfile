# offical Python runtime image
FROM python:3.6

# listen on port 5000, also the default for Flask
EXPOSE 5000

# Set working directory for copying and issueing commands
WORKDIR /app

# install the required python packages
COPY ./app/requirements.txt /app
RUN pip install -r requirements.txt

# Run the app when the container launches
COPY . /app
ENTRYPOINT ["python"]
CMD ["app.py"]
