import streamlit as st
import pandas as pd

# Update the path to your actual data file
COLOME_CSV_PATH = '/Users/oriolcolomefont/Documents/AMPLAB/Module 1/features.csv'
audio_analysis_colome = pd.read_csv(COLOME_CSV_PATH)

# UI for Tempo Search
st.sidebar.header('Tempo Search')
min_tempo, max_tempo = st.sidebar.slider('Select tempo range:', min_value=0, max_value=300, value=[90, 130])

# UI for Danceability Search
st.sidebar.header('Danceability Search')
min_danceability, max_danceability = st.sidebar.slider('Select danceability range:', min_value=0, max_value=3, value=[1, 2])

# UI for Key Estimation Profile
st.sidebar.header('Key Estimation Profile')
selected_profile = st.sidebar.radio('Select Key Estimation Profile:', ['temperley', 'krumhansl', 'edma'])

# UI for Key Selection
st.sidebar.header('Key Selection')
selected_key = st.sidebar.selectbox(f'Select Key ({selected_profile}):', audio_analysis_colome[f'Key ({selected_profile})'].unique())

# Apply filters based on user input
filtered_data = audio_analysis_colome[
    (audio_analysis_colome['BPM'] >= min_tempo) & (audio_analysis_colome['BPM'] <= max_tempo) &
    (audio_analysis_colome['Danceability'] >= min_danceability) & (audio_analysis_colome['Danceability'] <= max_danceability) &
    (audio_analysis_colome[f'Key ({selected_profile})'] == selected_key)
]

# Display the filtered data or generate the playlist as per your requirements
st.write('Filtered Data Based on Tempo, Danceability, and Key:')
st.write(filtered_data)