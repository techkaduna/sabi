import pytest
from sabi import translate, translator, Translator


@translator(ajasa=False)
def no_ajasa(text: str) -> str:
    return text


@translator(ajasa=True)
def with_ajasa(text: str) -> str:
    return text


def translate_file(in_file, out_file, ajasa: bool = False):
    with Translator(in_file, out_file, ajasa) as translated:
        return translated


args = [
    ("How are you", "How yu dey "),
    ("I saw a lady", "I saw a babe"),
    ("My father is here", "My papa dey here"),
]


@pytest.mark.parametrize(
    "english, translation",
    args,
)
def test_translate(english, translation):
    assert translate(english) == translation


@pytest.mark.parametrize(
    "english, translation",
    args,
)
def test_translator(english, translation):
    assert no_ajasa(english) == translation


@pytest.mark.parametrize(
    "english, translation",
    args,
)
def test_translator_with_ajasa(english, translation):
    result = with_ajasa(english)
    assert type(result) is type(translation)


@pytest.mark.parametrize(
    "in_file, out_file",
    [
        ("requirements.txt", "test-1.txt"),
        ("setup.py", "test-2.py"),
    ],
)
def test_file_translation(in_file, out_file, ajasa: bool = False):
    assert translate_file(in_file, out_file, ajasa) is True
