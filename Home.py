import streamlit as st 
from streamlit_extras.switch_page_button import switch_page
from streamlit_extras.grid import grid
from streamlit_extras.colored_header import colored_header
import os,time,subprocess,sys
from src.youtube_audio import set_ffmpeg

st.title('  Transcribo- An Video Analyzer')
st.subheader('Welcome to our AI-powered video analysis tool')
st.markdown(
        """
        <style>
        body {
            background-color: #f0f0f0; /* Light gray background */
            font-family: Arial, sans-serif; /* Set font to Arial */
        }
        </style>
        """,
        unsafe_allow_html=True
    )

st.write("This project provides various features to analyze YouTube videos.")

intro = "This web application is an AI tool with numerous features that can be used to accomplish various tasks on a specific 'Youtube video'," "Youtube Shots, or any other type of video, such as transcription and scrolling subtitle embeddings..\n "
app_description= """
Comprehensive Video Analysis: Develop a tool capable of analyzing various aspects of YouTube videos, including transcribing audio, performing sentiment analysis, and identifying named entities.

Enhanced Accessibility: Provide a user-friendly interface that makes it easy for users to interact with and extract insights from YouTube videos.

Automation: Automate the process of extracting metadata, generating descriptions, and identifying key topics covered in the videos.

Scalability: Design the tool to be scalable, allowing it to handle large volumes of video content efficiently and effectively.
 
"""

st.markdown(f"{intro}\n\n{app_description}",unsafe_allow_html=True)

colored_header(
    label="Apps",
    description=" ",
    color_name="blue-green-70",
)

col1, col2 = st.columns(2)
with col1:
    if st.button('Video Transcription'):
        switch_page('Transcripter')

with col2:
    if st.button('Subtitle Editor'):
        switch_page('Subtitle_Merger')

st.markdown("<hr>", unsafe_allow_html=True)


@st.cache_resource
def install_ffmpeg():
    from pydub import AudioSegment
    from pydub.utils import which
    import ffmpeg
    
    try:
        st.write('Installing ffmpeg and ffprobe dependencies...')
        # Run "apt install ffmpeg and ffprobe "
        
        subprocess.run([sys.executable, "-m", "pip", "install", "pydub","simpleaudio"], capture_output=True, text=True)
        subprocess.run(["sudo", "apt", "install", "ffmpeg"], capture_output=True, text=True)
        st.write("ffmpeg and ffprobe installed successfully.")
        
        virtual_env_path = "./venv"
        lib_path = "/usr/bin/ffmpeg"

        ffmpeg_binary = lib_path
        AudioSegment.ffmpeg = ffmpeg_binary
        AudioSegment.converter = which("ffmpeg")
        ffmpeg.input.ffprobe = '/usr/bin/ffprobe'

        st.write("ffmpeg and ffprobe setup done completely.")
    except Exception as e:
        st.error(f'Error: {e}')

if "dependencies" not in st.session_state:
    st.session_state.dependencies = True 
    try:
        set_ffmpeg()
        install_ffmpeg()
    except Exception as e:
        st.error(f'Error in Loading: {e}')
        pass
