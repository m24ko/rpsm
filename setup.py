try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup
config = {
    'description': 'modern jukebox',
    'author': 'Marko Suker, Vladimir Vulin',
    'url': 'https://github.com/m24ko/rpsm',
    'download_url': 'https://github.com/m24ko/rpsm',
    'author_email': 'email@gmail.com',
    'version': '0.1',
    'install_requires': [''],
    'packages': ['main'],
    'scripts': [],
    'name': 'raspberry pi sound machine'
    }

setup(**config)
