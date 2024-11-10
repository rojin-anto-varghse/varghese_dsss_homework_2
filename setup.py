from setuptools import setup, find_packages
import os

def read_requirements():
    """Safely reads requirements.txt and handles encoding issues."""
    with open("requirements.txt", encoding="utf-8") as f:
        return [line.strip() for line in f if line.strip()]

setup(
    name="varghese_dss_homework_2",
    version="0.1.0",
    author="Rojin Anto Varghese",
    author_email="rojin.anto.varghese@fau.de",
    description="Maths quiz application",
    long_description=open("README.md", encoding="utf-8").read() if os.path.exists("README.md") else "",
    long_description_content_type="text/markdown",
    url="https://github.com/rojin-anto-varghse/varghese_dsss_homework_2.git",
    packages=find_packages(),
    install_requires=read_requirements(),  # Calls the function to read requirements safely
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
