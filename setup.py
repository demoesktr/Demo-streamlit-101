"""
Setup configuration for Mortgage Calculator package.
"""

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = [line.strip() for line in fh if line.strip() and not line.startswith("#")]

setup(
    name="mortgage-calculator",
    version="1.0.0",
    author="Mortgage Calculator Team",
    description="A production-ready mortgage calculator application",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/mortgage-calculator",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: End Users/Desktop",
        "Intended Audience :: Financial and Insurance Industry",
        "Topic :: Office/Business :: Financial",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
    install_requires=requirements[:3],  # Only core dependencies
    extras_require={
        "dev": requirements[3:],  # Development dependencies
    },
    entry_points={
        "console_scripts": [
            "mortgage-calculator=main:main",
        ],
    },
)
