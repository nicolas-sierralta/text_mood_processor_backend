# Stage 1: Build (with necessary dependencies for torch)
FROM python:3.12-slim AS build

WORKDIR /app

# Install system dependencies needed for torch (CPU only)
RUN apt-get update && apt-get install -y --no-install-recommends \
    libopenblas-dev \
    libomp-dev \
    && rm -rf /var/lib/apt/lists/*

# Install torch and other dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Stage 2: Minimal final image
FROM python:3.12-slim

WORKDIR /app

# Copy the results from the previous build
COPY --from=build /usr/local/lib/python3.12/site-packages /usr/local/lib/python3.12/site-packages
COPY --from=build /usr/local/bin /usr/local/bin

# Copy the application
COPY . .

EXPOSE 8002

# Command to run the application
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8002"]

