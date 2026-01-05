#!/usr/bin/env python3
"""
COMPREHENSIVE DEMO OF ALL 5 PYTHON PROTOTYPES
=============================================

This script demonstrates all 5 innovative Python prototype patterns
for lyric analysis and prompt engineering.

Run with: python demo_all_prototypes.py
"""

import sys
from pathlib import Path

# Add prototypes directory to path
sys.path.insert(0, str(Path(__file__).parent / 'python_patterns'))

# Import all prototypes
# Note: Importing directly from files with numeric prefixes
import importlib

def load_module(name, path):
    """Load module from file path"""
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module

import importlib.util

# Load all prototype modules
emotional_arc_module = importlib.util.spec_from_file_location(
    "emotional_arc",
    "python_patterns/01_emotional_arc_analyzer.py"
)
emotional_arc = importlib.util.module_from_spec(emotional_arc_module)
emotional_arc_module.loader.exec_module(emotional_arc)

rhyme_scheme_module = importlib.util.spec_from_file_location(
    "rhyme_scheme",
    "python_patterns/02_rhyme_scheme_extractor.py"
)
rhyme_scheme = importlib.util.module_from_spec(rhyme_scheme_module)
rhyme_scheme_module.loader.exec_module(rhyme_scheme)

genre_classifier_module = importlib.util.spec_from_file_location(
    "genre_classifier",
    "python_patterns/03_genre_classifier.py"
)
genre_classifier = importlib.util.module_from_spec(genre_classifier_module)
genre_classifier_module.loader.exec_module(genre_classifier)

prompt_scorer_module = importlib.util.spec_from_file_location(
    "prompt_scorer",
    "python_patterns/04_prompt_quality_scorer.py"
)
prompt_scorer = importlib.util.module_from_spec(prompt_scorer_module)
prompt_scorer_module.loader.exec_module(prompt_scorer)

cross_lingual_module = importlib.util.spec_from_file_location(
    "cross_lingual",
    "python_patterns/05_cross_lingual_adapter.py"
)
cross_lingual = importlib.util.module_from_spec(cross_lingual_module)
cross_lingual_module.loader.exec_module(cross_lingual)

# Extract classes
EmotionalArcAnalyzer = emotional_arc.EmotionalArcAnalyzer
AdvancedRhymeAnalyzer = rhyme_scheme.AdvancedRhymeAnalyzer
EnsembleGenreClassifier = genre_classifier.EnsembleGenreClassifier
PromptQualityScorer = prompt_scorer.PromptQualityScorer
CrossLingualAdapter = cross_lingual.CrossLingualAdapter


def print_separator(title=""):
    """Print a formatted separator"""
    if title:
        print("\n" + "=" * 70)
        print(f"  {title}")
        print("=" * 70)
    else:
        print("=" * 70)


def demo_comprehensive_analysis():
    """Demonstrate all prototypes on a single song"""

    # Sample lyrics for comprehensive analysis
    sample_lyrics = """
    [Verse 1]
    Walking through these empty streets tonight
    Feeling like I've lost my way
    Every corner holds a memory tight
    Of the love we had yesterday

    [Chorus]
    But I'll rise up, touch the sky!
    Never gonna say goodbye!
    You're the reason I'm alive!
    This is how we survive!

    [Verse 2]
    Shadows dancing on the wall
    Whispers echo in the dark
    I can hear the destiny call
    Leaving its permanent mark

    [Bridge]
    Even if I fall, I'll stand again!
    Through the fire and the rain!

    [Chorus]
    But I'll rise up, touch the sky!
    Never gonna say goodbye!
    """

    sample_prompt = """
    Write a song about overcoming adversity and finding inner strength.

    Requirements:
    - Use an uplifting, anthemic tone
    - Include specific imagery (streets, sky, fire)
    - Maintain a verse-chorus structure
    - Rhyme scheme: AABB or ABAB
    - Length: 150-200 words

    Context:
    This is for a pop-rock audience, ages 18-35
    who enjoy motivational themes.
    """

    polish_lyrics = """
    [Verse 1]
    W nocnej ciszy słyszę serce bicie
    Myśli krążą w mojej głowie
    Szukam drogi przez te wszystkie dni
    Które przemijają tak głowie

    [Chorus]
    Lecz wstanę się, sięgnę po gwiazdy!
    Nigdy nie powiem goodbye!
    Ty jesteś powodem że żyję!
    Tak to my przetrwamy!
    """

    print_separator("COMPREHENSIVE LYRIC ANALYSIS DEMO")
    print("\nAnalyzing sample lyrics with all 5 prototypes...\n")

    # Prototype 1: Emotional Arc Analysis
    print_separator("1️⃣  EMOTIONAL ARC ANALYZER")
    emotion_analyzer = EmotionalArcAnalyzer()
    emotion_result = emotion_analyzer.analyze(sample_lyrics)

    print(f"\n📊 Pattern Detected: {emotion_result['pattern'].upper()}")
    print(f"   Confidence: {emotion_result['pattern_confidence']:.1%}")
    print(f"\n   Emotional Journey:")
    for point in emotion_result['arc'][:4]:  # First 4 points
        print(f"   - [{point.section}] Valence: {point.valence:+.2f}, "
              f"Arousal: {point.arousal:.2f}")

    # Prototype 2: Rhyme Scheme Extraction
    print_separator("2️⃣  RHYME SCHEME EXTRACTOR")
    rhyme_analyzer = AdvancedRhymeAnalyzer()
    rhyme_result = rhyme_analyzer.analyze_rhyme_scheme(sample_lyrics)

    print(f"\n🔤 Rhyme Scheme: {rhyme_result['rhyme_scheme']}")
    print(f"   Structure: {rhyme_result['structure']}")
    print(f"   Rhyme Density: {rhyme_result['statistics']['rhyme_density']:.2f}")
    print(f"   Total Matches: {len(rhyme_result['matches'])}")

    # Prototype 3: Genre Classification (using pre-trained data)
    print_separator("3️⃣  GENRE CLASSIFIER")
    print("\n⚠️  Note: Genre classifier requires training data.")
    print("   Creating synthetic training data for demonstration...")

    classifier = EnsembleGenreClassifier()

    # Create minimal training data
    training_lyrics = [
        """
        [Chorus]
        WE WILL ROCK YOU!
        Stand up and fight!
        Rock all night!
        """,
        """
        [Chorus]
        Baby I love you so much
        You're my perfect touch
        Dance with me tonight
        Hold me tight
        """,
        """
        [Verse]
        Stackin cash, flowin big
        Hustle hard, dig the rig
        Money tall, never fall
        That's how we ball
        """
    ]

    training_genres = ['rock', 'pop', 'hip_hop']

    try:
        metrics = classifier.train(training_lyrics, training_genres)
        prediction = classifier.predict(sample_lyrics, top_k=3)

        print(f"\n🎸 Top 3 Genre Predictions:")
        for i, pred in enumerate(prediction.predictions, 1):
            print(f"   {i}. {pred.genre}: {pred.confidence:.1%}")
    except Exception as e:
        print(f"\n❌ Classification demo failed: {e}")
        print("   (Requires more training data for accurate results)")

    # Prototype 4: Prompt Quality Scoring
    print_separator("4️⃣  PROMPT QUALITY SCORER")
    scorer = PromptQualityScorer()
    evaluation = scorer.evaluate(sample_prompt)

    print(f"\n✍️ Overall Score: {evaluation.overall_score:.1%} (Grade: {evaluation.grade})")
    print(f"\n   Top Dimensions:")
    for dim_score in sorted(evaluation.dimension_scores,
                           key=lambda x: x.score, reverse=True)[:3]:
        print(f"   - {dim_score.dimension.capitalize()}: {dim_score.score:.1%}")

    if evaluation.improvement_priority:
        print(f"\n   Priority Improvement: {evaluation.improvement_priority[0].capitalize()}")

    # Prototype 5: Cross-Lingual Adaptation
    print_separator("5️⃣  CROSS-LINGUAL ADAPTER")
    adapter = CrossLingualAdapter()

    # Detect language
    detected_lang = adapter.detect_language(polish_lyrics)
    print(f"\n🌐 Detected Language: {'Polish' if detected_lang == 'pl' else 'English'}")

    # Analyze rhythm
    rhythm = adapter.calculate_rhythm(polish_lyrics)
    print(f"   Rhythm Pattern (syllables per line): {rhythm[:4]}")

    # Cultural adaptation
    adapted, notes = adapter.adapt_cultural_references(polish_lyrics, 'pl', 'en')
    print(f"\n   Cultural Adaptations: {len(notes)} notes")

    # Rhyme scheme
    scheme = adapter.extract_rhyme_scheme(polish_lyrics, 'pl')
    print(f"   Rhyme Scheme: {''.join(scheme[:4])}")

    print_separator("DEMO COMPLETE")
    print("\n✅ All 5 prototypes demonstrated successfully!")
    print("\n📚 For detailed documentation, see: README.md")
    print("🔧 To run individual prototypes:")
    print("   cd prototypes/python_patterns")
    print("   python 01_emotional_arc_analyzer.py")
    print("   python 02_rhyme_scheme_extractor.py")
    print("   python 03_genre_classifier.py")
    print("   python 04_prompt_quality_scorer.py")
    print("   python 05_cross_lingual_adapter.py")


if __name__ == "__main__":
    try:
        demo_comprehensive_analysis()
    except KeyboardInterrupt:
        print("\n\n⚠️  Demo interrupted by user")
    except Exception as e:
        print(f"\n\n❌ Demo failed with error: {e}")
        import traceback
        traceback.print_exc()
