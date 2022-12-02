# setup.py - settings file for twine. This info is used to export this package to pypi.org
# https://pypi.org/manage/projects/

from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = '0.0.10'
DESCRIPTION = 'Generate a word cloud png file based on text or a URL contents.'
LONG_DESCRIPTION = 'A package that creates png image files based on text or the contents of a URL.'

setup(
    name="keywordcloud",
    #packages = ['YOURPACKAGENAME'],   # Chose the same as "name"
    version=VERSION,
    license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
    author="Jeffery Mandrake",
    author_email="<info@goinfosystems.com>",
    url = "https://amzto.com/",   # Link to your github or to your website
    download_url = "https://github.com/jmandrake/keywordcloud",    # Github Repo page
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages(),
    install_requires=['python-whois', 'py-thesaurus', 'random-proxies'],
    keywords=['python', 'keyword cloud', 'word cloud', 'wordcloud', 'keywordcloud', 'keywords', 'png', 'keyword'],
    classifiers=[
        'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Build Tools",
        "License :: OSI Approved :: MIT License",   # Again, pick a license
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)