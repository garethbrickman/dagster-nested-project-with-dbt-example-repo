from pathlib import Path

from dagster_dbt import DbtProject

ndr_project = DbtProject(
    project_dir=Path(__file__).joinpath("..", "..", "..", "dbt").resolve(),
    packaged_project_dir=Path(__file__).joinpath("..", "..", "dbt-project").resolve(),
)
ndr_project.prepare_if_dev()