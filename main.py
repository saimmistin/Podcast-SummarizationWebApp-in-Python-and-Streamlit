import streamlit as st
import glob
import json
from api_communication import save_transcript

# Page configuration
st.set_page_config(
    page_title="Podcast Summaries",
    page_icon=":headphones:",
    layout="wide"
)

# Title
st.title("Podcast Summaries")

# Sidebar
episode_id = st.sidebar.text_input("Enter Episode ID")
button = st.sidebar.button("Get Episode Summary", on_click=save_transcript, args=(episode_id,))

# Function to format time
def get_clean_time(start_ms):
    seconds = int((start_ms / 1000) % 60)
    minutes = int((start_ms / (1000 * 60)) % 60)
    hours = int((start_ms / (1000 * 60 * 60)) % 24)
    if hours > 0:
        start_t = f'{hours:02d}:{minutes:02d}:{seconds:02d}'
    else:
        start_t = f'{minutes:02d}:{seconds:02d}'
    return start_t

# Display episode summary
if button:
    filename = episode_id + '_chapters.json'
    with open(filename, 'r') as f:
        data = json.load(f)

    chapters = data['chapters']
    episode_title = data['episode_title']
    thumbnail = data['thumbnail']
    podcast_title = data['podcast_title']

    # Header
    st.header(f"{podcast_title} - {episode_title}")

    # Image
    st.image(thumbnail, width=200)

    # Summary
    st.markdown(f'#### {episode_title}')

    # Chapters
    for chp in chapters:
        with st.expander(f"{chp['gist']} - {get_clean_time(chp['start'])}"):
            st.write(chp['summary'])
