import setuptools
import os

with open("README.md", "r") as fh:
    long_description = fh.read()

def search_files(subfile,list_a):
    if os.path.isdir(subfile):
        for new_file in os.listdir(subfile):
            search_files(os.path.join(subfile, new_file), list_a)
    else:
        if not (("common.css" in subfile) or ("migrated" in subfile)):
            list_a.append(subfile)

WORKING_PATH = os.getcwd()
list_files=[]
search_files(os.path.join(WORKING_PATH,"tudthemes","themes"), list_files)



setuptools.setup(
    name="tudthemes",
    version="0.0.6",
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
    package_data = {"tudthemes": list_files},
    include_package_data=True,
    python_requires='>=3.7',
)