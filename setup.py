from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in requestaccessmanager/__init__.py
from requestaccessmanager import __version__ as version

setup(
	name="requestaccessmanager",
	version=version,
	description="USed to help system access requests",
	author="ANC",
	author_email="rajm@albertanewsprint.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
