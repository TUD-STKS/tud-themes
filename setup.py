import setuptools
import os

with open("README.md", "r") as fh:
    long_description = fh.read()

WORKING_PATH = os.getcwd()

setuptools.setup(
    name="tudthemes",
    version="0.0.4",
    author="Arne-Lukas Fietkau",
    author_email="arne-lukas.fietkau@tu-dresden.de",
    description="TU Dresden Corporate Design for Jupyter Notebooks",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/TUD-STKS/tud-themes",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Development Status :: 2 - Pre-Alpha",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Intended Audience :: Science/Research",
    ],
    keywords='tudthemes',
    project_urls={
        'Tracker': 'https://github.com/TUD-STKS/tud-themes/issues',
    },
    package_dir={'tudthemes': 'tudthemes'},
    package_data= {
        'tudthemes': [
                    os.path.join(WORKING_PATH,'tudthemes/themes/bright/custom/*'),
                    os.path.join(WORKING_PATH,'tudthemes/themes/dark/custom/*'),
                    os.path.join(WORKING_PATH,'tudthemes/themes/default/custom/*')
                    ]
    },
    include_package_data=True,
    python_requires='>=3.7',
)