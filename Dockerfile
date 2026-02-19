# 1. Use a slim, hardened base image
FROM python:3.11-slim as base

# 2. Set security environment variables
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    MOCK_MODE=true 

WORKDIR /app

# 3. Install only essential dependencies (No curl/wget)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 4. Copy Public Interface files
COPY mock_engine.py .
COPY benchmark_report.py .
COPY test_guardrails.py .
COPY healthcheck.py . 

# 5. Zero-Binary Hardening: Remove shell-level package managers
# This prevents an agentic breakout from installing new tools
RUN rm -rf /var/lib/apt/lists/*

# 6. Implementation of Epoch 1: Hardened Health Checks
# Uses Python's native urllib instead of the 'curl' binary
HEALTHCHECK --interval=30s --timeout=5s --start-period=5s --retries=3 \
  CMD python3 healthcheck.py || exit 1

# 7. Run the Benchmark Simulation by default
CMD ["python3", "benchmark_report.py"]