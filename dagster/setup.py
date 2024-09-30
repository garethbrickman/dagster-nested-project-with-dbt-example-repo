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
        "pandas",
        "matplotlib",
        "dbt-duckdb<1.9",
        "testresources",  # Added to satisfy launchpadlib
        "importlib-metadata>=6.0,<7",  # Downgraded to satisfy dbt-semantic-interfaces
        "protobuf>=5.26.1,<6.0dev",  # Upgraded to satisfy grpcio-health-checking
    ],
    extras_require={"dev": ["dagster-webserver", "pytest"]},
)
