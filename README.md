# Audio Segment Search and Retrieval System

This project implements an efficient and scalable **Audio Segment Search and Retrieval System**, enabling users to search for specific audio segments based on textual queries. The system is designed to process long audio files, segment them based on timestamped transcripts, and retrieve relevant audio clips using semantic search.

## Overview

The system consists of three primary components:

1. **Audio Segmentation**: Splits long audio files into smaller, manageable segments based on transcript timestamps.
2. **Vector Store**: Converts text-based segments into numerical embeddings and stores them for similarity search.
3. **Search Interface**: Enables users to search using natural language queries and retrieve relevant audio clips.

## Key Features

- **Precise Audio Segmentation**: Uses transcript timestamps (from VTT files) to create well-defined segments.
- **Context Preservation**: Implements overlapping segments to maintain context across speech boundaries.
- **Efficient Search and Retrieval**: Leverages semantic search for high-relevance matching.
- **Interactive Playback**: Allows users to listen to retrieved audio segments directly.

## System Components

### 1. Audio Segmentation
- **Purpose**: To divide long audio recordings into meaningful, context-rich segments.
- **Approach**:
  - Uses **VTT (WebVTT) files** for accurate timestamp extraction.
  - Segments the audio file based on timestamps while maintaining some overlap between segments for better context.
  - Saves each extracted segment as a separate **WAV file** for easy retrieval.

### 2. Vector Store
- **Purpose**: To store and retrieve audio segments efficiently based on text similarity.
- **Approach**:
  - Embeds textual content of each segment using **Sentence Transformers**.
  - Stores embeddings and metadata in **LanceDB**, a high-performance vector database.
  - Enables fast and scalable similarity searches based on user queries.

### 3. Search Interface
- **Purpose**: To allow users to search for specific phrases or topics and retrieve relevant audio segments.
- **Approach**:
  - Implements a **semantic search** mechanism that matches queries with segment embeddings.
  - Ranks results based on similarity scores to provide the most relevant matches first.
  - Provides an interactive interface to play retrieved audio clips.

## Key Classes and Their Responsibilities

### 1. `AudioSegmenter`
- Reads and processes **audio files** along with their corresponding **VTT transcripts**.
- Extracts timestamp information and generates **overlapping audio segments**.
- Saves segmented audio as WAV files and prepares metadata for storage.

### 2. `SegmentVectorStore`
- Converts text segments into **vector embeddings** using Sentence Transformers.
- Stores these embeddings along with metadata (text, timestamps, file paths) in **LanceDB**.
- Provides search functionality by performing **similarity matching** between user queries and stored embeddings.

### 3. `SimpleRetriever`
- Facilitates user-friendly search interactions.
- Accepts natural language queries and finds **most relevant audio segments**.
- Provides an interface for **audio playback**, allowing users to listen to the retrieved clips.

## Usage Guide

### Step 1: Initialize and Segment Audio Files
```python
segmenter = AudioSegmenter("input_audio.wav", "transcript.vtt")
segments = segmenter.create_segments()
```

### Step 2: Generate Embeddings and Store in Vector Database
```python
vector_store = SegmentVectorStore()
vector_store.index_segments(segments)
```

### Step 3: Perform Search and Retrieve Audio Segments
```python
retriever = SimpleRetriever(vector_store)
results = retriever.search("specific phrase or topic")
retriever.play_audio(results[0])
```

## Applications

- **Podcast and Lecture Search**: Quickly find and listen to relevant segments in long recordings.
- **Customer Support Calls**: Retrieve important moments from call logs based on keywords.
- **Legal and Compliance Review**: Search for key discussions in recorded meetings.
- **Educational Content Navigation**: Locate specific explanations or topics in recorded lessons.

## Future Enhancements
- **Multilingual Support**: Expanding to non-English transcripts and queries.
- **Speaker Identification**: Adding speaker diarization to improve retrieval accuracy.
- **Real-time Processing**: Enhancing efficiency for near-instantaneous search results.

This system provides a powerful and intuitive way to search and retrieve audio segments, making large audio datasets more accessible and useful!

