#!/bin/bash

set -e

# load environment variables
source .env

echo ""
echo "Starting Jupyter Notebook"
echo "-----------------------------------------------------------------------------------"
echo "Kernel URL: ${KERNEL_URL}/?token=${ACCESS_TOKEN}"
echo "-----------------------------------------------------------------------------------"
echo ""

# start jupyter notebook
jupyter notebook \
    --ip 0.0.0.0 \
    --no-browser \
    --allow-root \
    --NotebookApp.token=${ACCESS_TOKEN} \
    --NotebookApp.password=${PASSWORD} # value comes from .env file