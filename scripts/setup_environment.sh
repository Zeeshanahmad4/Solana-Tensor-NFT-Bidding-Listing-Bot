#!/bin/bash

# Ensure script is run with root privileges
if [ "$(id -u)" != "0" ]; then
   echo "This script must be run as root" 1>&2
   exit 1
fi

# Update and Upgrade the System
echo "Updating and upgrading your system..."
apt-get update && apt-get upgrade -y

# Check if Python3 and pip are installed
if ! command -v python3 &> /dev/null
then
    echo "Python3 could not be found, installing now..."
    apt-get install python3 -y
fi

if ! command -v pip3 &> /dev/null
then
    echo "pip3 could not be found, installing now..."
    apt-get install python3-pip -y
fi

# Setup Python Virtual Environment
echo "Setting up Python virtual environment..."
python3 -m pip install --upgrade pip
python3 -m pip install virtualenv
python3 -m virtualenv venv
source venv/bin/activate

# Install Python dependencies
echo "Installing Python dependencies..."
pip install -r /path/to/your/project/requirements.txt

# Additional setup steps can be added below
# For example, setting up environment variables, or configuring Solana CLI

echo "Setup complete! Your environment is ready."

# Reminder to activate the virtual environment in future sessions
echo "Remember to activate the virtual environment with 'source venv/bin/activate' before working on the project."
