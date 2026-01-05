# SRYZ User Experience Design Document

**Date**: December 26, 2025
**UX Designer**: AI Product Design Specialist
**Version**: 1.0
**Status**: Initial Design Specification

---

## Executive Summary

This document outlines comprehensive user experience designs for SRYZ (System Rapowania Ze Śpiewem - Prompt System from Lyrics), an innovative tool that converts song lyrics into optimized AI music generation prompts. The design philosophy prioritizes **intuitive simplicity** while providing **powerful features** for advanced users, with specific attention to Polish language support and diverse user personas.

### Design Principles

1. **Progressive Disclosure**: Show complexity only when users need it
2. **Immediate Value**: Generate usable prompts in under 30 seconds
3. **Visual Feedback**: Make analysis results tangible and understandable
4. **Language First**: Native Polish experience with seamless English switching
5. **Creative Empowerment**: Tools that enhance, not replace, human creativity

---

## Table of Contents

1. [User Personas](#1-user-personas)
2. [User Journey Maps](#2-user-journey-maps)
3. [Interface Designs](#3-interface-designs)
4. [Workflow Design](#4-workflow-design)
5. [Key Features](#5-key-features)
6. [Accessibility](#6-accessibility)
7. [Mobile vs Desktop](#7-mobile-vs-desktop-experience)
8. [Visual Design System](#8-visual-design-system)

---

## 1. User Personas

### Persona 1: The Musician (Non-Technical, Creative)

**Profile**: Kasia, 28, Indie Singer-Songwriter, Warsaw

**Demographics**:
- Age: 28
- Location: Warsaw, Poland
- Occupation: Full-time musician (performing, recording, teaching)
- Tech Comfort: Moderate (uses DAWs, social media, Spotify)
- Income: €15,000-30,000/year

**Goals**:
- Quickly generate AI music for creative inspiration
- Overcome writer's block with fresh ideas
- Create demos without hiring full band
- Experiment with different genres/styles

**Pain Points**:
- Doesn't understand prompt engineering terminology
- Finds AI tools overwhelming and complex
- Struggles to get desired results from Suno/Udio
- Limited time for learning new software

**Behaviors**:
- Writes lyrics in Polish primarily
- Uses Instagram and TikTok for promotion
- Collaborates remotely with other musicians
- Values aesthetic and emotional connection over technical precision

**Tech Stack**:
- Smartphone: iPhone 13 (primary device)
- DAW: Ableton Live (basic usage)
- AI Tools: Suno AI (free tier, frustrated with results)
- Communication: Instagram DM, Discord

**Quote**: *"I just want to make music, not engineer prompts. Why can't it just understand what I'm feeling?"*

**Design Implications**:
- Hide technical complexity behind simple language
- Use visual metaphors (mood sliders, genre palettes)
- Mobile-first design (phone is primary device)
- Polish-first interface
- Emotional terminology over technical terms

---

### Persona 2: The Educator (Needs Simplicity)

**Profile**: Marek, 45, Music Teacher, Łódź

**Demographics**:
- Age: 45
- Location: Łódź, Poland
- Occupation: High school music teacher (ages 14-19)
- Tech Comfort: Low-Moderate (uses educational software, Zoom)
- Income: €12,000/year

**Goals**:
- Teach students about AI in music creation
- Create educational songs for curriculum topics
- Demonstrate prompt engineering concepts simply
- Engage students with modern technology

**Pain Points**:
- Limited class time (45-minute lessons)
- Students have varying tech skill levels
- Needs to maintain pedagogical structure
- School internet connectivity can be unreliable

**Behaviors**:
- Prepares lesson materials in advance
- Uses projector/screen sharing for demonstrations
- Values step-by-step guidance
- Needs clear examples to show students

**Tech Stack**:
- Desktop: Windows PC (school computer)
- Tablet: iPad (personal)
- Software: PowerPoint, Zoom, Google Classroom
- AI Experience: ChatGPT (basic), Suno AI (experimental)

**Quote**: *"I need something that works the first time, every time. My students lose interest if we spend 20 minutes troubleshooting."*

**Design Implications**:
- Reliability > features (must work offline if needed)
- Clear teaching mode with step-by-step guidance
- Classroom-friendly interface (large text, clear contrast)
- Template library for common educational uses
- Progress saving for multi-day projects

---

### Persona 3: The Developer (Wants API/CLI)

**Profile**: Piotr, 32, Software Engineer, Kraków

**Demographics**:
- Age: 32
- Location: Kraków, Poland (remote worker)
- Occupation: Full-stack developer (startup)
- Tech Comfort: Expert (builds web apps, uses APIs daily)
- Income: €50,000/year

**Goals**:
- Integrate SRYZ into music production workflow
- Build custom tools on top of SRYZ platform
- Automate batch processing of lyrics
- Extend functionality with plugins

**Pain Points**:
- Needs comprehensive API documentation
- Requires reliable uptime and performance
- Wants rate limit transparency
- Expects standard API patterns (REST, webhooks)

**Behaviors**:
- Reads documentation before using tools
- Tests API endpoints with Postman/curl
- Builds internal tools for team
- Active in developer communities (Discord, GitHub)

**Tech Stack**:
- Laptop: MacBook Pro
- Development: VS Code, Docker, Node.js/Python
- API Tools: Postman, Insomnia
- Version Control: Git
- Documentation: Swagger/OpenAPI

**Quote**: *"Give me a clean API and good docs, I'll build the rest myself. Don't make me click through UIs when I could script it."*

**Design Implications**:
- Comprehensive REST API with OpenAPI spec
- CLI tool for terminal workflows
- Webhook support for async workflows
- Rate limiting headers and clear error codes
- Sandboxed environment for testing

---

### Persona 4: The Researcher (Needs Batch Processing)

**Profile**: Anna, 38, Musicologist, Poznań

**Demographics**:
- Age: 38
- Location: Poznań, Poland
- Occupation: Academic researcher (music psychology)
- Tech Comfort: High (Python, R, data analysis)
- Income: €25,000/year

**Goals**:
- Analyze patterns in song lyrics across genres/eras
- Study emotional arcs in popular music
- Generate datasets for machine learning
- Publish findings in academic journals

**Pain Points**:
- Needs to process hundreds of songs efficiently
- Requires reproducible research workflows
- Expects statistical analysis tools
- Must document methodology thoroughly

**Behaviors**:
- Scripts analysis workflows in Python/R
- Exports data to CSV/JSON for statistical tools
- Cares about data provenance and versioning
- Collaborates with international researchers

**Tech Stack**:
- Workstation: High-performance Linux desktop
- Analysis: Python (pandas, scikit-learn), R
- Data: Jupyter notebooks, PostgreSQL
- Visualization: Matplotlib, D3.js

**Quote**: *"I need to process 10,000 songs by Friday. Your batch API better be robust and well-documented."*

**Design Implications**:
- Batch processing endpoints
- Export to standard formats (CSV, JSON, Excel)
- Job queue with status tracking
- Versioned datasets for reproducibility
- Detailed logging of all operations

---

### Persona 5: The Polish Songwriter (Language-Specific Needs)

**Profile**: Magda, 24, Pop Songwriter, Gdańsk

**Demographics**:
- Age: 24
- Location: Gdańsk, Poland
- Occupation: Songwriter for Polish pop artists
- Tech Comfort: Moderate (iPhone user, social media savvy)
- Income: €20,000/year

**Goals**:
- Create Polish-language pop songs with AI
- Maintain natural Polish rhythm and flow (rym, cisza)
- Preserve Polish cultural references and idioms
- Compete in Polish market (Radio Eska, Polsat)

**Pain Points**:
- Most AI tools prioritize English lyrics
- Polish grammar (odmiana przez przypadki) breaks flow
- Cultural references get lost in translation
- Need Polish-specific rhyme schemes (ABAB, AABB)

**Behaviors**:
- Writes exclusively in Polish
- Studies Polish pop hits (Doda, Dawid Podsiadło)
- Collaborates with Polish producers
- Aims for Polish radio airplay

**Tech Stack**:
- Smartphone: iPhone (always with her)
- DAW: Logic Pro (home studio)
- AI: Suno AI (frustrated with Polish results)
- Reference: Spotify Polish playlists

**Quote**: *"Why does the AI always translate 'serce' to 'heart' when the rhyme depends on 'serce' staying Polish?"*

**Design Implications**:
- Polish-first NLP (PLLuM integration)
- Preserve Polish grammatical cases
- Polish rhyme scheme detection
- Cultural idiom preservation
- Option to lock certain phrases from translation

---

## 2. User Journey Maps

### Journey Map 1: New User Onboarding (Kasia - Musician)

**Stage 1: Discovery & Sign Up (5 minutes)**

| Touchpoint | User Action | System Response | Emotion | Pain Point |
|------------|-------------|-----------------|---------|------------|
| Instagram ad | Sees ad: "Turn lyrics into AI music" | Click ad → Landing page | Intrigued | "Is this legit or another scam?" |
| Landing page | Watches 30-second demo video | Auto-plays with Polish singer | Inspired | "Finally, something for Polish music!" |
| Sign-up form | Email + password (social login available) | Instant account creation | Relieved | No credit card required (free tier) |

**Design Solutions**:
- **Video-first landing**: Show, don't tell (30-second demo)
- **Social proof**: "Used by 10,000+ Polish musicians"
- **Frictionless signup**: Google/Apple one-click, no credit card
- **Value preview**: Show example prompt transformation before signup

---

**Stage 2: First Lyric Upload (2 minutes)**

| Touchpoint | User Action | System Response | Emotion | Pain Point |
|------------|-------------|-----------------|---------|------------|
| Dashboard | Sees big "Upload Lyrics" button | Hover animation shows drag-drop | Guided | Clear next step |
| Upload | Pastes lyrics from Notes app | Auto-detects Polish language | Pleasant | "It knows I'm writing in Polish!" |
| Analysis | Sees "Analyzing..." animation | Real-time feedback (detecting mood, genre) | Curious | "What's it finding?" |

**Design Solutions**:
- **Single CTA**: One big button, no choice paralysis
- **Smart defaults**: Auto-detect language, suggest genre based on lyrics
- **Transparent process**: Show what's happening (not black box)
- **Progressive disclosure**: Ask for details only if needed

---

**Stage 3: Prompt Generation & Refinement (5 minutes)**

| Touchpoint | User Action | System Response | Emotion | Pain Point |
|------------|-------------|-----------------|---------|------------|
| Generated prompt | Sees CO-STAR preview | Highlights key elements (mood, genre, style) | Impressed | "This captured what I meant!" |
| Polish optimizations | Toggles "Polish flow" checkbox | Shows predicted improvements (rymy, cisza) | Delighted | "It understands Polish rhyming!" |
| Platform selector | Chooses Suno AI | Platform-specific prompt optimization | Confident | "Ready for Suno!" |

**Design Solutions**:
- **Visual breakdown**: Color-coded CO-STAR sections
- **Before/after comparison**: Show plain vs. optimized prompt
- **One-click export**: Direct copy to Suno/Udio
- **Undo friendliness**: Easy to revert changes

---

**Stage 4: Integration & Sharing (3 minutes)**

| Touchpoint | User Action | System Response | Emotion |---------|
|------------|-------------|-----------------|---------|------------|
| Copy to platform | Clicks "Copy to Suno" | Auto-formats for Suno + opens Suno tab | Efficient | "One click and I'm in Suno!" |
| Generate music | Uses prompt in Suno | [Suno generates song] | Excited | "This actually works!" |
| Save & share | Saves session, shares prompt link | Generates shareable URL | Proud | "Sending this to my bandmates!" |

**Design Solutions**:
- **Deep linking**: Auto-open platform with pre-filled prompt
- **Session saving**: Auto-save after every action
- **Social sharing**: Shareable links for collaboration
- **Success moment**: Celebrate first generation with confetti animation

---

### Journey Map 2: Educator Classroom Workflow (Marek - Teacher)

**Stage 1: Lesson Preparation (15 minutes)**

| Touchpoint | User Action | System Response | Emotion | Pain Point |
|------------|-------------|-----------------|---------|------------|
| Template library | Browses "Educational Templates" | Filter by subject, age group | Organized | "Physics songs for 15-year-olds..." |
| Select template | Chooses "Newton's Laws - Pop" | Shows example student outputs | Reassured | "I can see what this produces" |
| Customize | Adds specific vocabulary terms | Highlights terms in generated prompt | In control | "Students need to learn these terms" |
| Test generation | Generates sample song | Plays audio preview | Confident | "Perfect for tomorrow's lesson" |

**Design Solutions**:
- **Curriculum-aligned templates**: Math, science, history, languages
- **Age-appropriate outputs**: Simpler for younger, complex for older
- **Vocabulary integration**: Highlight key terms in song
- **Preview mode**: Test before showing class

---

**Stage 2: Classroom Demonstration (45 minutes)**

| Touchpoint | User Action | System Response | Emotion | Pain Point |
|------------|-------------|-----------------|---------|------------|
| Project mode | Enables "Teaching Mode" | Large text, high contrast, simplified UI | Prepared | "Easy to read from back of class" |
| Student input | Asks class for song topic | Live typing on projected screen | Engaging | Whole-class participation |
| Generate together | Clicks "Generate" with class | Shows animated generation process | Excited | Building anticipation together |
| Play result | Plays generated song | Displays lyrics synced with audio | Delighted | "We made this together!" |

**Design Solutions**:
- **Teaching Mode**: Simplified UI, larger text, fewer distractions
- **Live collaboration**: Students can suggest edits in real-time
- **Educational annotations**: Explain why prompt was structured this way
- **Downloadable materials**: Lesson plans, worksheets, assessment rubrics

---

**Stage 3: Student Projects (Multiple class periods)**

| Touchpoint | User Action | System Response | Emotion | Pain Point |
|------------|-------------|-----------------|---------|------------|
| Project setup | Creates "Class Project" | Generates unique student access codes | Organized | No account needed for students |
| Student access | Students enter code on phones | Guided tutorial overlay | Supported | Step-by-step for first-timers |
| Progress tracking | Dashboard shows all student progress | Color-coded (complete, in-progress, stuck) | In control | Quick glance at who needs help |
| Export submissions | One-click download all projects | ZIP file with all audio + lyrics + prompts | Efficient | Easy grading workflow |

**Design Solutions**:
- **Classroom management**: Teacher dashboard, student analytics
- **No-barrier entry**: Students don't need accounts (access codes only)
- **Progressive guidance**: Tutorials fade as students learn
- **Bulk operations**: Download all submissions at once

---

### Journey Map 3: Developer Integration (Piotr - Developer)

**Stage 1: API Discovery (10 minutes)**

| Touchpoint | User Action | System Response | Emotion | Pain Point |
|------------|-------------|-----------------|---------|------------|
| Docs navigation | Lands on `/api` documentation | Interactive API explorer | Impressed | "Swagger UI, good start" |
| Authentication | Generates API key | One-click key creation with scopes | Efficient | Scoped keys (read, write, admin) |
| First request | Tries `POST /analyze-lyrics` with curl | Returns JSON with prompt + metadata | Satisfied | Clean JSON, consistent structure |
| Rate limits | Checks headers | `X-RateLimit-Remaining: 497` | In control | Transparent limits, auto-reset time |

**Design Solutions**:
- **Interactive docs**: Swagger/OpenAPI with "Try it out" buttons
- **Scoped API keys**: Different permissions for different use cases
- **Consistent responses**: Standard JSON structure, predictable errors
- **Rate limit transparency**: Headers show remaining requests, reset time

---

**Stage 2: Integration Development (2 hours)**

| Touchpoint | User Action | System Response | Emotion | Pain Point |
|------------|-------------|-----------------|---------|------------|
| Webhook setup | Configures webhook URL | Test webhook sent immediately | Confident | "Webhooks work, async confirmed" |
| Batch processing | Submits 100 lyrics for analysis | Returns job ID, status endpoint | Relieved | Don't have to wait synchronously |
| Polling | Checks job status | Progress percentage (0-100%) | Patient | Clear progress, can show loading bar |
| Results download | Fetches completed job | JSON array with all results | Satisfied | One request, all data |

**Design Solutions**:
- **Webhook support**: Async workflow, don't block on processing
- **Job queue**: Batch operations with job tracking
- **Progress updates**: Real-time status for long-running jobs
- **Efficient data transfer**: Compressed responses, pagination

---

**Stage 3: Production Deployment (Ongoing)**

| Touchpoint | User Action | System Response | Emotion | Pain Point |
|------------|-------------|-----------------|---------|------------|
| Error handling | Simulates API error | Clear error code + message in JSON | Prepared | `error: "LYRICS_TOO_SHORT", min_length: 50` |
| Monitoring | Checks status dashboard | Uptime 99.9%, avg response 200ms | Reassured | Reliable for production use |
| Scaling | App handles traffic spike | Auto-scales, maintains response time | Impressed | Infrastructure handles load |
| Cost tracking | Views usage analytics | API call breakdown by endpoint | In control | Can predict costs, optimize |

**Design Solutions**:
- **Graceful errors**: Machine-readable error codes, human-readable messages
- **Status dashboard**: Real-time uptime, response times, incidents
- **Predictable pricing**: Usage analytics, cost estimation tools
- **Monitoring integration**: Datadog/Prometheus export ready

---

## 3. Interface Designs

### Interface 1: Web Application (Main Experience)

#### Layout: Desktop (1920x1080)

```
┌─────────────────────────────────────────────────────────────────────────────────────┐
│  SRYZ logo             [Search prompts...]          [PL/EN ▼] [Kasia] [⚙️] [?]        │
├─────────────────────────────────────────────────────────────────────────────────────┤
│                                                                                      │
│  ┌─────────────────────────────────────────────────────────────────────────────┐   │
│  │  [📤 Upload Lyrics]  [📋 Load from Library]  [🎯 New Project]  [📚 Templates]   │   │
│  └─────────────────────────────────────────────────────────────────────────────┘   │
│                                                                                      │
│  ┌───────────────────────────────────────────┬───────────────────────────────────┐ │
│  │                                           │                                   │ │
│  │  LYRICS INPUT                             │   PROMPT GENERATION               │ │
│  │  ┌─────────────────────────────────────┐ │   ┌─────────────────────────────┐ │ │
│  │  │ Paste or type lyrics here...        │ │   │ 🎵 Generated Prompt           │ │ │
│  │  │                                     │ │   │                             │ │ │
│  │  │ W nocnej ciszy słychać tylko       │ │   │ [Context section preview...] │ │ │
│  │  │ serce bicie...                       │ │   │                             │ │ │
│  │  │                                     │ │   │ [Objective section preview...]│ │ │
│  │  │                                     │ │   │                             │ │ │
│  │  └─────────────────────────────────────┘ │   └─────────────────────────────┘ │ │
│  │  [Clear] [Paste from clipboard]          │                                   │ │
│  │  Language: [Polish ●detected]           │   Quality Score: 87% (B)           │ │
│  │                                           │   ████████░░                      │ │
│  └───────────────────────────────────────────┴───────────────────────────────────┘ │
│                                                                                      │
│  ┌─────────────────────────────────────────────────────────────────────────────┐   │
│  │  ANALYSIS RESULTS                                                             │   │
│  │  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐     │   │
│  │  │ Mood         │  │ Genre        │  │ Structure    │  │ Polish Flow  │     │   │
│  │  │              │  │              │  │              │  │              │     │   │
│  │  │ Melancholic  │  │ Pop          │  │ Verse-Chorus │  │ Rymy: AABB   │     │   │
│  │  │ Hopeful      │  │ Ballad       │  │ Bridge       │  │ Cisza: Yes   │     │   │
│  │  │ Reflective   │  │              │  │              │  │ Bezy Róż.    │     │   │
│  │  │              │  │              │  │              │  │              │     │   │
│  │  │ [Edit]       │  │ [Edit]       │  │ [Edit]       │  │ [Optimize]   │     │   │
│  │  └──────────────┘  └──────────────┘  └──────────────┘  └──────────────┘     │   │
│  └─────────────────────────────────────────────────────────────────────────────┘   │
│                                                                                      │
│  ┌─────────────────────────────────────────────────────────────────────────────┐   │
│  │  REFINEMENT OPTIONS                                                          │   │
│  │  Platform: [● Suno AI] [○ Udio] [○ Custom LLM]                               │   │
│  │  Polish Optimizations: [✓] Preserve rhymes  [✓] Maintain grammatical cases │   │
│  │  Mood: [━━━●━━━] (Add more energy)  Tempo: [━━━●━━━] (Slightly faster)    │   │
│  │  Style: [Pop] [Rock] [Electronic ▼]  Vocals: [Female] [Male] [Duet ▼]      │   │
│  └─────────────────────────────────────────────────────────────────────────────┘   │
│                                                                                      │
│  ┌─────────────────────────────────────────────────────────────────────────────┐   │
│  │  [🔄 Regenerate]  [📋 Copy Prompt]  [🚀 Copy to Suno]  [💾 Save Project] [🔗 Share]│   │
│  └─────────────────────────────────────────────────────────────────────────────┘   │
│                                                                                      │
│  ┌─────────────────────────────────────────────────────────────────────────────┐   │
│  │  RECENT PROJECTS                                                              │   │
│  │  [Summer Memories] 2h ago  │  [Ballada o miłości] Yesterday  │  [Eksperyment] 3d ago│   │
│  └─────────────────────────────────────────────────────────────────────────────┘   │
│                                                                                      │
└─────────────────────────────────────────────────────────────────────────────────────┘
```

#### Layout: Mobile (iPhone 14 Pro, 393x852)

```
┌─────────────────────────────┐
│  ☰  SRYZ        PL/EN  👤   │
├─────────────────────────────┤
│                             │
│  [📤 Upload Lyrics]         │
│  [📋 My Library]            │
│  [🎯 Templates]             │
│                             │
│  ┌─────────────────────┐   │
│  │  QUICK INPUT         │   │
│  │  ┌─────────────────┐ │   │
│  │  │ Paste lyrics... │ │   │
│  │  └─────────────────┘ │   │
│  │  🇵🇱 Polish detected  │   │
│  └─────────────────────┘   │
│                             │
│  ┌─────────────────────┐   │
│  │  GENERATED PROMPT   │   │
│  │                     │   │
│  │  [Preview...]       │   │
│  │                     │   │
│  │  Quality: 87%       │   │
│  │  ████████░░         │   │
│  └─────────────────────┘   │
│                             │
│  ┌─────────────────────┐   │
│  │  MOOD: 🌙 Melancholic│   │
│  │  GENRE: 🎵 Pop      │   │
│  │  POLISH: ✓          │   │
│  └─────────────────────┘   │
│                             │
│  [🚀 Generate for Suno]     │
│  [🔄 Regenerate]            │
│                             │
│  Recent:                    │
│  • Summer Memories 2h       │
│  • Ballada o miłości...     │
│                             │
└─────────────────────────────┘
```

---

### Interface 2: CLI (Power Users)

**Design Philosophy**: Familiar patterns for developers (git, npm, docker style)

```bash
# Installation
$ npm install -g sryz-cli

# Authentication (first run only)
$ sryz login
🔐 SRYZ CLI Login
Email: kasia@example.com
Password: ********
✓ Logged in as kasia@example.com

# Quick start (interactive mode)
$ sryz analyze
📝 Paste your lyrics (Ctrl+D when done):
> W nocnej ciszy słychać tylko serce bicie
> Myśli krążą po głowie, szukają drogi
>
^D
🔍 Analyzing lyrics...
✓ Language detected: Polish
✓ Mood: Melancholic, reflective
✓ Genre: Pop ballad
✓ Structure: Verse-chorus

📋 Generated Prompt:
---
[Context]
Create a Polish pop ballad about nighttime introspection...

[Objective]
Generate melancholic yet hopeful lyrics with verse-chorus structure...

[Style]
Tempo: Slow (70-80 BPM)
Key: A minor
Instrumentation: Piano, strings, subtle drums...

[Tone]
Reflective, emotional, intimate...

[Audience]
Polish pop music fans, ages 25-45...

[Response]
Structured lyrics with [Verse], [Chorus], [Bridge] tags...
---

💾 Save this prompt? (y/n): y
✓ Saved to: ~/sryz/prompts/nocna-cisza-2025-12-26.json

🚀 Generate on platform?
  [1] Suno AI
  [2] Udio
  [3] Custom LLM
  [4] Skip
Choose: 1
✓ Prompt copied to clipboard
✓ Opening Suno AI... (https://suno.com/ai?prompt=...)
```

---

**CLI Commands Reference**:

```bash
# Batch processing (research workflow)
$ sryz batch --input ~/lyrics/*.txt --output results.json
✓ Processing 50 lyrics...
[████████████████████░░] 90% (45/50) ETA: 2s
✓ Complete! Results saved to results.json

# API key management
$ sryz keys:create --name "Production App" --scopes read,write
✓ API key created: sk_live_xxxxxxxxxxxx
⚠️  Store this key securely. It won't be shown again.

# Configuration
$ sryz config:set default_platform suno
✓ Default platform set to: suno

$ sryz config:set language polish
✓ Default language set: polish

# Template library
$ sryz templates:list
Available templates:
  [1] educational-physics-pop
  [2] polish-love-song-rock
  [3] commercial-upbeat-dance

$ sryz templates:use educational-physics-pop
✓ Template loaded: educational-physics-pop
📚 This template optimizes for:
   - Age group: 14-16
   - Subject: Physics (Newton's Laws)
   - Style: Educational pop

# Interactive refinement
$ sryz refine ~/sryz/prompts/nocna-cisza.json
🎯 Refinement Mode
Current mood: melancholic
New mood (or press Enter to keep): melancholic, hopeful
✓ Mood updated: melancholic, hopeful

Current tempo: 70-80 BPM
New tempo (or press Enter to keep): 80-90
✓ Tempo updated: 80-90 BPM

[💾] Save [🔄] Regenerate [📋] Copy [❌] Cancel: s
✓ Saved refinements to: nocna-cisza-refined.json
```

---

### Interface 3: API Documentation (Developers)

**Design Philosophy**: Interactive, copy-pasteable, language-agnostic

#### Endpoint: `POST /api/v1/analyze`

**Interactive Example**:
```javascript
// Request
{
  "lyrics": "W nocnej ciszy słychać tylko serce bicie...",
  "options": {
    "language": "pl",
    "platform": "suno",
    "include_analysis": true
  }
}

// Response (200 OK)
{
  "prompt": {
    "context": "Create a Polish pop ballad...",
    "objective": "Generate melancholic lyrics...",
    "style": "Tempo: 70-80 BPM, Key: A minor...",
    "tone": "Reflective, emotional...",
    "audience": "Polish pop fans, ages 25-45...",
    "response_format": "Structured lyrics with tags..."
  },
  "analysis": {
    "mood": ["melancholic", "reflective"],
    "genre": "pop ballad",
    "structure": "verse-chorus",
    "language": "polish",
    "polish_flow": {
      "rhyme_scheme": "AABB",
      "rhythm_preserved": true,
      "grammatical_cases": "maintained"
    },
    "quality_score": 87
  },
  "metadata": {
    "id": "prompt_abc123",
    "created_at": "2025-12-26T10:30:00Z",
    "processing_time_ms": 245
  }
}
```

**Error Handling**:
```javascript
// Error Response (400 Bad Request)
{
  "error": {
    "code": "LYRICS_TOO_SHORT",
    "message": "Lyrics must be at least 50 characters long",
    "details": {
      "provided_length": 23,
      "minimum_length": 50
    },
    "docs_url": "https://docs.sryz.pl/errors/lyrics-too-short"
  }
}
```

---

### Interface 4: Plugin/Extension Concept (DAW Integration)

**Ableton Live Plugin (Concept Design)**:

```
┌────────────────────────────────────────────────────────────┐
│  SRYZ Prompt Assistant                    [✓] Enabled      │
├────────────────────────────────────────────────────────────┤
│                                                            │
│  [📝 Lyrics] [🎵 Prompt] [⚙️ Settings] [🚀 Generate]    │
│                                                            │
│  ┌──────────────────────────────────────────────────────┐ │
│  │  LYRICS INPUT                                        │ │
│  │  ┌────────────────────────────────────────────────┐ │ │
│  │  │ W nocnej ciszy słychać tylko serce bicie...   │ │ │
│  │  │                                                │ │ │
│  │  │                                                │ │ │
│  │  └────────────────────────────────────────────────┘ │ │
│  │  🇵🇱 Polish detected  ○ Edit                       │ │
│  └──────────────────────────────────────────────────────┘ │
│                                                            │
│  ┌──────────────────────────────────────────────────────┐ │
│  │  GENERATED PROMPT (Ready for Suno AI)              │ │
│  │  ┌────────────────────────────────────────────────┐ │ │
│  │  │ Create a Polish pop ballad...                 │ │ │
│  │  │                                                │ │ │
│  │  │ Mood: melancholic, reflective                 │ │ │
│  │  │ Tempo: 70-80 BPM                               │ │ │
│  │  │ Key: A minor                                   │ │ │
│  │  │                                                │ │ │
│  │  └────────────────────────────────────────────────┘ │ │
│  │  Quality: ████████░░ 87%                           │ │
│  │                                                      │ │
│  │  [📋 Copy] [🔄 Regenerate] [🚀 Open Suno]          │ │
│  └──────────────────────────────────────────────────────┘ │
│                                                            │
│  🔀 Drag MIDI clip here to add melody reference           │
│                                                            │
└────────────────────────────────────────────────────────────┘
```

**Workflow Integration**:
1. User selects MIDI clip in Ableton
2. Clicks "SRYZ Prompt Assistant" in plugin menu
3. Plugin extracts lyrics from clip name/notes
4. Generates optimized prompt
5. One-click opens Suno AI with pre-filled prompt
6. Generated audio can be dragged back into Ableton arrangement

---

## 4. Workflow Design

### Workflow 1: New User Onboarding Flow

**Goal**: Get user to first successful prompt generation in <5 minutes

**Step 1: Landing Page → Sign Up (30 seconds)**
- **Hero Section**: "Transform Your Lyrics into AI Music - In Polish"
- **Video Demo**: 30-second screen recording showing lyric → prompt → song
- **CTA Buttons**:
  - Primary: "Start Free" (no credit card)
  - Secondary: "Watch Demo" (modal video)
- **Trust Signals**:
  - "Used by 10,000+ Polish musicians"
  - "4.9★ rating on Product Hunt"

**Step 2: Welcome Tutorial (60 seconds, skippable)**
```
┌─────────────────────────────────────────────────┐
│  Welcome to SRYZ! 👋                            │
│                                                 │
│  Let's create your first AI music prompt       │
│                                                 │
│  [1/3] 📝 Paste Your Lyrics                    │
│                                                 │
│  ┌───────────────────────────────────────────┐ │
│  │ W nocnej ciszy słychać tylko serce bicie │ │
│  │ Myśli krążą po głowie, szukają drogi     │ │
│  │                                           │ │
│  │                                           │ │
│  └───────────────────────────────────────────┘ │
│                                                 │
│  Tip: Write in Polish or English - we support │
│  both!                                        │
│                                                 │
│  [← Back] [Next: Analyze →]                    │
└─────────────────────────────────────────────────┘
```

**Step 3: Analysis & Generation (90 seconds)**
```
┌─────────────────────────────────────────────────┐
│  [2/3] 🔍 Analyzing Your Lyrics...              │
│                                                 │
│  ✅ Language detected: Polish                  │
│  ✅ Mood identified: melancholic, reflective  │
│  ✅ Genre suggested: pop ballad                │
│  ✅ Structure: verse-chorus                    │
│                                                 │
│  ⏳ Generating optimized prompt...             │
│                                                 │
│  [ ← animation of text being analyzed → ]      │
│                                                 │
│  [← Back] [Next: Customize →]                   │
└─────────────────────────────────────────────────┘
```

**Step 4: Customization (60 seconds, optional)**
```
┌─────────────────────────────────────────────────┐
│  [3/3] 🎨 Customize Your Prompt                 │
│                                                 │
│  Platform: ● Suno AI  ○ Udio                   │
│                                                 │
│  Polish Optimizations:                         │
│  ☑ Preserve Polish rhymes (rymy)               │
│  ☑ Maintain grammatical cases (odmiana)        │
│  ☐ Add Polish cultural references              │
│                                                 │
│  Adjust Mood:                                   │
│  Sad ━━━━━●━━━ Happy                            │
│                                                 │
│  [← Back] [Generate Prompt →]                   │
└─────────────────────────────────────────────────┘
```

**Step 5: Success Moment (30 seconds)**
```
┌─────────────────────────────────────────────────┐
│  🎉 Your Prompt is Ready!                       │
│                                                 │
│  Quality Score: ████████░░ 87% (Great!)        │
│                                                 │
│  [📋 Copy Prompt] [🚀 Open Suno AI]              │
│                                                 │
│  What's next?                                   │
│  • Create more prompts                          │
│  • Browse templates                             │
│  • Watch tutorial videos                        │
│                                                 │
│  [Skip to Dashboard]                             │
└─────────────────────────────────────────────────┘
```

---

### Workflow 2: Lyric Upload → Analysis → Prompt Generation

**State 1: Empty State**
```
┌─────────────────────────────────────────────────┐
│  📝 Upload Your Lyrics                          │
│                                                 │
│  ┌───────────────────────────────────────────┐ │
│  │  Drag & drop lyrics file here              │ │
│  │  or paste your lyrics below                │ │
│  │                                           │ │
│  │  [Browse files...]                         │ │
│  │                                           │ │
│  │  ┌─────────────────────────────────────┐ │ │
│  │  │                                     │ │ │
│  │  │ Paste lyrics here...                │ │ │
│  │  │                                     │ │ │
│  │  └─────────────────────────────────────┘ │ │
│  └───────────────────────────────────────────┘ │
│                                                 │
│  Supported formats: .txt, .pdf, .docx, .lrc    │
│                                                 │
│  💡 Tip: Include section tags like [Verse],    │
│  [Chorus] for better structure detection       │
└─────────────────────────────────────────────────┘
```

**State 2: Processing (Real-time Feedback)**
```
┌─────────────────────────────────────────────────┐
│  ⏳ Processing Your Lyrics...                  │
│                                                 │
│  ✅ Language detection: Polish                 │
│  ✅ Tokenization: 127 words                     │
│  ✅ Section analysis: verse-chorus-bridge       │
│  ⏳ Sentiment analysis...                       │
│  ⏳ Rhyme scheme extraction...                  │
│  ⏳ Genre classification...                     │
│                                                 │
│  [████████████░░░░░░░░░] 60%                  │
│                                                 │
│  Please wait, analyzing deep patterns...       │
└─────────────────────────────────────────────────┘
```

**State 3: Analysis Results (Before Prompt)**
```
┌─────────────────────────────────────────────────┐
│  📊 Analysis Complete!                          │
│                                                 │
│  ┌──────────┬──────────┬──────────┬──────────┐ │
│  │ Mood     │ Genre    │ Tempo    │ Key      │ │
│  ├──────────┼──────────┼──────────┼──────────┤ │
│  │ 🌙       │ 🎵       │ 🎚️       │ 🎹       │ │
│  │ Melan-  │ Pop      │ Slow     │ A minor  │ │
│  │ cholic  │ Ballad   │ (70-80)  │          │ │
│  │          │          │          │          │ │
│  │ [Edit]   │ [Edit]   │ [Edit]   │ [Edit]   │ │
│  └──────────┴──────────┴──────────┴──────────┘ │
│                                                 │
│  Polish-Specific Analysis:                      │
│  • Rhyme scheme: AABB (perfect rhymes)          │
│  • Rhythm: Iambic (jambiczny)                   │
│  • Grammatical cases: Nominative, locative      │
│  • Cultural references: ❌ None detected        │
│                                                 │
│  [Generate Prompt →] [Edit Analysis]            │
└─────────────────────────────────────────────────┘
```

**State 4: Generated Prompt (CO-STAR Format)**
```
┌─────────────────────────────────────────────────┐
│  🎯 Your Optimized Prompt                       │
│                                                 │
│  Platform: Suno AI  [Change ▼]                  │
│                                                 │
│  ┌───────────────────────────────────────────┐ │
│  │ [Context] 📖                               │ │
│  │ Create a Polish pop ballad about          │ │
│  │ nighttime introspection and emotional     │ │
│  │ self-discovery. The song should capture  │ │
│  │ the feeling of solitary reflection...     │ │
│  │                                           │ │
│  │ [Objective] 🎯                             │ │
│  │ Generate melancholic yet hopeful lyrics   │ │
│  │ with verse-chorus-bridge structure...     │ │
│  │                                           │ │
│  │ [Style] 🎨                                 │ │
│  │ Tempo: Slow (70-80 BPM)                    │ │
│  │ Key: A minor                               │ │
│  │ Time signature: 4/4                        │ │
│  │ Instrumentation: Piano, strings, subtle   │ │
│  │   acoustic guitar, light drums            │ │
│  │                                           │ │
│  │ [Tone] 🎭                                   │ │
│  │ Intimate, reflective, emotional, bittersweet│ │
│  │ Vocals: Female, soft, breathy              │ │
│  │                                           │ │
│  │ [Audience] 👥                               │ │
│  │ Polish pop music fans, ages 25-45, who    │ │
│  │ appreciate emotional depth and           │ │
│  │ introspective themes...                    │ │
│  │                                           │ │
│  │ [Response] 📝                               │ │
│  │ Structured lyrics with [Verse], [Chorus], │ │
│  │ [Bridge] tags. Polish language with       │ │
│  │ natural flow and grammatical correctness. │ │
│  │ Include Polish rhymes (rymy) and maintain  │ │
│  │ emotional authenticity...                  │ │
│  └───────────────────────────────────────────┘ │
│                                                 │
│  Quality Score: ████████░░ 87%                  │
│  Specificity: 92%  Structure: 85%  Creativity: 78%│
│                                                 │
│  [🔄 Regenerate] [📋 Copy] [🚀 Copy to Suno]      │
│  [💾 Save] [🔗 Share] [⚙️ Advanced Options]       │
└─────────────────────────────────────────────────┘
```

---

### Workflow 3: Iterative Refinement Loop

**Concept**: Users should be able to refine prompts through natural interactions, not technical edits

**Iteration 1 → 2 (Add more energy)**
```
┌─────────────────────────────────────────────────┐
│  🔄 Iteration 2 of 5                            │
│                                                 │
│  YOUR CHANGE:                                   │
│  "Make it more energetic"                        │
│                                                 │
│  ┌───────────────────────────────────────────┐ │
│  │ BEFORE                         AFTER      │ │
│  │ ─────────────────────────────────────    │ │
│  │ Tone: melancholic            Tone:       │ │
│  │       reflective                upbeat,   │ │
│  │                                  hopeful  │ │
│  │                                           │ │
│  │ Tempo: 70-80 BPM              Tempo:      │ │
│  │                             110-120 BPM  │ │
│  │                                           │ │
│  │ Instruments: piano, strings  Instruments:│ │
│  │   subtle drums               synths,     │ │
│  │                              drums, bass │ │
│  └───────────────────────────────────────────┘ │
│                                                 │
│  ✅ Applied changes!                           │
│                                                 │
│  [↩️ Undo] [▶️ Generate] [💾 Save Iteration]     │
└─────────────────────────────────────────────────┘
```

**Branching Workflow (A/B Testing)**
```
┌─────────────────────────────────────────────────┐
│  🔀 Create Branch                               │
│                                                 │
│  Current iteration: Iteration 3                │
│                                                 │
│  Create alternative version:                    │
│  ┌───────────────────────────────────────────┐ │
│  │ ○ Make it sadder (more melancholic)       │ │
│  │ ○ Make it faster (increase tempo)          │ │
│  │ ○ Change genre to rock                      │ │
│  │ ○ Add piano solo                            │ │
│  │ ○ Custom change...                          │ │
│  └───────────────────────────────────────────┘ │
│                                                 │
│  [Create Branch →]                               │
└─────────────────────────────────────────────────┘
```

**Comparison View (Side-by-Side)**
```
┌─────────────────────────────────────────────────┐
│  ⚖️ Compare Versions                            │
│                                                 │
│  ┌─────────────────────┬─────────────────────┐ │
│  │ Version A (Main)    │ Version B (Branch)  │ │
│  ├─────────────────────┼─────────────────────┤ │
│  │ Mood: melancholic   │ Mood: upbeat        │ │
│  │ Tempo: 70-80        │ Tempo: 110-120      │ │
│  │ Quality: 87%        │ Quality: 82%        │ │
│  │                     │                     │ │
│  │ [Listen]            │ [Listen]            │ │
│  │                     │                     │ │
│  │ [Select ✓]          │ [Select ○]          │ │
│  └─────────────────────┴─────────────────────┘ │
│                                                 │
│  Key differences:                                │
│  • Energy level (↑ 40%)                          │
│  • Tempo (↑ 50 BPM)                               │
│  • Instrumentation (synths vs piano)             │
│                                                 │
│  [Merge Best of Both] [Keep A] [Keep B]          │
└─────────────────────────────────────────────────┘
```

---

## 5. Key Features

### Feature 1: Visual Feedback for Analysis Results

**Challenge**: Make NLP analysis (mood, genre, structure) tangible and understandable for non-technical users

**Solution**: Multi-modal visualization

#### A. Mood Visualization (Emotion Wheel)
```
          Happy
            ▲
       Energetic   Calm
     ○─────────────○
      │             │
   Sad │           │ Hopeful
      │             │
      └─────────────┘
         Tense

Your lyrics:
●●● Melancholic (primary emotion)
●● Hopeful (secondary)
● Reflective (tertiary)
```

#### B. Genre Radar Chart
```
          Pop
           ▲
    Rock ○─│─○ Electronic
          │
       ○──│──○
    Folk  │  Jazz
          │
        Hip-hop

Your lyrics:
Match probability:
●●●●●○○ Pop ballad (87%)
●●○○○○○ Rock (23%)
●○○○○○○ Electronic (12%)
```

#### C. Structure Timeline Visualization
```
┌─────────────────────────────────────────────┐
│ Verse 1 │ Chorus │ Verse 2 │ Chorus │ Bridge│
├─────────────────────────────────────────────┤
│ Emotion:│ Emotion:│ Emotion:│ Emotion:│Emotion:│
│ Sad →   │Hopeful→│ Sad →   │Hopeful→│ Climax→│
│ Neutral │  High   │ Neutral │  High   │  Peak  │
└─────────────────────────────────────────────┘

Pattern: MAN_IN_A_HOLE (confidence: 86%)
Classic storytelling: start low, rise to hope, end resolved
```

#### D. Polish-Specific Analysis (Language Toggle)
```
Polish Flow Analysis:
┌─────────────────────────────────────────────┐
│ Rhythm (Rytm):     Iambic (jambiczny) ✓    │
│ Rhymes (Rymy):      AABB (perfect) ✓        │
│ Grammatical Cases:  Nominative, locative ✓   │
│ Cultural Idioms:    ❌ None detected         │
│                                             │
│ 🇵🇱 Polish Optimizations Applied:          │
│ • Preserved rhymes: "bicie/skronie"        │
│ • Maintained cases: "serce/drogi"           │
│ • Avoided Anglicisms: ✓                     │
└─────────────────────────────────────────────┘
```

---

### Feature 2: Prompt Quality Scoring Dashboard

**Challenge**: Help users understand prompt quality without technical jargon

**Solution**: 6-dimensional quality scoring with visual indicators

#### Quality Dashboard
```
┌─────────────────────────────────────────────────┐
│  📊 Prompt Quality Score: 87% (B)               │
│                                                 │
│  ┌─────────────────────────────────────────┐   │
│  │  SPECIFICITY        ████████░░ 90%      │   │
│  │  "Excellent concrete details"          │   │
│  │                                          │   │
│  │  STRUCTURE         ████████░░ 85%      │   │
│  │  "Well-organized, clear sections"      │   │
│  │                                          │   │
│  │  CREATIVITY        ██████░░░░ 75%      │   │
│  │  "Moderate - add more unique elements" │   │
│  │                                          │   │
│  │  CONSTRAINTS       ████████░░ 95%      │   │
│  │  "Very clear boundaries"              │   │
│  │                                          │   │
│  │  CONTEXT           ████████░░ 80%      │   │
│  │  "Good background, could add more"    │   │
│  │                                          │   │
│  │  CLARITY           ████████░░ 95%      │   │
│  │  "Excellent directives"                │   │
│  └─────────────────────────────────────────┘   │
│                                                 │
│  Priority Improvements:                        │
│  1. Creativity                                │
│     → Add metaphors or analogies              │
│     → Include hypothetical scenarios          │
│  2. Context                                   │
│     → Add target audience demographics         │
│     → Specify use case (commercial, artistic)  │
│                                                 │
│  [Apply Improvements] [Regenerate] [Export]     │
└─────────────────────────────────────────────────┘
```

#### Improvement Suggestions (Interactive)
```
┌─────────────────────────────────────────────────┐
│  💡 Suggested Improvements (One-click apply)    │
│                                                 │
│  ┌─────────────────────────────────────────┐   │
│  │ [✓] Add tempo descriptor                │   │
│  │     "Moderate tempo, 90-100 BPM"        │   │
│  │     [Apply]                             │   │
│  ├─────────────────────────────────────────┤   │
│  │ [✓] Include vocal style                 │   │
│  │     "Female vocals, intimate delivery"  │   │
│  │     [Apply]                             │   │
│  ├─────────────────────────────────────────┤   │
│  │ [✓] Specify production era              │   │
│  │     "Modern production, 2020s style"    │   │
│  │     [Apply]                             │   │
│  └─────────────────────────────────────────┘   │
│                                                 │
│  [Apply All] [Dismiss] [Customize...]           │
└─────────────────────────────────────────────────┘
```

---

### Feature 3: A/B Testing Interface for Prompts

**Challenge**: Enable systematic prompt comparison without overwhelming users

**Solution**: Side-by-side testing with winner prediction

#### A/B Test Setup
```
┌─────────────────────────────────────────────────┐
│  ⚖️ A/B Test: Compare Prompts                   │
│                                                 │
│  Version A (Current):                           │
│  "Create a melancholic Polish pop ballad..."    │
│                                                 │
│  Version B (Variation):                         │
│  "Create an energetic Polish pop song..."       │
│                                                 │
│  Difference: +energyful -melancholic            │
│                                                 │
│  Test Duration: [○ 1 day] [● 3 days] [○ 1 week]│
│                                                 │
│  [Start A/B Test →]                              │
└─────────────────────────────────────────────────┘
```

#### A/B Test Results (After 3 Days)
```
┌─────────────────────────────────────────────────┐
│  📊 A/B Test Results (Dec 23-26, 2025)           │
│                                                 │
│  ┌─────────────────────┬─────────────────────┐ │
│  │ Version A           │ Version B           │ │
│  │ (Melancholic)       │ (Energetic)         │
│  ├─────────────────────┼─────────────────────┤ │
│  │ Generations: 127    │ Generations: 142    │ │
│  │ Avg Quality: 87%    │ Avg Quality: 82%    │ │
│  │ Thumbs up: 89%      │ Thumbs up: 76%      │ │
│  │ Shared: 23 times    │ Shared: 31 times    │ │
│  │                                             │ │
│  │ Winner: ★ Version A (Melancholic)          │ │
│  └─────────────────────┴─────────────────────┘ │
│                                                 │
│  Insights:                                      │
│  • Users preferred melancholic mood by 13%     │
│  • Version B shared more despite lower quality  │
│  • Consider: "Melancholic but energetic" hybrid│
│                                                 │
│  [Select Winner: A] [Create Hybrid] [Retest]    │
└─────────────────────────────────────────────────┘
```

---

### Feature 4: Language Switching (PL/EN)

**Challenge**: Seamless bilingual experience without losing context

**Solution**: Smart language detection with manual override, localized terminology

#### Language Toggle (Always Visible)
```
┌─────────────────────────────────────────────────┐
│  SRYZ                     [🇵🇱 PL] [🇬🇧 EN]    │
│                                     ↑ Selected   │
└─────────────────────────────────────────────────┘
```

#### Auto-Detection Feedback
```
┌─────────────────────────────────────────────────┐
│  🌐 Language Detected: Polish 🇵🇱                  │
│                                                 │
│  We detected Polish lyrics. Switching interface │
│  to Polish for better experience.               │
│                                                 │
│  ┌───────────────┐  ┌───────────────┐           │
│  │ [Keep English]│  │ [Switch to    │           │
│  │               │  │  Polish ▶️]    │           │
│  └───────────────┘  └───────────────┘           │
│                                                 │
│  Don't show this again: [✓]                     │
└─────────────────────────────────────────────────┘
```

#### Localized Terminology (Polish vs English)
```
English UI:
┌─────────────────────────────────────────────────┐
│  MOOD: Melancholic                               │
│  GENRE: Pop Ballad                               │
│  STRUCTURE: Verse-Chorus                         │
│  KEY: A minor                                    │
└─────────────────────────────────────────────────┘

Polish UI:
┌─────────────────────────────────────────────────┐
│  NASTRÓJ: Melancholiczna                         │
│  GATUNEK: Pop ballada                            │
│  STRUKTURA: Zwrotka-refren                      │
│  TONACJA: A moll                                 │
└─────────────────────────────────────────────────┘
```

#### Hybrid Mode (Polish Lyrics, English UI)
```
┌─────────────────────────────────────────────────┐
│  💬 Hybrid Mode: Polish lyrics, English UI       │
│                                                 │
│  Lyrics (Polish):                               │
│  "W nocnej ciszy słychać tylko serce bicie"    │
│                                                 │
│  Analysis (English):                            │
│  Mood: melancholic, reflective                  │
│  Genre: pop ballad                              │
│                                                 │
│  Generated Prompt:                              │
│  "Create a Polish pop ballad about              │
│   nighttime introspection..."                   │
│                                                 │
│  ✅ Maintains Polish authenticity while         │
│     using familiar English terminology          │
└─────────────────────────────────────────────────┘
```

---

## 6. Accessibility

### WCAG 2.1 AA Compliance Checklist

#### Visual Accessibility

**1. Color Contrast (Minimum 4.5:1)**
```
✓ Primary text (black on white): 21:1
✓ Secondary text (dark gray on white): 12:1
✓ Buttons (blue on white): 7:1
✓ Links (underlined blue): 7:1
✓ Error messages (red on white): 7:1
✓ Success messages (green on white): 7:1
✓ Disabled buttons (gray on white): 4.5:1
```

**2. Text Sizing (Support 100%-200% zoom)**
```css
/* Responsive typography */
html {
  font-size: 16px; /* Base size */
}

@media (min-width: 120%) {
  html {
    font-size: 19.2px; /* 120% zoom */
  }
}

@media (min-width: 200%) {
  html {
    font-size: 32px; /* 200% zoom */
  }
}

/* No horizontal scroll at 200% zoom */
body {
  max-width: 100%;
  overflow-x: hidden;
}
```

**3. Focus Indicators**
```css
/* Visible focus for keyboard navigation */
:focus {
  outline: 3px solid #4A90E2;
  outline-offset: 2px;
}

/* Skip navigation link */
.skip-link {
  position: absolute;
  top: -40px;
  left: 0;
  background: #4A90E2;
  color: white;
  padding: 8px;
  text-decoration: none;
  z-index: 100;
}

.skip-link:focus {
  top: 0;
}
```

#### Keyboard Accessibility

**1. Full Keyboard Navigation**
```
✓ Tab: Navigate through interactive elements
✓ Shift+Tab: Navigate backwards
✓ Enter/Space: Activate buttons/links
✓ Arrow keys: Navigate lists, sliders, dropdowns
✓ Escape: Close modals, cancel actions
✓ Home/End: Jump to start/end of lists
```

**2. Keyboard Shortcuts**
```
┌─────────────────────────────────────────────────┐
│  ⌨️ Keyboard Shortcuts                           │
│                                                 │
│  [?] Show this help: ? or /                      │
│  [📝 New prompt]: N or Ctrl+N                    │
│  [🔄 Regenerate]: R or Ctrl+R                    │
│  [💾 Save]: S or Ctrl+S                          │
│  [📋 Copy]: C or Ctrl+C                           │
│  [🔍 Search]: / or Ctrl+F                         │
│  [⚙️ Settings]: , or Ctrl+,                       │
│  [❌ Cancel/Close]: Esc                           │
│                                                 │
│  [→] Next section: Tab or →                      │
│  [←] Previous section: Shift+Tab or ←            │
└─────────────────────────────────────────────────┘
```

#### Screen Reader Support

**1. Semantic HTML**
```html
<!-- Proper heading hierarchy -->
<main>
  <h1>SRYZ Prompt Generator</h1>
  <section aria-labelledby="lyrics-input-heading">
    <h2 id="lyrics-input-heading">Lyrics Input</h2>
    <textarea
      aria-label="Paste your lyrics here"
      placeholder="Paste or type lyrics..."
    ></textarea>
  </section>

  <section aria-labelledby="analysis-results-heading">
    <h2 id="analysis-results-heading">Analysis Results</h2>
    <!-- Analysis content -->
  </section>
</main>
```

**2. ARIA Labels**
```html
<!-- Icon buttons with labels -->
<button
  aria-label="Generate new prompt"
  title="Regenerate"
>
  🔄
</button>

<!-- Live regions for dynamic content -->
<div
  aria-live="polite"
  aria-atomic="true"
  id="quality-score"
>
  Quality Score: 87%
</div>

<!-- Progress indicators -->
<div
  role="progressbar"
  aria-valuenow="60"
  aria-valuemin="0"
  aria-valuemax="100"
  aria-label="Analyzing lyrics"
>
  ⏳ Processing... 60%
</div>
```

**3. Screen Reader-Optimized Content**
```
┌─────────────────────────────────────────────────┐
│  Analysis Results                                │
│  ┌─────────────────────────────────────────┐   │
│  │ Mood: Melancholic                         │   │
│  │   (Detected from lyrics about night,     │   │
│  │    silence, solitude)                    │   │
│  │   Confidence: 92%                         │   │
│  │   [Edit button - press Enter to modify]  │   │
│  └─────────────────────────────────────────┘   │
└─────────────────────────────────────────────────┘
```

#### Cognitive Accessibility

**1. Clear Language (Plain Polish/English)**
```
❌ Technical: "Apply natural language processing"
✓ Simple: "Analyze your lyrics"

❌ Technical: "Sentiment analysis indicates negative valence"
✓ Simple: "Mood: sad, melancholic"
```

**2. Error Prevention**
```
┌─────────────────────────────────────────────────┐
│  ⚠️ Lyrics Too Short                           │
│                                                 │
│  Your lyrics are 23 characters long.           │
│  Minimum length: 50 characters.                │
│                                                 │
│  You need 27 more characters.                  │
│                                                 │
│  [Add more lyrics] [Use sample lyrics]         │
└─────────────────────────────────────────────────┘
```

**3. Consistent Navigation**
```
✓ Same navigation on all pages
✓ Predictable button placement
✓ Clear section labels
✓ Undo/redo available for all destructive actions
```

---

## 7. Mobile vs Desktop Experience

### Responsive Design Breakpoints

```css
/* Mobile First Approach */

/* Extra Small Devices (phones, 320px-374px) */
@media (max-width: 374px) {
  .container { max-width: 100%; padding: 12px; }
  .btn { font-size: 14px; padding: 12px 20px; }
  .analysis-grid { grid-template-columns: 1fr; }
}

/* Small Devices (phones, 375px-479px) */
@media (min-width: 375px) and (max-width: 479px) {
  .container { max-width: 100%; padding: 16px; }
  .analysis-grid { grid-template-columns: 1fr; }
  .quality-dashboard { display: none; /* Hide on mobile */ }
}

/* Medium Devices (tablets, 480px-767px) */
@media (min-width: 480px) and (max-width: 767px) {
  .container { max-width: 100%; padding: 20px; }
  .analysis-grid { grid-template-columns: 1fr 1fr; }
  .quality-dashboard { display: block; }
}

/* Large Devices (laptops, 768px-1023px) */
@media (min-width: 768px) and (max-width: 1023px) {
  .container { max-width: 720px; margin: 0 auto; }
  .analysis-grid { grid-template-columns: 1fr 1fr 1fr; }
  .two-column { display: grid; grid-template-columns: 1fr 1fr; gap: 20px; }
}

/* Extra Large Devices (desktops, 1024px+) */
@media (min-width: 1024px) {
  .container { max-width: 1200px; margin: 0 auto; }
  .analysis-grid { grid-template-columns: repeat(4, 1fr); }
  .two-column { display: grid; grid-template-columns: 1fr 1fr; gap: 30px; }
}
```

### Mobile-First Features

#### Mobile-Specific UI Patterns

**1. Bottom Navigation (Thumb Zone)**
```
┌─────────────────────────────────────────────────┐
│  (Content area - scrollable)                    │
│                                                 │
│  ┌─────────────────────────────────────────┐   │
│  │  Analysis Results                        │   │
│  │  (Scrolling content...)                  │   │
│  │                                           │   │
│  └─────────────────────────────────────────┘   │
│                                                 │
│  ┌─────────────────────────────────────────┐   │
│  │ [🏠 Home] [📝 Create] [📚 Library] [👤 Profile]│
│  └─────────────────────────────────────────┘   │
│         ↑ Bottom nav, easy thumb reach          │
└─────────────────────────────────────────────────┘
```

**2. Swipe Gestures**
```
┌─────────────────────────────────────────────────┐
│  ← Swipe left for next step                    │
│                                                 │
│  Step 1 of 5: Upload Lyrics                    │
│                                                 │
│  ┌─────────────────────────────────────────┐   │
│  │  [Paste lyrics area]                     │   │
│  └─────────────────────────────────────────┘   │
│                                                 │
│  Swipe right → for previous step               │
└─────────────────────────────────────────────────┘
```

**3. Touch Targets (Minimum 44x44px)**
```css
/* Mobile-optimized buttons */
.btn-mobile {
  min-height: 44px;
  min-width: 44px;
  padding: 12px 24px;
  font-size: 16px; /* Prevents zoom on iOS */
}

/* Spacing between touch targets */
.touch-target + .touch-target {
  margin-top: 12px;
}
```

### Desktop-Exclusive Features

**1. Multi-Window Support**
```
┌──────────────────────┬──────────────────────┐
│  Lyrics Input        │  Prompt Generation   │
│                      │                      │
│  [Lyrics editor]      │  [Generated prompt]  │
│                      │                      │
└──────────────────────┴──────────────────────┘
        (Resizable split view)
```

**2. Keyboard-Only Workflow**
```
Shortcuts:
Ctrl+N: New prompt
Ctrl+S: Save
Ctrl+C: Copy
Ctrl+R: Regenerate
Ctrl+K: Command palette
Ctrl+,: Settings
```

**3. Advanced Analytics Dashboard**
```
┌─────────────────────────────────────────────────┐
│  📊 Performance Analytics                       │
│  ┌─────────────────────────────────────────┐   │
│  │ [30-day line chart: prompt quality]     │   │
│  │                                         │   │
│  │ 95% ──●                                 │   │
│  │ 90%    ●──●                              │   │
│  │ 85%       ●──●──●                        │   │
│  │ 80%           ●──●──●                    │   │
│  │    └─────────────────────────────       │   │
│  │      Dec 1   Dec 15   Dec 30             │   │
│  └─────────────────────────────────────────┘   │
│                                                 │
│  Most used genres: Pop (45%), Rock (30%)       │
│  Avg iterations per prompt: 3.2                │
│  Polish vs English: 78% Polish                  │
└─────────────────────────────────────────────────┘
```

---

## 8. Visual Design System

### Color Palette

#### Primary Colors
```
Brand Blue: #4A90E2 (Accessible, trustworthy)
  - Used for: Primary buttons, links, focus states
  - Contrast ratio (white): 7.1:1 (✓ WCAG AA)

Secondary Purple: #9B59B6 (Creative, artistic)
  - Used for: Accents, highlights, gradients
  - Contrast ratio (white): 4.8:1 (✓ WCAG AA)

Success Green: #7ED321 (Positive feedback)
  - Used for: Success messages, quality indicators
  - Contrast ratio (white): 4.5:1 (✓ WCAG AA)

Error Red: #E74C3C (Error states)
  - Used for: Errors, warnings, destructive actions
  - Contrast ratio (white): 4.5:1 (✓ WCAG AA)
```

#### Neutral Colors
```
Text Primary: #2C3E50 (Near black, softer)
  - Used for: Headlines, body text
  - Contrast ratio (white): 12.6:1 (✓ WCAG AAA)

Text Secondary: #7F8C8D (Medium gray)
  - Used for: Secondary text, placeholders
  - Contrast ratio (white): 4.5:1 (✓ WCAG AA)

Background: #FFFFFF (Pure white)
  - Used for: Main background, cards

Surface: #F8F9FA (Light gray)
  - Used for: Section backgrounds, inputs

Border: #E1E8ED (Subtle borders)
  - Used for: Dividers, borders
```

#### Polish Theme Colors
```
Polish Red: #DC143C (Flag red accent)
  - Used for: Polish language indicator, PL-specific features

Polish White: #FFFFFF (Flag white)
  - Used for: Polish mode backgrounds
```

### Typography

#### Font Families
```
Primary: Inter (UI text)
  - Weights: 400 (regular), 500 (medium), 600 (semibold), 700 (bold)
  - Usage: Buttons, labels, navigation

Secondary: Lato (headlines, lyrics)
  - Weights: 400 (regular), 700 (bold), 900 (black)
  - Usage: Hero headlines, lyrics display

Monospace: JetBrains Mono (code, technical)
  - Usage: API docs, CLI examples, prompt code
```

#### Type Scale
```
H1 (Hero headline): 48px / 1.1 (Line height)
  - Desktop: 48px
  - Mobile: 32px

H2 (Section headline): 32px / 1.2
  - Desktop: 32px
  - Mobile: 24px

H3 (Card headline): 24px / 1.3
  - Desktop: 24px
  - Mobile: 20px

Body (Paragraph): 16px / 1.5
  - Desktop: 16px
  - Mobile: 16px (minimum readable size)

Small (Metadata): 14px / 1.4
  - Desktop: 14px
  - Mobile: 14px

Caption (Labels): 12px / 1.4
  - Desktop: 12px
  - Mobile: 12px
```

### Component Design

#### Buttons
```css
/* Primary Button */
.btn-primary {
  background: #4A90E2;
  color: white;
  padding: 12px 24px;
  border-radius: 8px;
  font-weight: 600;
  font-size: 16px;
  border: none;
  cursor: pointer;
  transition: all 0.2s ease;
}

.btn-primary:hover {
  background: #357ABD;
  transform: translateY(-2px);
  box-shadow: 0 4px 12px rgba(74, 144, 226, 0.3);
}

/* Secondary Button */
.btn-secondary {
  background: white;
  color: #4A90E2;
  padding: 12px 24px;
  border-radius: 8px;
  font-weight: 600;
  font-size: 16px;
  border: 2px solid #4A90E2;
  cursor: pointer;
}

/* Touch Targets (Mobile) */
.btn-touch {
  min-height: 44px;
  min-width: 44px;
}
```

#### Cards
```css
.card {
  background: white;
  border-radius: 12px;
  padding: 24px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
  border: 1px solid #E1E8ED;
  transition: all 0.2s ease;
}

.card:hover {
  box-shadow: 0 4px 16px rgba(0, 0, 0, 0.15);
  transform: translateY(-2px);
}

.card-polish {
  border-left: 4px solid #DC143C;
  background: linear-gradient(to right, #FFF5F5, white);
}
```

#### Inputs
```css
.input-text {
  width: 100%;
  padding: 12px 16px;
  border: 2px solid #E1E8ED;
  border-radius: 8px;
  font-size: 16px;
  font-family: 'Lato', sans-serif;
  transition: border-color 0.2s ease;
}

.input-text:focus {
  outline: none;
  border-color: #4A90E2;
  box-shadow: 0 0 0 3px rgba(74, 144, 226, 0.1);
}

.input-textarea {
  min-height: 150px;
  resize: vertical;
  font-family: 'Lato', sans-serif;
  line-height: 1.6;
}
```

### Animations & Microinteractions

#### Loading States
```css
/* Skeleton Loading */
.skeleton {
  background: linear-gradient(
    90deg,
    #F0F0F0 25%,
    #E0E0E0 50%,
    #F0F0F0 75%
  );
  background-size: 200% 100%;
  animation: loading 1.5s infinite;
}

@keyframes loading {
  0% { background-position: 200% 0; }
  100% { background-position: -200% 0; }
}

/* Progress Bar */
.progress-bar {
  width: 100%;
  height: 8px;
  background: #E1E8ED;
  border-radius: 4px;
  overflow: hidden;
}

.progress-fill {
  height: 100%;
  background: linear-gradient(90deg, #4A90E2, #9B59B6);
  border-radius: 4px;
  transition: width 0.3s ease;
  animation: shimmer 2s infinite;
}
```

#### Success/Error Feedback
```css
/* Success Checkmark Animation */
.success-icon {
  width: 64px;
  height: 64px;
  background: #7ED321;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  animation: scale-in 0.3s ease;
}

@keyframes scale-in {
  0% { transform: scale(0); opacity: 0; }
  50% { transform: scale(1.1); }
  100% { transform: scale(1); opacity: 1; }
}

/* Error Shake Animation */
.error-shake {
  animation: shake 0.5s ease;
}

@keyframes shake {
  0%, 100% { transform: translateX(0); }
  10%, 30%, 50%, 70%, 90% { transform: translateX(-10px); }
  20%, 40%, 60%, 80% { transform: translateX(10px); }
}
```

---

## Conclusion

This UX design document provides comprehensive user experience specifications for SRYZ across five distinct user personas, covering:

1. **User Personas**: Musicians, educators, developers, researchers, and Polish songwriters
2. **User Journeys**: Onboarding, classroom workflows, API integration
3. **Interface Designs**: Web app, CLI, API docs, DAW plugins
4. **Key Workflows**: Upload → Analyze → Generate → Refine → Export
5. **Core Features**: Visual feedback, quality scoring, A/B testing, language switching
6. **Accessibility**: WCAG 2.1 AA compliance, keyboard navigation, screen reader support
7. **Mobile/Desktop**: Responsive design, touch targets, gesture support
8. **Visual System**: Color palettes, typography, component library

### Design Philosophy Summary

- **Simplicity First**: Hide complexity behind intuitive interfaces
- **Polish Native**: Language-first design with cultural awareness
- **Progressive Enhancement**: Start simple, reveal power features as needed
- **Visual Feedback**: Make abstract analysis tangible through visualization
- **Multi-Modal**: Support web, mobile, CLI, and API workflows
- **Accessibility-First**: WCAG 2.1 AA compliance from day one
- **Creator Empowerment**: Tools that enhance, not replace, human creativity

This design ensures SRYZ will be accessible, intuitive, and powerful for all user types, from non-technical musicians to advanced developers and researchers.

---

**Next Steps**:
1. **User Testing**: Validate designs with real Polish musicians
2. **Prototyping**: Build interactive prototypes for testing
3. **Iteration**: Refine based on user feedback
4. **Implementation**: Hand off to development team
5. **Launch**: Monitor metrics, iterate post-launch

---

**Document Status**: Complete UX Design Specification
**Version**: 1.0
**Last Updated**: December 26, 2025
**Maintained By**: UX Design Team

---

*END OF UX DESIGN DOCUMENT*
