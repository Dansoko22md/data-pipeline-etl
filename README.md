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

1. Démarrer les services (Webserver, Scheduler, Postgres) :
   ```bash
   docker-compose up -d
   ```
2. Accéder à l’interface Airflow :
   - http://localhost:8081
   - Identifiants : `admin` / `admin`

## Pipeline ETL (Multi-tâches)
Le pipeline est désormais divisé en trois étapes distinctes pour une meilleure robustesse :
- **extract_task** : Lit les données brutes depuis `data/raw_data.csv`.
- **transform_task** : Calcule le prix en euros (`price_eur`) en appliquant un taux de conversion.
- **load_task** : Charge les données transformées dans la table `sales` de PostgreSQL.

## Architecture
- **Airflow Webserver** : Interface utilisateur pour monitorer les DAGs.
- **Airflow Scheduler** : Orchestrateur qui planifie et lance les tâches.
- **PostgreSQL** : Base de données de métadonnées Airflow et destination du chargement ETL.
- **Docker Compose** : Gestionnaire de conteneurs pour tout l'écosystème.

## PostgreSQL
- Host : postgres
- User : airflow
- Password : airflow
- DB : airflow

## Pour aller plus loin
- Ajouter des transformations
- Connecter à un dashboard (ex: Metabase)
- Orchestrer plusieurs pipelines
