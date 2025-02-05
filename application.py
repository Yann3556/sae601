"""
📝 **Instructions** :
- Installez toutes les bibliothèques nécessaires en fonction des imports présents dans le code, utilisez la commande suivante :conda create -n projet python pandas numpy ..........
- Complétez les sections en écrivant votre code où c’est indiqué.
- Ajoutez des commentaires clairs pour expliquer vos choix.
- Utilisez des emoji avec windows + ;
- Interprétez les résultats de vos visualisations (quelques phrases).
"""

### 1. Importation des librairies et chargement des données
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
import plotly.express as px

# Chargement des données
df = pd.read_csv("C:/Projet-20250205/ds_salaries.csv")


### 2. Exploration visuelle des données
#votre code 
st.title("📊 Visualisation des Salaires en Data Science")
st.markdown("Explorez les tendances des salaires à travers différentes visualisations interactives.")


if st.checkbox("Afficher un aperçu des données"):
    st.write(df.head())


#Statistique générales avec describe pandas 
#votre code 
st.subheader("📌 Statistiques générales")
st.write(df.describe())


### 3. Distribution des salaires en France par rôle et niveau d'expérience, uilisant px.box et st.plotly_chart
#votre code 
st.subheader("📈 Distribution des salaires en France")
fig = px.box(df, x='job_title', y='salary_in_usd', color='experience_level')
st.plotly_chart(fig)


### 4. Analyse des tendances de salaires :
#### Salaire moyen par catégorie : en choisisant une des : ['experience_level', 'employment_type', 'job_title', 'company_location'], utilisant px.bar et st.selectbox 

st.subheader("📈 Analyse des tendances de salaires")

categories = ['experience_level', 'employment_type', 'job_title', 'company_location']
categ = st.selectbox("Choisissez une catégorie :", categories)
salaire_moy = df.groupby(categ)['salary_in_usd'].mean().reset_index()
fig = px.bar(salaire_moy, x=categ, y='salary_in_usd', title=f'Salaire moyen par {categ}', labels={'salary_in_usd': 'Salaire moyen'})
st.plotly_chart(fig)

### 5. Corrélation entre variables
# Sélectionner uniquement les colonnes numériques pour la corrélation
#votre code 
st.subheader("🔗 Corrélations entre variables numériques")
numeric_df = df.select_dtypes(include=[np.number])

# Calcul de la matrice de corrélation
#votre code
correlation_matrix = numeric_df.corr()

# Affichage du heatmap avec sns.heatmap
#votre code 
fig, ax = plt.subplots(figsize=(10, 6))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', ax=ax)
st.pyplot(fig)

### 6. Analyse interactive des variations de salaire
# Une évolution des salaires pour les 10 postes les plus courants
# count of job titles pour selectionner les postes
# calcule du salaire moyen par an
#utilisez px.line
#votre code
st.subheader("🔗 Analyse interactive des variations de salaire")

postes = df['job_title'].value_counts().nlargest(10).index
filtre = df[df['job_title'].isin(postes)]
salaire_moy2 = filtre.groupby(['work_year', 'job_title'])['salary_in_usd'].mean().reset_index()
fig = px.line(salaire_moy2, x='work_year', y='salary_in_usd', color='job_title', 
              title='Évolution des salaires pour les 10 postes les plus courants',
              labels={'salary_in_usd': 'Salaire moyen', 'work_year': 'Année', 'job_title': 'Poste'})
st.plotly_chart(fig)


### 7. Salaire médian par expérience et taille d'entreprise
# utilisez median(), px.bar
#votre code 
st.subheader("🔗 Salaire médian par expérience et taille d'entreprise")

salaire_med = df.groupby(['company_size', 'experience_level'])['salary_in_usd'].median().reset_index()
fig = px.bar(
    salaire_med, 
    x='experience_level', 
    y='salary_in_usd', 
    color='company_size',  
    barmode='group',  
    title="Salaire médian par expérience et taille d'entreprise", 
    labels={
        'salary_in_usd': 'Salaire médian (USD)', 
        'experience_level': 'Niveau d expérience', 
        'company_size': 'Taille de l entreprise'
    }
)
st.plotly_chart(fig)

### 8. Ajout de filtres dynamiques
#Filtrer les données par salaire utilisant st.slider pour selectionner les plages 
#votre code 
st.subheader("🔗 Ajout de filtres dynamiques")

min_sal = int(df["salary_in_usd"].min())
max_sal = int(df["salary_in_usd"].max())

filtre1 = st.slider(
    "Sélectionnez une plage de salaire",
    min_value=min_sal,
    max_value=max_sal,
    value=(min_sal, max_sal), 
)
filtre2 = df[(df["salary_in_usd"] >= filtre1[0]) & (df["salary_in_usd"] <= filtre1[1])]
st.write(filtre2)

### 9.  Impact du télétravail sur le salaire selon le pays




### 10. Filtrage avancé des données avec deux st.multiselect, un qui indique "Sélectionnez le niveau d'expérience" et l'autre "Sélectionnez la taille d'entreprise"
#votre code 

