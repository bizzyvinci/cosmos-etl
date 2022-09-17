import os

from setuptools import find_packages, setup


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


long_description = read('README.md') if os.path.isfile("README.md") else ""

setup(
    name='cosmos-etl',
    version='0.0.2',
    author='Bisola Olasehinde',
    author_email='horlasehinde@gmail.com',
    description='Tools for exporting Cosmos blockchain data to CSV or JSON',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/bizzyvinci/cosmos-etl',
    packages=find_packages(),
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9'
    ],
    keywords=['cosmos', 'tendermint'],
    python_requires='>=3.7.2,<4',
    install_requires=[
        'blockchain-etl-common',
        'web3>=5.29,<6'
    ],
    entry_points={
        'console_scripts': [
            'cosmosetl=cosmosetl.cli:cli',
        ],
    },
    project_urls={
        'Bug Reports': 'https://github.com/bizzyvinci/cosmos-etl/issues',
        'Source': 'https://github.com/bizzyvinci/cosmos-etl',
    },
)
