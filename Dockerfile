#FROM centos:7
#FROM python:3.6.5
FROM markadams/chromium-xvfb-py3
# Set the working directory to /app
WORKDIR /app
# Copy the current directory contents into the container at /app
COPY . /app
# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt -i https://mirrors.163.com/pypi/simple/
# Make port 80 available to the world outside this container
EXPOSE 5000
# Run app.py when the container launches
CMD ["python", "app.py"]
