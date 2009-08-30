from setuptools import setup, find_packages
import sys, os

version = '0.1'

setup(name='PylonsTemplates',
      version=version,
      description="Extra paster templates for Pylons including repoze and AuthKit implementations",
      long_description="""\
""",
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='',
      author='Jason Stitt',
      author_email='jason@countergram.com',
      url='http://countergram.com/software/',
      license='',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          "Pylons>=0.9.7",
          "PasteScript>=1.6.3",
      ],
      entry_points="""
      [paste.paster_create_template]
      pylons_repoze_what = PylonsTemplates:PylonsRepozeWhat
      """,
      )
