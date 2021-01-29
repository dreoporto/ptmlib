import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="ptmlib",
    version="0.1.0",
    author="Andre Oporto",
    author_email="opor7ae@pendragonai.com",
    description="Pendragon Tiny ML Library",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/dreoporto/ptmlib",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)