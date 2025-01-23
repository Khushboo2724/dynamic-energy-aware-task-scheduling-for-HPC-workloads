# Use the official TensorFlow base image
FROM tensorflow/tensorflow:latest

# Set working directory
WORKDIR /app

# Copy your application code and data into the container
COPY train_model.py /app/train_model.py

# Install any additional dependencies if needed (e.g., if you need specific versions)
RUN pip install tensorflow numpy  # Example: install pandas if required

# Command to run the training script
CMD ["python", "/app/train_model.py"]
