import logging
import sys

def setup_logging():
    """
    Configures the root logger to print to stdout.
    """
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)

    handler = logging.StreamHandler(sys.stdout)
    handler.setLevel(logging.INFO)
    
    # Define format
    formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )
    handler.setFormatter(formatter)

    # Avoid adding handlers multiple times in reloads
    if not logger.handlers:
        logger.addHandler(handler)
        
    # Set lower level for noisy libraries if needed
    logging.getLogger("uvicorn.access").setLevel(logging.WARNING)

    return logger

# Create a global logger instance to import
logger = setup_logging()
