# Audio Segment Search and Retrieval System

This Jupyter notebook implements an audio segment search and retrieval system with the following key components:

## Main Components

1. Audio Segmentation
- Segments audio files based on transcript timestamps
- Uses VTT files for timing information  
- Creates overlapping chunks for better context
- Exports segments as individual WAV files

2. Vector Store 
- Embeds text segments using Sentence Transformers
- Indexes segments in LanceDB for similarity search
- Stores segment metadata (text, audio path, timestamps)

3. Search Interface
- Semantic search using text queries
- Returns ranked results with relevant audio segments
- Allows playback of matching audio segments

## Key Classes

### AudioSegmenter
- Processes audio and VTT files
- Creates overlapping segments
- Handles file I/O and metadata

### SegmentVectorStore  
- Creates and manages vector embeddings
- Interfaces with LanceDB
- Provides search functionality

### SimpleRetriever
- User-friendly search interface
- Audio playback capabilities
- Interactive query mode

## Usage

1. Initialize segmenter and create segments:
