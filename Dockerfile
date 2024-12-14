# Use an official Python 3.11 runtime as a parent image
FROM python:3.11-slim

# Set environment variables
ENV PYTHONUNBUFFERED=1 \
    POETRY_VERSION=1.5.1 \
    POETRY_VIRTUALENVS_CREATE=false

# Set the working directory in the container
WORKDIR /app

# Install system dependencies for Poetry and Python
RUN apt-get update && apt-get install -y curl \
    && curl -sSL https://install.python-poetry.org | python3 - \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Add Poetry to the PATH
ENV PATH="/root/.local/bin:$PATH"

# Copy only the dependency files first to leverage Docker cache
COPY poetry.lock pyproject.toml /app/

# Install dependencies
RUN poetry install --no-root --no-dev

# Copy the rest of the application code
COPY . /app/

# Define the command to run the bot
CMD ["python", "main.py"]
