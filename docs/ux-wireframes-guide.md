# SRYZ Visual Wireframes Guide

**Purpose**: Quick visual reference for core UI layouts
**Created**: December 26, 2025
**Target**: Developers, designers, stakeholders

---

## 1. Landing Page Wireframe

```
┌─────────────────────────────────────────────────────────────────────────────────────┐
│  ☰  SRYZ logo                                          [PL/EN ▼] [Sign Up] [Login]        │
├─────────────────────────────────────────────────────────────────────────────────────┤
│                                                                                      │
│  ╔═════════════════════════════════════════════════════════════════════════════╗ │
│  ║  🎵 Transform Your Lyrics into AI Music - In Polish                           ║ │
│  ║                                                                             ║ │
│  ║  [Watch 30-second demo ▶]                                                     ║ │
│  ║                                                                             ║ │
│  ║  SRYZ analyzes your song lyrics and generates optimized prompts              ║ │
│  ║  for AI music platforms like Suno AI and Udio.                              ║ │
│  ║                                                                             ║ │
│  ║  ✅ Native Polish support      ✅ 87% better prompts     ✅ Works with Suno & Udio ║ │
│  ║                                                                             ║ │
│  ║  [Start Free →]    [See How It Works]    [View Templates]                    ║ │
│  ╚═════════════════════════════════════════════════════════════════════════════╝ │
│                                                                                      │
│  ┌──────────────────┐  ┌──────────────────┐  ┌──────────────────┐               │
│  │ 📝 Upload        │  │ 🎯 Generate       │  │ 🚀 Create Music  │               │
│  │                  │  │                  │  │                  │               │
│  │ Paste or type     │  │ Get AI-optimized  │  │ Export to Suno   │               │
│  │ your lyrics       │  │ prompts in       │  │ or Udio with    │               │
│  │                  │  │ seconds          │  │ one click        │               │
│  │                  │  │                  │  │                  │               │
│  │ [Try Demo]        │  │ [See Example]     │  │ [Get Started]     │               │
│  └──────────────────┘  └──────────────────┘  └──────────────────┘               │
│                                                                                      │
│  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ │
│                                                                                      │
│  Trusted by 10,000+ Polish musicians                                            │
│  ⭐⭐⭐⭐⭐ 4.9/5 rating - Product Hunt                                          │
│  🏆 Featured in: TechCrunch, Billboard, Polityka                                   │
│                                                                                      │
│  ┌─────────────────────────────────────────────────────────────────────────────┐  │
│  │  "Finally, an AI tool that understands Polish music!"                      │  │
│  │  ~ Kasia, Indie Songwriter, Warsaw                                          │  │
│  └─────────────────────────────────────────────────────────────────────────────┘  │
│                                                                                      │
└─────────────────────────────────────────────────────────────────────────────────────┘
```

---

## 2. Main Application Wireframe (Desktop)

```
┌─────────────────────────────────────────────────────────────────────────────────────┐
│  SRYZ logo             [Search prompts...]                [PL/EN ▼] [Kasia] [⚙️]    │
├─────────────────────────────────────────────────────────────────────────────────────┤
│                                                                                      │
│  [📤 Upload] [📋 Library] [🎯 Templates] [💾 Saved] [🔗 Shared]                         │
│                                                                                      │
│  ┌─────────────────────────────────────────────────────────────────────────────┐   │
│  │  📝 LYRICS INPUT                           🎯 PROMPT GENERATION              │   │
│  │  ┌─────────────────────────────┐    ┌─────────────────────────────┐    │   │
│  │  │ Paste lyrics here...        │    │ [CO-STAR Framework Preview] │    │   │
│  │  │                             │    │                             │    │   │
│  │  │ W nocnej ciszy słychać...  │    │ [Context section...]       │    │   │
│  │  │ Myśli krążą po głowie...  │    │                             │    │   │
│  │  │                             │    │ [Objective section...]      │    │   │
│  │  └─────────────────────────────┘    │                             │    │   │
│  │  🇵🇱 Polish detected                    │ [Style section...]          │    │   │
│  │  [Clear] [Paste] [Upload file]       │                             │    │   │
│  └─────────────────────────────────────┘    └─────────────────────────────┘    │   │
│                                                 Quality: ████████░░ 87%           │   │
│  ┌─────────────────────────────────────────────────────────────────────────────┐   │
│  │  📊 ANALYSIS RESULTS                                                              │   │
│  │  ┌────────────┐  ┌────────────┐  ┌────────────┐  ┌────────────┐           │   │
│  │  │ Mood       │  │ Genre      │  │ Structure  │  │ Polish     │           │   │
│  │  │            │  │            │  │            │  │ Flow       │           │   │
│  │  │ Melan-     │  │ Pop        │  │ Verse-     │  │ Rymy: AABB │           │   │
│  │  │ cholic     │  │ Ballad     │  │ Chorus     │  │ Cisza: ✓   │           │   │
│  │  │ Hopeful    │  │            │  │ Bridge     │  │ Bezy Róż.  │           │   │
│  │  │            │  │            │  │            │  │            │           │   │
│  │  │ [Edit ▼]   │  │ [Edit ▼]   │  │ [Edit ▼]   │  │ [Optimize] │           │   │
│  │  └────────────┘  └────────────┘  └────────────┘  └────────────┘           │   │
│  └─────────────────────────────────────────────────────────────────────────────┘   │
│                                                                                      │
│  [🔄 Regenerate] [📋 Copy Prompt] [🚀 Copy to Suno] [💾 Save] [🔗 Share]                      │
│                                                                                      │
│  ┌─────────────────────────────────────────────────────────────────────────────┐   │
│  │  RECENT PROJECTS                                                                  │   │
│  │  [Summer Memories] 2h ago  │  [Ballada o miłości] Yesterday  │  [Eksperyment] 3d ago│   │
│  └─────────────────────────────────────────────────────────────────────────────┘   │
│                                                                                      │
└─────────────────────────────────────────────────────────────────────────────────────┘
```

---

## 3. Mobile Application Wireframe

```
┌─────────────────────────────────┐
│  ☰  SRYZ        PL/EN    👤     │
├─────────────────────────────────┤
│                                 │
│  [📤 Upload Lyrics]             │
│  [📋 My Library]                │
│  [🎯 Templates]                 │
│                                 │
│  ┌───────────────────────────┐  │
│  │  QUICK INPUT               │  │
│  │  ┌─────────────────────┐  │  │
│  │  │ Paste lyrics here... │  │  │
│  │  │                     │  │  │
│  │  └─────────────────────┘  │  │
│  │  🇵🇱 Polish detected         │  │
│  └───────────────────────────┘  │
│                                 │
│  [🚀 Generate for Suno]         │
│                                 │
│  ┌───────────────────────────┐  │
│  │  📊 Analysis                │  │
│  │  ┌─────────────────────┐  │  │
│  │  │ Mood: 🌙 Melancholic│  │  │
│  │  │ Genre: 🎵 Pop      │  │  │
│  │  │ Polish: ✓          │  │  │
│  │  └─────────────────────┘  │  │
│  └───────────────────────────┘  │
│                                 │
│  Recent:                        │
│  • Summer Memories 2h           │
│  • Ballada o miłości Yesterday   │
│                                 │
├─────────────────────────────────┤
│ [🏠 Home] [📝 Create] [📚 Lib.] [👤]│
└─────────────────────────────────┘
```

---

## 4. Prompt Generation Flow Wireframe

```
┌─────────────────────────────────────────────────────────────────────────────────────┐
│  ⏳ Processing Your Lyrics...                                                            │
├─────────────────────────────────────────────────────────────────────────────────────┤
│                                                                                      │
│  ✅ Language detected: Polish                                                         │
│  ✅ Tokenization: 127 words                                                          │
│  ⏳ Sentiment analysis...                                                             │
│  ⏳ Rhyme scheme extraction...                                                        │
│  ⏳ Genre classification...                                                           │
│                                                                                      │
│  [████████████████████░░░░] 80%                                                     │
│                                                                                      │
│  💡 We found: melancholic mood, pop ballad genre, AABB rhyme scheme                  │
│                                                                                      │
│  Estimated time: 10 seconds remaining                                                 │
│                                                                                      │
└─────────────────────────────────────────────────────────────────────────────────────┘
```

---

## 5. Quality Dashboard Wireframe

```
┌─────────────────────────────────────────────────────────────────────────────────────┐
│  📊 Prompt Quality Score: 87% (Grade B)                                                  │
├─────────────────────────────────────────────────────────────────────────────────────┤
│                                                                                      │
│  ┌─────────────────────────────────────────────────────────────────────────────┐   │
│  │  SPECIFICITY        ████████░░ 90%                                            │   │
│  │  └─ "Excellent concrete details"                                              │   │
│  │                                                                             │   │
│  │  STRUCTURE         ████████░░ 85%                                            │   │
│  │  └─ "Well-organized, clear sections"                                      │   │
│  │                                                                             │   │
│  │  CREATIVITY        ██████░░░░ 75%                                            │   │
│  │  └─ "Moderate - add more unique elements"                                 │   │
│  │                                                                             │   │
│  │  CONSTRAINTS       ████████░░ 95%                                            │   │
│  │  └─ "Very clear boundaries"                                                │   │
│  │                                                                             │   │
│  │  CONTEXT           ████████░░ 80%                                            │   │
│  │  └─ "Good background, could add more"                                     │   │
│  │                                                                             │   │
│  │  CLARITY           ████████░░ 95%                                            │   │
│  │  └─ "Excellent directives"                                                 │   │
│  └─────────────────────────────────────────────────────────────────────────────┘   │
│                                                                                      │
│  💡 Priority Improvements:                                                          │
│  ┌─────────────────────────────────────────────────────────────────────────────┐   │
│  │  1. Creativity (+10% potential)                                                │   │
│  │     → Add metaphors or analogies                                               │   │
│  │     → Include hypothetical scenarios                                           │   │
│  │                                                                             │   │
│  │  2. Context (+8% potential)                                                    │   │
│  │     → Add target audience demographics                                          │   │
│  │     → Specify use case (commercial/artistic)                                  │   │
│  └─────────────────────────────────────────────────────────────────────────────┘   │
│                                                                                      │
│  [Apply Improvements] [Regenerate] [Export]                                            │
└─────────────────────────────────────────────────────────────────────────────────────┘
```

---

## 6. A/B Testing Wireframe

```
┌─────────────────────────────────────────────────────────────────────────────────────┐
│  ⚖️  A/B Test: Compare Prompts                                                        │
├─────────────────────────────────────────────────────────────────────────────────────┤
│                                                                                      │
│  ┌─────────────────────────────┬─────────────────────────────┐                       │
│  │  Version A (Current)        │  Version B (Variation)      │                       │
│  ├─────────────────────────────┼─────────────────────────────┤                       │
│  │  "Create a melancholic       │  "Create an energetic        │                       │
│  │   Polish pop ballad..."      │   Polish pop song..."       │                       │
│  │                             │                             │                       │
│  │  Mood: melancholic           │  Mood: upbeat               │                       │
│  │  Tempo: 70-80 BPM             │  Tempo: 110-120 BPM          │                       │
│  │  Quality: 87% ★              │  Quality: 82%               │                       │
│  │                             │                             │                       │
│  │  [Listen]                    │  [Listen]                    │                       │
│  │  [👍 89] [👎 11]              │  [👍 76] [👎 24]              │                       │
│  │  [Select ○]                  │  [Select ○]                  │                       │
│  └─────────────────────────────┴─────────────────────────────┘                       │
│                                                                                      │
│  Key Differences:                                                                     │
│  • Energy level: +40% more energetic                                                │
│  • Tempo: +50 BPM faster                                                             │
│  • Instrumentation: synths vs piano                                                 │
│                                                                                      │
│  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ │
│                                                                                      │
│  📊 Test Results (Dec 23-26, 2025)                                                  │
│                                                                                      │
│  • Generations: 127 vs 142                                                          │
│  • Average quality: 87% vs 82%                                                      │
│  • Thumbs up: 89% vs 76%                                                            │
│  • Shared: 23 vs 31 times                                                           │
│                                                                                      │
│  Winner: ★ Version A (Melancholic) - 13% preference                                 │
│                                                                                      │
│  Insights: Users preferred melancholic mood, but Version B was shared more.         │
│  Consider: "Melancholic but energetic" hybrid approach                              │
│                                                                                      │
│  [Select Winner: A] [Create Hybrid] [Retest] [Close]                                 │
└─────────────────────────────────────────────────────────────────────────────────────┘
```

---

## 7. Polish Optimizations Wireframe

```
┌─────────────────────────────────────────────────────────────────────────────────────┐
│  🇵🇱 Polish Flow Optimizations                                                           │
├─────────────────────────────────────────────────────────────────────────────────────┤
│                                                                                      │
│  Your lyrics:                                                                       │
│  ┌─────────────────────────────────────────────────────────────────────────────┐   │
│  │  W nocnej ciszy słychać tylko serce bicie                                          │   │
│  │  Myśli krążą po głowie, szukają drogi                                              │   │
│  └─────────────────────────────────────────────────────────────────────────────┘   │
│                                                                                      │
│  Detected Patterns:                                                                │
│  ┌─────────────────────────────────────────────────────────────────────────────┐   │
│  │  ✅ Rhythm: Iambic (jambiczny)                                                 │   │
│  │     Pattern: x X x X (stressed unstressed)                                     │   │
│  │                                                                             │   │
│  │  ✅ Rhymes: AABB (perfect rhymes)                                               │   │
│  │     bicie/skronie (line 1-2)                                                   │   │
│  │     drogi/snu (line 3-4)                                                       │   │
│  │                                                                             │   │
│  │  ✅ Grammatical Cases: Nominative, locative                                       │   │
│  │     serce (nominative), głowie (locative)                                       │   │
│  │                                                                             │   │
│  │  ⚠️  Cultural Idioms: None detected                                            │   │
│  │     Suggestion: Add Polish idioms for authenticity                           │   │
│  └─────────────────────────────────────────────────────────────────────────────┘   │
│                                                                                      │
│  Optimizations Applied:                                                            │
│  ┌─────────────────────────────────────────────────────────────────────────────┐   │
│  │  ☑ Preserve Polish rhymes (rymy)                                                 │   │
│  │     Maintains "bicie/skronie" and "drogi/snu" rhyme sounds                       │   │
│  │                                                                             │   │
│  │  ☑ Maintain grammatical cases (odmiana)                                        │   │
│  │     Preserves "serce" and "głowie" case endings                                │   │
│  │                                                                             │   │
│  │  ☐ Add Polish cultural references                                               │   │
│  │     Example idioms: "jak sierotka w nocy", "polskie drogi"                      │   │
│  └─────────────────────────────────────────────────────────────────────────────┘   │
│                                                                                      │
│  Resulting Prompt Quality:                                                           │
│  Without optimizations: 72%                                                          │
│  With optimizations: 87% (↑15% improvement)                                         │
│                                                                                      │
│  [Apply All Optimizations] [Customize] [Learn More]                                  │
└─────────────────────────────────────────────────────────────────────────────────────┘
```

---

## 8. CLI Interface Wireframe

```bash
$ sryz analyze
📝 SRYZ Prompt Analyzer v1.0
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📄 Paste your lyrics (Ctrl+D when done):
> W nocnej ciszy słychać tylko serce bicie
> Myśli krążą po głowie, szukają drogi
> Chcę znaleźć odpowiedź na pytania
> Co niesie ze sobą jutro
>
^D

🔍 Analyzing lyrics...

  ✅ Language detection: Polish (99% confidence)
  ✅ Tokenization: 127 words, 4 lines
  ✅ Section detection: verse structure (no chorus found)
  ⏳ Sentiment analysis...
  ⏳ Rhyme scheme extraction...
  ⏳ Genre classification...

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Analysis Complete!
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  📊 Analysis Results:
     Mood: Melancholic (primary), Hopeful (secondary), Reflective (tertiary)
     Genre: Pop ballad (87%), Rock (12%), Electronic (1%)
     Structure: Verse only (consider adding chorus)
     Polish Flow: Rymy AABB, Rhythm iambic, Cases maintained

  🎯 Generated Prompt:
     ┌────────────────────────────────────────────────────────────────────┐
     │ [Context]                                                             │
     │ Create a Polish pop ballad about nighttime introspection and     │
     │ emotional self-discovery...                                          │
     │                                                                       │
     │ [Objective]                                                          │
     │ Generate melancholic yet hopeful lyrics with verse structure... │
     │                                                                       │
     │ [Style]                                                               │
     │ Tempo: Slow (70-80 BPM), Key: A minor, Time: 4/4                   │
     │ Instrumentation: Piano, strings, subtle drums...                    │
     │                                                                       │
     │ [Tone]                                                                │
     │ Intimate, reflective, emotional, bittersweet                         │
     │                                                                       │
     │ [Audience]                                                            │
     │ Polish pop fans, ages 25-45, appreciate emotional depth...         │
     │                                                                       │
     │ [Response]                                                            │
     │ Polish lyrics with natural flow, grammatical correctness,        │
     │ AABB rhyme scheme...                                                 │
     └────────────────────────────────────────────────────────────────────┘

  📈 Quality Score: ████████░░ 87% (Grade B)
     Specificity: 90% • Structure: 85% • Creativity: 75%

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  Options:
    [1] Regenerate with different settings
    [2] Edit analysis results
    [3] Copy prompt to clipboard
    [4] Save to file
    [5] Generate on Suno AI (opens browser)
    [6] View full analysis JSON
    [q] Quit

  Choose option [1-6/q]: 3

  ✓ Prompt copied to clipboard!

$ █
```

---

## 9. Settings & Preferences Wireframe

```
┌─────────────────────────────────────────────────────────────────────────────────────┐
│  ⚙️ Settings                                                                           │
├─────────────────────────────────────────────────────────────────────────────────────┤
│                                                                                      │
│  ┌─────────────────────────────────────────────────────────────────────────────┐   │
│  │  🌐 Language & Region                                                           │   │
│  │  ┌─────────────────────────────────────────────────────────────────────────┐  │   │
│  │  Interface Language: [🇵🇱 Polish ▼]                                           │  │   │
│  │  Default Lyrics Language: [Auto-detect ▼]                                 │  │   │
│  │  Timezone: [Europe/Warsaw (UTC+1) ▼]                                    │  │   │
│  │  Date Format: [DD.MM.YYYY ▼]                                               │  │   │
│  │                                                                             │  │
│  │  [Save Changes]                                                              │  │   │
│  │  └─────────────────────────────────────────────────────────────────────────┘  │   │
│  └─────────────────────────────────────────────────────────────────────────────┘   │
│                                                                                      │
│  ┌─────────────────────────────────────────────────────────────────────────────┐   │
│  │  🎵 Platform Preferences                                                         │   │
│  │  ┌─────────────────────────────────────────────────────────────────────────┐  │   │
│  │  Default Platform: [● Suno AI] [○ Udio] [○ Custom LLM]                   │  │   │
│  │  Auto-open platform after generation: [✓]                                  │  │   │
│  │  Copy prompt to clipboard on generate: [✓]                                  │  │   │
│  │                                                                             │  │
│  │  Connected Accounts:                                                          │  │   │
│  │  ☑ Suno AI (connected as kasia@email.com)                                  │  │   │
│  │  ☐ Udio (connect →)                                                            │  │   │
│  │                                                                             │  │
│  │  [Save Changes]                                                              │  │   │
│  │  └─────────────────────────────────────────────────────────────────────────┘  │   │
│  └─────────────────────────────────────────────────────────────────────────────┘   │
│                                                                                      │
│  ┌─────────────────────────────────────────────────────────────────────────────┐   │
│  │  🎨 Appearance                                                                    │   │
│  │  ┌─────────────────────────────────────────────────────────────────────────┐  │   │
│  │  Theme: [● Light] [○ Dark] [○ System]                                     │  │   │
│  │  Accent Color: [● Blue] [○ Purple] [○ Green] [○ Orange]                    │  │   │
│  │  Font Size: [● Medium (16px)] [○ Large (18px)] [○ Extra Large (20px)]         │  │   │
│  │  Animation Speed: [● Normal] [○ Reduced] [○ None]                             │  │   │
│  │                                                                             │  │
│  │  Accessibility:                                                               │  │   │
│  │  ☑ High contrast mode                                                          │  │   │
│  │  ☑ Reduce motion                                                               │  │   │
│  │  ☑ Screen reader optimization                                                  │  │   │
│  │                                                                             │  │
│  │  [Save Changes]                                                              │  │   │
│  │  └─────────────────────────────────────────────────────────────────────────┘  │   │
│  └─────────────────────────────────────────────────────────────────────────────┘   │
│                                                                                      │
│  ┌─────────────────────────────────────────────────────────────────────────────┐   │
│  │  🤖 Advanced Options                                                               │   │
│  │  ┌─────────────────────────────────────────────────────────────────────────┐  │   │
│  │  Processing: [● Balanced] [○ Fast] [○ High Quality]                       │  │   │
│  │  Save prompts automatically: [✓]                                           │  │   │
│  │  Anonymous analytics: [✓] Help improve SRYZ                                │  │   │
│  │  Beta features: [☐] Enable experimental features                           │  │   │
│  │                                                                             │  │
│  │  [Save Changes]                                                              │  │   │
│  │  └─────────────────────────────────────────────────────────────────────────┘  │   │
│  └─────────────────────────────────────────────────────────────────────────────┘   │
│                                                                                      │
│  [Save All Settings] [Reset to Defaults] [Cancel]                                         │
│                                                                                      │
└─────────────────────────────────────────────────────────────────────────────────────┘
```

---

## 10. Teaching Mode Wireframe (Educator Persona)

```
┌─────────────────────────────────────────────────────────────────────────────────────┐
│  🎓 TEACHING MODE ENABLED                                                             │
├─────────────────────────────────────────────────────────────────────────────────────┤
│  ⚙️ [Exit Teaching Mode]                                                               │
└─────────────────────────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────────────────────┐
│  👥 Class Project: Physics Songs - 15A (24 students)                                     │
│                                                                                      │
│  ┌─────────────────────────────────────────────────────────────────────────────┐   │
│  │  📚 Lesson: Newton's Laws of Motion                                               │   │
│  │  Subject: Physics (Mechanics)                                                   │   │
│  │  Age Group: 14-16 years old                                                     │   │
│  │  Duration: 45 minutes                                                             │   │
│  └─────────────────────────────────────────────────────────────────────────────┘   │
│                                                                                      │
│  🎯 Learning Objectives:                                                             │
│  • Understand Newton's three laws through music                                     │
│  • Memorize key terms: inertia, force, acceleration                              │
│  • Create memorable song with educational content                                   │
│                                                                                      │
│  ┌─────────────────────────────────────────────────────────────────────────────┐   │
│  │  📝 Student Inputs (Live)                                                        │   │
│  │  ┌─────────────────────────────────────────────────────────────────────────┐ │   │
│  │  │ "What key terms should we include?"                                         │ │   │
│  │  │ 💬 Class response: inertia, force, mass, acceleration...              │ │ │   │
│  │  │                                                                         │ │   │
│  │  │ [Add to prompt: + inertia, force, mass, acceleration]                  │ │   │
│  │  └─────────────────────────────────────────────────────────────────────────┘ │   │
│  │                                                                             │   │
│  │  Student Progress:                                                            │   │
│  │  ████████████████████████████░░░░ 20/24 Complete (83%)                     │   │
│  │                                                                             │   │
│  │  🟢 Ready: 20 students  🟡 In Progress: 4 students  🔴 Not Started: 0        │   │
│  └─────────────────────────────────────────────────────────────────────────────┘   │
│                                                                                      │
│  [Generate for Class] [Show Sample] [Download All Results]                                   │
└─────────────────────────────────────────────────────────────────────────────────────┘
```

---

## Wireframe Legend

### Symbols & Icons
- 📝 = Text input/editor
- 🎯 = Target/generation
- 📊 = Analysis/results
- 🚀 = Action/launch
- 💾 = Save
- 🔗 = Share
- ⚙️ = Settings
- 🔄 = Refresh/regenerate
- 📋 = Copy
- ✅ = Success/complete
- ⏳ = In progress
- ❌ = Error/failed
- ⚠️ = Warning
- 💡 = Tip/suggestion
- 🌐 = Language/international
- 🎵 = Music/audio
- 🎨 = Design/appearance
- 🤖 = AI/automation
- 👤 = User/profile
- 🏠 = Home/dashboard
- 📚 = Library/templates
- 🎓 = Education/teaching

### Color Coding in Wireframes
- ████████ = Primary action/selected
- ░░░░░░░░ = Disabled/inactive
- 🟢 = Success/complete
- 🟡 = In progress/warning
- 🔴 = Error/not started
- ⚫ = Inactive/unavailable

---

## Implementation Notes

### Responsive Breakpoints
```
Mobile:     320px - 479px   (Single column, stacked)
Tablet:     480px - 767px   (2 columns, simplified)
Laptop:     768px - 1023px  (3 columns, full features)
Desktop:    1024px+          (4 columns, all features)
```

### Touch Targets (Mobile)
- Minimum size: 44x44px (WCAG 2.1 AAA)
- Spacing: 12px between targets
- Bottom navigation: 56px height
- Tap targets: 48x48px recommended

### Font Sizes (Responsive)
```
H1 (Hero):     48px → 32px  (desktop → mobile)
H2 (Section):  32px → 24px
H3 (Card):     24px → 20px
Body:          16px (same)
Small:         14px (same)
Caption:       12px (same)
```

---

**Document Status**: Complete Visual Wireframes
**Version**: 1.0
**Last Updated**: December 26, 2025

---

*For complete UX documentation, see ux-design-document.md and ux-design-summary.md*
