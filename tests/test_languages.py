import pytest
from src.languages import LanguageMark


class TestFromStr:
    def test_normal_ru(self) -> None:
        assert LanguageMark.from_str("ru") == LanguageMark.RU
        assert LanguageMark.from_str("rus") == LanguageMark.RU
        assert LanguageMark.from_str("deu") != LanguageMark.RU
        assert LanguageMark.from_str("eng") != LanguageMark.RU

    def test_normal_en(self) -> None:
        assert LanguageMark.from_str("en") == LanguageMark.EN
        assert LanguageMark.from_str("eng") == LanguageMark.EN
        assert LanguageMark.from_str("jpn") != LanguageMark.EN
        assert LanguageMark.from_str("rus") != LanguageMark.EN

    def test_normal_de(self) -> None:
        assert LanguageMark.from_str("de") == LanguageMark.DE
        assert LanguageMark.from_str("deu") == LanguageMark.DE
        assert LanguageMark.from_str("der") == LanguageMark.DE
        assert LanguageMark.from_str("ja") != LanguageMark.DE
        assert LanguageMark.from_str("en") != LanguageMark.DE

    def test_normal_ja(self) -> None:
        assert LanguageMark.from_str("ja") == LanguageMark.JA
        assert LanguageMark.from_str("jpn") == LanguageMark.JA
        assert LanguageMark.from_str("ru") != LanguageMark.JA
        assert LanguageMark.from_str("de") != LanguageMark.JA

    def test_normal_fr(self) -> None:
        assert LanguageMark.from_str("fr") == LanguageMark.FR
        assert LanguageMark.from_str("fre") == LanguageMark.FR
        assert LanguageMark.from_str("fra") == LanguageMark.FR
        assert LanguageMark.from_str("ja") != LanguageMark.FR
        assert LanguageMark.from_str("en") != LanguageMark.FR

    def test_normal_it(self) -> None:
        assert LanguageMark.from_str("it") == LanguageMark.IT
        assert LanguageMark.from_str("ita") == LanguageMark.IT
        assert LanguageMark.from_str("ru") != LanguageMark.IT
        assert LanguageMark.from_str("ja") != LanguageMark.IT

    def test_wrong_1(self) -> None:
        with pytest.raises(NotImplementedError):
            LanguageMark.from_str("sh")

    def test_wrong_2(self) -> None:
        with pytest.raises(NotImplementedError):
            LanguageMark.from_str("ch")

    def test_wrong_3(self) -> None:
        with pytest.raises(NotImplementedError):
            LanguageMark.from_str("bl")

    def test_wrong_4(self) -> None:
        with pytest.raises(NotImplementedError):
            LanguageMark.from_str("pl")
