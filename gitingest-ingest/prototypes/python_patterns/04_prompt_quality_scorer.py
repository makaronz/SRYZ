"""
PROMPT QUALITY SCORER
=====================

INNOVATION: Multi-dimensional prompt evaluation for AI-generated content:
1. Specificity scoring (concrete details vs vague language)
2. Structural coherence (logical organization)
3. Creative potential (novelty and imaginative content)
4. Constraint clarity (explicit requirements)
5. Context richness (background information)
6. Action-verb density (clear directives)

EDGE CASES HANDLED:
- Short prompts (< 20 characters)
- Overly complex prompts (too many constraints)
- Ambiguous instructions
- Multi-part prompts with conflicting goals
"""

import re
import numpy as np
from typing import List, Dict, Tuple, Optional
from dataclasses import dataclass
from collections import Counter
import spacy

# Load spaCy for NLP analysis
try:
    nlp = spacy.load("en_core_web_sm")
except OSError:
    print("Warning: spaCy model not found. Install with: python -m spacy download en_core_web_sm")
    nlp = None

@dataclass
class QualityScore:
    """Score for a single quality dimension"""
    dimension: str
    score: float  # 0-1
    details: str  # Human-readable explanation
    suggestions: List[str]  # Improvement suggestions


@dataclass
class PromptEvaluation:
    """Complete prompt evaluation report"""
    overall_score: float  # 0-1
    dimension_scores: List[QualityScore]
    strengths: List[str]
    weaknesses: List[str]
    improvement_priority: List[str]  # Ordered by impact
    grade: str  # A, B, C, D, F


class PromptQualityScorer:
    """
    Comprehensive prompt quality evaluator.

    Innovation: Combines linguistic analysis with prompt engineering best practices:
    - NLP-based feature extraction
    - Heuristic scoring for prompt engineering principles
    - Actionable feedback generation
    - Comparative quality assessment
    """

    # Quality dimensions and their weights
    DIMENSIONS = {
        'specificity': 0.25,
        'structure': 0.20,
        'creativity': 0.15,
        'constraints': 0.15,
        'context': 0.15,
        'clarity': 0.10
    }

    # Specificity indicators (concrete details)
    SPECIFICITY_MARKERS = {
        'numbers': r'\b\d+\b',
        'measurements': r'\b(dollars|percent|pages|words|minutes|hours)\b',
        'proper_nouns': r'\b[A-Z][a-z]+\b',
        'quotes': r'["\'].*["\']',
        'examples': r'\b(e.g.|for example|such as|like)\b',
        'precise_terms': r'\b(exactly|precisely|specifically|must|should)\b'
    }

    # Structural markers
    STRUCTURE_MARKERS = {
        'introduction': r'\b(introduction|background|context|overview)\b',
        'requirements': r'\b(requirements|must|should|need|expectations)\b',
        'format': r'\b(format|structure|template|layout)\b',
        'constraints': r'\b(constraints|limitations|restrictions|boundaries)\b',
        'examples': r'\b(example|sample|reference|illustration)\b'
    }

    # Creative indicators
    CREATIVE_MARKERS = {
        'novel_combinations': r'\b(unique|innovative|creative|original|novel)\b',
        'metaphors': r'\b(like|as if|similar to|analogy)\b',
        'hypotheticals': r'\b(imagine|consider if|what if|suppose)\b',
        'comparisons': r'\b(compared to|versus|unlike|similar to)\b'
    }

    # Constraint indicators
    CONSTRAINT_MARKERS = {
        'negatives': r'\b(not|no|never|avoid|don\'t|must not)\b',
        'limits': r'\b(maximum|minimum|limit|within|between)\b',
        'requirements': r'\b(must|should|require|expect|need)\b',
        'format_specs': r'\b(format|template|structure|length|style)\b'
    }

    # Action verbs for clarity
    ACTION_VERBS = {
        'create', 'write', 'generate', 'develop', 'design', 'build', 'construct',
        'analyze', 'evaluate', 'assess', 'compare', 'examine', 'investigate',
        'explain', 'describe', 'detail', 'outline', 'specify', 'define',
        'implement', 'execute', 'perform', 'conduct', 'carry out'
    }

    def __init__(self):
        """Initialize scorer with NLP model"""
        self.nlp = nlp

    def preprocess_prompt(self, prompt: str) -> str:
        """Clean and normalize prompt text"""
        # Remove extra whitespace
        prompt = ' '.join(prompt.split())
        return prompt.strip()

    def calculate_specificity_score(self, prompt: str) -> QualityScore:
        """
        Score prompt specificity (concrete vs vague).

        Innovation: Counts concrete details:
        - Numbers and measurements
        - Proper nouns
        - Examples and quotes
        - Precise terminology
        """
        if not prompt:
            return QualityScore('specificity', 0.0, "Empty prompt", ["Add content"])

        prompt_lower = prompt.lower()
        word_count = len(prompt.split())

        if word_count < 10:
            return QualityScore(
                'specificity', 0.2,
                "Prompt too brief for specific details",
                ["Add more context and details", "Include examples or requirements"]
            )

        # Count specificity markers
        scores = []

        # Numbers (normalized by word count)
        numbers = len(re.findall(self.SPECIFICITY_MARKERS['numbers'], prompt))
        scores.append(min(numbers / (word_count * 0.1), 1.0))

        # Measurements
        measurements = len(re.findall(self.SPECIFICITY_MARKERS['measurements'], prompt_lower))
        scores.append(min(measurements / (word_count * 0.05), 1.0))

        # Proper nouns (capitalized words)
        proper_nouns = len(re.findall(self.SPECIFICITY_MARKERS['proper_nouns'], prompt))
        scores.append(min(proper_nouns / (word_count * 0.15), 1.0))

        # Quotes
        quotes = len(re.findall(self.SPECIFICITY_MARKERS['quotes'], prompt))
        scores.append(min(quotes / 2, 1.0))  # Max 2 quotes for full score

        # Examples
        examples = len(re.findall(self.SPECIFICITY_MARKERS['examples'], prompt_lower))
        scores.append(min(examples, 1.0))

        # Precise terms
        precise = len(re.findall(self.SPECIFICITY_MARKERS['precise_terms'], prompt_lower))
        scores.append(min(precise / (word_count * 0.05), 1.0))

        # Calculate weighted average
        specificity_score = np.mean(scores)

        # Generate feedback
        if specificity_score >= 0.7:
            details = "Excellent specificity with concrete details"
            suggestions = []
        elif specificity_score >= 0.4:
            details = "Moderate specificity, could use more concrete details"
            suggestions = [
                "Add specific numbers or measurements",
                "Include proper nouns and names",
                "Provide examples or use cases"
            ]
        else:
            details = "Low specificity, too vague or general"
            suggestions = [
                "Add specific numbers, dates, or measurements",
                "Include concrete examples",
                "Use proper nouns and precise terminology",
                "Add quotes or references to exact requirements"
            ]

        return QualityScore('specificity', specificity_score, details, suggestions)

    def calculate_structure_score(self, prompt: str) -> QualityScore:
        """
        Score prompt structural organization.

        Innovation: Detects logical organization:
        - Introduction/background
        - Clear requirements section
        - Format specifications
        - Examples or references
        - Logical flow indicators
        """
        if not prompt:
            return QualityScore('structure', 0.0, "Empty prompt", ["Add content"])

        prompt_lower = prompt.lower()

        # Check for structural elements
        has_intro = bool(re.search(self.STRUCTURE_MARKERS['introduction'], prompt_lower))
        has_requirements = bool(re.search(self.STRUCTURE_MARKERS['requirements'], prompt_lower))
        has_format = bool(re.search(self.STRUCTURE_MARKERS['format'], prompt_lower))
        has_examples = bool(re.search(self.STRUCTURE_MARKERS['examples'], prompt_lower))

        # Check for paragraph structure (multiple paragraphs = better organization)
        paragraphs = [p.strip() for p in prompt.split('\n') if p.strip()]
        paragraph_score = min(len(paragraphs) / 4, 1.0)  # 4+ paragraphs is ideal

        # Check for bullet points or numbered lists
        has_list = bool(re.search(r'^\s*[-*•]\s|^ \d+\.\s', prompt, re.MULTILINE))
        list_score = 1.0 if has_list else 0.5

        # Calculate structure score
        structure_elements = [
            has_intro,
            has_requirements,
            has_format,
            has_examples
        ]
        element_score = sum(structure_elements) / len(structure_elements)

        structure_score = 0.6 * element_score + 0.2 * paragraph_score + 0.2 * list_score

        # Generate feedback
        if structure_score >= 0.7:
            details = "Well-structured with clear organization"
            suggestions = []
        elif structure_score >= 0.4:
            details = "Moderately structured, could be more organized"
            suggestions = [
                "Use clear section headers",
                "Organize with bullet points or numbered lists",
                "Separate context from requirements"
            ]
        else:
            details = "Poorly structured, lacks organization"
            suggestions = [
                "Add clear section headers (Context, Requirements, Format)",
                "Use bullet points for lists",
                "Separate into logical paragraphs",
                "Add examples or reference sections"
            ]

        return QualityScore('structure', structure_score, details, suggestions)

    def calculate_creativity_score(self, prompt: str) -> QualityScore:
        """
        Score creative potential of prompt.

        Innovation: Measures novelty and imaginative content:
        - Unique word combinations
        - Metaphorical language
        - Hypothetical scenarios
        - Comparative references
        """
        if not prompt:
            return QualityScore('creativity', 0.0, "Empty prompt", ["Add content"])

        prompt_lower = prompt.lower()

        # Check creative markers
        creative_elements = []

        # Novel combinations
        novel = len(re.findall(self.CREATIVE_MARKERS['novel_combinations'], prompt_lower))
        creative_elements.append(min(novel / 2, 1.0))

        # Metaphors and analogies
        metaphors = len(re.findall(self.CREATIVE_MARKERS['metaphors'], prompt_lower))
        creative_elements.append(min(metaphors / 3, 1.0))

        # Hypotheticals
        hypotheticals = len(re.findall(self.CREATIVE_MARKERS['hypotheticals'], prompt_lower))
        creative_elements.append(min(hypotheticals / 2, 1.0))

        # Comparisons
        comparisons = len(re.findall(self.CREATIVE_MARKERS['comparisons'], prompt_lower))
        creative_elements.append(min(comparisons / 3, 1.0))

        # Vocabulary diversity (unique words / total words)
        words = prompt.split()
        if len(words) > 0:
            vocab_diversity = len(set(words)) / len(words)
            creative_elements.append(vocab_diversity)

        creativity_score = np.mean(creative_elements)

        # Generate feedback
        if creativity_score >= 0.7:
            details = "High creative potential with imaginative elements"
            suggestions = []
        elif creativity_score >= 0.4:
            details = "Moderate creative potential"
            suggestions = [
                "Add metaphors or analogies",
                "Include hypothetical scenarios",
                "Use comparative examples"
            ]
        else:
            details = "Low creative potential, very straightforward"
            suggestions = [
                "Add creative comparisons or analogies",
                "Include hypothetical 'what if' scenarios",
                "Use more diverse vocabulary",
                "Add imaginative elements or novel approaches"
            ]

        return QualityScore('creativity', creativity_score, details, suggestions)

    def calculate_constraints_score(self, prompt: str) -> QualityScore:
        """
        Score constraint clarity.

        Innovation: Measures how well constraints are specified:
        - Negative constraints (what NOT to do)
        - Limitations and boundaries
        - Explicit requirements
        - Format specifications
        """
        if not prompt:
            return QualityScore('constraints', 0.0, "Empty prompt", ["Add content"])

        prompt_lower = prompt.lower()

        # Count constraint types
        constraints = []

        # Negative constraints
        negatives = len(re.findall(self.CONSTRAINT_MARKERS['negatives'], prompt_lower))
        constraints.append(min(negatives / 3, 1.0))

        # Limits
        limits = len(re.findall(self.CONSTRAINT_MARKERS['limits'], prompt_lower))
        constraints.append(min(limits / 2, 1.0))

        # Requirements
        requirements = len(re.findall(self.CONSTRAINT_MARKERS['requirements'], prompt_lower))
        constraints.append(min(requirements / 4, 1.0))

        # Format specs
        format_specs = len(re.findall(self.CONSTRAINT_MARKERS['format_specs'], prompt_lower))
        constraints.append(min(format_specs / 2, 1.0))

        # Balance check: not too many constraints (over-constrained)
        constraint_count = negatives + limits + requirements + format_specs
        word_count = len(prompt.split())
        constraint_ratio = constraint_count / max(word_count, 1)

        # Penalize over-constraining (too many constraints per word)
        if constraint_ratio > 0.3:
            overconstraint_penalty = 0.3
        else:
            overconstraint_penalty = 0.0

        constraints_score = np.mean(constraints) - overconstraint_penalty

        # Generate feedback
        if constraints_score >= 0.7:
            details = "Clear constraints and boundaries"
            suggestions = []
        elif constraints_score >= 0.4:
            details = "Some constraints, could be clearer"
            suggestions = [
                "Specify what NOT to do",
                "Add clear limitations or boundaries",
                "Explicitly state requirements"
            ]
        else:
            details = "Unclear or missing constraints"
            suggestions = [
                "Add negative constraints (what to avoid)",
                "Specify clear boundaries",
                "State requirements explicitly",
                "Include format specifications"
            ]

        if overconstraint_penalty > 0:
            suggestions.append("Consider reducing constraints - may be over-constrained")

        return QualityScore('constraints', max(constraints_score, 0.0), details, suggestions)

    def calculate_context_score(self, prompt: str) -> QualityScore:
        """
        Score context richness.

        Innovation: Measures background information:
        - Background/context section
        - Target audience specification
        - Purpose/goal statement
        - Domain-specific terminology
        """
        if not prompt:
            return QualityScore('context', 0.0, "Empty prompt", ["Add content"])

        prompt_lower = prompt.lower()

        # Check for context elements
        context_elements = []

        # Background/introduction
        has_background = any(term in prompt_lower for term in
            ['background', 'context', 'introduction', 'overview', 'history'])
        context_elements.append(1.0 if has_background else 0.0)

        # Target audience
        has_audience = any(term in prompt_lower for term in
            ['audience', 'target', 'reader', 'user', 'demographic'])
        context_elements.append(1.0 if has_audience else 0.0)

        # Purpose/goal
        has_purpose = any(term in prompt_lower for term in
            ['purpose', 'goal', 'objective', 'aim', 'intention'])
        context_elements.append(1.0 if has_purpose else 0.0)

        # Domain terminology (jargon indicates domain expertise)
        # Use spaCy if available for better detection
        if self.nlp:
            doc = self.nlp(prompt)
            # Count technical terms (noun chunks > 2 words)
            technical_terms = [chunk for chunk in doc.noun_chunks if len(chunk) > 2]
            tech_score = min(len(technical_terms) / 3, 1.0)
            context_elements.append(tech_score)
        else:
            # Fallback: check for longer words (indicates technical content)
            long_words = [w for w in prompt.split() if len(w) > 8]
            tech_score = min(len(long_words) / 5, 1.0)
            context_elements.append(tech_score)

        # Length score (longer prompts typically have more context)
        word_count = len(prompt.split())
        length_score = min(word_count / 100, 1.0)  # 100 words = full score
        context_elements.append(length_score * 0.5)  # Weighted less

        context_score = np.mean(context_elements)

        # Generate feedback
        if context_score >= 0.7:
            details = "Rich context with clear background"
            suggestions = []
        elif context_score >= 0.4:
            details = "Moderate context, could use more background"
            suggestions = [
                "Add background or context section",
                "Specify target audience",
                "Clarify purpose or goal"
            ]
        else:
            details = "Minimal context, lacks background information"
            suggestions = [
                "Add background information",
                "Specify target audience or users",
                "Clarify purpose and goals",
                "Include domain-specific context"
            ]

        return QualityScore('context', context_score, details, suggestions)

    def calculate_clarity_score(self, prompt: str) -> QualityScore:
        """
        Score clarity through action verbs and directness.

        Innovation: Measures clear directive language:
        - Action verb density
        - Direct statements
        - Ambiguity avoidance
        """
        if not prompt:
            return QualityScore('clarity', 0.0, "Empty prompt", ["Add content"])

        words = prompt.lower().split()

        # Count action verbs
        action_verbs = [w for w in words if w in self.ACTION_VERBS]
        action_density = len(action_verbs) / max(len(words), 1)

        # Normalize: 1 action verb per 10 words = excellent
        action_score = min(action_density * 10, 1.0)

        # Check for ambiguity markers
        ambiguous_terms = ['maybe', 'perhaps', 'possibly', 'might', 'could be', 'sort of', 'kind of']
        ambiguity_count = sum(1 for term in ambiguous_terms if term in prompt.lower())

        # Penalize ambiguity
        ambiguity_penalty = min(ambiguity_count / 5, 0.5)

        clarity_score = action_score - ambiguity_penalty

        # Generate feedback
        if clarity_score >= 0.7:
            details = "Clear directives with strong action verbs"
            suggestions = []
        elif clarity_score >= 0.4:
            details = "Moderately clear, could be more direct"
            suggestions = [
                "Use more action verbs",
                "Remove ambiguous language",
                "Make directives more explicit"
            ]
        else:
            details = "Unclear, lacks direct instructions"
            suggestions = [
                "Start with clear action verbs",
                "Remove vague or ambiguous terms",
                "Make instructions explicit and direct",
                "Use imperative mood for requirements"
            ]

        return QualityScore('clarity', max(clarity_score, 0.0), details, suggestions)

    def evaluate(self, prompt: str) -> PromptEvaluation:
        """
        Complete prompt evaluation.

        Returns comprehensive quality assessment.
        """
        prompt = self.preprocess_prompt(prompt)

        # Calculate dimension scores
        dimension_scores = [
            self.calculate_specificity_score(prompt),
            self.calculate_structure_score(prompt),
            self.calculate_creativity_score(prompt),
            self.calculate_constraints_score(prompt),
            self.calculate_context_score(prompt),
            self.calculate_clarity_score(prompt)
        ]

        # Calculate weighted overall score
        overall_score = sum(
            score.score * self.DIMENSIONS[score.dimension]
            for score in dimension_scores
        )

        # Identify strengths and weaknesses
        strengths = [
            score.dimension for score in dimension_scores
            if score.score >= 0.7
        ]
        weaknesses = [
            score.dimension for score in dimension_scores
            if score.score < 0.5
        ]

        # Prioritize improvements by impact (weight × gap from perfect)
        improvement_priority = [
            score.dimension for score in sorted(
                dimension_scores,
                key=lambda s: (1.0 - s.score) * self.DIMENSIONS[s.dimension],
                reverse=True
            ) if score.score < 0.8
        ]

        # Assign letter grade
        if overall_score >= 0.9:
            grade = 'A'
        elif overall_score >= 0.8:
            grade = 'B'
        elif overall_score >= 0.7:
            grade = 'C'
        elif overall_score >= 0.6:
            grade = 'D'
        else:
            grade = 'F'

        return PromptEvaluation(
            overall_score=overall_score,
            dimension_scores=dimension_scores,
            strengths=strengths,
            weaknesses=weaknesses,
            improvement_priority=improvement_priority,
            grade=grade
        )


def demo_usage():
    """Demonstrate prompt quality scorer with examples"""

    scorer = PromptQualityScorer()

    print("=" * 70)
    print("PROMPT QUALITY SCORER DEMO")
    print("=" * 70)

    # Example prompts of varying quality
    prompts = [
        ("Poor Prompt", """
            write a blog post about music
        """),

        ("Average Prompt", """
            Write a blog post about hip hop music. It should be interesting
            and talk about the history. Make it around 500 words.
        """),

        ("Good Prompt", """
            I need a blog post about the evolution of hip hop music.

            Requirements:
            - Cover the period from 1970s to present
            - Discuss key artists and their contributions
            - Explain major stylistic changes
            - Include specific examples of songs

            Format: Blog post with clear headings
            Length: 800-1000 words
            Audience: Music enthusiasts, age 18-35
        """),

        ("Excellent Prompt", """
            CONTEXT:
            I'm creating content for a music education website targeting
            college students studying music history. This post will be
            part of a series on genre evolution.

            REQUIREMENTS:
            Write an 800-1000 word blog post analyzing the evolution of
            hip hop from 1973 (Bronx origins) to present day.

            MUST INCLUDE:
            - 5 key eras with specific date ranges
            - 3-5 pioneer artists per era with their innovations
            - Technical analysis of production techniques (sampling, drum machines)
            - Cultural context for each major shift
            - Specific song examples (minimum 10) with release dates

            CONSTRAINTS:
            - Do NOT cover gangsta rap in detail (separate article planned)
            - Avoid academic jargon; keep accessible to undergraduates
            - Maximum 100 words per artist
            - Use APA citations for sources

            FORMAT:
            - Catchy title with SEO keywords
            - Clear section headings (H2)
            - Timeline or infographic suggestion
            - Discussion questions at the end

            STYLE:
            Engaging but authoritative. Use analogies to compare hip hop
            evolution to other art forms. Include at least one metaphor
            describing the genre's growth.
        """)
    ]

    for name, prompt in prompts:
        print(f"\n{'=' * 70}")
        print(f"📝 {name}")
        print("=" * 70)
        print(f"Prompt:\n{prompt.strip()}\n")

        evaluation = scorer.evaluate(prompt)

        print(f"\nOverall Score: {evaluation.overall_score:.1%} (Grade: {evaluation.grade})")

        print(f"\nDimension Scores:")
        for dim_score in evaluation.dimension_scores:
            print(f"  {dim_score.dimension.capitalize()}: {dim_score.score:.1%}")
            print(f"    → {dim_score.details}")

        if evaluation.strengths:
            print(f"\n✅ Strengths: {', '.join(evaluation.strengths)}")

        if evaluation.weaknesses:
            print(f"\n❌ Weaknesses: {', '.join(evaluation.weaknesses)}")

        if evaluation.improvement_priority:
            print(f"\n🎯 Priority Improvements:")
            for i, priority in enumerate(evaluation.improvement_priority, 1):
                # Find suggestions for this dimension
                suggestions = next(
                    (s.suggestions for s in evaluation.dimension_scores if s.dimension == priority),
                    []
                )
                print(f"  {i}. {priority.capitalize()}")
                for suggestion in suggestions[:2]:  # Top 2 suggestions
                    print(f"     - {suggestion}")

    return scorer


if __name__ == "__main__":
    demo_usage()
