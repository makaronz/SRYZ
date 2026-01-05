# Quick Start Implementation Guide
## SRYZ Music Analysis & Creative Production

**Audio File:** 1766703089788_4cdwq9.m4a (4:10, AAC, 48kHz, stereo)
**Last Updated:** December 26, 2025

---

## 🚀 5-Minute Quick Start

### Option 1: Completely Free Workflow

```bash
# 1. TRANSCRIPTION (FREE)
# Go to: https://elevenlabs.io/speech-to-text/polish
# Upload your M4A file
# Download Polish transcript

# 2. BPM DETECTION (FREE)
# Go to: https://bpm-finder.net/
# Upload audio file
# Note the BPM result

# 3. EMOTION ANALYSIS (Basic - FREE)
# Use this Python script:
pip install librosa numpy

python3 << 'EOF'
import librosa
import json

y, sr = librosa.load('1766703089788_4cdwq9.m4a', sr=48000)
tempo, _ = librosa.beat.beat_track(y=y, sr=sr)

# Basic spectral features
spectral_centroid = librosa.feature.spectral_centroid(y=y, sr=sr)[0]
energy = librosa.feature.rms(y=y)[0]

results = {
    "bpm": float(tempo),
    "energy_level": "high" if energy.mean() > 0.1 else "medium",
    "brightness": "bright" if spectral_centroid.mean() > 3000 else "warm"
}

print(json.dumps(results, indent=2))
EOF
```

### Option 2: Premium Workflow (Best Results)

```bash
# 1. TRANSCRIPTION ($20-50)
# Go to: https://www.lalal.ai/
# Upload for 95%+ accuracy transcription
# Download time-stamped lyrics

# 2. BPM VERIFICATION ($58)
# Purchase: Mixed In Key Live
# Verify tempo and detect beat grid

# 3. PROFESSIONAL EMOTION ANALYSIS
# Use Music.AI or develop custom model
# (see comprehensive report for details)
```

---

## 📋 Complete Workflow Checklist

### Phase 1: Audio Analysis (Day 1)

- [ ] **Transcription**
  - [ ] Upload to ElevenLabs (free) or LALAL.AI (paid)
  - [ ] Download transcript
  - [ ] Manually correct Polish lyrics
  - [ ] Save as `transcription.txt`

- [ ] **Tempo Detection**
  - [ ] Upload to BPM Finder (https://bpm-finder.net/)
  - [ ] Note BPM value
  - [ ] Check for tempo changes
  - [ ] Document time signature (likely 4/4)

- [ ] **Emotion Analysis**
  - [ ] Run Python analysis script (below)
  - [ ] Document valence (positive/negative)
  - [ ] Document arousal (calm/energetic)
  - [ ] Note dominant emotions

### Phase 2: Visual Planning (Day 2)

- [ ] **Moodboard Creation**
  - [ ] Create account on Milanote (free trial)
  - [ ] Collect color palette based on emotion
  - [ ] Add location reference images
  - [ ] Include lighting examples
  - [ ] Add wardrobe references
  - [ ] Export moodboard PDF

- [ ] **Story Development**
  - [ ] Define narrative arc
  - [ ] Outline scenes with timestamps
  - [ ] Map song sections to story
  - [ ] Identify key visual moments

### Phase 3: Scriptwriting (Day 3)

- [ ] **Draft Script**
  - [ ] Use dual-column format template
  - [ ] Fill in timestamps (0:00-0:30, etc.)
  - [ ] Add camera directions
  - [ ] Include lyrics in audio column
  - [ ] Describe visuals in video column

- [ ] **Storyboard**
  - [ ] Create visual panels for key scenes
  - [ ] Draw camera movements
  - [ ] Note transitions
  - [ ] Reference moodboard elements

---

## 🛠️ Implementation Scripts

### Script 1: Complete Audio Analysis (Python)

Save as `analyze_audio.py`:

```python
#!/usr/bin/env python3
"""
Quick SRYZ Audio Analysis
Analyzes BPM, energy, and basic mood
"""

import librosa
import json
import sys
from pathlib import Path

def analyze_audio(audio_file):
    """Analyze audio file and extract features"""

    print(f"Loading {audio_file}...")
    y, sr = librosa.load(audio_file, sr=48000, duration=250)  # 4:10 max

    print("Analyzing tempo...")
    tempo, beats = librosa.beat.beat_track(y=y, sr=sr)

    print("Extracting features...")
    spectral_centroid = librosa.feature.spectral_centroid(y=y, sr=sr)[0]
    spectral_rolloff = librosa.feature.spectral_rolloff(y=y, sr=sr)[0]
    zero_crossing_rate = librosa.feature.zero_crossing_rate(y)[0]
    mfccs = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=13)
    energy = librosa.feature.rms(y=y)[0]

    # Determine mood based on features
    brightness = spectral_centroid.mean()
    energy_level = energy.mean()

    if brightness > 3000:
        brightness_desc = "bright (happy, upbeat)"
    elif brightness > 2000:
        brightness_desc = "balanced (mixed emotions)"
    else:
        brightness_desc = "warm/dark (melancholic, sad)"

    if energy_level > 0.15:
        energy_desc = "high energy (intense, powerful)"
    elif energy_level > 0.08:
        energy_desc = "medium energy (calm, steady)"
    else:
        energy_desc = "low energy (gentle, soft)"

    results = {
        "file": str(audio_file),
        "duration_minutes": len(y) / sr / 60,
        "bpm": round(float(tempo), 2),
        "energy_level": energy_desc,
        "brightness": brightness_desc,
        "features": {
            "spectral_centroid_mean": round(float(brightness), 2),
            "energy_mean": round(float(energy_level), 4),
            "zero_crossing_rate_mean": round(float(zero_crossing_rate.mean()), 4)
        },
        "mood_suggestions": {
            "valence": "positive" if brightness > 2500 else "negative/mixed",
            "arousal": "high" if energy_level > 0.1 else "low"
        }
    }

    return results

if __name__ == "__main__":
    audio_file = sys.argv[1] if len(sys.argv) > 1 else "1766703089788_4cdwq9.m4a"

    if not Path(audio_file).exists():
        print(f"Error: File {audio_file} not found")
        sys.exit(1)

    results = analyze_audio(audio_file)

    # Save results
    output_file = "audio_analysis_results.json"
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(results, f, indent=2, ensure_ascii=False)

    print(f"\n✅ Analysis complete!")
    print(f"📊 Results saved to {output_file}")
    print(f"\n🎵 Summary:")
    print(f"   BPM: {results['bpm']}")
    print(f"   Energy: {results['energy_level']}")
    print(f"   Brightness: {results['brightness']}")
```

Run it:
```bash
python3 analyze_audio.py 1766703089788_4cdwq9.m4a
```

### Script 2: Polish Lyrics Sentiment Analysis

Save as `analyze_lyrics.py`:

```python
#!/usr/bin/env python3
"""
Polish Lyrics Sentiment Analysis
Basic emotion detection from lyrics
"""

import json
import sys
from pathlib import Path

# Simple Polish emotion keywords
POLISH_EMOTIONS = {
    "positive": [
        "kochać", "miłość", "szczęśliwy", "radosny", "wesoły",
        "radosław", "radość", "uśmiech", "ciepły", "słońce",
        "latać", "wolność", "nadzieja", "snować", "marzyć"
    ],
    "negative": [
        "smutek", "płakać", "żałoba", "ból", "strata",
        "samotny", "tęsknota", "brak", "czerń", "noc",
        "zapomnieć", "żyć", "umierać", "śmierć", "koń"
    ],
    "energetic": [
        "tańczyć", "skakać", "biec", "szybki", "mocny",
        "siła", "energia", "pot", "krzyk", "wibracja"
    ],
    "calm": [
        "spokój", "cisza", "oddych", "powoli", "ciekły",
        "sen", "marzenie", "spokojny", "łagodny"
    ]
}

def analyze_lyrics(lyrics_file):
    """Analyze Polish lyrics for emotions"""

    print(f"Reading {lyrics_file}...")
    with open(lyrics_file, "r", encoding="utf-8") as f:
        lyrics = f.read().lower()

    print("Analyzing emotions...")
    emotion_counts = {}

    for emotion, keywords in POLISH_EMOTIONS.items():
        count = sum(1 for keyword in keywords if keyword in lyrics)
        emotion_counts[emotion] = count

    # Determine dominant emotions
    total_positive = emotion_counts["positive"]
    total_negative = emotion_counts["negative"]
    total_energetic = emotion_counts["energetic"]
    total_calm = emotion_counts["calm"]

    sentiment = "positive" if total_positive > total_negative else "negative"
    energy = "energetic" if total_energetic > total_calm else "calm"

    results = {
        "file": str(lyrics_file),
        "sentiment": sentiment,
        "energy": energy,
        "emotion_counts": emotion_counts,
        "dominant_emotions": [
            sentiment,
            energy
        ]
    }

    return results

if __name__ == "__main__":
    lyrics_file = sys.argv[1] if len(sys.argv) > 1 else "transcription.txt"

    if not Path(lyrics_file).exists():
        print(f"Error: File {lyrics_file} not found")
        print("Please transcribe audio first!")
        sys.exit(1)

    results = analyze_lyrics(lyrics_file)

    # Save results
    output_file = "lyrics_analysis_results.json"
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(results, f, indent=2, ensure_ascii=False)

    print(f"\n✅ Analysis complete!")
    print(f"📊 Results saved to {output_file}")
    print(f"\n🎤 Lyrics Summary:")
    print(f"   Sentiment: {results['sentiment']}")
    print(f"   Energy: {results['energy']}")
    print(f"   Positive words: {results['emotion_counts']['positive']}")
    print(f"   Negative words: {results['emotion_counts']['negative']}")
```

### Script 3: Moodboard Generator

Save as `generate_moodboard.py`:

```python
#!/usr/bin/env python3
"""
Moodboard Suggestion Generator
Recommends visual elements based on audio/lyrics analysis
"""

import json

# Load analysis results
try:
    with open("audio_analysis_results.json", "r") as f:
        audio_results = json.load(f)
except:
    audio_results = None

try:
    with open("lyrics_analysis_results.json", "r") as f:
        lyrics_results = json.load(f)
except:
    lyrics_results = None

# Determine mood
if audio_results:
    valence = audio_results["mood_suggestions"]["valence"]
    arousal = audio_results["mood_suggestions"]["arousal"]
else:
    valence = "positive"  # default
    arousal = "medium"    # default

# Generate moodboard suggestions
if valence == "positive" and arousal == "high":
    moodboard = {
        "mood": "Happy & Energetic",
        "color_palette": {
            "primary": ["yellow", "orange", "bright blue"],
            "secondary": ["white", "light green", "pink"],
            "accents": ["red", "gold"]
        },
        "lighting": "natural, bright, sunny",
        "locations": [
            "outdoor park/beach",
            "urban street",
            "rooftop skyline",
            "festival/concert"
        ],
        "camera_techniques": [
            "handheld movement",
            "dynamic shots",
            "quick cuts",
            "whip pans"
        ],
        "wardrobe": {
            "style": "casual, colorful",
            "colors": "bright, warm tones",
            "accessories": "minimal, fun"
        },
        "props": [
            "musical instruments",
            "colorful accessories",
            "everyday objects"
        ]
    }
elif valence == "positive" and arousal == "low":
    moodboard = {
        "mood": "Content & Relaxed",
        "color_palette": {
            "primary": ["pastel blue", "soft green", "cream"],
            "secondary": ["light pink", "lavender", "peach"],
            "accents": ["gold", "soft yellow"]
        },
        "lighting": "soft, diffused, golden hour",
        "locations": [
            "cozy indoor spaces",
            "nature settings",
            "home environment",
            "quiet cafes"
        ],
        "camera_techniques": [
            "slow pans",
            "static shots",
            "smooth dollies",
            "gentle transitions"
        ],
        "wardrobe": {
            "style": "comfortable, relaxed",
            "colors": "soft, muted tones",
            "fabrics": "natural, comfortable"
        },
        "props": [
            "books",
            "plants",
            "personal items"
        ]
    }
else:  # negative or mixed
    moodboard = {
        "mood": "Melancholic & Introspective",
        "color_palette": {
            "primary": ["gray", "dark blue", "black"],
            "secondary": ["muted purple", "dark green", "brown"],
            "accents": ["silver", "white"]
        },
        "lighting": "low light, dramatic shadows",
        "locations": [
            "urban night",
            "rainy streets",
            "empty spaces",
            "industrial settings"
        ],
        "camera_techniques": [
            "slow motion",
            "depth of field",
            "handheld (shaky)",
            "long takes"
        ],
        "wardrobe": {
            "style": "dark, layered",
            "colors": "muted, dark tones",
            "textures": "rough, worn"
        },
        "props": [
            "mirrors",
            "old photographs",
            "symbolic objects"
        ]
    }

# Save moodboard
with open("moodboard_suggestions.json", "w", encoding="utf-8") as f:
    json.dump(moodboard, f, indent=2, ensure_ascii=False)

print("✅ Moodboard suggestions generated!")
print(f"📊 Saved to moodboard_suggestions.json")
print(f"\n🎨 Mood: {moodboard['mood']}")
print(f"🎨 Colors: {', '.join(moodboard['color_palette']['primary'])}")
print(f"💡 Lighting: {moodboard['lighting']}")
print(f"📍 Locations: {', '.join(moodboard['locations'][:2])}")
```

Run all three scripts:
```bash
# Complete pipeline
python3 analyze_audio.py 1766703089788_4cdwq9.m4a
python3 analyze_lyrics.py transcription.txt  # after transcription
python3 generate_moodboard.py
```

---

## 📝 Script Template (Dual-Column Format)

Create `script_template.md`:

```markdown
# SRYZ MUSIC VIDEO SCRIPT
## Song: [Title from transcription]
## BPM: [From analysis]
## Mood: [From moodboard]

---

| TIME | AUDIO | VIDEO |
|------|-------|-------|
| 0:00-0:30 | [Instrumental intro] | **Opening Shot**<br>Wide shot of [location from moodboard]<br>[Lighting: natural/golden hour]<br>Camera slowly pans right |
| 0:30-1:00 | **Verse 1**<br>"[First lyrics]" | **Character Introduction**<br>Close-up of protagonist<br>[Wardrobe: described in moodboard]<br>Walking down [location] |
| 1:00-1:30 | **Chorus**<br>"[Chorus lyrics]" | **Performance Sequence**<br>Quick cuts: close-ups, mid-shots<br>High energy camera movement<br>Matching beat |
| 1:30-2:00 | **Verse 2**<br>"[Second verse lyrics]" | **Story Development**<br>Flashback or narrative progression<br>[Props from moodboard]<br>Continuity from Verse 1 |
| 2:00-2:30 | **Chorus**<br>"[Chorus lyrics]" | **Performance Intensified**<br>More dynamic shots<br>Crowd scenes (if applicable)<br>Peak energy |
| 2:30-3:00 | **Bridge**<br>"[Bridge lyrics]" | **Emotional Peak**<br>Slow motion emphasis<br>Dramatic lighting change<br>Close-up emotional performance |
| 3:00-3:30 | **Final Chorus**<br>"[Chorus lyrics]" | **Climax**<br>Maximum visual impact<br>All elements combined<br>[Special effects if budget allows] |
| 3:30-4:10 | **Outro**<br>[Instrumental fade] | **Resolution**<br>Return to opening location<br>Final wide shot<br>Fade to black |

---

## MOODBOARD REFERENCES

**Colors:** [Primary colors from moodboard]
**Lighting:** [Lighting scheme from moodboard]
**Locations:** [Locations from moodboard]
**Wardrobe:** [Wardrobe from moodboard]
**Props:** [Key props from moodboard]

---

## TECHNICAL NOTES

- **Camera:** [Camera model available]
- **Format:** [Resolution: 1080p/4K]
- **Frame Rate:** [24fps for cinematic / 60fps for smooth]
- **Color Grading:** [Warm/cool/contrast]
- **Aspect Ratio:** [16:9 standard / 2.35:1 cinematic]
```

---

## 🎯 Next Steps

1. **Transcribe audio** using recommended tools
2. **Run analysis scripts** to get BPM and mood
3. **Create moodboard** using suggestions
4. **Fill in script template** with creative vision
5. **Storyboard** key scenes
6. **Plan shoot** based on script

---

## 💡 Pro Tips

- **Transcription**: Use time-stamped output for easier video sync
- **BPM Detection**: Verify with multiple tools for accuracy
- **Moodboard**: Include actual image references, not just descriptions
- **Script**: Be specific about camera angles and movements
- **Storyboard**: Draw simple panels or use photos from moodboard

---

**Need Help?** Refer to the comprehensive research report for detailed explanations of each step.
