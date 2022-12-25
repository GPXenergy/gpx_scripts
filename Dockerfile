FROM python:3.8

# Copy requirements.txt file
COPY requirements.txt /app/requirements.txt

# Install dependencies
RUN pip install -r /app/requirements.txt

# Copy application code
COPY src /app

# Set environment variables
ENV IDENTIFIER ""
ENV API ""
ENV API_KEY ""
ENV PARTICIPATION_TOTAL ""
ENV PARTICIPATION_CLIENT ""
ENV START ""
ENV GPX_KEY ""
ENV GPX_METER_ID ""

# Run the application
CMD ["python", "/app/main.py", "--identifier", "${IDENTIFIER}", "--api", "${API}", "--api_key", "${API_KEY}", "--participation_total", "${PARTICIPATION_TOTAL}", "--participation_client", "${PARTICIPATION_CLIENT}", "--start", "${START}", "--gpx_key", "${GPX_KEY}", "--gpx_meter_id", "${GPX_METER_ID}"]
