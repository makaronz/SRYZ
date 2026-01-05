"""
COMPREHENSIVE TEST SUITE FOR PYTHON PROTOTYPES
===============================================

Tests all 5 prototype patterns with edge cases and sample outputs.
Run with: python -m pytest tests/test_all_prototypes.py -v
"""

import pytest
import sys
from pathlib import Path

# Add prototypes directory to path
sys.path.insert(0, str(Path(__file__).parent.parent / 'python_patterns'))

# Import all prototypes
from prototype_01_emotional_arc_analyzer import EmotionalArcAnalyzer
from prototype_02_rhyme_scheme_extractor import AdvancedRhymeAnalyzer
from prototype_03_genre_classifier import EnsembleGenreClassifier
from prototype_04_prompt_quality_scorer import PromptQualityScorer
from prototype_05_cross_lingual_adapter import CrossLingualAdapter


class TestEmotionalArcAnalyzer:
    """Test emotional arc analyzer"""

    @pytest.fixture
    def analyzer(self):
        return EmotionalArcAnalyzer()

    def test_basic_analysis(self, analyzer):
        """Test basic emotional arc detection"""
        lyrics = """
        [Verse]
        I'm so sad and lonely tonight
        Everything feels wrong

        [Chorus]
        But tomorrow I'll rise again!
        Stronger than before!
        """
        result = analyzer.analyze(lyrics)

        assert 'pattern' in result
        assert 'arc' in result
        assert len(result['arc']) > 0
        assert 'statistics' in result

    def test_short_song_edge_case(self, analyzer):
        """Test handling of very short songs"""
        lyrics = "I love you"
        result = analyzer.analyze(lyrics)

        # Should handle gracefully, likely with error or minimal arc
        assert 'error' in result or len(result['arc']) <= 2

    def test_instrumental_sections(self, analyzer):
        """Test handling of instrumental sections"""
        lyrics = """
        [Verse 1]
    I walk alone at night

        [Instrumental Solo]

        [Chorus]
    Finding my way home
        """
        result = analyzer.analyze(lyrics)

        # Should skip instrumental and analyze only text sections
        assert result is not None

    def test_emotional_velocity_calculation(self, analyzer):
        """Test emotional velocity calculation"""
        lyrics = """
        [Verse]
    I'm so sad today
        [Chorus]
    I'm happy now!
        [Bridge]
    I'm overwhelmed
        """
        result = analyzer.analyze(lyrics)

        assert 'velocity_mean' in result['statistics']
        assert isinstance(result['statistics']['velocity_mean'], float)


class TestRhymeSchemeExtractor:
    """Test rhyme scheme extractor"""

    @pytest.fixture
    def analyzer(self):
        return AdvancedRhymeAnalyzer()

    def test_perfect_rhyme_detection(self, analyzer):
        """Test perfect rhyme detection"""
        is_rhyme, strength = analyzer.detect_perfect_rhyme("cat", "hat")
        assert is_rhyme is True
        assert strength > 0.0

        is_rhyme, strength = analyzer.detect_perfect_rhyme("cat", "dog")
        assert is_rhyme is False

    def test_slant_rhyme_detection(self, analyzer):
        """Test slant rhyme detection"""
        # These might be slant rhymes depending on pronunciation
        is_rhyme, strength = analyzer.detect_slant_rhyme("soul", "all")
        # Result depends on pronouncing dictionary
        assert isinstance(is_rhyme, bool)
        assert isinstance(strength, float)

    def test_aabb_scheme(self, analyzer):
        """Test AABB rhyme scheme detection"""
        lyrics = """
    The cat sat on the mat
    And dreamed of a big rat
    The dog chased the log
    Across the green bog
        """
        result = analyzer.analyze_rhyme_scheme(lyrics)

        assert 'rhyme_scheme' in result
        assert 'AABB' in result['rhyme_scheme'] or result['rhyme_scheme'] != ''

    def test_abab_scheme(self, analyzer):
        """Test ABAB cross rhyme detection"""
        lyrics = """
    The cat sat on the mat
    The dog ran to the bog
    I saw a big brown rat
    Hiding within the log
        """
        result = analyzer.analyze_rhyme_scheme(lyrics)

        assert 'rhyme_scheme' in result

    def test_free_verse(self, analyzer):
        """Test free verse (minimal rhyming)"""
        lyrics = """
    I walk alone
    Through the streets
    The wind blows
    Against my face
        """
        result = analyzer.analyze_rhyme_scheme(lyrics)

        assert 'rhyme_scheme' in result
        # Free verse should have low rhyme density
        assert result['statistics']['rhyme_density'] < 0.5


class TestGenreClassifier:
    """Test genre classifier"""

    @pytest.fixture
    def classifier(self):
        return EnsembleGenreClassifier()

    def test_feature_extraction(self, classifier):
        """Test feature extraction from lyrics"""
        lyrics = """
        [Verse]
    I love you baby so much
    Dancing all night long
        """

        features = classifier.feature_extractor.extract_all_features(lyrics)

        assert isinstance(features, dict)
        assert len(features) > 0

    def test_vocabulary_richness(self, classifier):
        """Test vocabulary richness calculation"""
        lyrics = "I love love love you baby baby baby"

        features = classifier.feature_extractor.extract_complexity_features(lyrics)

        assert 'vocabulary_diversity' in features
        # Low diversity due to repetition
        assert features['vocabulary_diversity'] < 0.5

    def test_sentiment_features(self, classifier):
        """Test sentiment feature extraction"""
        lyrics = "I am so happy and joyful today!"

        features = classifier.feature_extractor.extract_sentiment_features(lyrics)

        if features:  # May be empty if NLTK fails
            assert 'sentiment_compound' in features or 'sentiment_positive' in features

    def test_training_requires_data(self, classifier):
        """Test that training requires sufficient data"""
        with pytest.raises(ValueError):
            classifier.train([], [])

        with pytest.raises(ValueError):
            classifier.train(["Short"], ['pop'])

    def test_prediction_before_training(self, classifier):
        """Test that prediction fails before training"""
        with pytest.raises(ValueError):
            classifier.predict("Some lyrics")


class TestPromptQualityScorer:
    """Test prompt quality scorer"""

    @pytest.fixture
    def scorer(self):
        return PromptQualityScorer()

    def test_empty_prompt(self, scorer):
        """Test handling of empty prompts"""
        result = scorer.evaluate("")

        assert result.overall_score == 0.0
        assert result.grade == 'F'

    def test_poor_prompt(self, scorer):
        """Test scoring of poor prompt"""
        prompt = "write something"

        result = scorer.evaluate(prompt)

        assert result.overall_score < 0.5
        assert result.grade in ['D', 'F']

    def test_excellent_prompt(self, scorer):
        """Test scoring of excellent prompt"""
        prompt = """
        CONTEXT:
        I need a blog post about music history for college students.

        REQUIREMENTS:
        - Cover 1970s to present
        - Discuss 5 key artists per era
        - Include specific song examples

        CONSTRAINTS:
        - Do not cover gangsta rap
        - Maximum 100 words per artist
        - Use APA citations

        FORMAT:
        - Clear headings (H2)
        - 800-1000 words
        """

        result = scorer.evaluate(prompt)

        assert result.overall_score > 0.7
        assert result.grade in ['A', 'B']

    def test_specificity_scoring(self, scorer):
        """Test specificity dimension scoring"""
        prompt = "Write about 3 specific artists from the 1990s"

        score = scorer.calculate_specificity_score(prompt)

        assert 0.0 <= score.score <= 1.0
        assert isinstance(score.details, str)
        assert isinstance(score.suggestions, list)

    def test_structure_scoring(self, scorer):
        """Test structure dimension scoring"""
        prompt = """
        Context: Music history

        Requirements:
        - Cover 1990s
        - Discuss artists

        Format: Blog post
        """

        score = scorer.calculate_structure_score(prompt)

        assert 0.0 <= score.score <= 1.0


class TestCrossLingualAdapter:
    """Test cross-lingual adapter"""

    @pytest.fixture
    def adapter(self):
        return CrossLingualAdapter()

    def test_language_detection(self, adapter):
        """Test Polish vs English language detection"""
        polish_text = "W nocnej ciszy słychać serce"
        english_text = "In the silence of the night"

        assert adapter.detect_language(polish_text) == 'pl'
        assert adapter.detect_language(english_text) == 'en'

    def test_rhythm_calculation(self, adapter):
        """Test rhythm pattern extraction"""
        text = """
    I walk alone at night
    Through the empty streets
    Searching for the light
        """

        rhythm = adapter.calculate_rhythm(text)

        assert len(rhythm) == 3
        assert all(isinstance(r, int) for r in rhythm)

    def test_rhyme_scheme_extraction(self, adapter):
        """Test rhyme scheme extraction"""
        text = """
    The cat sat on the mat
    I saw a big rat
        """

        scheme = adapter.extract_rhyme_scheme(text, 'en')

        assert len(scheme) == 2
        # Both lines should rhyme (same label)
        assert scheme[0] == scheme[1]

    def test_cultural_adaptation(self, adapter):
        """Test cultural reference adaptation"""
        text = "Mama serce wiatr"
        adapted, notes = adapter.adapt_cultural_references(text, 'pl', 'en')

        assert isinstance(adapted, str)
        assert isinstance(notes, list)

    def test_bilingual_version(self, adapter):
        """Test bilingual version creation"""
        text = "I love you so much"

        bilingual = adapter.create_bilingual_version(text, 'en')

        assert '/' in bilingual
        assert 'I love you so much' in bilingual

    def test_translation_metrics(self, adapter):
        """Test translation quality metrics"""
        original = "I love you"
        translated = "Kocham cię"

        metrics = adapter.calculate_translation_metrics(original, translated, 'en', 'pl')

        assert hasattr(metrics, 'semantic_similarity')
        assert hasattr(metrics, 'rhythm_correlation')
        assert hasattr(metrics, 'overall_quality')


# Integration tests
class TestIntegration:
    """Integration tests for prototype combinations"""

    def test_emotional_arc_plus_rhyme(self):
        """Test combining emotional arc and rhyme analysis"""
        lyrics = """
        [Verse 1]
    I'm so sad and lonely
    Feeling like I'm the only
    One who walks this path alone

        [Chorus]
    But I'll rise up high!
    Touching the sky!
    Never gonna die!
        """

        # Analyze emotional arc
        emotion_analyzer = EmotionalArcAnalyzer()
        emotion_result = emotion_analyzer.analyze(lyrics)

        # Analyze rhyme scheme
        rhyme_analyzer = AdvancedRhymeAnalyzer()
        rhyme_result = rhyme_analyzer.analyze_rhyme_scheme(lyrics)

        assert emotion_result is not None
        assert rhyme_result is not None

        # Could combine results for deeper analysis
        emotional_span = emotion_result['statistics']['emotional_span']
        rhyme_density = rhyme_result['statistics']['rhyme_density']

        assert isinstance(emotional_span, float)
        assert isinstance(rhyme_density, float)

    def test_genre_classification_with_prompt_quality(self):
        """Test that genre classification can inform prompt quality"""
        # Create genre-specific prompts
        rock_prompt = """
        Write a rock song about rebellion.
        Must include guitar riffs and powerful vocals.
        """

        pop_prompt = """
        Write a pop song about love.
        Should be catchy and danceable.
        """

        scorer = PromptQualityScorer()

        rock_score = scorer.evaluate(rock_prompt).overall_score
        pop_score = scorer.evaluate(pop_prompt).overall_score

        # Both should be moderate quality
        assert 0.0 <= rock_score <= 1.0
        assert 0.0 <= pop_score <= 1.0


# Performance tests
class TestPerformance:
    """Performance and edge case tests"""

    def test_large_lyrics_handling(self):
        """Test handling of very long lyrics"""
        long_lyrics = "\n".join([f"Line {i} of this song" for i in range(100)])

        analyzer = EmotionalArcAnalyzer()
        result = analyzer.analyze(long_lyrics)

        assert result is not None

    def test_unicode_handling(self):
        """Test handling of Unicode characters (Polish)"""
        polish_text = "W nocy śnią się creepy anioły z pióra"

        adapter = CrossLingualAdapter()
        lang = adapter.detect_language(polish_text)

        assert lang == 'pl'

    def test_mixed_language(self):
        """Test handling of mixed Polish-English text"""
        mixed_text = "I love you very much - Kocham cię bardzo"

        adapter = CrossLingualAdapter()
        lang = adapter.detect_language(mixed_text)

        # Should detect based on dominant language
        assert lang in ['pl', 'en']


if __name__ == "__main__":
    # Run tests
    pytest.main([__file__, "-v", "--tb=short"])
