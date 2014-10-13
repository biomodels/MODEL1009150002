from setuptools import setup, find_packages

setup(name='MODEL1009150002',
      version=20140916,
      description='MODEL1009150002 from BioModels',
      url='http://www.ebi.ac.uk/biomodels-main/MODEL1009150002',
      maintainer='Stanley Gu',
      maintainer_url='stanleygu@gmail.com',
      packages=find_packages(),
      package_data={'': ['*.xml', 'README.md']},
    )