"""
Utility to print versions of all major dependencies
Used for debugging, reproducibility, and deployment checks
"""

import importlib
from importlib.metadata import version, PackageNotFoundError


PACKAGES = [
    "langchain",
    "langchain-core",
    "langchain-community",
    "langchain-groq",
    "langchain-text-splitters",
    "streamlit",
    "python-dotenv",
    "setuptools" , 
    "pillow" ,
]


def get_package_version(pkg_name: str) -> str:
    try:
        return version(pkg_name)
    except PackageNotFoundError:
        return "NOT INSTALLED"


def print_versions() -> dict:
    """
    Returns a dictionary of package versions
    """
    versions = {}
    for pkg in PACKAGES:
        versions[pkg] = get_package_version(pkg)
    return versions


if __name__ == "__main__":
    versions = print_versions()
    print("\n📦 Installed Package Versions:\n")
    for k, v in versions.items():
        print(f"{k:30}=={v}")
