import pathlib
import re
import setuptools

HERE = pathlib.Path(__file__).parent

README = (HERE / "README.md").read_text(encoding = "utf8")

with open(HERE / "disnakeBetter/__init__.py") as file:
    version = re.search(
        r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]', file.read(), re.MULTILINE).group(1)

setuptools.setup(
    name = "SpendScheme",
    author = "HåperStudio",
    url = "https://github.com/HaperStudio/disnakeBetter",
    version = version,
    packages = setuptools.find_packages(),
    license = "MIT",
    description = "disnakeBetter is an extension for working in conjunction with the disnake standard library.",
    long_description = README,
    long_description_content_type = "text/markdown",
    include_package_data = True,
    python_requires = ">=3.8",
    zip_safe = False,
    test_suite = "tests",
    project_urls = {
        "Documentation (GitHub)": "https://github.com/HaperStudio/disnakeBetter/blob/main/README.md",
        "Source (GitHub)": "https://github.com/HaperStudio/disnakeBetter",
    },
    classifiers = [
        "License :: OSI Approved :: MPL-2.0 license",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: Implementation :: CPython",
        "Topic :: Communications :: Chat",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet",
        "Topic :: Software Development :: Libraries",
        "Topic :: Software Development :: Libraries :: Application Frameworks",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Utilities",
        "Typing :: Typed",
    ]
)