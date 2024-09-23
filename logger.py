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
