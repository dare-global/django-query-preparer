import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="django-query-preparer",
    version="1.0.2",
    author="Dare",
    author_email="https://dare.global/",
    description="A package to prepare queries in postgres before execution",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/dare-global/django-query-preparer",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Framework :: Django",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
