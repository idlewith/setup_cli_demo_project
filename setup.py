from setuptools import setup, find_packages


setup(
    name="cli_demo",
    version="0.0.1",
    description="cli demo description",
    packages=find_packages(),
    entry_points={"console_scripts": ["clio=cli_demo.main:main"]},
    setup_requires=["wheel"],
)
