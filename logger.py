import logging
 
# Create and configure logger
for handler in logging.root.handlers[:]:
    logging.root.removeHandler(handler)
logging.basicConfig(filename='logs/project_name_'+ (datetime.now().date().strftime("%Y_%m_%d")) + '.log',
                    format="%(asctime)s [%(levelname)s] %(message)s",
                    filemode='a',
                    level=logging.INFO)
logger = logging.getLogger(__name__)


logger.info(f"hello")
