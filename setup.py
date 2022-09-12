import setuptools

with open("README.md", "r", encoding='UTF-8') as fh:
    long_description = fh.read()

setuptools.setup(
    name="bd09convertor",
    version="0.0.3",
    author="Piao Yang",
    author_email="495384481@qq.com",
    description="BD09 coordinates conversion tool for Python.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/46319943/BD09Convertor",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.5',

    install_requires=[],
)
