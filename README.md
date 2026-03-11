# Data Pipeline ETL Project

## Objectif
Construire un pipeline ETL (Extract, Transform, Load) avec Airflow, PostgreSQL, Python et Docker.

## Structure du projet
```
data-pipeline-etl/
├── dags/
│   └── etl_pipeline.py
├── scripts/
│   ├── extract.py
│   ├── transform.py
│   └── load.py
├── data/
│   └── raw_data.csv
├── docker-compose.yml
└── README.md
```

## Exemple de données

```
product,price,country
Laptop,1200,USA
Phone,800,France
```

## Lancer le projet

1. Démarrer les services (Airflow, Postgres, Metabase) :
   ```bash
   docker-compose up -d
   ```
2. Accéder aux interfaces :
   - **Airflow** : http://localhost:8081 (admin / admin)
   - **Metabase** : http://localhost:3001 (Configuration initiale requise)

## Pipeline ETL (Multi-tâches & Robuste)
Le pipeline est divisé en quatre étapes :
- **cleanup_old_data** : Supprime les données incohérentes de la base Postgres.
- **extract_task** : Lit `data/raw_data.csv` avec validation (vérifie si vide ou prix négatifs).
- **transform_task** : Calcule le prix en euros (`price_eur`).
- **load_task** : Charge les données finales dans PostgreSQL.

## Visualisation (BI)
Metabase est inclus pour créer des dashboards. Pour connecter Metabase à vos données :
1. Choisissez **PostgreSQL** comme base de données.
2. Host : `postgres` (si Metabase est dans le même réseau Docker) ou `localhost` (si accès externe).
3. Port : `5432` (interne) ou `5433` (externe).
4. Database/User/Pass : `airflow`.

## Architecture
- **Airflow** : Orchestration et validation.
- **PostgreSQL** : Stockage des données (port 5433 pour accès externe).
- **Metabase** : Visualisation BI (port 3000).

## PostgreSQL
- Host : postgres
- User : airflow
- Password : airflow
- DB : airflow

## Pour aller plus loin
- Ajouter des transformations
- Connecter à un dashboard (ex: Metabase)
- Orchestrer plusieurs pipelines
