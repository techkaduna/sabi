"""
Sabi - Tok like sabi pesin.
Translate plain English (oyinbo) words or texts into Naija
pidgin English, as e dey hot.

Copyright (c) 2024 Kolawole A. Olalekan.

"""

import random
from typing import List
from functools import wraps

WORDS = {
    ("hey", "hello", "hi"): random.choice(
        [
            "haffa na",
            "haffa",
            "sup",
        ]
    ),
    ("man",): "guy",
    ("pride",): "steeze",
    ("child",): "pikin",
    ("lady",): "babe",
    ("ladies",): "babes",
    (
        "eat",
        "eaten",
        "ate",
    ): random.choice(
        [
            "chop",
            "chow",
        ]
    ),
    ("father",): "papa",
    ("mother",): "mama",
    ("fathers",): "papa dem",
    ("mothers",): "mama dem",
    ("problem",): random.choice(
        [
            "wahala",
            "yawa",
        ]
    ),
    ("happened", "happening"): random.choice(
        [
            "sup",
            "shele",
        ]
    ),
    ("what",): "wetin",
    ("someone",): "pesin",
    ("gun",): "kala",
    ("police",): "popo",
    (
        "soldier",
        "soldiers",
    ): "sojo",
    (
        "walk",
        "move",
        "walking",
    ): "waka",
    ("go",): "comot",
    # ("is",): "dey",
    ("am","are", "is", ): "be",
    ("said",): "tok",
    ("told",): "tell",
    ("him", "her", "it"): "am",
    ("beautiful", "handsome"): "fine",
    ("don't",): "no",
    ("will",): "go",
    ("they",): "dem",
    ("fast",): "sharp",
    ("beat",): "colet",
    ("did",): "shey",
    (
        "asked",
        "ask",
    ): "say make",
    ("money",): "moni",
    (
        "is",
        "doing",
        "was",
    ): "dey",
    ("strong", "hefty"): "gidigba",
    ("know",): "sabi",
    ("now",): "na",
    (
        "leave",
        "go",
    ): "comot",
    ("say",): "tok",
    ("carried", ): "carry",

}

PHRASES = {
    ("are you",): "yu dey",
    # ("who are you",): "who yu be",
    ("want to",): "won",
    ("wants to",): "won",
    ("is he",): "he dey",
    ("is she",): "she dey",
    (
        "did it",
        "do it",
    ): "do am",
    ("said that",): "tok say",
    ("beautiful lady",): "fine babe",
    ("handsome man",): "fine bobo",
    ("is that",): "shey na",
    (
        "shut up",
        "stop",
    ): "hol-am",
    ("wanted to",): "bin won",
    ("hear me",): "hear me so",
    (
        "it is",
        "is a ",
        "this is",
    ): "na",
    (
        "how is",
        "how did",
    ): "how",
    (
        "what is",
        "what did",
    ): "wetin",
    (
        "where is",
        "where did",
    ): "where",
    (
        "who is",
        "who did",
    ): "who",
    ("what a"): "see",
    ("let us",): "make we",
    ("have you",): "you don",
    ("carry a", "carried a", ): "carry",
    ("say that", "said that", ): "tok am",
}

RANDOM_PHRASE = [
    "shu",
    "see me see trobu",
    "for dis area so",
    "na whining be that",
    "you dey whine",
    "omo",
    "wahala",
    "sharp",
    "you and who",
    "for this place",
]


def search_for_word(word: str, source: dict | None) -> str:
    """Search for a word in a dictonary where the keys are tuples.

    Parameters
    --------------
    word: str
        Word to search for in the dictionary.
    source: dict
        Source from which word is to be searched.

    return:
        word: str
    """

    if source is None or type(source) is not dict:
        raise TypeError(f"source expected type dict but got type {type(source)}")

    # will handle this later
    # punctuations = [".", ",", ":", ";", "?", "!"]
    # is_endswith_symbol = [word.endswith(i) for i in punctuations]

    word_tup = [i for i in list(source.keys())]
    for tup in word_tup:
        if word.lower() in tup:
            _translation = source[tup]
            return _translation
    else:
        return word


def search_for_phrase(phrase: str) -> List[str]:
    """Search for a phrase from the dictionary PHRASES.

    Parameters
    --------------
    phrase: str
        Phrase to search for in the dictionary.

    return:
        _phrase: List[str]
    """

    _phrase = phrase.split(" ")
    word_length = len(_phrase)
    for i in range(word_length - 1):
        if i == word_length - 1:
            pass
        else:  # then he remembers "explicit is better than implicit"
            first_word = _phrase[i]
            second_word = _phrase[i + 1]
            _phrase_ = f"{first_word} {second_word}"
            _pidgin = search_for_word(_phrase_, PHRASES)
            if _pidgin != _phrase_:
                _phrase[i], _phrase[i + 1] = _pidgin, ""

    return _phrase


class Translator:
    """Context manager for translating words in a file to pidgin saved in another file.

    Parameters
    -------------
    in_file
        Path to the file to be translated.
    out_file
        Path to the output file where translated words are to be saved.
        Will create a file named `pidgin-n` in the working directory if
        the argument is not specified - where n is random integer between 1 - 10.
    ajasa: bool
        Randomly start sentence(s) with popular pidgin slangs if True.
    ::
        `with Translator('english.txt', 'pidgin.txt', ajasa=False) as translated:`
            `if translated is True:`
                `print('Translated!')`

    """

    def __init__(
        self,
        in_file,
        out_file: str = f"pidgin-{random.randint(1,10)}",
        ajasa: bool = False,
    ) -> None:
        self._filepath = in_file
        self._filename = out_file
        self.is_ajasa = ajasa
        self.filedesc = None
        self._to_file = None

    def __enter__(self) -> bool:
        try:
            self.filedesc = open(self._filepath, "r")
        except FileNotFoundError:
                return {"result": False, 
                    "why": f"File {self._filepath} not found.", }
        
        self._to_file = open(self._filename, "w+")
        sentence_list = self.filedesc.readlines()
        translated_words = [translate(i, ajasa=self.is_ajasa) for i in sentence_list]
        self._to_file.writelines(translated_words)

        return True

    def __exit__(self, exc_type, exc_val, exc_obj):
        if self.filedesc:
            self.filedesc.close()
        if self._to_file:
            self._to_file.close()


def translator(ajasa: bool = False):
    """Decorator version of sabi.translate function."""

    def translator_base(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                _text = func(*args, **kwargs)
            except Exception as err:
                print(err)
                return None
            _pidgin = translate(_text, ajasa)
            return _pidgin

        return wrapper

    return translator_base


def translate(english: str, ajasa: bool = False) -> str:  # ajasa means popular slang
    """Translate plain English word or text into (Ng) pidgin English.

    Parameters
    -------------
    english: str
        English word to be translated to Naija pidgin.
    ajasa: bool
        Randomly start sentence(s) with popular pidgin slangs if True.
    """

    words = search_for_phrase(english)
    translation = [search_for_word(word, WORDS) for word in words]
    if ajasa is True:
        _ajasa = f"{str(random.choice(RANDOM_PHRASE))}!"
    else:
        _ajasa = ""

    return f"{_ajasa}{' '.join(translation)}"


def main(argv=None):
    """
    Entry point for command-line use.

    These arguments will be updated in the nearest future
    as neccessary.
    """

    import argparse
    import sys
    from rich.console import Console
    from rich.text import Text

    console = Console(color_system="standard", style="bold blue")
    err_console = Console(color_system="standard", style="bold red")

    parser = argparse.ArgumentParser(
        prog="sabi",
        description="""\
            Sabi - Tok like sabi boi.

            Translate plain English words or texts into Naija
            pidgin English, as e dey hot.
        """,
        usage="sabi -h for usage help.",
        epilog="sabi - Tok like sabi boi.",
    )

    if not argv:
        argv = sys.argv[1:]

    parser.add_argument(
        "--oyinbo",
        help="Translate plain English words text to Naija pidgin.",
    )
    parser.add_argument(
        "--long-tok",
        dest="file",
        help="Translate the words in a text file to Naija pidgin.",
    )
    parser.add_argument(
        "--out-file",
        dest="output",
        default=None,
        help="Output file after --long-tok.",
    )
    parser.add_argument(
        "--ajasa",
        action="store_true",
        help="Adds a popular pidgin slang to translated text.",
    )
    parser.add_argument(
        "-v", "--version", action="store_true", help="Print program version and leave."
    )

    args = parser.parse_args(argv)

    err_text = Text(
        "Sup! Error processing English."
        " Be like water don pas garri - add garri "
        "make we for make confam eba.\n"
        "GET help with: sabi -h."
    )

    if args.oyinbo is not None:
        _text = Text(str(translate(str(args.oyinbo), args.ajasa)))
        console.print(_text)
    elif args.file is not None:
        filename = (
            f"pidgin-{random.randint(1, 10)}"
            if args.output is None
            else str(args.output)
        )

        with Translator(args.file, filename, args.ajasa) as is_translated:
            if is_translated is True:
                console.rule(f"FILE GENERATED AS {filename}.")
            else:
                err_console.bell()
                console.rule("ERROR")
                err_console.print(f"{err_text}\n{is_translated.get('why')}")
                sys.exit(1)
    elif args.version is True:
        console.print("sabi v0.1.3")
    else:
        err_console.print(err_text)
        sys.exit(1)
