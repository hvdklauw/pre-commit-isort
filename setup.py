from setuptools import find_packages
from setuptools import setup


setup(
    name='pre_commit_isosrt',
    description='pre commit isort support',
    url='https://github.com/hvdklauw/pre-commit-isort',
    version='0.1.0',

    author='Harro van der Klauw',
    author_email='hvdklauw@gmail.com',

    platforms='linux',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
    ],

    packages=find_packages('.', exclude=('tests*', 'testing*')),
    install_requires=[
        # quickfix to prevent pep8 conflicts
        'isort',
    ],
    entry_points={
        'console_scripts': [
        ],
    },
)
