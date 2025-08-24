from setuptools import setup, find_packages

setup(
    name="salvatore-framework",
    version="1.0.0",
    packages=find_packages(),
    install_requires=["requests", "networkx"],
    author="YourName",
    author_email="your.email@example.com",
    description="Salvatore Juggernaut Apex - Truth-seeking AI framework with multi-agent orchestration",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/YourNameAI/salvatore-framework",
    license="OpenMDW"
)