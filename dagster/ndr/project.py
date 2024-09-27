from pathlib import Path

from dagster_dbt import DbtProject

ndr_project = DbtProject(
    project_dir=Path(__file__).joinpath("..", "..", "..", "dbt").resolve()
)
ndr_project.prepare_if_dev()