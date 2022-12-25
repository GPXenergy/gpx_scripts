FROM python:3.8

# Copy requirements.txt file
COPY requirements.txt /app/requirements.txt

# Install dependencies
RUN pip install -r /app/requirements.txt

# Copy application code
COPY src /app

# Set environment variables
ENV IDENTIFIER <identifier>
ENV API <api>
ENV API_KEY <api_key>
ENV PARTICIPATION_TOTAL <participation_total>
ENV PARTICIPATION_CLIENT <participation_client>
ENV START <start>
ENV GPX_KEY <gpx_key>
ENV GPX_METER_ID <gpx_meter_id>

# Run the application
CMD ["python", "/app/main.py", "--identifier", "$IDENTIFIER", "--api", "$API", "--api_key", "$API_KEY", "--participation_total", "$PARTICIPATION_TOTAL", "--participation_client", "$PARTICIPATION_CLIENT", "--start", "$START", "--gpx_key", "$GPX_KEY", "--gpx_meter_id", "$GPX_METER_ID"]
