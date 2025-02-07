Projet d'Analyse des Salaires en Data Science

📄 Description du Projet

Ce projet vise à explorer les tendances salariales dans le domaine de la Data Science en utilisant des données issues de Kaggle. L'application interactive est développée avec Streamlit et permet de visualiser divers aspects des salaires, en fonction du niveau d'expérience, du type d'emploi, du poste et de la localisation de l'entreprise.

📊 Données utilisées

Le jeu de données utilisé provient de Kaggle et contient des informations sur les salaires en Data Science, notamment :

job_title : Titre du poste

salary_in_usd : Salaire en USD

experience_level : Niveau d'expérience

employment_type : Type d'emploi

company_location : Localisation de l'entreprise

company_size : Taille de l'entreprise

work_year : Année de travail

📂 Contenu du Projet

Le projet contient les fichiers suivants :

application.py : Script Python principal contenant le code pour charger et analyser les données avec pandas, matplotlib, seaborn, plotly et streamlit.

Projet_SAE.ipynb : Notebook Jupyter contenant des analyses exploratoires.

🛠 Installation et Pré-requis

Avant d'exécuter le projet, assurez-vous d'installer les dépendances nécessaires. Vous pouvez créer un environnement virtuel et installer les packages en exécutant la commande suivante :

conda create -n projet python pandas numpy matplotlib seaborn streamlit plotly -y
conda activate projet

Ou avec pip :

pip install pandas numpy matplotlib seaborn streamlit plotly

🚀 Lancement de l'Application

Une fois les dépendances installées, lancez l'application Streamlit avec la commande suivante :

streamlit run application.py

L'application propose les fonctionnalités suivantes :

📊 Exploration des données : Aperçu des données et statistiques générales.

📈 Visualisation des salaires : Analyse des tendances salariales par rôle et niveau d'expérience.

🔗 Corrélations entre variables : Heatmap des corrélations.

📉 Évolution des salaires : Analyse interactive des variations de salaires.

🏢 Impact de l'entreprise et de l'expérience : Comparaison des salaires en fonction de la taille d'entreprise et de l'expérience.

🎛 Filtres dynamiques : Possibilité de filtrer les données en fonction du salaire et d'autres critères.


