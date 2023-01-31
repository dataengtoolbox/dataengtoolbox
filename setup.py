import os
from setuptools import setup

with open(os.path.join("src", "dataengtoolbox", "VERSION"), "r") as version_file:
    version = version_file.read().strip()

with open("README.md", "r") as readme:
    readme_content = readme.read()

with open("requirements.txt", "r") as requirements:
    requirement_list = requirements.read().strip().splitlines()


setup(
    name="dataengtoolbox",
    version=version,
    description="Data Engineering Toolbox",
    long_description=readme_content,
    long_description_content_type="text/markdown",
    author="ITESO MAF - Data Engineering Course",
    package_dir={
        "": "src"
    },
    install_requires=requirement_list,
    python_requires=">=3.8.10",
    scripts=[
        "bin/dataengtoolbox",
    ]
)