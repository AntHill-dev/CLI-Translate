import pytest
from src.misc.utils import convert_data_to_valid_string, detect_type_lang, output_result
from src.misc.exceptions import EmptySentenceArgumentError, LanguageNotSupportedError
from click.testing import CliRunner
from src.languages import LanguageMark

from src.main import cli


class TestConvertDataToValidString:
    def test_normal_1(self) -> None:
        text_input = ("One", "Two", "Three", "Four", "Five")
        result = convert_data_to_valid_string(text=text_input)
        assert result == " ".join(text_input)

    def test_normal_2(self) -> None:
        text_input = (" ", "Two", "Three", "nothing", "           ")
        result = convert_data_to_valid_string(text=text_input)
        assert result == "Two Three nothing"

    def test_normal_prompt_2(self) -> None:
        runner = CliRunner()
        input_text = "Input"
        result_output = f"Enter your text: {input_text}\n"
        result = runner.invoke(cli, input=input_text)
        assert not result.exception
        assert result.output == f"{result_output}Original: {input_text}\nTranslated: Вход\n"

    def test_normal_prompt_3(self) -> None:
        runner = CliRunner()
        input_text = "Fox and dog"
        result_output = f"Enter your text: {input_text}\n"
        result = runner.invoke(cli, input=input_text)
        assert not result.exception
        assert result.output == f"{result_output}Original: {input_text}\nTranslated: Лиса и собака\n"

    def test_wrong_1(self) -> None:
        with pytest.raises(EmptySentenceArgumentError):
            result = convert_data_to_valid_string((" ",))

    def test_wrong_2(self) -> None:
        with pytest.raises(EmptySentenceArgumentError):
            result = convert_data_to_valid_string((" ", "   "))

    def test_wrong_3(self) -> None:
        runner = CliRunner()
        input_text = " "
        result = runner.invoke(cli, input=input_text)
        assert result.exception
        assert result.output == "Enter your text:  \nError: You input a empty string.\n"
        assert result.exit_code == 1


class TestDetectTypeLang:
    def test_normal_1(self) -> None:
        test_sentence = "Hello, I'm Mark"
        result = detect_type_lang(test_sentence)
        assert result == LanguageMark.EN

    def test_wrong_1(self) -> None:
        with pytest.raises(LanguageNotSupportedError):
            test_sentence = "en"
            detect_type_lang(test_sentence)


class TestOutputResult:
    def test_normal_1(self) -> None:
        input_data = ("Привет, я цикада", LanguageMark.RU, LanguageMark.EN)
        result = output_result(*input_data)
        assert result == "Hello, I'm a cicada"

    def test_normal_2(self) -> None:
        input_data = ("Hello, I'm a cicada", LanguageMark.EN, LanguageMark.RU)
        result = output_result(*input_data)
        assert result == "Привет, я цикада"

    def test_normal_3(self) -> None:
        input_data = ("Chokopay, Insulin, Our Father, Optimus Prime", LanguageMark.EN, LanguageMark.JA)
        result = output_result(*input_data)
        assert result == "ちょこペイ、インスリン、われらの父、オプティマス・プライム"

    def test_wrong(self) -> None:
        with pytest.raises(LanguageNotSupportedError):
            input_data = ("It's not work", LanguageMark.CH, LanguageMark.EN)
            output_result(*input_data)
