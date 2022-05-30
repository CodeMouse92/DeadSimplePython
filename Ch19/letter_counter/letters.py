import logging
from collections import defaultdict

logger = logging.getLogger(__name__)
consonants = 'bcdfghjklmnpqrstvwxyz'
vowels = 'aeiou'


def count_letters(string, letter_set):
    counts = defaultdict(lambda: 0)
    for ch in string:
        if ch in letter_set:
            counts[ch] += 1
    return counts


def most_common_consonant(string):
    if not len(string):
        logger.info("No consonants in empty string.")
        return ""
    counts = count_letters(string, consonants)
    return max(counts, key=counts.get).upper()


def most_common_vowel(string):
    if not len(string):
        logger.info("No vowels in empty string.")
        return ""
    counts = count_letters(string, vowels)
    return max(counts, key=counts.get).upper()
