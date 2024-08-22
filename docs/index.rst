**Sabi** - Translate plain English to Naija pidgin
===================================================

A simple module to translate plain English to Nigerian (Naija) pidgin English.

I had been planning on writing a Python package (academic reasons) and had been researching.
Then I encountered *arrr.py* while doing some Python study - so I decided, why not? And the result? na you *SABI*.

There is the pidginUNMT project, which is more than capable for the job, but then - there's numpy and there's pandas.

*sabi - tok like sabi pesin*

Installation
------------

To install using pip, run:

   .. code-block:: shell

      $ pip install sabi

Usage Example
--------------

Here are some examples of how to use the `sabi` package:

- **A simple translation**

   .. code-block:: python

      from sabi import translate

      text = "Hello World"
      pidgin = translate(text)
      print(pidgin)

- **Translating from a file into another file**

   .. code-block:: python

      from sabi import Translator

      with Translator('english.txt', 'pidgin.txt', ajasa=False) as translated:
          if translated is True:
              print('Translated!')

- **Using a decorator**

   .. code-block:: python

      from sabi import translator

      @translator(ajasa=True)
      def word(text: str) -> str:
          return text

      word("How are you")

*Trivial right? Uuugh! I know.*

Command-line Usage
-------------------

After installing `sabi`, you can run it from your shell as follows:

- **Translate text**

   .. code-block:: shell

      $ sabi --oyinbo 'how are you'

   This command will translate the text *how are you* into its pidgin equivalent.

- **Translate a file**

   .. code-block:: shell

      $ sabi --long-tok english.txt --out-file pidgin.txt

   This command translates the entire file `english.txt` located in the current working directory.

- **Help text**

   To print the help text, use:

   .. code-block:: shell

      $ sabi -h
      $ sabi --help

   And for a more `sabi boi` help text, use:

   .. code-block:: shell

      $ sabi

Contribution
------------

This project is still quite buggy and is under active development. Contributing to this project would be greatly appreciated. Currently, there are no codes of conduct (working on it).

The source code for this project is hosted on GitHub: `<https://github.com/techkaduna/sabi>`_. Everyone is free to contribute, and I'd really appreciate it.

Authors
--------

- Kolawole Olalekan (`andrewolakola@gmail.com`)
