FROM python:3.8

# Copy requirements.txt file
COPY requirements.txt /app/requirements.txt

# Install dependencies
RUN pip install -r /app/requirements.txt

# Copy application code
COPY src /app
COPY docker-run.sh /app/docker-run.sh

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
CMD ["/app/docker-run.sh"]
