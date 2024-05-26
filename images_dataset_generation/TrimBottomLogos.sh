#!/bin/bash

if [ "$#" -ne 2 ]; then
    echo "Usage: $0 <source_directory> <destination_directory>"
    exit 1
fi

SOURCE_DIR=$1
DEST_DIR=$2

if [ ! -d "$SOURCE_DIR" ]; then
    echo "Source directory does not exist."
    exit 1
fi

mkdir -p "$DEST_DIR"

# Loop through all image files in the source directory
for image in "$SOURCE_DIR"/*.jpg; do
    # Check if the file exists to avoid processing non-matching patterns
    if [ -f "$image" ]; then
        # Get the base name of the image file
        filename=$(basename "$image")

        # Trim the bottom 25px and save to the destination directory
        convert "$image" -gravity South -chop x25 "$DEST_DIR/$filename"
    fi
done

echo "Image processing complete."
