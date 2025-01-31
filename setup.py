from setuptools import setup, find_packages
from pathlib import Path

# Read the long description from README.md
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text(encoding="utf-8")

setup(
    name="alien_language",
    version="0.2.2",
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "alien-translate=alien_language.translator:main",
        ],
    },
    description="A Python to Alien Language translator. Translate Python code into a fun, alien-like syntax!",
    long_description=long_description,
    long_description_content_type="text/markdown",  # Specify the format of the long description
    author="Ishan Oshada",
    author_email="ishan.kodithuwakku.offical@gmail.com",
    url="https://github.com/ishanoshada/alien-language",
    project_urls={
        "Source Code": "https://github.com/ishanoshada/alien-language",
        "Bug Tracker": "https://github.com/ishanoshada/alien-language/issues",
        "Documentation": "https://github.com/ishanoshada/alien-language#readme",
    },
    keywords=[
        "alien language",
        "python translator",
        "fun programming",
        "code translation",
        "python to alien",
        "programming language",
    ],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Intended Audience :: Education",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Software Development :: Interpreters",
        "Topic :: Education",
        "Topic :: Games/Entertainment",
    ],
    license="MIT",  # Explicitly specify the license
   
)