WITH data_prepros AS (
    SELECT
        {% for attribut in parameters_sql.list_of_attributs %}
            {{ attribut }}{% if not loop.last %},{% endif %}
        {% endfor %}
    FROM {{ parameters_sql.name_dataset }}.{{ parameters_sql.name_table }}
)

SELECT
    *
FROM data_prepros
{% if parameters_sql.incremental%}
WHERE date_delta >= to_timestamp('{{ date_filter }}', 'dd/mm/yyyy hh24:mi:ss'
{% endif %}
