from setuptools import setup, find_packages

setup(
    name="documind",
    version="0.1",
    packages=find_packages(include=["documind", "documind.*", "utils", "utils.*"]),
    install_requires=[],
)