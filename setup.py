from __future__ import annotations

from pathlib import Path

from setuptools import setup

here = Path(__file__).resolve().parent

with (here / "requirements.txt").open() as f:
    requirements = f.read().split("\n")


def long_description():
    """Load README.rst."""
    with Path("README.rst").open(encoding="utf-8") as f:
        return f.read()


dev_requiremnets = ["pytest", "hypothesis"]
setup(
    name="yamlloader",
    version="1.3.2",
    author='Jonas Eschle "Mayou36", Johannes Lade "SebastianJL"',
    author_email="jonas.eschle@phynix.science, johannes.lade@phynix.science",
    maintainer='Jonas Eschle "Mayou36"',
    maintainer_email="jonas.eschle@phynix.science",
    url="https://github.com/Phynix/yamlloader",
    download_url="https://github.com/Phynix/yamlloader",
    license="MIT License",
    description="Ordered YAML loader and dumper for PyYAML.",
    long_description=long_description(),
    keywords=["YAML", "loader", "dumper", "ordered", "OrderedDict", "pyyaml"],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Intended Audience :: System Administrators",
        "Intended Audience :: Science/Research",
        "Natural Language :: English",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Topic :: Software Development :: Libraries",
        "Topic :: Utilities",
    ],
    packages=["yamlloader", "yamlloader.ordereddict"],
    python_requires=">=3.7",
    install_requires=requirements,
    tests_require=dev_requiremnets,
    extras_require={"dev": dev_requiremnets},
    zip_safe=False,
)
