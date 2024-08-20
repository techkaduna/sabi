#!/usr/bin/env python
"""
Sabi - Tok like sabi boi.
            
Translate plain English (oyinbo) words or texts into Naija
pidgin English, as e dey hot.

Copyright (c) 2024 Kolawole A. Olalekan.

Permission is hereby granted, free of charge, to any person obtaining a copy of
this software and associated documentation files (the "Software"), to deal in
the Software without restriction, including without limitation the rights to
use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of
the Software, and to permit persons to whom the Software is furnished to do so,
subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS
FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR
COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER
IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""


import random
from typing import Any, List

WORDS = {
    ("hey", "hello", "hi"): random.choice(["haffa na", "haffa", "sup"]),
    ("man", ): "guy",
    ("pride", ): "steeze",
    ("child",): "pikin",
    ("lady", ): "babe", 
    ("ladies",): "babes",
    ("eat", ): "chop",
    ("father",): "papa",
    ("mother", ): "mama",
    ("fathers", ): "papa dem",
    ("mothers", ): "mama dem",
    ("problem", ): random.choice(["wahala", "yawa"]),
    ("happened", "happening" ): random.choice(["sup", "shele"]),
    ("what", ): "wetin",
    ("someone", ): "pesin",
    ("gun", ): "kala",
    ("police", ): "popo",
    ("soldier", "soldiers", ): "sojo", 
    ("walk", "move", "walking", ): "waka",
    ("go", ): "comot",
    ("is", ): "dey",
    ("am", ): "be",
    ("said", ): "tok",
    ("told", ): "tell",
    ("him", "she", "it"): "am",
    ("beautiful", "handsome"): "fine",
    ("don't", ): "no",
    ("will", ): "go",
    ("they", ): "dem",
    ("fast", ): "sharp",
    ("beat", ): "colet",
    ("did", ): "shey",
    ("asked", "ask", ):  "say make",
    ("money", ): "moni",
    ("is", "doing", "was", ): "dey",
    ("strong", "hefty"): "gidigba",
    ("know", ): "sabi",
    ("now", ): "na",
    ("leave", "go", ): "comot",


}

PHRASES = {
    ("are you", ): "yu dey", 
    # ("who are you",): "who yu be", 
    ("want to", ): "won",
    ("wants to",): "won",
    ("is he",): "he dey",
    ("is she", ): "she dey",
    ("did it", "do it", ): "do am",
    ("said that", ): "tok say",
    ("beautiful lady", ): "fine babe",
    ("handsome man", ): "fine bobo", 
    ("is that", ): "shey na",
    ("shut up", "stop", ): "hol-am",
    ("wanted to", ): "bin won",
    ("hear me", ): "hear me so",
    ("it is", "is a ", "this is", ): "na",
    ("how is", "how did", ): "how",
    ("what is", "what did", ): "wetin",
    ("where is", "where did", ): "where",
    ("who is", "who did", ): "who",
    ("what a"): "see",
    
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

def search_for_word(word: str, source: (dict | None)) -> (Any | str):
    """Search for a word in a dictonary.
    
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
        word: List[str]
    """

    _phrase = phrase.split(" ")
    word_length = len(_phrase)
    for i in range(word_length - 1):
        if i == word_length - 1:
            pass
        else:    # then he remembers "explicit is better than implicit"
            first_word = _phrase[i]
            second_word = _phrase[i + 1]
            _phrase_ = f"{first_word} {second_word}"
            _pidgin = search_for_word(_phrase_, PHRASES)
            if _pidgin != _phrase_:
                _phrase[i], _phrase[i+1] = _pidgin, ""

    return _phrase        

def translate(english: str, ajasa: bool) -> str:      # ajasa means popular slang
    """ Translate plain English word or text into (Ng) pidgin English."""
    words = search_for_phrase(english)
    translation = [search_for_word(word, WORDS) for word in words]
    if ajasa is True:
        _ajasa = f"{str(random.choice(RANDOM_PHRASE))}!"
    else:
        _ajasa = ""
    
    return f"{_ajasa}{' '.join(translation)}"


def main(argv=None):
    """
    Handle all arguments passed by the user.

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
        usage="sabi --oyinbo 'plain oyinbo text'",
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
        "--ajasa",
        action="store_true",
        help="Adds a popular pidgin slang to translated text.",
    )

    args = parser.parse_args(argv)

    
    if args.oyinbo is not None:
        _text = Text(str(translate(str(args.oyinbo), args.ajasa)))
        console.print(_text)
    elif args.file is not None:
        filename = f"pidgin-{random.randint(1, 10)}"
        with console.status("READING FILE......", spinner="clock", speed=1):
            with open(f"{args.file}", "r") as _from:
                _text = _from.read()
                translation = translate(_text, args.ajasa)
        with console.status("WRITING FILE....", spinner="clock", speed=1):
            with open(f"{filename}", "w") as to:
                to.write(translation)
        console.rule(f"FILE GENERATED AS {filename}.")
    else:
        _text = Text(
            "Sup! Error processing English."
            " Be like water don pas garri - add garri "
            "make we for make confam eba.\n"
            "GET help with [sabi -h]."
              )
        err_console.print(_text)
        sys.exit(1)
