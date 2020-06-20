from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(name='processio',
      version='1.2.0',
      description='Takes the hassle away from multiprocessing of functions and parsing of big dataset`s.',
      url='https://github.com/AdaptedAS/processio',
      author='Odd Jøren Røland',
      long_description=long_description,
      long_description_content_type="text/markdown",
      author_email='odd@adapted.no',
      license='MIT',
      packages=['processio'],
      platforms=['any'],
      keywords=['multiprocessing', 'code speed'],
      include_package_data=True,
      classifiers=[
          'License :: OSI Approved :: MIT License',
          'Natural Language :: English',
          'Intended Audience :: Developers',
          'Topic :: Software Development :: Libraries',
          'Topic :: Software Development :: Libraries :: Python Modules',
          'Development Status :: 5 - Production/Stable',
          'Programming Language :: Python',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.4',
          'Programming Language :: Python :: 3.5',
          'Programming Language :: Python :: 3.6',
          'Programming Language :: Python :: 3.7',
      ],
      zip_safe=False
      )
