import streamlit as st
import lancedb
from sentence_transformers import SentenceTransformer
import sounddevice as sd
import soundfile as sf
import os
import numpy as np
import base64

class AudioRetriever:
    def __init__(self, audio_dir: str = "segments"):
        self.model = SentenceTransformer('all-MiniLM-L6-v2')
        self.db = lancedb.connect("segments.db")
        self.audio_dir = audio_dir
        
    def search(self, query: str, limit: int = 5):
        table = self.db.open_table("segments")
        query_vector = self.model.encode(query).tolist()
        
        results = table.search(
            query_vector,
            vector_column_name="vector"
        ).limit(limit).to_list()
        
        return results
    
    def get_audio_path(self, audio_filename: str) -> str:
        """Get full path for audio file"""
        return os.path.join(self.audio_dir, audio_filename)

def get_audio_player_html(audio_path: str) -> str:
    """Create HTML audio player for the given audio file"""
    audio_file = open(audio_path, 'rb')
    audio_bytes = audio_file.read()
    audio_base64 = base64.b64encode(audio_bytes).decode()
    return f'''
        <audio controls>
            <source src="data:audio/wav;base64,{audio_base64}" type="audio/wav">
            Your browser does not support the audio element.
        </audio>
    '''

def main():
    st.set_page_config(
        page_title="Audio Segment Retriever",
        page_icon="🎵",
        layout="wide"
    )
    
    st.title("🔍 Audio Segment Search")
    
    # Initialize retriever
    retriever = AudioRetriever()
    
    # Search interface
    query = st.text_input(
        "Enter your search query:",
        placeholder="What would you like to search for?"
    )
    
    num_results = st.slider(
        "Number of results:",
        min_value=1,
        max_value=10,
        value=5
    )
    
    if query:
        results = retriever.search(query, limit=num_results)
        
        if results:
            st.write("---")
            st.subheader("Search Results")
            
            for i, result in enumerate(results, 1):
                with st.expander(f"Result {i}: {result['id']}", expanded=True):
                    # Display text
                    st.markdown("**Text Content:**")
                    st.write(result['text'])
                    
                    # Display audio player
                    st.markdown("**Audio Player:**")
                    audio_path = retriever.get_audio_path(result['audio_file'])
                    if os.path.exists(audio_path):
                        st.markdown(get_audio_player_html(audio_path), unsafe_allow_html=True)
                    else:
                        st.error(f"Audio file not found: {result['audio_file']}")
                    
                    # Display metadata
                    st.markdown("**File Information:**")
                    st.info(f"Audio filename: {result['audio_file']}")
                
                st.write("---")
        else:
            st.warning("No results found for your query.")
    
    # Add some helpful information at the bottom
    with st.sidebar:
        st.markdown("### How to use")
        st.markdown("""
        1. Enter your search query in the text box
        2. Adjust the number of results you want to see
        3. Click on each result to:
           - Read the text content
           - Play the audio
           - View file information
        """)
        
        st.markdown("### About")
        st.markdown("""
        This app uses semantic search to find relevant audio segments
        based on their transcribed text content. The search is powered
        by sentence transformers and LanceDB.
        """)

if __name__ == "__main__":
    main()