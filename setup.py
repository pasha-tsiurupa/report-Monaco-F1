import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="monaco_Q1_report",
    version="0.1.0",
    author="Pavlo Tsiurupa",
    author_email="pavlotsiurupa@gmail.com",
    description="Report of Monaco Q1 stage",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://git.foxminded.com.ua/pavlo_tsiurupa/task-6-report-monaco-f1",

    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "report"},
    packages=setuptools.find_packages(where="report"),
    python_requires=">=3.10",
)
