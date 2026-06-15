# Natural Language Processing eBook Analysis

This repository contains a collection of Jupyter notebooks that demonstrate various Natural Language Processing (NLP) and text analysis techniques applied to the book "Miracle in the Andes" by Nando Parrado.

## Project Overview

This project serves as a practical introduction to text analysis, regular expressions, and NLP techniques using Python. The analysis is performed on "Miracle in the Andes," a gripping survival story about the 1972 Uruguayan Air Force Flight 571 crash in the Andes mountains.

## Repository Contents

### Notebooks

1. **`Book_Analysis.ipynb`** - Basic text analysis using string methods and regular expressions
   - Chapter counting and extraction
   - Word frequency analysis
   - Sentence extraction (e.g., sentences containing "love")
   - Introduction to regex patterns

2. **`Regex_Book.ipynb`** - Advanced regular expression techniques
   - Paragraph extraction based on keywords
   - Chapter title extraction
   - Custom word search function
   - Pattern matching for text mining

3. **`NLP-Book_Analysis.ipynb`** - Natural Language Processing analysis
   - Word frequency analysis with stopword filtering
   - Sentiment analysis using NLTK's SentimentIntensityAnalyzer
   - Chapter-by-chapter sentiment scoring
   - Most common words identification (excluding stop words)

### Data

- **`miracle_in_the_andes.txt`** - The complete text of "Miracle in the Andes" used for analysis

### Configuration

- **`.gitignore`** - Git ignore file for Python projects

## Key Features

### Text Analysis Capabilities
- **Word Frequency Analysis**: Count and rank the most frequently used words
- **Sentiment Analysis**: Analyze the emotional tone of text at both book and chapter levels
- **Pattern Matching**: Extract specific text patterns using regular expressions
- **Chapter Analysis**: Break down the book into chapters for individual analysis

### Technologies Used
- **Python**: Primary programming language
- **NLTK**: Natural Language Toolkit for advanced NLP operations
- **Regular Expressions**: For pattern matching and text extraction
- **Jupyter Notebooks**: Interactive development environment

## Getting Started

### Prerequisites
```bash
pip install nltk jupyter
```

### NLTK Setup
After installing NLTK, you'll need to download the required datasets:
```python
import nltk
nltk.download('stopwords')
nltk.download('vader_lexicon')
```

### Running the Analysis
1. Clone this repository
2. Open any of the Jupyter notebooks
3. Run the cells sequentially to see the analysis results

## Analysis Results

The notebooks demonstrate various insights about "Miracle in the Andes":

- **Most Common Words**: After filtering stop words, identify the key themes and concepts
- **Sentiment by Chapter**: Track the emotional journey throughout the book
- **Pattern Extraction**: Find specific themes, locations, or concepts mentioned in the text
- **Statistical Analysis**: Word counts, chapter lengths, and frequency distributions

## Educational Value

This project is ideal for:
- Learning basic NLP concepts
- Understanding regular expressions in practice
- Exploring text analysis workflows
- Getting hands-on experience with NLTK
- Understanding sentiment analysis techniques

## Future Enhancements

Potential areas for expansion:
- Named Entity Recognition (NER)
- Topic modeling
- Comparative analysis with other survival stories
- Visualization of sentiment trends
- Advanced text preprocessing techniques

## Contributing

Feel free to fork this repository and add your own analysis techniques or apply these methods to other texts.