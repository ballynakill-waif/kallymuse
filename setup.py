
from setuptools import setup, find_packages

setup(
        name='kallymuse',
	package_dir = {"": "src"},
        description='a python module designed for the purpose of making snippets out of music21',
        version='0.0.1',
	packages=['kallymuse'],
	data_files = [('/usr/local/share/man/man1', ['docs/man/kallymuse.1/'])],
	long_description='this python module for use with music21. it aims at making anki flashcards from the notes in a given piece of music. To do this it gives the user asses to python classes that can convert strings into music notation.',
	install_requires=[
		'ipykernel',
        'music21',
	]
        )   

