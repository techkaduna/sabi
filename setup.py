from setuptools import setup, find_packages

def read_file(filename):
    with open(filename, "r") as _file:
        output = _file.read()
    return output

setup(
    name="sabi",
    version="0.1.2",
    packages=find_packages(),
    description="A simple module to translate plain English to Nigerian (Naija) pidgin English.",
    long_description=read_file("README.rst")+"\n\n"+read_file("CHANGES.rst"),
    long_description_content_type="text/x-rst",
    author="Kolawole Andrew",
    author_email="andrewolakola@gmail.com",
    url="https://github.com/techkaduna/sabi",
    py_modules=[
        "sabi",
    ],
    requires=[
        "rich",
    ],
    license="MIT",
    classifiers=[
        "Environment :: Console",
        "Intended Audience :: Education",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.6",
        "Topic :: Education",
    ],
    entry_points={
        "console_scripts": ["sabi=sabi:main"],
    },
)
