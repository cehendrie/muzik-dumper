from setuptools import setup

def readme():
    with open('README.rst') as f:
        return f.read()

setup(name='muzik-dumpster',
      version='0.0.1',
      description='a simple process for sorting text based music libraries',
      url='http://github.com/cehendrie/muzik-dumpster',
      author='Charles Hendrie',
      author_email='cehendrie@outlook.com',
      license='MIT',
      packages=['muzikdumpster'],
      install_requires=[
          'markdown',
      ],
      include_package_data=True,
      zip_safe=False)
