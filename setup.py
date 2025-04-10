from setuptools import setup
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

AUTHOR_NAME = 'Dean Aura'
SRC_REPO = 'src'
LIST_OF_REQUIREMENTS = ['streamlit']

setup(
    name = SRC_REPO,
    author = AUTHOR_NAME,
    description = 'A simple python package for movie recommendation',
    long_description = long_description,
    long_description_content_type = 'text/markdown',
    package = [SRC_REPO],
    pyhton_requires = '>=3.7',
    install_requires = LIST_OF_REQUIREMENTS,
)