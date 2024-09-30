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
    ],
    extras_require={"dev": ["dagster-webserver"]},
)
