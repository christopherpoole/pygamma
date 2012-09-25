from setuptools import setup

setup(
    name = "pygamma",
    version = "0.1",
    author = "Christopher Poole",
    author_email = "mail@christopherpoole.net",
    description = "Perform a gamma evaluation comparing 2 n-dim radiotherapy dose distributions",
    keywords = "radiotherapy, gamma evaluation, distance to agreement",
    url = "http://github.com/christopherpoole/pygamma",
    packages = ["dta"],    
    long_description=open("README.md").read(),
)
