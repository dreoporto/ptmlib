import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="dre-lib-dreoporto",
    version="0.1.0",
    author="Andre Oporto",
    author_email="andreoporto@gmail.com",
    description="My common utility code for Python Machine Learning",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/dreoporto/dre-lib",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)