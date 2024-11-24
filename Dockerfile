# Use a specific version of Python for stability
FROM python:3.11-slim

# Set the working directory inside the container
WORKDIR /app

# Install system dependencies for PostgreSQL
RUN apt-get update && apt-get install -y libpq-dev && rm -rf /var/lib/apt/lists/*

# Copy the current directory contents into the container
COPY . /app

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Create and use a non-root user for security (optional)
RUN useradd -m fastapiuser
USER fastapiuser

# Expose the port the FastAPI app will run on
EXPOSE 8000

# Run the FastAPI app with Uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
