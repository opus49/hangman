from setuptools import setup, find_packages

with open("README.rst") as fh_in:
    README = fh_in.read()

setup(
    name="hangman",
    version="0.1",
    description="Source code for Hangman tutorial",
    long_description=README,
    long_description_content_type="text/x-rst",
    url="https://github.com/opus49/hangman",
    author="Mike Puskar",
    author_email="puskar49@gmail.com",
    license="MIT",
    classifiers=[
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Operating System :: POSIX",
        "Programming Language :: Python :: 3.6"
    ],
    packages=find_packages(),
    python_requires=">=3.6",
    include_package_data=True,
    entry_points={
        "console_scripts": [
            "hangman = hangman.cli.main:main",
        ]
    },
    test_suite="nose.collector"
)
