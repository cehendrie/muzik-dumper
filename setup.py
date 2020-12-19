from setuptools import setup, find_packages


setup(
    name='muzik-dumpster',
    version='1.0.1',
    description='A simple process for sorting text based music collections',
    url='http://github.com/cehendrie/muzik-dumpster',
    author='Charles Hendrie',
    author_email='cehendrie@outlook.com',
    license='MIT',
    packages=find_packages(),
    entry_points={'console_scripts': ['mdump=muzikdumpster.muzikdumpster:main']})
