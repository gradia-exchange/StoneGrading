from setuptools import find_packages, setup

setup(
    name="stonegrading",
    packages=find_packages(include=["stonegrading"]),
    version="0.1.0",
    long_description_content_type="text/markdown",
    long_description="Will add it soon",
    description="Diamond Stone Grading Package. It ships stone fields for reports and actual stones",
    author="Gradia Limited",
    license="MIT",
    install_requires=[],
    setup_requires=["pytest-runner"],
    tests_requires=["pytest==6.2.2"],
    test_suite="tests",
)
