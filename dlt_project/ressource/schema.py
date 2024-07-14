from typing import List, Optional, Union

import dlt
from pydantic import BaseModel


@dlt.resource(name="user", columns={"tags": {"data_type": "complex"}})
def get_users(): ...


# the `table_schema` method gets table schema generated by a resource
print(get_users().compute_table_schema())


"""
Version 2 : Data contract

Choses à noter :

- Les champs avec un Optional type sont marqués comme nullable
- Les champs avec un Uniontype sont convertis vers le premier None type (et non) répertorié dans l'union. Par exemple, status: Union[int, str]les résultats sont dans une bigint colonne.
- list et dict les champs de modèle pydantic imbriqués utiliseront le complex
  type qui signifie qu'ils seront stockés en tant qu'objet JSON dans la base de données au lieu de créer des tables enfants.
"""


class Address(BaseModel):
    street: str
    city: str
    postal_code: str


class User(BaseModel):
    id: int
    name: str
    tags: List[str]
    email: Optional[str]
    address: Address
    status: Union[int, str]


@dlt.resource(name="user", columns=User)
def get_users(): ...