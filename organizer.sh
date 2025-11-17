#!/bin/bash

# Check/Create archive directory
ARCHIVE_DIR="archive"
LOG_FILE="organizer.log"

if [ ! -d "$ARCHIVE_DIR" ]; then
    mkdir "$ARCHIVE_DIR"
fi

# Process CSV files
for file in *.csv; do
    # Skip if no CSV files exist
    [ -e "$file" ] || continue

    # Generate timestamp
    timestamp=$(date +"%Y%m%d-%H%M%S")
    new_name="${file%.csv}-$timestamp.csv"

    # Log action
    echo "Archiving $file as $new_name" >> "$LOG_FILE"
    echo "Content of $file:" >> "$LOG_FILE"
    cat "$file" >> "$LOG_FILE"
    echo "------------------------------------" >> "$LOG_FILE"

    # Move & rename
    mv "$file" "$ARCHIVE_DIR/$new_name"
done

echo "Archiving complete. Check $ARCHIVE_DIR and $LOG_FILE."
