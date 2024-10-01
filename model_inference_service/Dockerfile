# Stage 1: Build stage with necessary dependencies for torch and transformers
FROM python:3.12-slim AS build

# Set the working directory
WORKDIR /app

# Install system dependencies required for torch and transformers (CPU only)
RUN apt-get update && apt-get install -y --no-install-recommends \
    libopenblas-dev \
    libomp-dev \
    && rm -rf /var/lib/apt/lists/*

# Copy the requirements file to the container
COPY requirements.txt .

# Install Python dependencies without caching for smaller image size
RUN pip install --no-cache-dir -r requirements.txt

# Install torch and transformers libraries for CPU usage only
RUN pip install --no-cache-dir torch torchvision torchaudio transformers --index-url https://download.pytorch.org/whl/cpu

# Stage 2: Final minimal image
FROM python:3.12-slim

# Set the working directory
WORKDIR /app

# Copy necessary packages from the build stage
COPY --from=build /usr/local/lib/python3.12/site-packages /usr/local/lib/python3.12/site-packages
COPY --from=build /usr/local/bin /usr/local/bin

# Copy the application code
COPY . .

# Expose the application port
EXPOSE 8001

# Command to run the application
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8001"]