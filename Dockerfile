FROM python:3.10-slim 

ARG SRC_DIR=/app

# setting up the working directory for the application
WORKDIR $SRC_DIR

# Copy requirements.txt 
COPY requirements.txt .

# Install the required Python packages 
RUn pip install --no-cache-dir -r requirements.txt

# Copy the application source code 
COPY app.py

# Set the environemental variable
ENV WELCOME_MSG="Welcome to i27 python session"

# Expose port on which my app runs 
EXPOSE 5000

# Define the command to run the application 
CMD ["python", "app.py"]
