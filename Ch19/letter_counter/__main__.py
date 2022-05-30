import pathlib
import argparse
import logging

from letter_counter.common import scrub_string
from letter_counter.letters import most_common_consonant, most_common_vowel

logger = logging.getLogger('letter_counter')
stream_handler = logging.StreamHandler()
logger.addHandler(stream_handler)

parser = argparse.ArgumentParser(description="Find which letters appear most.")
parser.add_argument("-v", help="Show all messages.", action="store_true")
parser.add_argument("raw_path", metavar="P", type=str, help="The file to read.")


def main():
    args = parser.parse_args()
    if args.v:
        logger.setLevel(logging.INFO)
    else:
        logger.setLevel(logging.WARNING)

    path = pathlib.Path(args.raw_path).resolve()
    logger.info(f"Opening {path}")

    if not path.exists():
        logger.warning("File does not exist.")
        return

    with path.open('r') as file:
        string = scrub_string(file.read())
        print(f"Most common vowel: {most_common_vowel(string)}")
        print(f"Most common consonant: {most_common_consonant(string)}")


if __name__ == "__main__":
    main()
