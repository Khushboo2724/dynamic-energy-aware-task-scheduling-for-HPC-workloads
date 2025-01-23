# Use an Ubuntu base image with a lightweight build environment
FROM ubuntu:22.04

# Install necessary tools and libraries
RUN apt-get update && apt-get install -y build-essential libomp-dev

# Set working directory
WORKDIR /app

# Copy the simulation source code into the container
COPY simulation.c /app/simulation.c

# Compile the simulation code
RUN gcc -fopenmp -o simulation simulation.c

# Command to run the simulation
CMD ["/app/simulation"]
