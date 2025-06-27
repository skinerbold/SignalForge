from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = [line.strip() for line in fh if line.strip() and not line.startswith("#")]

setup(
    name="signalforge",
    version="1.0.0",
    author="Skiner Bold",
    author_email="contato@skinerbold.com",
    description="SignalForge - Ferramenta moderna para análise de sinais e sistemas lineares",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/skiner-bold/signalforge",
    project_urls={
        "Bug Tracker": "https://github.com/skiner-bold/signalforge/issues",
        "Documentation": "https://github.com/skiner-bold/signalforge/blob/main/docs/TUTORIAL.md",
    },
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Education",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Scientific/Engineering",
        "Topic :: Education",
    ],
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    python_requires=">=3.8",
    install_requires=requirements,
    extras_require={
        "dev": [
            "pytest>=6.0",
            "pytest-cov>=2.0",
            "black>=21.0",
            "flake8>=3.8",
            "mypy>=0.812",
        ],
    },
    entry_points={
        "console_scripts": [
            "signalforge=src.app:main",
        ],
    },
)
