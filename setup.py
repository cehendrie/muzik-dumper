import shutil
from distutils import sysconfig
from setuptools import setup

# PYTHONPATH hack!!!
# Needed for this script to execute the application successfully.
# 'muzikdumpster' package needs to be added to the path (sys.path).
# Using the .pth convention to add the package sys.path.
# The setup(data_files) parameter should be doing the copy but isn't working.
# See: https://stackoverflow.com/questions/2145779/setup-py-installing-just-a-pth-file
site_packages_path = sysconfig.get_python_lib()
shutil.copy('muzikdumpster.pth', site_packages_path)


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
      zip_safe=False,
      scripts=['bin/muzik-dumpster'],
      data_files=[(site_packages_path, ['muzikdumpster.pth'])])
