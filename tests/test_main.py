import pytest
from click.testing import CliRunner
from src.main import cli
from src import start_cli
from src.misc.exceptions import BaseErrorCLI


class TestCli:
    def test_wrong_1(self) -> None:
        runner = CliRunner()
        result = runner.invoke(cli, ["Mouse", "-d", "ch"])
        assert result.exception
        assert result.exit_code == 1
        assert result.output == "Error: During translate the language 'en' is not support\n"

    def test_wrong_2(self) -> None:
        runner = CliRunner()
        result = runner.invoke(cli, input=" ")
        assert result.exception
        assert result.exit_code == 1
        assert result.output == "Enter your text:  \nError: You input a empty string.\n"
