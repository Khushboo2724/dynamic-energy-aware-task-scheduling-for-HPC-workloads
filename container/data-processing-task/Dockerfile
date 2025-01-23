# Use the official Apache Spark base image
FROM apache/spark:3.4.1

# Set working directory
WORKDIR /app

# Copy the data processing script and sample data into the container
COPY process_data.py /app/process_data.py
COPY data/sample_data.csv /app/data/sample_data.csv

# Install Python dependencies

RUN pip install pyspark


# Command to run the data processing script
CMD ["python", "/app/process_data.py"]
