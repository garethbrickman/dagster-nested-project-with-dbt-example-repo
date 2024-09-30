from setuptools import find_packages, setup

setup(
    name="ndr",
    packages=find_packages(),
    package_data={
        "ndr": [
            "dbt-project/**/*",
        ],
    },
    install_requires=[
        "dagster",
        "dagster-cloud",
        "dagster-dbt",
        "dbt-duckdb<1.9",
        "grpcio<1.66.0",
        "grpcio-health-checking<1.66.0",
        "protobuf>=4.0,<5.0",
        "importlib-metadata<7,>=6.0",
    ],
    extras_require={"dev": ["dagster-webserver"]},
)
