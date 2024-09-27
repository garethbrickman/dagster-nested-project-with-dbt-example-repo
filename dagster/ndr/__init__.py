from dagster import (
    Definitions,
    load_assets_from_package_module,
)
from dagster_dbt import DbtCliResource
from .assets import ndr_dbt_assets
from .project import ndr_project

defs = Definitions(
    assets=[ndr_dbt_assets],
    resources={
        "dbt": DbtCliResource(project_dir=ndr_project),
    },
)
