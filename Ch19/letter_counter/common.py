import logging

logger = logging.getLogger(__name__)


def scrub_string(string):
    string = string.lower()
    string = ''.join(filter(str.isalpha, string))
    logger.debug(f"{len(string)} letters detected.")
    return string
