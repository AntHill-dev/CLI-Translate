import pytest

from src.misc.exceptions import EmptySentenceArgumentError
from src.misc.utils import get_only_letters_from


class TestGetOnlyLettersFrom:
    def test_eq_one(self) -> None:
        result = get_only_letters_from("some word")
        assert result == {char for char in "some word" if char.isalpha()}

    def test_eq_two(self) -> None:
        result = get_only_letters_from("abc           ")
        assert result == {"a", "b", "c"}

    def test_eq_three(self) -> None:
        result = get_only_letters_from("a;sldjfoeiaalsdf")
        assert result == {"a", "s", "l", "d", "j", "f", "o", "e", "i"}

    def test_eq_four(self) -> None:
        result = get_only_letters_from("234234O")
        assert result == {"O"}

    def test_eq_five(self) -> None:
        result = get_only_letters_from("fjpq3894jP(*FHa(*H")
        assert result == {"f", "j", "p", "q", "P", "F", "H", "a"}

    def test_neq_one(self) -> None:
        result = get_only_letters_from("abslfjsdfp")
        assert result != {"a", "b", "c"}

    def test_neq_two(self) -> None:
        result = get_only_letters_from("abcpsdf")
        assert result != {"a", "b", "c", "p", "s", "d"}

    def test_neq_three(self) -> None:
        result = get_only_letters_from("(*&H#@(D")
        assert result != {"a"}

    def test_neq_four(self) -> None:
        result = get_only_letters_from("234234A")
        assert result != {"O"}

    def test_neq_five(self) -> None:
        result = get_only_letters_from("))A")
        assert result != {"f", "j", "p", "q", "P", "F", "H", "a"}

    def test_exception_1(self) -> None:
        with pytest.raises(EmptySentenceArgumentError):
            result = get_only_letters_from("1234")

    def test_exception_2(self) -> None:
        with pytest.raises(EmptySentenceArgumentError):
            result = get_only_letters_from("(*@#(*(89432432")

    def test_exception_3(self) -> None:
        with pytest.raises(EmptySentenceArgumentError):
            result = get_only_letters_from(")~!*)#!)#)*02302340*)#@)*$20384")

    def test_exception_4(self) -> None:
        with pytest.raises(EmptySentenceArgumentError):
            result = get_only_letters_from("     64    *#@")
