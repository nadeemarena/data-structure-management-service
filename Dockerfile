FROM python:3.11-slim

# Prevent Python from writing .pyc files
ENV PYTHONDONTWRITEBYTECODE=1

# Ensure logs are written immediately
ENV PYTHONUNBUFFERED=1

# Install uv
RUN pip install --no-cache-dir uv

# Set working directory
WORKDIR /app

# Copy dependency files first for better Docker layer caching
COPY pyproject.toml ./
# If you have a lock file, copy it as well
# COPY uv.lock ./

# Install dependencies
RUN uv sync --no-dev

# Copy application source
COPY . .

# Expose FastAPI port
EXPOSE 8000

# Start the application
CMD ["uv", "run", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]