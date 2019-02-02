from setuptools import setup

setup(
  name='icelander_generator',
  packages=['icelander_generator'], # this must be the same as the name above
  version='0.1',
  description='A utility to generate random Icelanders',
  author='7oi',
  author_email='7oi@7oi.is',
  license='MIT',
  url='https://github.com/7oi/IcelanderGenerator',
  install_requires=['lxml', 'requests', 'kennitala'],
  keywords=['tests', 'generator'],
  classifiers = [],
)
