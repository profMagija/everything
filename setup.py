import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="everything",
    version="0.0.1",
    author="Nikola Bebić",
    author_email="nikola.bebic99@gmail.com",
    description="A module containing everything",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/profMagija/everything",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)