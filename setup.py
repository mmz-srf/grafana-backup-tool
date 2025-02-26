from grafana_backup.constants import (PKG_NAME, PKG_VERSION)
from setuptools import setup, find_packages

# Global variables
name = PKG_NAME
version = PKG_VERSION
requires = [
    'requests',
    'docopt',
    'boto3',
    'azure-storage-blob',
    'google-cloud-storage'
]

setup(
    name=name,
    version=version,
    description='A Python-based application to backup Grafana settings using the Grafana API',
    long_description_content_type='text/markdown',
    long_description=open('README.md', 'r').read(),
    author="author",
    author_email="noreply@srf.ch",
    url="https://github.com/mmz-srf/grafana-backup-tool",
    entry_points={
        'console_scripts': [
            'grafana-backup = grafana_backup.cli:main'
        ]
    },
    packages=find_packages(),
    install_requires=requires,
    package_data={'': ['conf/*']},
)
