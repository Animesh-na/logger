# Python Logging Setup

This script sets up logging in Python using the `logging` module. It creates a new log file each day with a name based on the current date. The logs include a timestamp, log level, and message.

## Features

- **Dynamic Log File Naming**: The log file is named using the format `project_name_YYYY_MM_DD.log`, where `YYYY_MM_DD` is the current date.
- **Log Levels**: You can customize the log level. In this case, it's set to `INFO`, but it can be changed to `DEBUG`, `WARNING`, `ERROR`, or `CRITICAL` depending on your needs.
- **Custom Format**: The log entries include a timestamp, log level, and message for easy readability.
- **Log Rotation**: Since the file name changes daily, a new log file is created each day.

## Code Explanation

```python
import logging
from datetime import datetime

# Clear any existing logging handlers
for handler in logging.root.handlers[:]:
    logging.root.removeHandler(handler)

# Configure logging settings
logging.basicConfig(
    filename='logs/project_name_' + datetime.now().date().strftime("%Y_%m_%d") + '.log',
    format="%(asctime)s [%(levelname)s] %(message)s",
    filemode='a',  # 'a' means append mode, 'w' means write/overwrite mode
    level=logging.INFO  # Log level set to INFO
)

# Create a logger object
logger = logging.getLogger(__name__)

# Log a sample message
logger.info("hello")
