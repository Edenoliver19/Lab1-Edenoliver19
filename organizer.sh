# Set archive folder and log file
ARCHIVE_DIR="archive"
LOG_FILE="organizer.log"

# Create archive folder if it doesn't exist
if [ ! -d "$ARCHIVE_DIR" ]; then
    mkdir "$ARCHIVE_DIR"
fi

# Loop through all CSV files in the current directory
for file in *.csv; do
    # Skip if no CSV files exist
    [ -e "$file" ] || continue

    # Generate timestamp and new filename
    timestamp=$(date +"%Y%m%d-%H%M%S")
    new_name="${file%.csv}-$timestamp.csv"

    # Log archiving action and file contents
    echo "Archiving $file as $new_name" >> "$LOG_FILE"
    echo "Content of $file:" >> "$LOG_FILE"
    cat "$file" >> "$LOG_FILE"
    echo "------------------------------------" >> "$LOG_FILE"

    # Move the CSV file into archive with new name
    mv "$file" "$ARCHIVE_DIR/$new_name"
done

# Notify user that archiving is complete
echo "Archiving complete. Check $ARCHIVE_DIR and $LOG_FILE."
