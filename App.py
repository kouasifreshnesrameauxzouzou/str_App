
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Chargement des données (exemple avec des données aléatoires)
data = pd.DataFrame({
    'x': range(10),
    'y': [3, 1, 4, 1, 5, 9, 2, 6, 5, 3],
    'z': [5, 8, 2, 7, 1, 6, 3, 9, 4, 7]
})

# Première visualisation (graphique à barres)
st.bar_chart(data['y'])

# Deuxième visualisation (graphique linéaire)
st.line_chart(data[['x', 'z']])

# Troisième visualisation (heatmap avec Seaborn)
fig, ax = plt.subplots()
sns.heatmap(data[['y', 'z']].corr(), annot=True, cmap='coolwarm', ax=ax)
st.pyplot(fig)

