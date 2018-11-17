#!/usr/bin/env python
# Thanks to: https://github.com/kennethreitz/setup.py
import os
import re
import sys

from codecs import open

from setuptools import setup
from setuptools.command.test import test as TestCommand


class PyTest(TestCommand):
    user_options = [('pytest-args=', 'a', "arguments to pass into py.test")]

    def initialize_options(self):
        TestCommand.initialize_options(self)
        try:
            from multiprocessing import cpu_count
            self.pytest_args = ['-n', str(cpu_count()), '--boxed']
        except (ImportError, NotImplementedError):
            self.pytest_args = ['-n', '1', '--boxed']

    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        import pytest

        errno = pytest.main(self.pytest_args)
        sys.exit(errno)


# 'setup.py publish' shortcut.
#if sys.argv[-1] == 'publish':
#    os.system('python setup.py sdist bdist_wheel')
#    os.system('twine upload dist/*')
#    sys.exit()

packages = ['bitlab_assessment']

requires = []
test_requirements = [
    'pytest-cov',
    'pytest>=3.8.0'
]

with open('README.md', 'r', 'utf-8') as f:
    readme = f.read()

setup(
    name='bitlab_assessment',
    version='1.0.0',
    description='Fax, scan and print the internet!',
    long_description=readme,
    long_description_content_type='text/markdown',
    author='John Faucett',
    author_email='john.faucett@protonmail.com',
    url='https://github.com/johnfaucett/assessment-37109100009.git',
    packages=packages,
    package_data={'': ['LICENSE']},
    package_dir={'bitlab_assessment': 'bitlab_assessment'},
    include_package_data=True,
    python_requires=">=2.6",
    install_requires=requires,
    license='MIT',
    zip_safe=False,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy'
    ],
    cmdclass={'test': PyTest},
    tests_require=test_requirements,
    extras_require={},
)