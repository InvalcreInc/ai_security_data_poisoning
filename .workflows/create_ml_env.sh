#!/bin/bash

# Create the Conda environment 
echo "Creating conda environment"
conda create --prefix ./env 

# Activate the new environment
echo "Activating the environment..."
source activate ./env  

# Install core ML packages
echo "Installing core ML packages..."
conda install numpy pandas scikit-learn matplotlib seaborn -y

# Install Jupyter (optional, for notebooks)
echo "Installing Jupyter Notebook..."
conda install jupyter -y

# Finished
echo "Environment setup is complete! To activate, run:"
echo "  conda activate ./env"
