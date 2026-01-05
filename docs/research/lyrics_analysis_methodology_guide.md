# Lyrics Analysis: Practical Methodology Guide

**Companion to:** `lyrics_analysis_research.md`
**Focus:** Implementation strategies, code examples, and workflows
**Date:** 2025-12-26

---

## Quick Reference: Analysis Types

| Analysis Type | Primary Tools | Output | Difficulty |
|---------------|---------------|--------|------------|
| **Sentiment** | VADER, TextBlob | Positive/negative scores | ⭐ Easy |
| **Topic Modeling** | LDA, NMF | Theme distributions | ⭐⭐ Medium |
| **Rhyme Analysis** | Custom, phonetic algorithms | Rhyme schemes, density | ⭐⭐⭐ Hard |
| **Metaphor Detection** | ML models, WordNet | Figurative language locations | ⭐⭐⭐ Hard |
| **Genre Classification** | Scikit-learn, BERT | Category predictions | ⭐⭐ Medium |
| **Style Transfer** | GPT-3, RNNs | Transformed lyrics | ⭐⭐⭐⭐ Expert |

---

## 1. Complete Analysis Pipeline

### Phase 1: Data Collection

```python
import requests
import json
from pathlib import Path

def fetch_lyrics(artist, song, api_key):
    """
    Fetch lyrics using Musixmatch API or similar
    Note: Always respect API terms of service and copyright
    """
    # Example structure - implement with actual API
    url = f"https://api.musixmatch.com/ws/1.1/track.lyrics.get"
    params = {
        'track': song,
        'artist': artist,
        'apikey': api_key
    }
    response = requests.get(url, params=params)
    return response.json()

# Alternative: Load from local files
def load_lyrics_from_directory(directory_path):
    """
    Load lyrics from text files in a directory
    Each file: artist_song.txt
    """
    lyrics_dict = {}
    path = Path(directory_path)
    for file in path.glob("*.txt"):
        with open(file, 'r', encoding='utf-8') as f:
            lyrics_dict[file.stem] = f.read()
    return lyrics_dict
```

### Phase 2: Preprocessing Suite

```python
import spacy
import re
from string import punctuation

# Load spaCy model (download first: python -m spacy download en_core_web_sm)
nlp = spacy.load("en_core_web_sm")

class LyricsPreprocessor:
    def __init__(self, remove_stopwords=True, lemmatize=True):
        self.remove_stopwords = remove_stopwords
        self.lemmatize = lemmatize

    def clean_text(self, text):
        """Basic cleaning while preserving structure"""
        # Remove verse/chorus markers if needed
        text = re.sub(r'\[.*?\]', '', text)

        # Remove excessive whitespace
        text = re.sub(r'\s+', ' ', text)

        return text.strip()

    def tokenize(self, text):
        """Tokenize with spaCy"""
        doc = nlp(text)
        tokens = []
        for token in doc:
            # Skip stopwords and punctuation if configured
            if self.remove_stopwords and token.is_stop:
                continue
            if token.is_punct:
                continue

            # Use lemma if lemmatization enabled
            word = token.lemma_ if self.lemmatize else token.text
            tokens.append(word.lower())

        return tokens

    def extract_lines(self, text):
        """Extract individual lines for structural analysis"""
        lines = [line.strip() for line in text.split('\n')]
        # Filter empty lines
        return [line for line in lines if line]

    def get_sentence_boundaries(self, text):
        """Get sentence boundaries for stanza detection"""
        doc = nlp(text)
        return [(sent.start_char, sent.end_char) for sent in doc.sents]

# Usage
preprocessor = LyricsPreprocessor(remove_stopwords=True, lemmatize=True)
clean_lyrics = preprocessor.clean_text(raw_lyrics)
tokens = preprocessor.tokenize(clean_lyrics)
lines = preprocessor.extract_lines(clean_lyrics)
```

---

## 2. Sentiment Analysis Implementation

### VADER Approach (Recommended for Lyrics)

```python
from nltk.sentiment import SentimentIntensityAnalyzer
import nltk

# Download VADER lexicon (first time only)
nltk.download('vader_lexicon')

class LyricsSentimentAnalyzer:
    def __init__(self):
        self.sia = SentimentIntensityAnalyzer()

    def analyze_song(self, lyrics, by_line=False):
        """
        Analyze sentiment of lyrics

        Args:
            lyrics: Full lyrics text
            by_line: If True, analyze each line separately

        Returns:
            Dictionary with sentiment scores
        """
        if by_line:
            lines = lyrics.split('\n')
            line_scores = []
            for line in lines:
                if line.strip():
                    scores = self.sia.polarity_scores(line)
                    line_scores.append({
                        'line': line,
                        'compound': scores['compound'],
                        'positive': scores['pos'],
                        'negative': scores['neg'],
                        'neutral': scores['neu']
                    })
            return line_scores
        else:
            return self.sia.polarity_scores(lyrics)

    def get_emotional_arc(self, lyrics):
        """Track emotional changes throughout song"""
        lines = [l for l in lyrics.split('\n') if l.strip()]
        scores = []
        for line in lines:
            score = self.sia.polarity_scores(line)
            scores.append(score['compound'])

        return {
            'arc': scores,
            'min': min(scores),
            'max': max(scores),
            'mean': sum(scores) / len(scores),
            'variance': sum((x - sum(scores)/len(scores))**2 for x in scores) / len(scores)
        }

# Usage
analyzer = LyricsSentimentAnalyzer()

# Whole song sentiment
song_sentiment = analyzer.analyze_song(lyrics)
print(f"Overall sentiment: {song_sentiment['compound']:.3f}")

# Emotional arc
arc = analyzer.get_emotional_arc(lyrics)
print(f"Emotional range: {arc['min']:.3f} to {arc['max']:.3f}")
```

### Custom Emotion Categories

```python
from textblob import TextBlob

class EmotionClassifier:
    """Beyond positive/negative to specific emotions"""

    EMOTION_LEXICON = {
        'joy': ['happy', 'love', 'beautiful', 'wonderful', 'amazing'],
        'sadness': ['sad', 'cry', 'lonely', 'heartbreak', 'pain'],
        'anger': ['angry', 'hate', 'fight', 'rage', 'furious'],
        'fear': ['scared', 'afraid', 'dark', 'nightmare', 'terror'],
        'anticipation': ['wait', 'coming', 'soon', 'ready', 'expect'],
        'surprise': ['shock', 'sudden', 'unexpected', 'surprise'],
        'trust': ['believe', 'faith', 'trust', 'honest', 'true'],
        'disgust': ['disgust', 'sick', 'wrong', 'dirty']
    }

    def classify_emotions(self, text):
        """Classify emotions using keyword matching"""
        text_lower = text.lower()
        emotion_scores = {}

        for emotion, keywords in self.EMOTION_LEXICON.items():
            score = sum(1 for kw in keywords if kw in text_lower)
            emotion_scores[emotion] = score

        # Normalize
        total = sum(emotion_scores.values()) or 1
        return {k: v/total for k, v in emotion_scores.items()}
```

---

## 3. Topic Modeling with LDA

```python
import gensim
from gensim import corpora
from gensim.models import LdaModel
import matplotlib.pyplot as plt

class LyricsTopicModeler:
    def __init__(self, num_topics=5, passes=10):
        self.num_topics = num_topics
        self.passes = passes
        self.dictionary = None
        self.corpus = None
        self.model = None

    def prepare_corpus(self, lyrics_list):
        """
        Prepare corpus from multiple songs

        Args:
            lyrics_list: List of preprocessed token lists
        """
        # Create dictionary
        self.dictionary = corpora.Dictionary(lyrics_list)

        # Filter extremes (optional)
        self.dictionary.filter_extremes(no_below=2, no_above=0.5)

        # Create corpus
        self.corpus = [self.dictionary.doc2bow(lyrics) for lyrics in lyrics_list]

    def train_model(self):
        """Train LDA model"""
        self.model = LdaModel(
            corpus=self.corpus,
            id2word=self.dictionary,
            num_topics=self.num_topics,
            random_state=100,
            passes=self.passes,
            alpha='auto',
            per_word_topics=True
        )

    def get_topics(self, num_words=10):
        """Extract topics with top words"""
        return self.model.print_topics(num_topics=self.num_topics,
                                       num_words=num_words)

    def infer_topics(self, new_lyrics):
        """Infer topics for new lyrics"""
        bow = self.dictionary.doc2bow(new_lyrics)
        return self.model.get_document_topics(bow)

    def visualize_topics(self):
        """Simple topic visualization"""
        topics = self.get_topics(num_words=5)

        for idx, topic in topics:
            print(f"Topic {idx}:")
            print("-" * 40)
            # Parse topic string
            words = [word.split("*")[1].strip('"')
                    for word in topic.split(" + ")]
            print(", ".join(words))
            print()

# Usage
# Assume we have preprocessed multiple songs
preprocessor = LyricsPreprocessor()
song_tokens_list = [preprocessor.tokenize(song) for song in lyrics_collection]

modeler = LyricsTopicModeler(num_topics=5)
modeler.prepare_corpus(song_tokens_list)
modeler.train_model()
topics = modeler.get_topics(num_words=10)
```

---

## 4. Rhyme Analysis

```python
import pronouncing
import re

class RhymeAnalyzer:
    def __init__(self):
        """Initialize with CMU pronunciation dictionary"""
        # Using pronouncing library (pip install pronouncing)

    def get_rhyme_sound(self, word):
        """Get ARPABet pronunciation for rhyme matching"""
        phones = pronouncing.phones_for_word(word)
        if phones:
            # Return last stressed vowel and following sounds
            return pronouncing.rhyming_part(phones[0])
        return None

    def count_rhymes(self, lines):
        """
        Count end rhymes in lyrics

        Returns:
            Rhyme scheme (e.g., ['A', 'A', 'B', 'A'])
            Rhyme density (proportion of rhyming lines)
        """
        scheme = []
        rhyme_sounds = {}

        # Extract last word from each line
        last_words = []
        for line in lines:
            if line.strip():
                words = line.split()
                if words:
                    last_words.append(words[-1].lower().strip(punctuation))

        # Assign rhyme scheme letters
        current_letter = 65  # ASCII 'A'
        for word in last_words:
            sound = self.get_rhyme_sound(word)

            if sound in rhyme_sounds:
                scheme.append(rhyme_sounds[sound])
            else:
                rhyme_sounds[sound] = chr(current_letter)
                scheme.append(chr(current_letter))
                current_letter += 1
                if current_letter > 90:  # Past 'Z'
                    current_letter = 65

        # Calculate rhyme density
        rhyme_counts = {}
        for letter in scheme:
            rhyme_counts[letter] = rhyme_counts.get(letter, 0) + 1

        rhyming_lines = sum(count - 1 for count in rhyme_counts.values() if count > 1)
        density = rhyming_lines / len(lines) if lines else 0

        return {
            'scheme': scheme,
            'density': density,
            'unique_rhymes': len(rhyme_counts)
        }

    def find_internal_rhymes(self, line):
        """Find rhymes within a line"""
        words = re.findall(r'\b\w+\b', line.lower())
        rhymes = []

        for i, word1 in enumerate(words):
            for word2 in words[i+1:]:
                if pronouncing.rhymes(word1, word2):
                    rhymes.append((word1, word2))

        return rhymes
```

---

## 5. Stylistic Feature Extraction

```python
import numpy as np
from collections import Counter

class StylisticAnalyzer:
    def analyze_vocabulary_richness(self, lyrics):
        """
        Calculate Type-Token Ratio (TTR)
        Higher = more diverse vocabulary
        """
        words = lyrics.lower().split()
        unique_words = set(words)

        ttr = len(unique_words) / len(words) if words else 0

        return {
            'total_words': len(words),
            'unique_words': len(unique_words),
            'ttr': ttr
        }

    def analyze_readability(self, lyrics):
        """
        Calculate Flesch-Kincaid Grade Level
        Adapted for lyrics (may differ from prose)
        """
        sentences = [s for s in lyrics.split('\n') if s.strip()]
        words = lyrics.split()

        if not sentences:
            return {'fk_grade': 0}

        total_sentences = len(sentences)
        total_words = len(words)
        syllables = sum(self._count_syllables(word) for word in words)

        # Flesch-Kincaid formula
        fk_grade = (0.39 * (total_words / total_sentences) +
                   11.8 * (syllables / total_words) - 15.59)

        return {'fk_grade': fk_grade}

    def _count_syllables(self, word):
        """Estimate syllables in word"""
        word = word.lower()
        count = 0
        vowels = 'aeiouy'

        if word[0] in vowels:
            count += 1

        for index in range(1, len(word)):
            if word[index] in vowels and word[index - 1] not in vowels:
                count += 1

        if word.endswith('e'):
            count -= 1

        if word.endswith('le') and len(word) > 2 and word[-3] not in vowels:
            count += 1

        return count if count > 0 else 1

    def analyze_repetition_patterns(self, lyrics):
        """Find repeated phrases and structures"""
        lines = [l.strip() for l in lyrics.split('\n') if l.strip()]

        # Count line repetitions
        line_counts = Counter(lines)

        # Find n-gram repetitions
        bigrams = []
        for i in range(len(lines) - 1):
            bigrams.append((lines[i], lines[i+1]))

        bigram_counts = Counter(bigrams)

        return {
            'repeated_lines': [(line, count) for line, count in line_counts.most_common(10) if count > 1],
            'repeated_bigrams': [(bigram, count) for bigram, count in bigram_counts.most_common(10) if count > 1]
        }
```

---

## 6. Genre Classification

```python
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report

class GenreClassifier:
    def __init__(self):
        self.vectorizer = TfidfVectorizer(max_features=1000)
        self.classifier = MultinomialNB()

    def prepare_data(self, lyrics_labels):
        """
        Prepare training data

        Args:
            lyrics_labels: List of (lyrics, genre) tuples
        """
        lyrics = [item[0] for item in lyrics_labels]
        genres = [item[1] for item in lyrics_labels]

        # Split data
        X_train, X_test, y_train, y_test = train_test_split(
            lyrics, genres, test_size=0.2, random_state=42
        )

        # Vectorize
        X_train_vec = self.vectorizer.fit_transform(X_train)
        X_test_vec = self.vectorizer.transform(X_test)

        return X_train_vec, X_test_vec, y_train, y_test

    def train(self, lyrics_labels):
        """Train classifier"""
        X_train, X_test, y_train, y_test = self.prepare_data(lyrics_labels)

        self.classifier.fit(X_train, y_train)

        # Evaluate
        y_pred = self.classifier.predict(X_test)
        report = classification_report(y_test, y_pred)

        return report

    def predict(self, lyrics):
        """Predict genre for new lyrics"""
        lyrics_vec = self.vectorizer.transform([lyrics])
        prediction = self.classifier.predict(lyrics)
        probabilities = self.classifier.predict_proba(lyrics)

        return {
            'genre': prediction[0],
            'confidence': max(probabilities[0])
        }
```

---

## 7. Complete Analysis Workflow

```python
class LyricsAnalysisSuite:
    """Complete lyrics analysis pipeline"""

    def __init__(self, lyrics_text):
        self.lyrics = lyrics_text
        self.preprocessor = LyricsPreprocessor()
        self.sentiment_analyzer = LyricsSentimentAnalyzer()
        self.rhyme_analyzer = RhymeAnalyzer()
        self.stylistic_analyzer = StylisticAnalyzer()

    def run_complete_analysis(self):
        """Run all analyses and return comprehensive report"""
        # Preprocess
        clean_text = self.preprocessor.clean_text(self.lyrics)
        lines = self.preprocessor.extract_lines(clean_text)
        tokens = self.preprocessor.tokenize(clean_text)

        # Run all analyses
        results = {}

        # 1. Sentiment
        results['sentiment'] = self.sentiment_analyzer.analyze_song(clean_text)
        results['emotional_arc'] = self.sentiment_analyzer.get_emotional_arc(clean_text)

        # 2. Rhyme
        results['rhyme'] = self.rhyme_analyzer.count_rhymes(lines)

        # 3. Stylistic
        results['vocabulary'] = self.stylistic_analyzer.analyze_vocabulary_richness(clean_text)
        results['readability'] = self.stylistic_analyzer.analyze_readability(clean_text)
        results['repetition'] = self.stylistic_analyzer.analyze_repetition_patterns(clean_text)

        # 4. Structure
        results['structure'] = {
            'total_lines': len(lines),
            'total_words': len(tokens),
            'avg_line_length': np.mean([len(line.split()) for line in lines])
        }

        return results

    def generate_report(self, results):
        """Generate human-readable report"""
        report = f"""
=== LYRICS ANALYSIS REPORT ===

STRUCTURE:
- Total Lines: {results['structure']['total_lines']}
- Total Words: {results['structure']['total_words']}
- Avg Line Length: {results['structure']['avg_line_length']:.2f} words

SENTIMENT:
- Overall: {results['sentiment']['compound']:.3f}
- Positive: {results['sentiment']['pos']:.3f}
- Negative: {results['sentiment']['neg']:.3f}
- Neutral: {results['sentiment']['neu']:.3f}
- Emotional Range: {results['emotional_arc']['min']:.3f} to {results['emotional_arc']['max']:.3f}

RHYME:
- Scheme: {''.join(results['rhyme']['scheme'][:20])}...
- Density: {results['rhyme']['density']:.3f}
- Unique Rhymes: {results['rhyme']['unique_rhymes']}

VOCABULARY:
- Unique Words: {results['vocabulary']['unique_words']}
- Type-Token Ratio: {results['vocabulary']['ttr']:.3f}

READABILITY:
- Grade Level: {results['readability']['fk_grade']:.1f}
"""
        return report

# Usage
# lyrics = """Your song lyrics here"""
# suite = LyricsAnalysisSuite(lyrics)
# results = suite.run_complete_analysis()
# report = suite.generate_report(results)
# print(report)
```

---

## 8. Advanced: Metaphor Detection (Conceptual)

```python
# Note: Full metaphor detection requires trained ML models
# This is a simplified keyword-based approach

class MetaphorDetector:
    """Basic metaphor detection using linguistic markers"""

    METAPHOR_MARKERS = [
        'like', 'as if', 'as though',
        'is a', 'was a', 'seems like',
        'metaphor', 'symbolizes', 'represents'
    ]

    CONCEPTUAL_METAPHORS = {
        'LOVE_IS_JOURNEY': ['travel', 'path', 'road', 'crossroads', 'journey'],
        'LIFE_IS_DREAM': ['dream', 'nightmare', 'waking', 'sleep'],
        'ARGUMENT_IS_WAR': ['attack', 'defend', 'win', 'lose', 'battle'],
        'TIME_IS_MONEY': ['spend', 'save', 'waste', 'invest', 'cost'],
        'HAPPY_IS_UP': ['uplifting', 'high', 'raise', 'cheer up'],
        'SAD_IS_DOWN': ['down', 'low', 'depressed', 'fall']
    }

    def find_similes(self, text):
        """Find explicit similes using markers"""
        similes = []
        lines = text.split('\n')

        for line in lines:
            for marker in self.METAPHOR_MARKERS:
                if marker in line.lower():
                    similes.append((line.strip(), marker))
                    break

        return similes

    def detect_conceptual_metaphors(self, text):
        """Detect conceptual metaphors using domain mapping"""
        text_lower = text.lower()

        detected = []
        for metaphor, keywords in self.CONCEPTUAL_METAPHORS.items():
            matches = [kw for kw in keywords if kw in text_lower]
            if matches:
                detected.append({
                    'metaphor': metaphor,
                    'evidence': matches,
                    'confidence': len(matches) / len(keywords)
                })

        return detected
```

---

## Installation Requirements

```bash
# Core NLP
pip install spacy
python -m spacy download en_core_web_sm

# Text processing
pip install nltk
pip install textblob

# Machine learning
pip install scikit-learn
pip install gensim

# Lyrics-specific
pip install pronouncing

# Visualization (optional)
pip install matplotlib
pip install wordcloud

# Download NLTK data
python -c "import nltk; nltk.download('vader_lexicon'); nltk.download('punkt')"
```

---

## Best Practices

### 1. Data Ethics
- Always respect copyright and API terms
- Don't reproduce full lyrics without permission
- Use official APIs (Musixmatch, Genius) when available

### 2. Analysis Validity
- Consider genre-specific conventions
- Account for era/context differences
- Validate findings with domain experts

### 3. Computational Efficiency
- Preprocess once, store results
- Use batch processing for large datasets
- Cache expensive operations (rhyme detection)

### 4. Interpretation
- Quantitative results need qualitative context
- Cross-reference multiple metrics
- Consider lyrical intent and artistic choices

---

## Common Pitfalls

1. **Over-cleaning:** Removing too much structure (punctuation, line breaks)
2. **Genre bias:** Applying rap metrics to pop lyrics
3. **Cultural context:** Missing references, slang, idioms
4. **Small samples:** Drawing conclusions from limited data
5. **Confidence overstatement:** ML predictions are probabilistic

---

## Next Steps

After mastering these basics, explore:
- **Deep learning:** BERT embeddings for semantic analysis
- **Multimodal:** Combining audio features with lyrics
- **Real-time:** Streaming analysis for live performances
- **Cross-lingual:** Analyzing lyrics in multiple languages
- **Generation:** Creating new lyrics with AI models

---

**Document Status:** Complete
**Version:** 1.0
**Related:** `lyrics_analysis_research.md`

---

*For theoretical foundations and research sources, refer to the companion research document.*
