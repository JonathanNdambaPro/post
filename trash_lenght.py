text = """Monter une data stack, c’est aussi cher que 100 Urus Mansory ou aussi complexe qu’une fusée SpaceX 😬

On me parle souvent de deux options :
💸 On utilise que des services managed, puis 3 mois plus tard tu comprends pourquoi AWS est l’asset le plus rentable d’Amazon.
😣 On monte tout dans un K8S et c’est parti pour des maux de tête si t’es pas ops.

Pourtant, on peut facilement créer une data stack gratuite, robuste et facile à mettre en place 👇

🐍 Python : Bon, je ne suis pas vraiment obligé de t’expliquer pourquoi, pas vrai ?
🗃️ SQL : (Bon, je ne suis pas vraiment obligé de t’expliquer pourquoi, pas vrai ?)²
🏗️ Dlthub (Ingestion) : Le problème d'Airbyte/Fivetran c’est que soit la config c'est du K8S ou le service-managed, Dlt fait la même chose mais seulement avec du Python.
💾 PostgreSQL (OLTP) : Pour avoir l’état courant de la structure.
🌐 DuckDB (OLAP) : Pour avoir l’état des données historiques et permettre aux analystes de s’amuser sans casser la prod.
🛠️ Dbt : Pour intégrer les principes de software dans le SQL.
</> FastAPI : Pour exposer ces données facilement.
📊 Streamlit/Plotly : Pour faire de jolis graphiques sans utiliser ce truc qu’ils appellent Power BI.
🔄 Airflow/Dagster : Pour orchestrer le tout.
📦 Docker : Bon, c’est le plus dur de la liste mais plus de "ça marche pas sur ma machine".

Avec ça, on a une bonne stack facile à mettre en place pour tester son MVP avant de passer aux choses sérieuses. Sinon, toi tu fais comment ?
Dis-moi tout en commentaire.
"""

lenght_text = len(text)

print(lenght_text)
