import sqlglot
from sqlglot import transpile

output = transpile("SELECT EPOCH_MS(1618088028295)", read="duckdb", write="hive")[0]

# transpile("SELECT EPOCH_MS(1618088028295)", read="duckdb", write="hive")[0]


sql = """
WITH baz AS (SELECT a, c FROM foo WHERE a = 1)
SELECT f.a, b.b, baz.c, CAST("b"."a" AS REAL) d
FROM foo f JOIN bar b ON f.a = b.a LEFT JOIN baz ON f.a = baz.a
"""

# print(transpile(output, write="spark", identify=True, pretty=True)[0])


sql = """
SELECT foo FROM (SELECT baz FROM t
"""

# sqlglot.transpile(sql)

where = sqlglot.condition("x=1").and_("y=1")
sql = sqlglot.select("*").from_("y").where(where).sql()


# print(sqlglot.transpile(sql, pretty=True)[0])


sql = """
SELECT A OR (B OR (C AND D))
FROM x
WHERE Z = date '2021-01-01' + INTERVAL '1' month OR 1 = 0
"""

schema = {"x": {"A": "INT", "B": "INT", "C": "INT", "D": "INT", "Z": "STRING"}}

print(
    sqlglot.optimizer.optimize(sqlglot.parse_one(sql), schema=schema).sql(pretty=True)
)
