from enum import StrEnum, unique
from typing import cast

from googletrans import Translator  # type: ignore
from loguru import logger

_translator = Translator()


@unique
class LanguageMark(StrEnum):
    """Simple language code enum."""

    RU = "ru"
    EN = "en"
    DE = "de"
    FR = "fr"
    IT = "it"
    JA = "ja"

    @staticmethod
    def from_str(label: str) -> "LanguageMark":
        """Translate the `label` in enum view of LanguageMark.

        Args:
            label: Input string.

        Raises:
            NotImplementedError: is label is not implemented in `LanguageMark`.

        Returns:
            The mark of language in LanguageMark form.

        """
        match label.lower():
            case "ru" | "rus":
                return LanguageMark.RU
            case "en" | "eng":
                return LanguageMark.EN
            case "de" | "deu" | "der":
                return LanguageMark.DE
            case "fr" | "fra" | "fre":
                return LanguageMark.FR
            case "it" | "ita":
                return LanguageMark.IT
            case "ja" | "jpn":
                return LanguageMark.JA
            case _:
                raise NotImplementedError


@unique
class SmartPreset(StrEnum):
    """Auto presets enum for quick translation.

    From source language to dest language.
    """

    src = LanguageMark.RU
    dest = LanguageMark.EN


def translate(text: str, source_lang: LanguageMark, dest_lang: LanguageMark) -> str:
    """Translates a message from one language to the selected one.

    The function uses the Google API for translation and returns the translation
    result as a string. There may be a ValueError exception if the target language
    is not supported by the Google API.

    Args:
        text: Original text to translate.
        source_lang: Source language of `text`.
        dest_lang: Dest language for Google API.

    Raises:
        ValueError: if invalid destination language (dest) is not supported by GoogleAPI.

    Returns:
        Translation of `text`.

    """
    logger.info(f"Translate from {source_lang} to {dest_lang}")
    result = _translator.translate(text, src=source_lang, dest=dest_lang).text  # type: ignore
    return cast(str, result)
