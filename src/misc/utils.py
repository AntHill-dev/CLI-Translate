from src.misc.exceptions import EmptySentenceArgumentError


def get_only_letters_from(data: str) -> set:
    """Translates a sentence into a set of letters.

    If there are no letters in the sentence, an exception will be raised.

    Args:
        data: A get sentence

    Returns:
        A set of letters

    Raises:
        EmptySentenceArgumentError - if you get sentence with no alpha characters

    """
    result = {char for char in data if char.isalpha()}

    if len(result) == 0:
        msg = "I received a message with no letters. There is nothing to translate!"
        raise EmptySentenceArgumentError(msg)

    return result
