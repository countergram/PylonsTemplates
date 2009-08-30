from setuptools import setup, find_packages
import sys, os

version = '0.1'

setup(name='PylonsTemplates',
      version=version,
      description="Extra paster templates for Pylons including repoze.what implementation",
      long_description="""\
      PylonsTemplates gives you additional paster templates for Pylons applications.
      (Right now, there is one.)
      
      Based on the default Pylons paster template, the pylons_repoze_what template
      implements a working authorization system based on repoze.what and
      repoze.what-quickstart. (Authentication by repoze.who is automatically set
      up as well.) The template generates:
      
      * User, Group and Permission models for SQLALchemy
      * A login (& logout) controller
      * A minimal template for the login form.
      * A package dependency on repoze.what-pylons, which includes decorators
        you can use on controllers and actions.
      * Commented out sample code in websetup.py that creates a user, group,
        and permission.
""",
      classifiers=[
          "Development Status :: 3 - Alpha",
          "Environment :: Console",
          "Framework :: Pylons",
          "Framework :: Paste",
          "Intended Audience :: Developers",
          "License :: OSI Approved :: MIT License",
          "Natural Language :: English",
          "Operating System :: OS Independent",
          "Programming Language :: Python :: 2",
          "Topic :: Internet :: WWW/HTTP",
          "Topic :: Utilities",
      ],
      keywords='',
      author='Jason Stitt',
      author_email='jason@countergram.com',
      url='http://countergram.com/software/PylonsTemplates',
      license='MIT',
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
