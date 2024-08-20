**Sabi** - Translate plain English to Naija pidgin.
===================================================

A simple module to translate plain English to Nigerian (Naija) pidgin English.

I had been planning on writing a Python package (academic reasons)
and had been researching, then I encountered *arrr.py* while doing some Python study - 
so I decided, why not?  And the result ? na you *SABI*.

There is the pidginUNMT project, which is more than capable for the job but then - 
there's numpy and there's pandas.

*sabi - tok like sabi pesin*

Installation
------------

   - Using dear pip

   ::

      $ pip install sabi

Usage Example
--------------

   - A simple translation

   ::

      from sabi import translate

      text = "Hello World"
      pidgin = translate(text)
      print(pidgin)

   - Translating from a file into another file

   ::

       from sabi import Translator

       with Translator('english.txt', 'pidgin.txt', ajasa=False) as translated:
            if translated is True:
                print('Translated!')

   - Or using a decorator

   ::

       from sabi import translator

       @translator(ajasa=True)
       def word(text: str) -> str:
           return text

        word("How are you")

*Trivial right ? Uuugh! I know.*

Command-line Usage
-------------------

   - On installing *sabi*, you'd be able to run *sabi* from your shell as follows:

   ::

      $ sabi --oyinbo 'how are you'
      
   - The command about would translate the text *how are you* into its pidgin equivalent,
   ::

      $ sabi --long-tok english.txt
   - while the command above translates a whole file called english located in the current working directory.
   
   - To print the non-sabi boy help text offerable
   ::

      $ sabi -h
      $ sabi --help
   - and for the *sabi boy help text*
   ::

      $ sabi


Contibution
------------

This project is still quite buggy and is under active development.
Contributing to this would be such a great honor because I am really not expecting it,
infact there are no codes of conduct (working on it..).
The source code for this project is hosted on GitHub `<https://github.com/techkaduna/sabi>`_. 
Every one is free to contribute, I'd reall appreciate it.

Authors:
--------------------
   - Kolawole Olalekan   `andrewolakola@gmail.com`
   

