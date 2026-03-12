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
- **transform_task** : Calcule le prix en euros (`price_eur`), ajoute une **catégorie de prix** et un **horodatage de traitement**.
- **load_task** : Charge les données finales dans PostgreSQL.

## Visualisation (BI) avec Metabase

Metabase est inclus pour créer des dashboards. Suivez ces étapes pour une première visualisation :

1. **Connexion initiale** : Accédez à [http://localhost:3001](http://localhost:3001).
2. **Configuration de la base de données** :
   - Type : **PostgreSQL**
   - Host : `postgres`
   - Port : `5432`
   - Database/User/Pass : `airflow`
3. **Créer un graphique (Exemple : Ventes par Catégorie)** :
   - Cliquez sur **+ Nouveau** > **Question**.
   - Sélectionnez votre base `airflow` et la table `sales`.
   - Cliquez sur **Visualisation** et choisissez **Graphique en barres**.
   - Regroupez par `price_category` et observez la répartition de vos produits !

## Architecture
- **Airflow** : Orchestration et validation.
- **PostgreSQL** : Stockage des données (port 5433 pour accès externe).
- **Metabase** : Visualisation BI (port 3001).
- **Données enrichies** : Colonnes `price_category` (Bas/Milieu/Haut de gamme) et `processed_at`.

## PostgreSQL
- Host : `localhost` (externe) ou `postgres` (interne Docker)
- Port : `5433` (externe) ou `5432` (interne)
- User/Pass : `airflow` / `airflow`
- DB : `airflow`
- Table cible : `sales`

## Pour aller plus loin
- Ajouter des transformations
- Connecter à un dashboard (ex: Metabase)
- Orchestrer plusieurs pipelines
