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

1. Démarrer les services :
   ```bash
   docker-compose up
   ```
2. Accéder à l’interface Airflow :
   - http://localhost:8080
   - Identifiants : admin / admin

## Pipeline ETL
- **Extract** : Lecture du fichier CSV
- **Transform** : Conversion du prix en euros
- **Load** : Chargement dans PostgreSQL (table `sales`)

## PostgreSQL
- Host : postgres
- User : airflow
- Password : airflow
- DB : airflow

## Pour aller plus loin
- Ajouter des transformations
- Connecter à un dashboard (ex: Metabase)
- Orchestrer plusieurs pipelines
