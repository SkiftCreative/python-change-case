import os
from setuptools import setup

readmefile = os.path.join(os.path.dirname(__file__), 'README.rst')
with open(readmefile) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='change_case',
    version='0.5.1',
    packages=['change_case'],
    include_package_data=True,
    license='MIT License',
    description='change between one type of casing and another',
    long_description=README,
    url='https://github.com/SkiftCreative/python-change-case',
    author='Shawn McElroy',
    author_email='shawn@skift.io',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Utilities'
    ],
)
