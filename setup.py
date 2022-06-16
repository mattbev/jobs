"""
PyPI build file
"""
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

docs_extras = ["sphinx", "docutils", "sphinx-rtd-theme"]

setuptools.setup(
    name="jobs",
    version="0.1.0",
    author="Matt Beveridge",
    description="Drop-in multiprocessing.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    keywords=[],
    install_requires=[],
    extras_require={"docs": docs_extras},
    license="MIT",
    packages=setuptools.find_packages(),
    include_package_data=True,
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
