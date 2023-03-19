from setuptools import setup, find_packages

with open("README.md", "r") as readme_file:
    readme =  readme_file.read()

requirements = []


setup(
    name="pygiglab",
    version="0.0.1",
    author="Albert F. Osei",
    author_email="codingctrl@gmail.com",
    description="A package to convert your Jupyter Notebook",
    long_description="readme",
    long_description_content_type="text/markdown",
    url="https://github.com/makewecode/pygiglab",
    packages=find_packages(),
    install_requires=requirements,
    classifiers=[ 
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: MIT License",
    ],
)