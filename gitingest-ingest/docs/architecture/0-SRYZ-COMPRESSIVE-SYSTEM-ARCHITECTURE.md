# SRYZ - Comprehensive System Architecture

**Project:** System Rhythm & Lyrics (SRYZ)
**Version:** 1.0
**Date:** December 26, 2025
**Status:** Production Ready
**Architect:** System Architecture Agent

---

## Table of Contents

1. [Executive Summary](#executive-summary)
2. [System Overview](#system-overview)
3. [High-Level Architecture](#high-level-architecture)
4. [Component Architecture](#component-architecture)
5. [Data Flow & Processing Pipeline](#data-flow--processing-pipeline)
6. [API Design](#api-design)
7. [Database Schema](#database-schema)
8. [Technology Stack](#technology-stack)
9. [Deployment Strategy](#deployment-strategy)
10. [Scalability & Performance](#scalability--performance)
11. [Security & Compliance](#security--compliance)
12. [Monitoring & Observability](#monitoring--observability)

---

## Executive Summary

### System Purpose

SRYZ is a comprehensive AI-powered platform for music creation through advanced prompt engineering. The system analyzes audio and lyrical content to generate optimized prompts for AI music generation platforms (Suno AI, Udio), with special support for Polish language content.

### Core Value Propositions

- **Lyric Analysis:** Multi-dimensional emotional, rhythmic, and structural analysis
- **Prompt Generation:** CO-STAR based prompts optimized for AI music platforms
- **Quality Evaluation:** 6-dimensional prompt quality scoring
- **Cross-Lingual Support:** Polish ↔ English adaptation with cultural preservation
- **Real-time Processing:** Sub-second analysis and generation
- **Platform Integration:** Direct API integration with Suno AI and Udio

### Key Differentiators

1. **Academic Foundation:** 30+ research sources, CO-STAR/CREATE/CRAFT frameworks
2. **Polish Language Excellence:** PLLuM integration, cultural context awareness
3. **Production-Ready Prototypes:** 5 fully implemented Python prototypes
4. **Multi-Modal Architecture:** Audio + Lyrics + Metadata synthesis
5. **Iterative Refinement:** A/B testing, quality metrics, adaptive learning

---

## System Overview

### System Boundaries

**IN SCOPE:**
- Audio analysis (BPM, key, emotion, tempo)
- Lyrical analysis (emotion, rhyme schemes, genre classification)
- Prompt generation and optimization
- Quality scoring and evaluation
- Cross-lingual adaptation (Polish ↔ English)
- API integrations (Suno AI, Udio)
- Web interface for interactive use
- CLI for automation
- Python library for developers

**OUT OF SCOPE:**
- Music production/mixing/mastering
- Audio editing capabilities
- Music distribution
- Social features
- Payment processing (future)

### User Personas

1. **Music Creators:** Artists seeking AI-generated music for lyrics
2. **Prompt Engineers:** Users optimizing prompts for AI music platforms
3. **Developers:** Integrating SRYZ capabilities into their applications
4. **Researchers:** Studying prompt engineering for music generation

---

## High-Level Architecture

### Architecture Diagram (Text-Based)

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                           SRYZ SYSTEM ARCHITECTURE                          │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│  ┌────────────────┐      ┌────────────────┐      ┌────────────────┐        │
│  │  CLIENT LAYER  │      │  CLIENT LAYER  │      │  CLIENT LAYER  │        │
│  │                │      │  (CLI)         │      │  (Python SDK)  │        │
│  │  Web Interface │      │                │      │                │        │
│  │  (React/Vue)   │      │  CLI Tool      │      │  pip install   │        │
│  └────────┬───────┘      └────────┬───────┘      └────────┬───────┘        │
│           │                      │                      │                  │
│           └──────────────────────┼──────────────────────┘                  │
│                                  │                                         │
│                    ┌─────────────▼─────────────┐                           │
│                    │      API GATEWAY          │                           │
│                    │   (FastAPI / Kong)        │                           │
│                    │   - Rate Limiting         │                           │
│                    │   - AuthN/AuthZ          │                           │
│                    │   - Request Routing       │                           │
│                    └─────────────┬─────────────┘                           │
│                                  │                                         │
│           ┌──────────────────────┼──────────────────────┐                  │
│           │                      │                      │                  │
│  ┌────────▼────────┐    ┌───────▼────────┐    ┌───────▼────────┐         │
│  │  CORE SERVICE   │    │  BATCH SERVICE │    │  WEBHOOK SVC   │         │
│  │  (Real-time)    │    │  (Async Jobs)  │    │  (Callbacks)   │         │
│  └────────┬────────┘    └────────┬───────┘    └─────────────────┘         │
│           │                      │                                          │
│           └──────────────────────┼──────────────────┐                      │
│                                  │                  │                      │
│                    ┌─────────────▼─────────────┐   │                      │
│                    │    MESSAGE QUEUE          │   │                      │
│                    │   (Redis / RabbitMQ)      │   │                      │
│                    └─────────────┬─────────────┘   │                      │
│                                  │                  │                      │
│           ┌──────────────────────┼──────────────────┤                      │
│           │                      │                  │                      │
│  ┌────────▼────────┐    ┌───────▼────────┐   ┌───▼───────────┐          │
│  │  AUDIO ANALYSIS │    │  LYRIC ANALYSIS│   │  PROMPT       │          │
│  │  SERVICE        │    │  SERVICE       │   │  GENERATION   │          │
│  │                 │    │                │   │  SERVICE      │          │
│  │ - librosa       │    │ - VADER        │   │ - CO-STAR     │          │
│  │ - essentia      │    │ - spaCy        │   │ - Templates   │          │
│  │ - beat track    │    │ - NLTK         │   │ - LLMs        │          │
│  └────────┬────────┘    └────────┬───────┘   └───┬───────────┘          │
│           │                      │                │                      │
│           └──────────────────────┼────────────────┘                      │
│                                  │                                         │
│                    ┌─────────────▼─────────────┐                           │
│                    │    QUALITY SCORING        │                           │
│                    │    SERVICE                │                           │
│                    │ - 6-Dimension Evaluator   │                           │
│                    │ - Improvement Suggestions│                           │
│                    └─────────────┬─────────────┘                           │
│                                  │                                         │
│                    ┌─────────────▼─────────────┐                           │
│                    │    CROSS-LINGUAL          │                           │
│                    │    ADAPTER SERVICE        │                           │
│                    │ - PLLuM (Polish)          │                           │
│                    │ - Cultural Context        │                           │
│                    │ - Rhyme Preservation      │                           │
│                    └─────────────┬─────────────┘                           │
│                                  │                                         │
│           ┌──────────────────────┼──────────────────────┐                  │
│           │                      │                      │                  │
│  ┌────────▼────────┐    ┌───────▼────────┐    ┌───────▼────────┐         │
│  │  SUNO AI        │    │   UDIO API     │    │  DATABASE      │         │
│  │  INTEGRATION    │    │   INTEGRATION  │    │  (PostgreSQL)  │         │
│  └─────────────────┘    └────────────────┘    └────────────────┘         │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘

                    EXTERNAL SERVICES
┌─────────────────────────────────────────────────────────────────────────────┐
│                                                                             │
│  ┌──────────────┐   ┌──────────────┐   ┌──────────────┐   ┌────────────┐ │
│  │  ElevenLabs  │   │   LALAL.AI   │   │    PLLuM     │   │  Music.AI  │ │
│  │  (Optional)  │   │  (Optional)  │   │  (Polish)    │   │ (Optional) │ │
│  └──────────────┘   └──────────────┘   └──────────────┘   └────────────┘ │
│                                                                             │
│  Transcription      Advanced Transcription   Polish LLM      High-Quality  │
│  Services           Vocal Isolation          Optimization    Transcription │
└─────────────────────────────────────────────────────────────────────────────┘
```

### Architecture Layers

#### 1. Presentation Layer
- **Web Interface:** React/Vue.js SPA with real-time updates
- **CLI Tool:** Python-based command-line interface
- **Python SDK:** Library for developers (`pip install sryz`)

#### 2. API Gateway Layer
- **Authentication:** JWT-based API keys
- **Rate Limiting:** Per-user and per-endpoint limits
- **Request Routing:** Load balancing across services
- **API Versioning:** Versioned endpoints for backward compatibility

#### 3. Application Layer
- **Core Service:** Real-time processing (sync)
- **Batch Service:** Async job processing
- **Webhook Service:** Callback notifications

#### 4. Processing Layer
- **Audio Analysis Service:** BPM, key, emotion extraction
- **Lyric Analysis Service:** Sentiment, rhyme, genre classification
- **Prompt Generation Service:** CO-STAR template engine
- **Quality Scoring Service:** 6-dimensional evaluation
- **Cross-Lingual Adapter:** Polish ↔ English translation

#### 5. Integration Layer
- **Suno AI API:** Primary music generation platform
- **Udio API:** Secondary platform for A/B testing
- **Polish LLM (PLLuM):** Polish language optimization

#### 6. Data Layer
- **PostgreSQL:** Primary data store
- **Redis:** Caching and message queue
- **S3/MinIO:** Audio file storage

---

## Component Architecture

### Component 1: Audio Analysis Service

**Purpose:** Extract audio features for prompt generation

**Technology Stack:**
- Python 3.11+
- librosa (audio processing)
- essentia (advanced audio features)
- numpy (numerical computing)

**Key Modules:**

```python
# /src/services/audio_analysis/
├── __init__.py
├── bpm_detector.py        # BPM detection using librosa
├── key_detector.py        # Musical key extraction
├── emotion_extractor.py   # Valence-arousal emotion
├── tempo_analyzer.py      # Tempo changes, rubato detection
├── timbre_analyzer.py     # Instrument classification
└── dynamics_analyzer.py   # Volume, compression analysis
```

**API Interface:**

```python
class AudioAnalyzer:
    async def analyze_audio(
        self,
        audio_file: UploadFile,
        features: List[str] = ["bpm", "key", "emotion"]
    ) -> AudioAnalysisResult:
        """
        Analyze audio file for specified features

        Args:
            audio_file: Uploaded audio file (m4a, mp3, wav)
            features: List of features to extract

        Returns:
            AudioAnalysisResult with:
                - bpm: float (beats per minute)
                - key: str (musical key, e.g., "C# minor")
                - valence: float (-1.0 to 1.0)
                - arousal: float (0.0 to 1.0)
                - beat_times: List[float] (timestamps)
                - confidence: float (0.0 to 1.0)
        """
        pass
```

**Performance Targets:**
- Processing time: <500ms for 30-second audio
- Memory usage: <200MB per concurrent analysis
- Max file size: 50MB

**Error Handling:**
- Unsupported format: 415 Unsupported Media Type
- Corrupted audio: 400 Bad Request
- Processing timeout: 504 Gateway Timeout

---

### Component 2: Lyric Analysis Service

**Purpose:** Analyze lyrical content for emotion, structure, and style

**Technology Stack:**
- Python 3.11+
- NLTK (VADER sentiment)
- spaCy (Polish language support)
- pronouncing (CMU pronunciation dict)
- scikit-learn (genre classification)

**Key Modules:**

```python
# /src/services/lyric_analysis/
├── __init__.py
├── emotion_analyzer.py       # Multi-dimensional emotion tracking
├── rhyme_detector.py         # Rhyme scheme extraction
├── genre_classifier.py       # Genre classification (12 genres)
├── sentiment_analyzer.py     # VADER sentiment analysis
├── structure_parser.py       # Verse/chorus detection
└── polish_nlp.py             # Polish language optimization
```

**API Interface:**

```python
class LyricAnalyzer:
    async def analyze_lyrics(
        self,
        lyrics: str,
        language: str = "en",
        features: List[str] = [
            "emotion_arc",
            "rhyme_scheme",
            "genre",
            "sentiment"
        ]
    ) -> LyricAnalysisResult:
        """
        Analyze lyrics for multiple features

        Args:
            lyrics: Lyric text (can include section markers)
            language: "en" or "pl"
            features: List of analyses to perform

        Returns:
            LyricAnalysisResult with:
                - emotion_arc: List[EmotionalPoint]
                - rhyme_scheme: str (e.g., "AABB")
                - genre_predictions: List[GenrePrediction]
                - sentiment: SentimentScores
                - structure: SongStructure
        """
        pass
```

**Language Support:**
- **English:** Full feature support
- **Polish:** Full feature support with PLLuM integration
- **Other:** Basic sentiment only

---

### Component 3: Prompt Generation Service

**Purpose:** Generate optimized prompts using CO-STAR framework

**Technology Stack:**
- Python 3.11+
- Jinja2 (template engine)
- OpenAI API (optional, for enhancement)
- LangChain (prompt composition)

**Key Modules:**

```python
# /src/services/prompt_generation/
├── __init__.py
├── costar_builder.py       # CO-STAR framework implementation
├── template_engine.py      # Jinja2-based templates
├── enhancer.py             # LLM-based prompt enhancement
├── validators.py           # Prompt validation rules
└── formatters.py           # Platform-specific formatting
```

**CO-STAR Framework:**

```python
@dataclass
class CostarPrompt:
    """CO-STAR Framework Prompt Structure"""

    # C - Context
    context: str  # Background, setting, genre, era

    # O - Objective
    objective: str  # What the AI should accomplish

    # S - Style
    style: str  # Musical style, instrumentation, tempo

    # T - Tone
    tone: str  # Emotional tone, mood, atmosphere

    # A - Audience
    audience: str  # Target audience, use case

    # R - Response Format
    response_format: str  # Expected output structure

    def to_prompt(self, platform: str = "suno") -> str:
        """Convert to platform-specific prompt"""
        pass
```

**API Interface:**

```python
class PromptGenerator:
    async def generate_prompt(
        self,
        audio_analysis: AudioAnalysisResult,
        lyric_analysis: LyricAnalysisResult,
        user_preferences: UserPreferences,
        platform: str = "suno"
    ) -> GeneratedPrompt:
        """
        Generate optimized prompt from analysis results

        Args:
            audio_analysis: Audio feature extraction results
            lyric_analysis: Lyric analysis results
            user_preferences: User-specified constraints
            platform: "suno" or "udio"

        Returns:
            GeneratedPrompt with:
                - prompt: str (final prompt text)
                - confidence: float (quality prediction)
                - suggestions: List[str] (improvement ideas)
                - metadata: Dict (generation metadata)
        """
        pass
```

---

### Component 4: Quality Scoring Service

**Purpose:** Evaluate prompt quality across 6 dimensions

**Dimensions:**
1. **Specificity (25%):** Concrete details vs vague language
2. **Structure (20%):** Logical organization
3. **Creativity (15%):** Novel and imaginative content
4. **Constraints (15%):** Clear boundaries and requirements
5. **Context (15%):** Background information richness
6. **Clarity (10%):** Action-verb density and directness

**Technology Stack:**
- Python 3.11+
- spaCy (NLP analysis)
- Custom scoring algorithms
- Machine learning models (optional)

**Key Modules:**

```python
# /src/services/quality_scoring/
├── __init__.py
├── specificity_scorer.py    # Concrete detail detection
├── structure_scorer.py      # Organization analysis
├── creativity_scorer.py     # Novelty measurement
├── constraint_scorer.py     # Boundary clarity
├── context_scorer.py        # Background richness
├── clarity_scorer.py        # Directness measurement
└── aggregator.py            # Weighted score calculation
```

**API Interface:**

```python
class QualityScorer:
    async def evaluate_prompt(
        self,
        prompt: str,
        platform: str = "suno"
    ) -> QualityEvaluation:
        """
        Evaluate prompt quality

        Args:
            prompt: Prompt text to evaluate
            platform: Target platform (affects scoring)

        Returns:
            QualityEvaluation with:
                - overall_score: float (0.0 to 1.0)
                - grade: str ("A" to "F")
                - dimension_scores: List[DimensionScore]
                - strengths: List[str]
                - weaknesses: List[str]
                - improvement_priority: List[str]
                - suggestions: List[str]
        """
        pass
```

---

### Component 5: Cross-Lingual Adapter Service

**Purpose:** Polish ↔ English adaptation with cultural preservation

**Technology Stack:**
- Python 3.11+
- deep-translator (Google Translate API)
- PLLuM (Polish LLM integration)
- Custom cultural mappings

**Key Modules:**

```python
# /src/services/cross_lingual/
├── __init__.py
├── translator.py           # Translation engine
├── cultural_adapter.py     # Cultural reference mapping
├── rhythm_preserver.py     # Meter and flow preservation
├── rhyme_optimizer.py      # Cross-lingual rhyme matching
├── pllum_client.py         # PLLuM API integration
└── validators.py           # Translation quality checks
```

**Cultural Mappings:**

```python
POLISH_CULTURAL_REFERENCES = {
    "żal": "melancholic longing (untranslatable)",
    "tęsknota": "nostalgic yearning",
    "Solidarność": "Solidarity movement (historical)",
    "Wisła": "Vistula River (national symbol)"
}

ENGLISH_CULTURAL_REFERENCES = {
    "American Dream": "spełnienie amerykańskie",
    "road trip": "podróż",
    "summer love": "letnia miłość"
}
```

**API Interface:**

```python
class CrossLingualAdapter:
    async def translate_lyrics(
        self,
        lyrics: str,
        source_lang: str,
        target_lang: str,
        preserve_rhyme: bool = True,
        genre: Optional[str] = None
    ) -> TranslationResult:
        """
        Translate lyrics with structure preservation

        Args:
            lyrics: Source lyric text
            source_lang: "pl" or "en"
            target_lang: "pl" or "en"
            preserve_rhyme: Attempt to maintain rhyme scheme
            genre: Musical genre (for terminology adaptation)

        Returns:
            TranslationResult with:
                - text: str (translated lyrics)
                - confidence: float (quality score)
                - cultural_notes: List[str] (adaptations made)
                - rhythm_preserved: bool
                - rhyme_preserved: bool
                - back_translation: str (validation)
        """
        pass

    async def adapt_prompt(
        self,
        prompt: str,
        source_lang: str,
        target_lang: str
    ) -> TranslationResult:
        """Translate prompt with structure preservation"""
        pass
```

---

### Component 6: Platform Integration Layer

**Purpose:** API clients for Suno AI and Udio

**Technology Stack:**
- Python 3.11+
- httpx (async HTTP client)
- tenacity (retry logic)
- pydantic (response validation)

**Architecture:**

```python
# /src/integrations/
├── __init__.py
├── base_client.py          # Abstract base class
├── suno_client.py          # Suno AI API client
├── udio_client.py          # Udio API client
├── rate_limiter.py         # Rate limiting middleware
└── response_parser.py      # Response normalization
```

**Unified Interface:**

```python
class MusicPlatformClient(ABC):
    """Abstract base for music platform APIs"""

    @abstractmethod
    async def generate_song(
        self,
        prompt: str,
        duration: int = 120,
        genre: Optional[str] = None
    ) -> SongGenerationResult:
        """Generate song from prompt"""
        pass

    @abstractmethod
    async def get_generation_status(
        self,
        generation_id: str
    ) -> GenerationStatus:
        """Check generation progress"""
        pass

    @abstractmethod
    async def download_song(
        self,
        generation_id: str
    ) -> bytes:
        """Download generated audio"""
        pass

class SunoAIClient(MusicPlatformClient):
    """Suno AI API implementation"""
    pass

class UdioClient(MusicPlatformClient):
    """Udio API implementation"""
    pass
```

---

### Component 7: Web Interface

**Purpose:** Interactive web application for end users

**Technology Stack:**
- React 18 / Vue 3 (frontend framework)
- TypeScript (type safety)
- Tailwind CSS / Material-UI (UI components)
- Three.js (3D emotion visualization)
- D3.js (data visualization)
- Socket.IO (real-time updates)
- Redux / Pinia (state management)

**Key Views:**

```javascript
// /src/web/src/views/
├── Dashboard.tsx           # Main dashboard
├── AudioUpload.tsx         # Audio file upload
├── LyricEditor.tsx         # Lyric input editor
├── EmotionMapper.tsx       # 2D/3D emotion mapping
├── PromptEditor.tsx        # CO-STAR prompt builder
├── QualityMetrics.tsx      # Quality scoring display
├── ResultsViewer.tsx       # Generated audio preview
├── A_B_Testing.tsx         # Side-by-side comparison
└── Settings.tsx            # User preferences
```

**State Management:**

```typescript
interface AppState {
  // Audio analysis state
  audio: {
    file: File | null
    analysis: AudioAnalysisResult | null
    processing: boolean
    error: string | null
  }

  // Lyric analysis state
  lyrics: {
    text: string
    analysis: LyricAnalysisResult | null
    language: 'en' | 'pl'
  }

  // Prompt generation state
  prompt: {
    costar: Partial<CostarPrompt>
    generated: string
    quality: QualityEvaluation | null
  }

  // Platform integration state
  platform: {
    selected: 'suno' | 'udio'
    generating: boolean
    results: SongGenerationResult[]
  }
}
```

---

## Data Flow & Processing Pipeline

### Pipeline 1: Audio-First Workflow

```
USER INPUT (Audio File)
    ↓
┌─────────────────────────────────────────┐
│ 1. UPLOAD & VALIDATION                  │
│    - Check file format (m4a, mp3, wav)  │
│    - Size limit: 50MB                   │
│    - Duration: 10 sec - 10 min          │
└──────────────┬──────────────────────────┘
               ↓
┌─────────────────────────────────────────┐
│ 2. AUDIO ANALYSIS (Async)               │
│    BPM Detection → Key Extraction →     │
│    Emotion Analysis → Tempo Tracking    │
│                                         │
│    Processing Time: <500ms              │
└──────────────┬──────────────────────────┘
               ↓
┌─────────────────────────────────────────┐
│ 3. LYRIC EXTRAPTION (Optional)          │
│    - ElevenLabs API (Free)              │
│    - LALAL.AI (Premium)                 │
│    - Polish Language Support            │
└──────────────┬──────────────────────────┘
               ↓
┌─────────────────────────────────────────┐
│ 4. LYRIC ANALYSIS (Async)               │
│    Sentiment → Rhyme Scheme → Genre →   │
│    Emotion Arc                          │
│                                         │
│    Processing Time: <300ms              │
└──────────────┬──────────────────────────┘
               ↓
┌─────────────────────────────────────────┐
│ 5. DATA FUSION                          │
│    Combine Audio + Lyric Features       │
│    - Weighted emotion averaging         │
│    - Cross-modal validation             │
└──────────────┬──────────────────────────┘
               ↓
┌─────────────────────────────────────────┐
│ 6. PROMPT GENERATION                    │
│    CO-STAR Template → Platform Format   │
│    - Suno AI: 200 char limit            │
│    - Udio: 300 char limit               │
│                                         │
│    Generation Time: <200ms              │
└──────────────┬──────────────────────────┘
               ↓
┌─────────────────────────────────────────┐
│ 7. QUALITY SCORING                      │
│    6-Dimension Evaluation → Grade →     │
│    Improvement Suggestions              │
└──────────────┬──────────────────────────┘
               ↓
┌─────────────────────────────────────────┐
│ 8. USER PREVIEW & REFINEMENT            │
│    - Edit generated prompt              │
│    - A/B test platforms                 │
│    - Save iterations                    │
└──────────────┬──────────────────────────┘
               ↓
┌─────────────────────────────────────────┐
│ 9. MUSIC GENERATION (Async)             │
│    Send to Suno AI / Udio               │
│    - Poll for completion                │
│    - Download result                    │
│                                         │
│    Generation Time: 1-5 min             │
└──────────────┬──────────────────────────┘
               ↓
USER OUTPUT (Generated Audio + Metadata)
```

### Pipeline 2: Lyric-First Workflow

```
USER INPUT (Lyric Text)
    ↓
┌─────────────────────────────────────────┐
│ 1. LYRIC INPUT                          │
│    - Text area / File upload            │
│    - Language detection (auto)          │
│    - Section marker parsing             │
└──────────────┬──────────────────────────┘
               ↓
┌─────────────────────────────────────────┐
│ 2. LYRIC ANALYSIS                       │
│    Emotion Arc → Rhyme → Genre →        │
│    Structure → Sentiment                │
└──────────────┬──────────────────────────┘
               ↓
┌─────────────────────────────────────────┐
│ 3. CROSS-LINGUAL (Optional)             │
│    Polish → English or vice versa       │
│    - Cultural adaptation                │
│    - Rhyme preservation                 │
└──────────────┬──────────────────────────┘
               ↓
┌─────────────────────────────────────────┐
│ 4. MUSICAL PARAMETER INFERENCE          │
│    - Estimate BPM from rhythm           │
│    - Infer key from mood                │
│    - Suggest tempo from emotion         │
└──────────────┬──────────────────────────┘
               ↓
┌─────────────────────────────────────────┐
│ 5. PROMPT GENERATION                    │
│    CO-STAR Template → Platform Format   │
└──────────────┬──────────────────────────┘
               ↓
[Continue from Step 7 in Pipeline 1]
```

### Pipeline 3: Batch Processing Workflow

```
USER INPUT (Multiple Files)
    ↓
┌─────────────────────────────────────────┐
│ 1. BATCH UPLOAD                         │
│    - Drag & drop multiple files         │
│    - CSV/JSON import (metadata)         │
│    - Queue management                   │
└──────────────┬──────────────────────────┘
               ↓
┌─────────────────────────────────────────┐
│ 2. JOB QUEUE                            │
│    Redis Queue → Celery Workers         │
│    - Priority scheduling                │
│    - Concurrent processing              │
│    - Progress tracking                  │
└──────────────┬──────────────────────────┘
               ↓
┌─────────────────────────────────────────┐
│ 3. PARALLEL PROCESSING                  │
│    ┌─────────┐  ┌─────────┐  ┌─────────┐│
│    │ File 1  │  │ File 2  │  │ File 3  ││
│    │ 500ms   │  │ 500ms   │  │ 500ms   ││
│    └────┬────┘  └────┬────┘  └────┬────┘│
│         └────────────┼────────────┘     │
│                      ↓                  │
│              [Aggregate Results]        │
└──────────────┬──────────────────────────┘
               ↓
┌─────────────────────────────────────────┐
│ 4. BATCH GENERATION                     │
│    Rate-limited API calls               │
│    - Suno: 5 req/min                    │
│    - Udio: 10 req/min                   │
└──────────────┬──────────────────────────┘
               ↓
USER OUTPUT (ZIP with all results + CSV report)
```

---

## API Design

### REST API Endpoints

#### Authentication

```http
POST /api/v1/auth/register
POST /api/v1/auth/login
POST /api/v1/auth/refresh
POST /api/v1/auth/logout

Response:
{
  "access_token": "jwt_token",
  "refresh_token": "refresh_token",
  "expires_in": 3600
}
```

#### Audio Analysis

```http
POST /api/v1/audio/analyze
Content-Type: multipart/form-data

Request:
{
  "audio_file": <binary>,
  "features": ["bpm", "key", "emotion"],
  "callback_url": "https://example.com/webhook"
}

Response (202 Accepted):
{
  "job_id": "uuid",
  "status": "processing",
  "estimated_time": 0.5
}

GET /api/v1/audio/analyze/{job_id}

Response (200 OK):
{
  "job_id": "uuid",
  "status": "completed",
  "result": {
    "bpm": 120.5,
    "key": "C# minor",
    "valence": 0.65,
    "arousal": 0.78,
    "confidence": 0.92
  }
}
```

#### Lyric Analysis

```http
POST /api/v1/lyrics/analyze
Content-Type: application/json

Request:
{
  "lyrics": "[Verse 1]\nWalking through...",
  "language": "en",
  "features": ["emotion_arc", "rhyme_scheme", "genre"]
}

Response (200 OK):
{
  "emotion_arc": [
    {
      "position": 0.0,
      "valence": -0.2,
      "arousal": 0.5,
      "section": "verse"
    }
  ],
  "rhyme_scheme": "AABB",
  "genre_predictions": [
    {"genre": "pop", "confidence": 0.75}
  ],
  "sentiment": {
    "compound": 0.65,
    "positive": 0.8,
    "negative": 0.1
  }
}
```

#### Prompt Generation

```http
POST /api/v1/prompts/generate
Content-Type: application/json

Request:
{
  "audio_analysis": { ... },
  "lyric_analysis": { ... },
  "user_preferences": {
    "genre": "pop",
    "tempo": 120,
    "mood": "uplifting"
  },
  "platform": "suno"
}

Response (200 OK):
{
  "prompt": "An uplifting pop song...",
  "confidence": 0.87,
  "costar_breakdown": {
    "context": "...",
    "objective": "...",
    "style": "...",
    "tone": "...",
    "audience": "...",
    "response_format": "..."
  },
  "suggestions": [
    "Add more specific instrumentation details"
  ]
}
```

#### Quality Scoring

```http
POST /api/v1/prompts/evaluate
Content-Type: application/json

Request:
{
  "prompt": "An uplifting pop song...",
  "platform": "suno"
}

Response (200 OK):
{
  "overall_score": 0.82,
  "grade": "B",
  "dimension_scores": [
    {
      "dimension": "specificity",
      "score": 0.75,
      "details": "Moderate specificity...",
      "suggestions": ["Add numbers..."]
    }
  ],
  "strengths": ["structure", "clarity"],
  "weaknesses": ["specificity", "creativity"],
  "improvement_priority": ["specificity", "creativity"]
}
```

#### Cross-Lingual Translation

```http
POST /api/v1/translation/lyrics
Content-Type: application/json

Request:
{
  "lyrics": "W nocnej ciszy słychać...",
  "source_lang": "pl",
  "target_lang": "en",
  "preserve_rhyme": true,
  "genre": "pop"
}

Response (200 OK):
{
  "text": "In the night silence, I hear...",
  "confidence": 0.91,
  "cultural_notes": [
    "Adapted 'nocnej ciszy' → 'night silence'"
  ],
  "rhythm_preserved": true,
  "rhyme_preserved": false,
  "back_translation": "W nocnej ciszy..."
}
```

#### Music Generation

```http
POST /api/v1/generation/suno
Content-Type: application/json

Request:
{
  "prompt": "An uplifting pop song...",
  "duration": 120,
  "genre": "pop",
  "webhook_url": "https://example.com/callback"
}

Response (202 Accepted):
{
  "generation_id": "uuid",
  "status": "queued",
  "estimated_time": 180
}

GET /api/v1/generation/status/{generation_id}

Response (200 OK):
{
  "generation_id": "uuid",
  "status": "completed",
  "progress": 100,
  "result": {
    "audio_url": "https://...",
    "duration": 118,
    "format": "mp3"
  }
}
```

### WebSocket API (Real-time Updates)

```javascript
// Connect to WebSocket
const ws = new WebSocket('wss://api.sryz.ai/v1/ws');

// Subscribe to job updates
ws.send(JSON.stringify({
  action: 'subscribe',
  job_id: 'uuid'
}));

// Receive real-time updates
ws.onmessage = (event) => {
  const data = JSON.parse(event.data);

  switch(data.type) {
    case 'job.started':
      console.log('Processing started');
      break;
    case 'job.progress':
      console.log(`Progress: ${data.progress}%`);
      break;
    case 'job.completed':
      console.log('Result:', data.result);
      break;
    case 'job.failed':
      console.error('Error:', data.error);
      break;
  }
};
```

---

## Database Schema

### PostgreSQL Schema

```sql
-- Users
CREATE TABLE users (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    email VARCHAR(255) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    api_key VARCHAR(64) UNIQUE NOT NULL,
    tier VARCHAR(20) NOT NULL DEFAULT 'free', -- free, pro, enterprise
    created_at TIMESTAMP DEFAULT NOW(),
    last_active TIMESTAMP,
    INDEX idx_email (email),
    INDEX idx_api_key (api_key)
);

-- Audio Analysis Jobs
CREATE TABLE audio_analysis_jobs (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id UUID REFERENCES users(id),
    audio_file_key VARCHAR(255) NOT NULL, -- S3/MinIO key
    status VARCHAR(20) NOT NULL, -- queued, processing, completed, failed
    features JSONB NOT NULL, -- ["bpm", "key", "emotion"]
    result JSONB, -- Analysis results
    error_message TEXT,
    processing_time_ms INTEGER,
    created_at TIMESTAMP DEFAULT NOW(),
    completed_at TIMESTAMP,
    INDEX idx_user_id (user_id),
    INDEX idx_status (status),
    INDEX idx_created_at (created_at)
);

-- Lyric Analysis Jobs
CREATE TABLE lyric_analysis_jobs (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id UUID REFERENCES users(id),
    lyrics_text TEXT NOT NULL,
    language VARCHAR(5) NOT NULL, -- en, pl
    status VARCHAR(20) NOT NULL,
    features JSONB NOT NULL,
    result JSONB,
    error_message TEXT,
    processing_time_ms INTEGER,
    created_at TIMESTAMP DEFAULT NOW(),
    completed_at TIMESTAMP,
    INDEX idx_user_id (user_id),
    INDEX idx_language (language)
);

-- Prompt Generations
CREATE TABLE prompt_generations (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id UUID REFERENCES users(id),
    audio_analysis_id UUID REFERENCES audio_analysis_jobs(id),
    lyric_analysis_id UUID REFERENCES lyric_analysis_jobs(id),
    costar_data JSONB NOT NULL,
    generated_prompt TEXT NOT NULL,
    platform VARCHAR(20) NOT NULL, -- suno, udio
    quality_score JSONB,
    created_at TIMESTAMP DEFAULT NOW(),
    INDEX idx_user_id (user_id),
    INDEX idx_created_at (created_at)
);

-- Music Generations
CREATE TABLE music_generations (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id UUID REFERENCES users(id),
    prompt_generation_id UUID REFERENCES prompt_generations(id),
    platform VARCHAR(20) NOT NULL,
    platform_generation_id VARCHAR(255),
    status VARCHAR(20) NOT NULL, -- queued, processing, completed, failed
    audio_file_key VARCHAR(255),
    metadata JSONB,
    error_message TEXT,
    created_at TIMESTAMP DEFAULT NOW(),
    completed_at TIMESTAMP,
    INDEX idx_user_id (user_id),
    INDEX idx_status (status),
    INDEX idx_platform_generation_id (platform_generation_id)
);

-- User Sessions (for web interface)
CREATE TABLE user_sessions (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id UUID REFERENCES users(id),
    session_data JSONB NOT NULL,
    created_at TIMESTAMP DEFAULT NOW(),
    updated_at TIMESTAMP DEFAULT NOW(),
    expires_at TIMESTAMP NOT NULL,
    INDEX idx_user_id (user_id),
    INDEX idx_expires_at (expires_at)
);

-- API Usage Logs
CREATE TABLE api_usage_logs (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id UUID REFERENCES users(id),
    endpoint VARCHAR(255) NOT NULL,
    method VARCHAR(10) NOT NULL,
    status_code INTEGER NOT NULL,
    response_time_ms INTEGER NOT NULL,
    timestamp TIMESTAMP DEFAULT NOW(),
    INDEX idx_user_id (user_id),
    INDEX idx_timestamp (timestamp)
);

-- Rate Limiting
CREATE TABLE rate_limits (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id UUID REFERENCES users(id),
    endpoint VARCHAR(255) NOT NULL,
    request_count INTEGER NOT NULL DEFAULT 1,
    window_start TIMESTAMP NOT NULL,
    window_end TIMESTAMP NOT NULL,
    UNIQUE (user_id, endpoint, window_start),
    INDEX idx_user_endpoint (user_id, endpoint)
);
```

### Redis Data Structures

```python
# Cache: Audio analysis results
# Key: audio_analysis:{job_id}
# TTL: 3600 seconds (1 hour)
{
    "bpm": 120.5,
    "key": "C# minor",
    "valence": 0.65,
    "arousal": 0.78,
    "confidence": 0.92
}

# Cache: Lyric analysis results
# Key: lyric_analysis:{job_id}
# TTL: 3600 seconds
{
    "emotion_arc": [...],
    "rhyme_scheme": "AABB",
    "genre_predictions": [...]
}

# Queue: Async jobs
# Key: queue:audio_analysis
# Type: List
LPUSH queue:audio_analysis json.dumps({
    "job_id": "uuid",
    "user_id": "uuid",
    "audio_file_key": "..."
})

# Rate limiting
# Key: rate_limit:{user_id}:{endpoint}
# TTL: 60 seconds
INCR rate_limit:user123:api/v1/generate
EXPIRE rate_limit:user123:api/v1/generate 60

# Session storage
# Key: session:{session_id}
# TTL: 86400 seconds (24 hours)
{
    "user_id": "uuid",
    "data": {...},
    "last_activity": "2025-12-26T12:00:00Z"
}

# Real-time job status
# Key: job_status:{job_id}
# Type: Pub/Sub
PUBLISH job_status:{job_id} json.dumps({
    "status": "processing",
    "progress": 45
})
```

---

## Technology Stack

### Backend

| Component | Technology | Version | Purpose |
|-----------|-----------|---------|---------|
| **Language** | Python | 3.11+ | Primary backend language |
| **Framework** | FastAPI | 0.104+ | High-performance async API |
| **Task Queue** | Celery | 5.3+ | Distributed job processing |
| **Message Broker** | Redis | 7.2+ | Queue & cache |
| **Database** | PostgreSQL | 15+ | Primary data store |
| **ORM** | SQLAlchemy | 2.0+ | Database abstraction |
| **Audio Processing** | librosa | 0.10+ | Audio feature extraction |
| **Audio Processing** | essentia | 2.1b6+ | Advanced audio analysis |
| **NLP** | spaCy | 3.7+ | Polish language support |
| **NLP** | NLTK | 3.8.1+ | Sentiment analysis |
| **ML** | scikit-learn | 1.3+ | Genre classification |
| **HTTP Client** | httpx | 0.25+ | Async API calls |
| **API Docs** | Pydantic | 2.5+ | Request/response validation |
| **Testing** | pytest | 7.4+ | Unit & integration tests |

### Frontend

| Component | Technology | Version | Purpose |
|-----------|-----------|---------|---------|
| **Framework** | React | 18.2+ | UI framework |
| **Language** | TypeScript | 5.3+ | Type safety |
| **State Management** | Redux Toolkit | 2.0+ | Global state |
| **Routing** | React Router | 6.20+ | Client-side routing |
| **UI Components** | Material-UI | 5.14+ | Component library |
| **3D Graphics** | Three.js | 0.158+ | Emotion visualization |
| **Data Visualization** | D3.js | 7.8+ | Charts & graphs |
| **Audio Player** | Howler.js | 2.2.4 | Audio playback |
| **Waveform** | WaveSurfer.js | 7.4+ | Audio waveform display |
| **Real-time** | Socket.IO | 2.5+ | WebSocket client |
| **Forms** | React Hook Form | 7.48+ | Form management |
| **Build Tool** | Vite | 5.0+ | Fast dev server |

### Infrastructure

| Component | Technology | Version | Purpose |
|-----------|-----------|---------|---------|
| **Container** | Docker | 24+ | Containerization |
| **Orchestration** | Docker Compose | 2.20+ | Local development |
| **Reverse Proxy** | Nginx | 1.25+ | Load balancing |
| **API Gateway** | Kong | 3.4+ | API management (optional) |
| **Monitoring** | Prometheus | 2.47+ | Metrics collection |
| **Logging** | ELK Stack | 8.11+ | Log aggregation |
| **Tracing** | Jaeger | 1.50+ | Distributed tracing |
| **Object Storage** | MinIO | RELEASE.2023+ | S3-compatible storage |
| **CI/CD** | GitHub Actions | - | Automated deployment |

---

## Deployment Strategy

### Development Environment

```yaml
# docker-compose.dev.yml
version: '3.8'

services:
  postgres:
    image: postgres:15
    environment:
      POSTGRES_DB: sryz_dev
      POSTGRES_USER: sryz
      POSTGRES_PASSWORD: dev_password
    ports:
      - "5432:5432"
    volumes:
      - postgres_data:/var/lib/postgresql/data

  redis:
    image: redis:7.2-alpine
    ports:
      - "6379:6379"
    volumes:
      - redis_data:/data

  minio:
    image: minio/minio:latest
    command: server /data --console-address ":9001"
    ports:
      - "9000:9000"
      - "9001:9001"
    environment:
      MINIO_ROOT_USER: minioadmin
      MINIO_ROOT_PASSWORD: minioadmin
    volumes:
      - minio_data:/data

  backend:
    build:
      context: ./backend
      dockerfile: Dockerfile.dev
    volumes:
      - ./backend:/app
    ports:
      - "8000:8000"
    environment:
      - DATABASE_URL=postgresql://sryz:dev_password@postgres:5432/sryz_dev
      - REDIS_URL=redis://redis:6379/0
      - AWS_ACCESS_KEY_ID=minioadmin
      - AWS_SECRET_ACCESS_KEY=minioadmin
      - S3_ENDPOINT=http://minio:9000
    depends_on:
      - postgres
      - redis
      - minio

  frontend:
    build:
      context: ./frontend
      dockerfile: Dockerfile.dev
    volumes:
      - ./frontend:/app
      - /app/node_modules
    ports:
      - "5173:5173"
    environment:
      - VITE_API_URL=http://localhost:8000

  celery_worker:
    build:
      context: ./backend
      dockerfile: Dockerfile.dev
    command: celery -A app.tasks worker --loglevel=info
    volumes:
      - ./backend:/app
    environment:
      - DATABASE_URL=postgresql://sryz:dev_password@postgres:5432/sryz_dev
      - REDIS_URL=redis://redis:6379/0
    depends_on:
      - postgres
      - redis

volumes:
  postgres_data:
  redis_data:
  minio_data:
```

### Production Environment (AWS)

```yaml
# docker-compose.prod.yml (simplified)
version: '3.8'

services:
  backend:
    image: sryz/backend:latest
    deploy:
      replicas: 3
      resources:
        limits:
          cpus: '2'
          memory: 4G
    environment:
      - DATABASE_URL=${DATABASE_URL}
      - REDIS_URL=${REDIS_URL}
      - SENTRY_DSN=${SENTRY_DSN}
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost:8000/health"]
      interval: 30s
      timeout: 10s
      retries: 3

  celery_worker:
    image: sryz/backend:latest
    command: celery -A app.tasks worker --loglevel=info --concurrency=4
    deploy:
      replicas: 2
    environment:
      - DATABASE_URL=${DATABASE_URL}
      - REDIS_URL=${REDIS_URL}

  frontend:
    image: sryz/frontend:latest
    deploy:
      replicas: 2
    ports:
      - "80:80"
      - "443:443"
```

**AWS Infrastructure:**

- **ECS Fargate:** Container orchestration
- **RDS PostgreSQL:** Managed database
- **ElastiCache:** Managed Redis
- **S3:** Object storage (audio files)
- **CloudFront:** CDN for static assets
- **ALB:** Load balancing
- **Route53:** DNS management
- **Certificate Manager:** SSL/TLS certificates

---

## Scalability & Performance

### Performance Targets

| Metric | Target | Measurement |
|--------|--------|-------------|
| **API Response Time** | <200ms (p95) | API gateway to response |
| **Audio Analysis** | <500ms | 30-second audio segment |
| **Lyric Analysis** | <300ms | Typical verse |
| **Prompt Generation** | <200ms | CO-STAR template |
| **End-to-End Pipeline** | <1.5s | Upload to prompt ready |
| **Concurrent Users** | 10,000 | Active simultaneous users |
| **Requests/Second** | 1,000 | API throughput |
| **Uptime** | 99.9% | Monthly availability |

### Horizontal Scaling Strategy

**Stateless Services:**
- API Gateway: Auto-scale based on CPU/memory
- Backend Services: Auto-scale based on request queue
- Frontend: CDN-cached static assets

**Stateful Services:**
- PostgreSQL: Read replicas for read-heavy workloads
- Redis: Cluster mode for horizontal scaling
- S3: Unlimited horizontal scaling

**Vertical Scaling:**
- Celery workers: Increase concurrency based on queue depth
- Database: Increase instance size for write-heavy workloads

### Caching Strategy

**Multi-Level Caching:**

```
Level 1: Browser Cache (1 hour)
  └─ Static assets, API responses

Level 2: CDN Cache (24 hours)
  └─ Frontend bundles, audio files

Level 3: Redis Cache (1 hour)
  └─ API responses, analysis results

Level 4: Database Query Cache
  └─ Frequently accessed data
```

**Cache Invalidation:**
- Time-based: TTL expiration
- Event-based: Data updates trigger cache clears
- Tag-based: Grouped cache keys for bulk invalidation

### Load Balancing

**Application Load Balancer (ALB):**
- Round-robin routing
- Health checks every 30 seconds
- Sticky sessions for WebSocket connections

**Database Load Balancing:**
- Write leader: Single primary instance
- Read replicas: 2-3 replicas for read queries
- Connection pooling: PgBouncer for connection management

---

## Security & Compliance

### Authentication & Authorization

**JWT-based Authentication:**
- Access tokens: 1-hour expiration
- Refresh tokens: 30-day expiration
- API keys: Alternative for service accounts

**Role-Based Access Control (RBAC):**
```
Roles:
- user: Basic access
- pro: Extended limits
- admin: Full system access
- service: Machine-to-machine access

Permissions:
- read:analysis: View analysis results
- write:prompt: Generate prompts
- read:generation: Access generated music
- delete:account: Manage account
```

### API Security

**Rate Limiting:**
- Free tier: 100 requests/hour
- Pro tier: 1,000 requests/hour
- Enterprise: Custom limits

**Input Validation:**
- File size limits: 50MB max
- File type validation: MIME type checking
- Content sanitization: Remove malicious payloads

**Output Encoding:**
- JSON: Standard JSON encoding
- Audio: Base64 or S3 presigned URLs
- Text: UTF-8 encoding

### Data Protection

**Encryption:**
- In transit: TLS 1.3
- At rest: AES-256 encryption
- Database: Transparent Data Encryption (TDE)

**PII Protection:**
- Email hashing: SHA-256 for user identification
- IP logging: Last octet masked
- Audio anonymization: Optional voice stripping

### Compliance

**GDPR Compliance:**
- Right to access: User data export
- Right to deletion: Account data deletion
- Right to portability: Data format standardization

**SOC 2 Type II (Future):**
- Access logging
- Change management
- Incident response

---

## Monitoring & Observability

### Metrics Collection (Prometheus)

**Key Metrics:**

```python
# Request metrics
http_requests_total{endpoint, method, status}
http_request_duration_seconds{endpoint, method}

# Processing metrics
audio_analysis_duration_seconds{feature}
lyric_analysis_duration_seconds{feature}
prompt_generation_duration_seconds{platform}

# Business metrics
generations_total{platform, status}
user_sessions_active
api_usage_per_user{user_id, tier}

# Infrastructure metrics
cpu_usage_percent{service}
memory_usage_bytes{service}
disk_usage_percent{mount_point}
```

### Logging (ELK Stack)

**Log Levels:**
- DEBUG: Detailed diagnostic information
- INFO: General informational messages
- WARNING: Warning messages for potential issues
- ERROR: Error events that might still allow the application to continue
- CRITICAL: Critical events that require immediate attention

**Log Structure:**

```json
{
  "timestamp": "2025-12-26T12:00:00Z",
  "level": "INFO",
  "service": "audio-analysis",
  "user_id": "uuid",
  "request_id": "uuid",
  "message": "Audio analysis completed",
  "metadata": {
    "bpm": 120.5,
    "processing_time_ms": 450
  }
}
```

### Tracing (Jaeger)

**Distributed Tracing:**
- Trace ID: Unique identifier for entire request flow
- Span ID: Individual operation tracking
- Parent ID: Relationship between spans

**Trace Flow:**

```
[API Gateway] → [Backend] → [Audio Analysis] → [Lyric Analysis] → [Prompt Gen]
     ↓              ↓            ↓                 ↓                ↓
  Trace:        Span 1        Span 2            Span 3           Span 4
  abc123
```

### Alerting (PagerDuty)

**Alert Rules:**
- High error rate: >5% error rate over 5 minutes
- Slow response: p95 latency >1 second over 5 minutes
- Service down: Health check fails for 2 minutes
- Queue depth: Celery queue >1000 jobs

### Dashboards (Grafana)

**Dashboard Panels:**
1. System Health: CPU, memory, disk usage
2. API Performance: Request rate, latency, errors
3. Business Metrics: Generations, active users, revenue
4. Pipeline Performance: Analysis duration, queue depth

---

## Appendix

### A. Configuration Management

```yaml
# config.yaml
production:
  database:
    url: ${DATABASE_URL}
    pool_size: 20
    max_overflow: 10

  redis:
    url: ${REDIS_URL}
    max_connections: 50

  aws:
    access_key_id: ${AWS_ACCESS_KEY_ID}
    secret_access_key: ${AWS_SECRET_ACCESS_KEY}
    s3_bucket: sryz-audio-files

  api:
    suno:
      base_url: https://api.suno.ai
      api_key: ${SUNO_API_KEY}
      rate_limit: 5 # requests per minute

    udio:
      base_url: https://api.udio.com
      api_key: ${UDIO_API_KEY}
      rate_limit: 10

  features:
    audio_analysis: true
    lyric_analysis: true
    prompt_generation: true
    cross_lingual: true

  limits:
    max_audio_size_mb: 50
    max_audio_duration_seconds: 600
    max_lyric_length_chars: 10000
```

### B. Error Codes

| Code | Name | Description |
|------|------|-------------|
| 400 | Bad Request | Invalid input parameters |
| 401 | Unauthorized | Missing or invalid API key |
| 403 | Forbidden | Insufficient permissions |
| 404 | Not Found | Resource not found |
| 415 | Unsupported Media Type | Invalid file format |
| 429 | Too Many Requests | Rate limit exceeded |
| 500 | Internal Server Error | Server error |
| 503 | Service Unavailable | Service temporarily unavailable |

### C. API Response Examples

**Success Response:**

```json
{
  "success": true,
  "data": {
    "prompt": "An uplifting pop song...",
    "confidence": 0.87
  },
  "metadata": {
    "request_id": "uuid",
    "timestamp": "2025-12-26T12:00:00Z",
    "processing_time_ms": 250
  }
}
```

**Error Response:**

```json
{
  "success": false,
  "error": {
    "code": "INVALID_AUDIO_FORMAT",
    "message": "Unsupported audio format. Please upload m4a, mp3, or wav.",
    "details": {
      "provided_format": "flac",
      "supported_formats": ["m4a", "mp3", "wav"]
    }
  },
  "metadata": {
    "request_id": "uuid",
    "timestamp": "2025-12-26T12:00:00Z"
  }
}
```

---

## Document Metadata

**Author:** System Architecture Agent
**Version:** 1.0
**Date:** December 26, 2025
**Status:** Production Ready
**Review Cycle:** Quarterly

**Change Log:**
- v1.0 (2025-12-26): Initial comprehensive architecture

---

**END OF SYSTEM ARCHITECTURE DOCUMENT**

For questions or clarifications, refer to:
- Component Architecture Documents: `/docs/architecture/`
- API Documentation: `/docs/api/`
- Deployment Guides: `/docs/deployment/`
