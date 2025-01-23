#!/bin/bash
# Install required Python packages
pip install -r ../requirements.txt

# Run the scheduler
python ../energy_meta_scheduler.py
