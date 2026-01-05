# Lyrics Analysis - Quick Reference Guide

**Companion:** Methodology Guide & Research Document
**Purpose:** Fast lookup for common analysis tasks
**Date:** 2025-12-26

---

## 🚀 Quick Start (5 Minutes)

```python
# Install dependencies
pip install spacy nltk textblob pronouncing gensim scikit-learn
python -m spacy download en_core_web_sm

# Basic analysis
import spacy
from nltk.sentiment import SentimentIntensityAnalyzer

nlp = spacy.load("en_core_web_sm")
sia = SentimentIntensityAnalyzer()

# Your lyrics
lyrics = "Your song lyrics here"

# Analyze
sentiment = sia.polarity_scores(lyrics)
doc = nlp(lyrics)

print(f"Sentiment: {sentiment['compound']:.2f}")
print(f"Words: {len([t for t in doc if not t.is_punct])}")
print(f"Unique: {len(set([t.text.lower() for t in doc]))}")
```

---

## 📊 Analysis Types at a Glance

### 1. Sentiment Analysis
**Tool:** VADER (NLTK)
**Output:** -1 (negative) to +1 (positive)
**Time:** Instant
**Use:** Mood classification, emotional tracking

```python
from nltk.sentiment import SentimentIntensityAnalyzer
sia = SentimentIntensityAnalyzer()
score = sia.polarity_scores(lyrics)['compound']
```

### 2. Topic Modeling
**Tool:** LDA (Gensim)
**Output:** Topic distributions with keywords
**Time:** Minutes (requires training)
**Use:** Thematic categorization, content discovery

```python
from gensim.models import LdaModel
lda = LdaModel(corpus, num_topics=5, id2word=dictionary)
topics = lda.print_topics(num_words=5)
```

### 3. Rhyme Analysis
**Tool:** pronouncing + custom
**Output:** Rhyme scheme (AABB, ABAB), density
**Time:** Seconds
**Use:** Structural analysis, genre classification

```python
import pronouncing
rhymes = pronouncing.rhymes("love")  # ['glove', 'above', 'dove']
```

### 4. Genre Classification
**Tool:** Scikit-learn (Naive Bayes, SVM)
**Output:** Category predictions
**Time:** Hours (requires training data)
**Use:** Music categorization, recommendation

```python
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB

vec = TfidfVectorizer()
clf = MultinomialNB()
```

### 5. Style Transfer
**Tool:** GPT-3, RNNs, VAEs
**Output:** Transformed lyrics
**Time:** Variable
**Use:** Creative applications, remixing

---

## 🛠️ Essential Libraries

| Library | Install | Best For |
|---------|---------|----------|
| **spaCy** | `pip install spacy` | Production NLP |
| **NLTK** | `pip install nltk` | Research/education |
| **TextBlob** | `pip install textblob` | Quick sentiment |
| **pronouncing** | `pip install pronouncing` | Rhyme detection |
| **Gensim** | `pip install gensim` | Topic modeling |
| **Scikit-learn** | `pip install scikit-learn` | ML classification |
| **Transformers** | `pip install transformers` | BERT, GPT models |

---

## 📈 Metrics Reference

### Sentiment Scores
- **> 0.05:** Positive
- **< -0.05:** Negative
- **-0.05 to 0.05:** Neutral

### Type-Token Ratio (Vocabulary Richness)
- **0.5-0.6:** High diversity
- **0.3-0.5:** Medium diversity
- **< 0.3:** Low diversity (repetitive)

### Flesch-Kincaid Grade Level
- **8-10:** Simple, pop-friendly
- **11-14:** Moderate complexity
- **15+:** Complex, academic

### Rhyme Density
- **> 0.7:** Highly rhyming (rap, musical theater)
- **0.4-0.7:** Moderate (pop, country)
- **< 0.4:** Low (free verse, experimental)

---

## 🎯 Common Workflows

### Workflow 1: Single Song Analysis
```
Input: Lyrics text
↓
Preprocess (tokenize, clean)
↓
Parallel Analyses:
  - Sentiment (VADER)
  - Structure (lines, stanzas)
  - Rhyme (scheme detection)
  - Vocabulary (richness)
↓
Output: Comprehensive report
```

### Workflow 2: Collection Analysis
```
Input: Multiple songs (corpus)
↓
Preprocess all
↓
Topic Modeling (LDA)
↓
Genre Classification (ML)
↓
Comparative Analysis
↓
Output: Trends, patterns, clusters
```

### Workflow 3: Style Transfer
```
Input: Source lyrics + Target style
↓
Extract features (rhythm, rhyme, sentiment)
↓
Apply style constraints
↓
Generate with LLM/GPT
↓
Validate (singability, coherence)
↓
Output: Transformed lyrics
```

---

## ⚡ Performance Tips

### Speed Optimization
1. **Vectorize operations:** Use NumPy/pandas instead of loops
2. **Cache expensive ops:** Save preprocessed data
3. **Batch processing:** Process multiple songs in parallel
4. **Lazy loading:** Load models only when needed

### Memory Management
1. **Limit vocabulary:** Filter rare words in dictionaries
2. **Use generators:** Process large files line-by-line
3. **Clear memory:** Delete intermediate variables
4. **Chunk data:** Process corpora in batches

### Quality Improvements
1. **Ensemble methods:** Combine multiple classifiers
2. **Cross-validation:** Validate on multiple splits
3. **Domain adaptation:** Fine-tune for specific genres
4. **Human evaluation:** Validate AI findings with experts

---

## 📚 Data Sources

### Legal APIs
- **Musixmatch:** Lyrics + metadata
- **Genius:** Lyrics + annotations
- **Spotify API:** Audio features + lyrics (via Musixmatch)

### Open Datasets
- **Million Song Dataset:** Lyrics + metadata
- ** lyricsdatasets:** GitHub collections
- **Kaggle:** Various lyrics datasets

### Academic Resources
- **ACL Anthology:** NLP papers
- **arXiv:** Preprints (cs.CL, cs.IR)
- **ResearchGate:** Academic publications

---

## 🚨 Common Issues & Solutions

### Issue: "Module not found"
**Solution:**
```bash
pip install library_name
python -m spacy download en_core_web_sm  # For spaCy
```

### Issue: Poor rhyme detection
**Solution:** Use phonetic libraries (pronouncing, CMU dict)
```python
import pronouncing
phones = pronouncing.phones_for_word("word")
```

### Issue: Low classification accuracy
**Solution:**
- Increase training data
- Try different algorithms (SVM, Random Forest)
- Use feature engineering (TF-IDF, embeddings)
- Balance classes (SMOTE, weighting)

### Issue: Memory error with large corpora
**Solution:**
- Process in chunks
- Use generators
- Limit vocabulary size
- Use sparse matrices

---

## 🔍 Advanced Techniques

### BERT Embeddings for Semantic Analysis
```python
from transformers import BertModel, BertTokenizer
tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
model = BertModel.from_pretrained('bert-base-uncased')

# Get contextual embeddings
inputs = tokenizer(lyrics, return_tensors='pt')
outputs = model(**inputs)
embeddings = outputs.last_hidden_state
```

### Attention Mechanisms
```python
import torch
import torch.nn as nn

class AttentionAnalyzer(nn.Module):
    def __init__(self, hidden_dim):
        super().__init__()
        self.attention = nn.Linear(hidden_dim, 1)

    def forward(self, embeddings):
        weights = torch.softmax(self.attention(embeddings), dim=1)
        return torch.sum(weights * embeddings, dim=1)
```

### Multimodal Analysis (Audio + Lyrics)
```python
# Combine audio features with lyric embeddings
audio_features = extract_audio_features(mp3_file)
lyric_embeddings = get_bert_embeddings(lyrics)

# Fusion
combined = torch.cat([audio_features, lyric_embeddings], dim=-1)
```

---

## 📖 Further Learning

### Online Courses
- **Coursera:** NLP Specialization (deeplearning.ai)
- **edX:** Applied Text Mining in Python
- **Fast.ai:** Practical Deep Learning for Coders

### Books
- "Speech and Language Processing" (Jurafsky & Martin)
- "Natural Language Processing with Python" (Bird, Klein, Loper)
- "Text Mining with R" (Silge & Robinson)

### Communities
- **Stack Overflow:** NLP, Python tags
- **Reddit:** r/LanguageTechnology, r/MachineLearning
- **Discord:** AI/ML servers
- **GitHub:** Open source NLP projects

### Papers to Read
1. "Lyrics Information Processing" (Watanabe, 2020)
2. "VADER: A Parsimonious Rule-Based Model" (Hutto & Gilbert)
3. "Using Automated Rhyme Detection in Rap" (Hirjee & Brown)
4. "Rhythm Decode: AI-Powered Lyric Analysis" (2025)

---

## 🎓 Project Ideas

### Beginner
- Sentiment analysis of favorite artist
- Rhyme scheme analyzer
- Vocabulary richness comparison

### Intermediate
- Genre classification system
- Topic modeling of decade trends
- Lyric recommendation engine

### Advanced
- Style transfer between artists
- Multimodal mood detection
- Real-time lyric visualizer
- AI lyric generator with constraints

---

## ✅ Quality Checklist

Before deploying analysis:
- [ ] Preprocessing preserves structure
- [ ] Results validated against human judgment
- [ ] Genre-specific conventions considered
- [ ] Sufficient sample size (n > 100 for statistics)
- [ ] Cross-validation performed
- [ ] Ethical guidelines followed (copyright, attribution)
- [ ] Documentation complete
- [ ] Code reproducible

---

## 🆘 Getting Help

### Debug Strategy
1. **Check input data:** Is it clean, properly formatted?
2. **Verify installation:** Are all dependencies installed?
3. **Test on known sample:** Does it work on simple examples?
4. **Isolate component:** Which specific step fails?
5. **Read error messages:** What do they actually say?

### Resources
- **Stack Overflow:** Search error messages
- **GitHub Issues:** Check library repositories
- **Documentation:** Read official docs first
- **Papers:** Check methodology sections

---

## 📞 Quick Commands Reference

```bash
# Install everything
pip install spacy nltk textblob gensim scikit-learn pronouncing transformers
python -m spacy download en_core_web_sm

# Download NLTK data
python -c "import nltk; nltk.download('vader_lexicon'); nltk.download('punkt')"

# Quick sentiment test
python -c "from nltk.sentiment import SentimentIntensityAnalyzer; print(SentimentIntensityAnalyzer().polarity_scores('I love this song'))"

# Check spaCy installation
python -c "import spacy; print(spacy.__version__)"

# Test pronouncing
python -c "import pronouncing; print(pronouncing.rhymes('test'))"
```

---

## 🎯 Summary: What to Use When

| Goal | Tool | Complexity |
|------|------|------------|
| **Quick sentiment** | VADER | ⭐ |
| **Topic discovery** | LDA | ⭐⭐ |
| **Genre prediction** | Scikit-learn | ⭐⭐ |
| **Semantic analysis** | BERT/Transformers | ⭐⭐⭐ |
| **Creative generation** | GPT-3/RNNs | ⭐⭐⭐⭐ |
| **Complete pipeline** | All of above | ⭐⭐⭐⭐⭐ |

---

**Version:** 1.0
**Last Updated:** 2025-12-26
**Related Documents:**
- `lyrics_analysis_research.md` (Theory & sources)
- `lyrics_analysis_methodology_guide.md` (Implementation)

---

*Start simple, iterate often, validate results!*
