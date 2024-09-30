from setuptools import find_packages, setup

setup(
    name="ndr",
    packages=find_packages(),
    package_data={
        "ndr": [
            "dbt-project/**/*",
        ],
    },
    python_requires='>=3.8',
    install_requires=[
        "dagster",
        "dagster-cloud",
        "dagster-dbt",
        "boto3",
        "pandas",
        "matplotlib",
        "dbt-duckdb<1.9",
        "protobuf>=5.26.1"
    ],
    extras_require={"dev": ["dagster-webserver", "pytest"]},
)
