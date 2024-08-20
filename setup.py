from setuptools import setup, find_packages

with open("README.rst", "r") as _file:
    readme = _file.read()

setup(
    name="sabi",
    version='0.0.1',
    packages=find_packages(),
    description="A simple module to translate plain English to Nigerian (Naija) pidgin English.",
    long_description=readme,
    long_description_content_type='text/rst',
    author="Kolawole Andrew",
    author_email="andrewolakola@gmail.com",
    url="https://github.com/techkaduna/sabi",
    py_modules=["sabi",],
    license="MIT",
    classifiers=[
        "Environment :: Console",
        "Intended Audience :: Education",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.6",
        "Topic :: Education",
    ],
    entry_points={"console_scripts": ["sabi=sabi:main"],},
)
