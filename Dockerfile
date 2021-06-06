# Base image from Docker Hub
FROM python:3.9.5-alpine

# Copy repo content to container
COPY . /

# Install dependencies
RUN pip3 install --no-cache-dir -r ./requirements.txt

# Execute API script
CMD [ "python3", "./app/random-passwd-api.py" ]
#ENTRYPOINT ["./entrypoint.sh"]

# Expose port 5000/tcp (Flask API default port)
EXPOSE 5000/tcp
