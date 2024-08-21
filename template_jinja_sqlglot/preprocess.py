from enum import StrEnum
from pathlib import Path

import sqlglot
from jinja2 import Environment, FileSystemLoader
from pydantic import BaseModel, Field


class ParammeterTableToRequest(BaseModel):
    list_of_attributs: list[str]
    name_dataset: str = Field(min_length=3, pattern=r"^dwh_.*")
    name_table: str = Field(min_length=3, pattern=r"^fact_.*")
    incremental: bool = True
    date_filter: str


class MapperSql(StrEnum):
    SQL_TEMPLATE_DELTA = "sql_template_delta"


FOLDER_JINJA_TEMPLATE = Path(__file__).resolve().parent / "sql_template"

JINJA_SQL_MAPPER = {MapperSql.SQL_TEMPLATE_DELTA: f"{MapperSql.SQL_TEMPLATE_DELTA}.sql"}


def get_jinja_template(source: str):
    environment = Environment(loader=FileSystemLoader(FOLDER_JINJA_TEMPLATE))

    template_name = JINJA_SQL_MAPPER[source]
    template = environment.get_template(template_name)

    return template


def get_sql_postgres_operator(source: str) -> str:
    template = get_jinja_template(source)
    list_of_attributs = [f"attribut_{index}" for index in range(10)]

    parameters_sql = ParammeterTableToRequest(
        list_of_attributs=list_of_attributs,
        name_table="fact_table",
        name_dataset="dwh_dataset",
        date_filter="2O24/08/19",
    )

    sql_postgres = template.render(parameters_sql=parameters_sql)

    return sql_postgres


if __name__ == "__main__":
    sql_request = get_sql_postgres_operator(MapperSql.SQL_TEMPLATE_DELTA)

    sqlglot.transpile(sql_request)
