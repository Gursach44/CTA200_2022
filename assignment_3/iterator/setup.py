from setuptools import setup, find_packages
import pathlib

here = pathlib.Path(__file__).parent.resolve()
long_description = (here / "README.md").read_text(encoding="utf-8")

setup(
    name="iterator",
    version="1",
    description="The iterative function used in assignment 3.",
    author="Gurman Sachdeva",
    author_email="gurman.sachdeva@mail.utoronto.ca",
    packages=find_packages(),
)
