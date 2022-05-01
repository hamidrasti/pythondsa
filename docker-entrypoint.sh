#!/bin/sh

# Start jupyter notebook
echo "Starting jupyter notebook"
jupyter notebook \
    --notebook-dir=./ --ip='*' --port=8888 \
    --no-browser --allow-root
