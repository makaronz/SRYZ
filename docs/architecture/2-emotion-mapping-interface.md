# Emotion Mapping Interface: Visual Multi-Dimensional Prompt System

**Architecture Type:** Interactive Visualization & Emotion-to-Prompt Mapping
**Version:** 1.0
**Date:** 2025-12-26
**Status:** Design Specification

---

## Executive Summary

The Emotion Mapping Interface creates a visual, interactive system where emotions are mapped across multiple dimensions (valence, arousal, dominance, tempo) and translated into optimized prompts through an intuitive graphical interface. Users can visually explore emotional spaces, see real-time prompt previews, and adjust emotional parameters to fine-tune AI music generation outputs.

---

## System Architecture Diagram

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                     EMOTION MAPPING INTERFACE                                 │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │                    VISUALIZATION LAYER                                │   │
│  │  ┌────────────────┐  ┌────────────────┐  ┌────────────────┐         │   │
│  │  │ 2D Emotion     │  │ 3D Emotion     │  │ Timeline       │         │   │
│  │  │ Plane (Valence-│  │ Space (VAD-T)  │  │ Progression    │         │   │
│  │  │ Arousal)       │  │                │  │                │         │   │
│  │  │ [Interactive]  │  │ [Interactive]  │  │ [Interactive]  │         │   │
│  │  └────────────────┘  └────────────────┘  └────────────────┘         │   │
│  │  ┌────────────────┐  ┌────────────────┐  ┌────────────────┐         │   │
│  │  │ Heat Map       │  │ Radar Charts   │  │ Genre Clusters │         │   │
│  │  │ (Emotion       │  │ (Multi-        │  │ (Emotion       │         │   │
│  │  │  Distribution) │  │  Dimensional)  │  │  Patterns)     │         │   │
│  │  └────────────────┘  └────────────────┘  └────────────────┘         │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│                                      │                                        │
│                                      ▼                                        │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │                    INTERACTION LAYER                                   │   │
│  │  ┌──────────────────────────────────────────────────────────────┐   │   │
│  │  │ Gesture & Input Controller                                     │   │   │
│  │  │ - Mouse/Touch interaction                                      │   │   │
│  │  │ - Voice commands ("more energetic", "make it sadder")         │   │   │
│  │  │ - MIDI controller integration (sliders, knobs)                │   │   │
│  │  │ - Keyboard shortcuts for quick adjustments                    │   │   │
│  │  └──────────────────────────────────────────────────────────────┘   │   │
│  │  ┌──────────────────────────────────────────────────────────────┐   │   │
│  │  │ Real-Time Emotion Tracker                                     │   │   │
│  │  │ - Emotional state positioning                                  │   │   │
│  │  │ - Transition path recording                                   │   │   │
│  │  │ - Undo/Redo emotional changes                                 │   │   │
│  │  └──────────────────────────────────────────────────────────────┘   │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│                                      │                                        │
│                                      ▼                                        │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │                  EMOTION ANALYSIS ENGINE                              │   │
│  │  ┌──────────────────────────────────────────────────────────────┐   │   │
│  │  │ Multi-Dimensional Emotion Model                                │   │   │
│  │  │                                                                │   │   │
│  │  │  Valence (Positive ↔ Negative)                                 │   │   │
│  │  │    ┌─────────────────────────────────┐                         │   │   │
│  │  │    │    Joy     │    Tension          │                         │   │   │
│  │  │    │ (+0.8)     │    (+0.5)           │                         │   │   │
│  │  │    ├────────────┼────────────┐        │                         │   │   │
│  │  │    │ Contentment│  Neutral   │        │                         │   │   │
│  │  │    │ (+0.2)     │  (0.0)     │        │                         │   │   │
│  │  │    ├────────────┼────────────┤        │                         │   │   │
│  │  │    │ Sadness    │    Anger   │        │                         │   │   │
│  │  │    │ (-0.6)     │    (-0.3)  │        │                         │   │   │
│  │  │    └─────────────────────────────────┘                         │   │   │
│  │  │                                                                │   │   │
│  │  │  Arousal (Calm ↔ Excited)                                      │   │   │
│  │  │  Dominance (Submissive ↔ Dominant)                             │   │   │
│  │  │  Tempo (Slow ↔ Fast)                                           │   │   │
│  │  └──────────────────────────────────────────────────────────────┘   │   │
│  │  ┌──────────────────────────────────────────────────────────────┐   │   │
│  │  │ Emotion-to-Prompt Translator                                   │   │   │
│  │  │ - Semantic mapping from emotions to descriptive language      │   │   │
│  │  │ - Genre-specific emotion vocabulary                            │   │   │
│  │  │ - Cultural emotion expression adapters (PL/EN)                │   │   │
│  │  └──────────────────────────────────────────────────────────────┘   │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│                                      │                                        │
│                                      ▼                                        │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │                   PROMPT GENERATION ENGINE                            │   │
│  │  ┌──────────────────────────────────────────────────────────────┐   │   │
│  │  │ Visual Prompt Builder                                          │   │   │
│  │  │ - Drag-and-drop emotion blocks                                 │   │   │
│  │  │ - Real-time prompt preview                                     │   │   │
│  │  │ - Visual feedback on prompt quality                           │   │   │
│  │  └──────────────────────────────────────────────────────────────┘   │   │
│  │  ┌──────────────────────────────────────────────────────────────┐   │   │
│  │  │ Emotion Tag Library                                            │   │   │
│  │  │ - 200+ emotion-specific tags organized by dimensions          │   │   │
│  │  │ - Polish language emotion tags (rześnik emocjonalny)          │   │   │
│  │  │ - Genre-specific emotional vocabulary                         │   │   │
│  │  └──────────────────────────────────────────────────────────────┘   │   │
│  │  ┌──────────────────────────────────────────────────────────────┐   │   │
│  │  │ Prompt Quality Scorer                                          │   │   │
│  │  │ - Emotional coherence metrics                                 │   │   │
│  │  │ - Genre appropriateness scoring                               │   │   │
│  │  │ - Language naturalness evaluation                             │   │   │
│  │  └──────────────────────────────────────────────────────────────┘   │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│                                      │                                        │
│                                      ▼                                        │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │                        OUTPUT LAYER                                    │   │
│  │  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐  ┌───────────┐ │   │
│  │  │ Suno AI      │  │ Udio         │  │ PLLuM        │  │ Export    │ │   │
│  │  │ Prompts      │  │ Prompts      │  │ Prompts      │  │ (JSON/MD) │ │   │
│  │  └──────────────┘  └──────────────┘  └──────────────┘  └───────────┘ │   │
│  │  ┌──────────────────────────────────────────────────────────────┐   │   │
│  │  │ Visualization Exports                                          │   │   │
│  │  │ - Emotion trajectory screenshots                               │   │   │
│  │  │ - Animated progression videos (GIF/MP4)                       │   │   │
│  │  │ - Interactive HTML exports                                     │   │   │
│  │  └──────────────────────────────────────────────────────────────┘   │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## Key Components

### 1. Visualization Layer

#### A. 2D Emotion Plane (Valence-Arousal)
```javascript
class EmotionPlane2D {
  constructor(canvasId) {
    this.canvas = document.getElementById(canvasId);
    this.ctx = this.canvas.getContext('2d');
    this.currentPosition = { x: 0, y: 0 }; // Valence, Arousal
    this.history = []; // Track user's emotional journey
  }

  render() {
    // Draw coordinate system
    this.drawAxes();

    // Draw emotion quadrants
    this.drawQuadrants();

    // Draw current position
    this.drawCurrentPosition();

    // Draw history path
    this.drawHistoryPath();

    // Draw emotion labels
    this.drawEmotionLabels();
  }

  drawQuadrants() {
    const quadrants = [
      { name: 'Joy/Excitement', color: 'rgba(255, 200, 0, 0.2)', x: 1, y: 1 },
      { name: 'Contentment/Relaxation', color: 'rgba(0, 200, 255, 0.2)', x: 1, y: -1 },
      { name: 'Sadness/Depression', color: 'rgba(100, 100, 150, 0.2)', x: -1, y: -1 },
      { name: 'Anger/Tension', color: 'rgba(255, 50, 50, 0.2)', x: -1, y: 1 }
    ];

    quadrants.forEach(q => {
      this.ctx.fillStyle = q.color;
      this.ctx.fillRect(
        q.x > 0 ? this.canvas.width / 2 : 0,
        q.y > 0 ? 0 : this.canvas.height / 2,
        this.canvas.width / 2,
        this.canvas.height / 2
      );
    });
  }

  handleInput(x, y) {
    // Update position
    this.currentPosition = { x, y };
    this.history.push({ x, y, timestamp: Date.now() });

    // Trigger prompt regeneration
    this.onPositionChange(this.currentPosition);

    // Re-render
    this.render();
  }

  onPositionChange(position) {
    const valence = position.x; // -1 to 1
    const arousal = position.y;  // -1 to 1
    const emotion = this.getEmotionFromPosition(valence, arousal);

    // Generate prompt based on emotion
    const prompt = promptGenerator.generateFromEmotion(emotion);

    // Update preview
    promptPreview.update(prompt);
  }
}
```

**Visual Layout:**
```
      AROUSAL (Excited)
          ▲
          │
   Anger  │  Joy/Excitement
   Tension│  (High Valence,
          │   High Arousal)
  ─────────┼────────────▶ VALENCE (Positive)
  Sadness  │  Contentment
  (Low     │  (High Valence,
   Valence,│   Low Arousal)
   Low     │
   Arousal)│
          ▼
     (Calm/Relaxed)
```

#### B. 3D Emotion Space (VAD-T Model)
```javascript
class EmotionSpace3D {
  constructor(containerId) {
    this.container = document.getElementById(containerId);
    this.scene = new THREE.Scene();
    this.camera = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 1000);
    this.renderer = new THREE.WebGLRenderer({ antialias: true });
    this.controls = new THREE.OrbitControls(this.camera, this.renderer.domElement);

    // Dimensions: Valence (X), Arousal (Y), Dominance (Z)
    this.currentPosition = new THREE.Vector3(0, 0, 0);
    this.emotionPoints = [];

    this.init();
  }

  init() {
    // Create emotion cloud
    this.createEmotionCloud();

    // Create current position marker
    this.createPositionMarker();

    // Create trajectory line
    this.createTrajectoryLine();

    // Set up lighting
    this.setupLighting();

    // Start animation loop
    this.animate();
  }

  createEmotionCloud() {
    const emotions = [
      { name: 'Ecstasy', position: { x: 0.9, y: 0.9, z: 0.8 }, color: 0xffdd00 },
      { name: 'Joy', position: { x: 0.7, y: 0.6, z: 0.5 }, color: 0xffaa00 },
      { name: 'Interest', position: { x: 0.5, y: 0.4, z: 0.3 }, color: 0xff8800 },
      { name: 'Pleasure', position: { x: 0.6, y: 0.2, z: 0.4 }, color: 0x00ddff },
      { name: 'Contentment', position: { x: 0.4, y: -0.2, z: 0.2 }, color: 0x00aaff },
      { name: 'Sleepiness', position: { x: 0.1, y: -0.6, z: -0.2 }, color: 0x8888ff },
      { name: 'Neutral', position: { x: 0, y: 0, z: 0 }, color: 0xaaaaaa },
      { name: 'Boredom', position: { x: -0.2, y: -0.4, z: -0.3 }, color: 0x886688 },
      { name: 'Sadness', position: { x: -0.6, y: -0.5, z: -0.4 }, color: 0x6666aa },
      { name: 'Grief', position: { x: -0.8, y: -0.7, z: -0.6 }, color: 0x444488 },
      { name: 'Anxiety', position: { x: -0.5, y: 0.3, z: -0.4 }, color: 0xff6688 },
      { name: 'Fear', position: { x: -0.7, y: 0.5, z: -0.6 }, color: 0xff4466 },
      { name: 'Anger', position: { x: -0.6, y: 0.7, z: -0.3 }, color: 0xff4444 },
      { name: 'Rage', position: { x: -0.9, y: 0.9, z: -0.7 }, color: 0xff0000 }
    ];

    emotions.forEach(emotion => {
      const geometry = new THREE.SphereGeometry(0.08, 16, 16);
      const material = new THREE.MeshPhongMaterial({
        color: emotion.color,
        emissive: emotion.color,
        emissiveIntensity: 0.3
      });
      const sphere = new THREE.Mesh(geometry, material);
      sphere.position.set(emotion.position.x, emotion.position.y, emotion.position.z);
      sphere.userData = { name: emotion.name };

      this.scene.add(sphere);
      this.emotionPoints.push(sphere);
    });
  }

  createTrajectoryLine() {
    const material = new THREE.LineBasicMaterial({
      color: 0x00ff88,
      linewidth: 2
    });
    const geometry = new THREE.BufferGeometry();
    this.trajectoryLine = new THREE.Line(geometry, material);
    this.trajectoryPoints = [];
    this.scene.add(this.trajectoryLine);
  }

  updatePosition(valence, arousal, dominance) {
    this.currentPosition.set(valence, arousal, dominance);

    // Update marker
    this.positionMarker.position.copy(this.currentPosition);

    // Add to trajectory
    this.trajectoryPoints.push(this.currentPosition.clone());
    const positions = new Float32Array(this.trajectoryPoints.length * 3);
    this.trajectoryPoints.forEach((point, i) => {
      positions[i * 3] = point.x;
      positions[i * 3 + 1] = point.y;
      positions[i * 3 + 2] = point.z;
    });
    this.trajectoryLine.geometry.setAttribute('position', new THREE.BufferAttribute(positions, 3));

    // Find nearest emotion
    const nearestEmotion = this.findNearestEmotion(this.currentPosition);

    // Generate prompt
    const prompt = this.generatePromptFromPosition(
      valence,
      arousal,
      dominance,
      nearestEmotion
    );

    return prompt;
  }
}
```

#### C. Timeline Progression View
```javascript
class EmotionTimeline {
  constructor(containerId) {
    this.container = document.getElementById(containerId);
    this.timeline = [];
    this.sections = ['intro', 'verse1', 'chorus', 'verse2', 'bridge', 'chorus', 'outro'];
    this.currentSection = 0;
  }

  render() {
    this.container.innerHTML = '';

    // Create timeline track
    const track = document.createElement('div');
    track.className = 'timeline-track';

    // Create section markers
    this.sections.forEach((section, index) => {
      const marker = document.createElement('div');
      marker.className = 'timeline-marker';
      marker.textContent = section;
      marker.onclick = () => this.selectSection(index);

      if (index === this.currentSection) {
        marker.classList.add('active');
      }

      track.appendChild(marker);
    });

    // Draw emotion curve
    const canvas = document.createElement('canvas');
    canvas.className = 'emotion-curve';
    this.drawEmotionCurve(canvas);

    this.container.appendChild(track);
    this.container.appendChild(canvas);
  }

  drawEmotionCurve(canvas) {
    const ctx = canvas.getContext('2d');
    const width = canvas.width = this.container.clientWidth;
    const height = canvas.height = 150;

    // Clear canvas
    ctx.clearRect(0, 0, width, height);

    // Draw grid
    this.drawGrid(ctx, width, height);

    // Draw emotion curve
    if (this.timeline.length > 0) {
      ctx.beginPath();
      ctx.strokeStyle = '#00ff88';
      ctx.lineWidth = 3;

      this.timeline.forEach((point, index) => {
        const x = (index / (this.timeline.length - 1)) * width;
        const y = height - ((point.valence + 1) / 2) * height; // Map -1..1 to height..0

        if (index === 0) {
          ctx.moveTo(x, y);
        } else {
          ctx.lineTo(x, y);
        }
      });

      ctx.stroke();

      // Draw section boundaries
      this.sections.forEach((section, index) => {
        const x = (index / (this.sections.length - 1)) * width;
        ctx.beginPath();
        ctx.strokeStyle = '#666';
        ctx.lineWidth = 1;
        ctx.setLineDash([5, 5]);
        ctx.moveTo(x, 0);
        ctx.lineTo(x, height);
        ctx.stroke();
        ctx.setLineDash([]);
      });
    }
  }

  addSection(emotion) {
    this.timeline.push(emotion);
    this.render();
  }
}
```

---

### 2. Interaction Layer

#### A. Gesture & Input Controller
```javascript
class InputController {
  constructor(emotionPlane, emotionSpace) {
    this.emotionPlane = emotionPlane;
    this.emotionSpace = emotionSpace;
    this.setupEventListeners();
    this.setupVoiceControl();
    this.setupMIDIControl();
  }

  setupEventListeners() {
    // Mouse/Touch input
    this.emotionPlane.canvas.addEventListener('mousedown', this.handleDragStart.bind(this));
    this.emotionPlane.canvas.addEventListener('mousemove', this.handleDragMove.bind(this));
    this.emotionPlane.canvas.addEventListener('mouseup', this.handleDragEnd.bind(this));

    // Touch support
    this.emotionPlane.canvas.addEventListener('touchstart', this.handleTouchStart.bind(this));
    this.emotionPlane.canvas.addEventListener('touchmove', this.handleTouchMove.bind(this));
    this.emotionPlane.canvas.addEventListener('touchend', this.handleTouchEnd.bind(this));

    // Keyboard shortcuts
    document.addEventListener('keydown', this.handleKeyPress.bind(this));
  }

  handleKeyPress(event) {
    const shortcuts = {
      'ArrowUp': () => this.adjustEmotion('arousal', 0.1),
      'ArrowDown': () => this.adjustEmotion('arousal', -0.1),
      'ArrowRight': () => this.adjustEmotion('valence', 0.1),
      'ArrowLeft': () => this.adjustEmotion('valence', -0.1),
      'w': () => this.adjustEmotion('dominance', 0.1),
      's': () => this.adjustEmotion('dominance', -0.1),
      'r': () => this.resetEmotion(),
      'z': () => this.undo(),
      'y': () => this.redo()
    };

    if (shortcuts[event.key]) {
      event.preventDefault();
      shortcuts[event.key]();
    }
  }

  setupVoiceControl() {
    if ('webkitSpeechRecognition' in window) {
      this.recognition = new webkitSpeechRecognition();
      this.recognition.continuous = true;
      this.recognition.interimResults = true;

      this.recognition.onresult = (event) => {
        const transcript = event.results[event.results.length - 1][0].transcript.toLowerCase();
        this.processVoiceCommand(transcript);
      };

      this.recognition.start();
    }
  }

  processVoiceCommand(command) {
    const emotionMap = {
      'happy': { valence: 0.7, arousal: 0.5 },
      'sad': { valence: -0.6, arousal: -0.4 },
      'angry': { valence: -0.5, arousal: 0.7 },
      'energetic': { valence: 0.6, arousal: 0.8 },
      'calm': { valence: 0.3, arousal: -0.5 },
      'tense': { valence: -0.3, arousal: 0.6 },
      'more excited': { delta: { arousal: 0.2 } },
      'make it sadder': { delta: { valence: -0.3, arousal: -0.1 } },
      'brighter': { delta: { valence: 0.2 } }
    };

    // Parse command
    for (const [keyword, emotion] of Object.entries(emotionMap)) {
      if (command.includes(keyword)) {
        if (emotion.delta) {
          this.adjustEmotionMultiple(emotion.delta);
        } else {
          this.setEmotion(emotion);
        }
        break;
      }
    }
  }

  setupMIDIControl() {
    navigator.requestMIDIAccess().then(midiAccess => {
      for (const input of midiAccess.inputs.values()) {
        input.onmidimessage = this.handleMIDIMessage.bind(this);
      }
    });
  }

  handleMIDIMessage(message) {
    const [status, data1, data2] = message.data;

    // Map MIDI CC to emotion dimensions
    if (status >= 176 && status <= 191) {  // Control Change
      const ccNumber = data1;
      const value = data2 / 127;  // Normalize to 0-1

      const ccMapping = {
        1: 'valence',      // Mod wheel
        2: 'arousal',      // Breath control
        3: 'dominance'     // Foot controller
      };

      if (ccMapping[ccNumber]) {
        const dimension = ccMapping[ccNumber];
        const normalizedValue = (value - 0.5) * 2;  // Map to -1 to 1
        this.setEmotionDimension(dimension, normalizedValue);
      }
    }
  }
}
```

---

### 3. Emotion Analysis Engine

#### A. Multi-Dimensional Emotion Model
```python
from typing import Dict, List, Tuple
import numpy as np

class MultiDimensionalEmotionModel:
    """
    Models emotions across multiple dimensions: Valence, Arousal, Dominance, Tempo
    """

    def __init__(self):
        # Emotion space boundaries
        self.dimensions = {
            'valence': (-1.0, 1.0),      # Negative ↔ Positive
            'arousal': (-1.0, 1.0),      # Calm ↔ Excited
            'dominance': (-1.0, 1.0),    # Submissive ↔ Dominant
            'tempo': (60.0, 180.0)       # BPM range
        }

        # Predefined emotion templates
        self.emotion_templates = {
            'ecstatic': {'valence': 0.9, 'arousal': 0.9, 'dominance': 0.7, 'tempo': 140},
            'joyful': {'valence': 0.7, 'arousal': 0.6, 'dominance': 0.5, 'tempo': 120},
            'content': {'valence': 0.5, 'arousal': -0.2, 'dominance': 0.3, 'tempo': 90},
            'calm': {'valence': 0.2, 'arousal': -0.6, 'dominance': -0.1, 'tempo': 70},
            'sad': {'valence': -0.6, 'arousal': -0.4, 'dominance': -0.5, 'tempo': 75},
            'depressed': {'valence': -0.9, 'arousal': -0.7, 'dominance': -0.8, 'tempo': 60},
            'anxious': {'valence': -0.4, 'arousal': 0.5, 'dominance': -0.6, 'tempo': 110},
            'angry': {'valence': -0.5, 'arousal': 0.7, 'dominance': 0.4, 'tempo': 130},
            'furious': {'valence': -0.8, 'arousal': 0.9, 'dominance': 0.7, 'tempo': 160},
            'neutral': {'valence': 0.0, 'arousal': 0.0, 'dominance': 0.0, 'tempo': 100}
        }

    def get_emotion_state(self, valence: float, arousal: float, dominance: float, tempo: float) -> Dict:
        """
        Returns complete emotion state with labels
        """
        # Validate inputs
        valence = np.clip(valence, *self.dimensions['valence'])
        arousal = np.clip(arousal, *self.dimensions['arousal'])
        dominance = np.clip(dominance, *self.dimensions['dominance'])
        tempo = np.clip(tempo, *self.dimensions['tempo'])

        # Find nearest template
        nearest_emotion = self._find_nearest_emotion(valence, arousal, dominance)

        return {
            'valence': valence,
            'arousal': arousal,
            'dominance': dominance,
            'tempo': tempo,
            'primary_emotion': nearest_emotion['name'],
            'intensity': nearest_emotion['distance'],
            'coordinates': (valence, arousal, dominance),
            'tempo_category': self._categorize_tempo(tempo)
        }

    def _find_nearest_emotion(self, valence: float, arousal: float, dominance: float) -> Dict:
        """
        Finds the nearest predefined emotion using Euclidean distance
        """
        min_distance = float('inf')
        nearest = None

        for name, template in self.emotion_templates.items():
            distance = np.sqrt(
                (valence - template['valence']) ** 2 +
                (arousal - template['arousal']) ** 2 +
                (dominance - template['dominance']) ** 2
            )

            if distance < min_distance:
                min_distance = distance
                nearest = {'name': name, 'distance': distance}

        return nearest

    def _categorize_tempo(self, tempo: float) -> str:
        """
        Categorizes BPM into musical terms
        """
        if tempo < 60:
            return 'largo'
        elif tempo < 72:
            return 'adagio'
        elif tempo < 96:
            return 'andante'
        elif tempo < 120:
            return 'moderato'
        elif tempo < 156:
            return 'allegro'
        else:
            return 'presto'

    def interpolate_emotions(self, emotion1: Dict, emotion2: Dict, t: float) -> Dict:
        """
        Interpolates between two emotions for transitions
        t: 0.0 to 1.0 (0 = emotion1, 1 = emotion2)
        """
        return {
            'valence': emotion1['valence'] + (emotion2['valence'] - emotion1['valence']) * t,
            'arousal': emotion1['arousal'] + (emotion2['arousal'] - emotion1['arousal']) * t,
            'dominance': emotion1['dominance'] + (emotion2['dominance'] - emotion1['dominance']) * t,
            'tempo': emotion1['tempo'] + (emotion2['tempo'] - emotion1['tempo']) * t
        }
```

#### B. Emotion-to-Prompt Translator
```python
class EmotionToPromptTranslator:
    """
    Translates emotion coordinates into natural language prompts
    """

    def __init__(self, language='en'):
        self.language = language
        self.load_vocabulary()

    def load_vocabulary(self):
        """
        Loads emotion vocabulary for different languages and genres
        """
        self.vocabulary = {
            'en': {
                'valence_positive': ['joyful', 'uplifting', 'bright', 'cheerful', 'optimistic'],
                'valence_negative': ['melancholic', 'somber', 'dark', 'bleak', 'gloomy'],
                'arousal_high': ['energetic', 'intense', 'dynamic', 'powerful', 'vibrant'],
                'arousal_low': ['calm', 'gentle', 'peaceful', 'serene', 'tranquil'],
                'dominance_high': ['confident', 'bold', 'assertive', 'commanding', 'strong'],
                'dominance_low': ['vulnerable', 'tender', 'soft', 'delicate', 'subtle']
            },
            'pl': {
                'valence_positive': ['radosny', 'podniosły', 'jasny', 'wesoły', 'optymistyczny'],
                'valence_negative': ['melancholijny', 'ponury', 'ciemny', 'smutny', 'zgaszony'],
                'arousal_high': ['energetyczny', 'intensywny', 'dynamiczny', 'mocny', 'żywy'],
                'arousal_low': ['spokojny', 'łagodny', 'pokoju', 'cichy', 'delikatny'],
                'dominance_high': ['pewny siebie', 'odważny', 'zdecydowany', 'mocny', 'silny'],
                'dominance_low': ['bezbronny', 'tkliwy', 'miękki', 'subtelny', 'wrażliwy']
            }
        }

        self.genre_modifiers = {
            'pop': {
                'high_arousal': 'catchy', 'low_arousal': 'laid-back',
                'high_valence': 'feel-good', 'low_valence': 'heartbreak'
            },
            'rock': {
                'high_arousal': 'hard-driving', 'low_arousal': 'acoustic',
                'high_valence': 'anthemic', 'low_valence': 'grunge'
            },
            'electronic': {
                'high_arousal': 'high-energy', 'low_arousal': 'ambient',
                'high_valence': 'uplifting', 'low_valence': 'dark'
            },
            'hip-hop': {
                'high_arousal': 'hard-hitting', 'low_arousal': 'chill',
                'high_valence': 'triumphant', 'low_valence': 'gritty'
            }
        }

    def translate_emotion_to_prompt(self, emotion_state: Dict, genre: str = 'pop') -> str:
        """
        Generates natural language prompt from emotion state
        """
        valence = emotion_state['valence']
        arousal = emotion_state['arousal']
        dominance = emotion_state['dominance']
        tempo = emotion_state['tempo']
        primary_emotion = emotion_state['primary_emotion']

        # Select vocabulary based on language
        vocab = self.vocabulary[self.language]

        # Build prompt components
        components = []

        # Primary emotion
        components.append(primary_emotion)

        # Valence descriptor
        if valence > 0.3:
            components.append(np.random.choice(vocab['valence_positive']))
        elif valence < -0.3:
            components.append(np.random.choice(vocab['valence_negative']))

        # Arousal descriptor
        if arousal > 0.3:
            components.append(np.random.choice(vocab['arousal_high']))
        elif arousal < -0.3:
            components.append(np.random.choice(vocab['arousal_low']))

        # Dominance descriptor
        if dominance > 0.4:
            components.append(np.random.choice(vocab['dominance_high']))
        elif dominance < -0.4:
            components.append(np.random.choice(vocab['dominance_low']))

        # Genre-specific modifiers
        if genre in self.genre_modifiers:
            modifiers = self.genre_modifiers[genre]

            if arousal > 0.5:
                components.append(modifiers['high_arousal'])
            elif arousal < -0.5:
                components.append(modifiers['low_arousal'])

            if valence > 0.5:
                components.append(modifiers['high_valence'])
            elif valence < -0.5:
                components.append(modifiers['low_valence'])

        # Tempo descriptor
        components.append(f"{int(tempo)} BPM")

        # Combine into natural language prompt
        prompt = self._construct_natural_prompt(components, genre)

        return prompt

    def _construct_natural_prompt(self, components: List[str], genre: str) -> str:
        """
        Constructs natural language prompt from components
        """
        # Remove duplicates while preserving order
        seen = set()
        unique_components = [x for x in components if not (x in seen or seen.add(x))]

        # Construct prompt based on genre conventions
        if genre in ['pop', 'rock']:
            prompt = f"A {', '.join(unique_components[:-1])} {genre} song at {unique_components[-1]}"
        elif genre == 'electronic':
            prompt = f"{', '.join(unique_components[:-1])} electronic track, {unique_components[-1]}"
        elif genre == 'hip-hop':
            prompt = f"{', '.join(unique_components[:-1])} hip-hop beat, {unique_components[-1]}"
        else:
            prompt = f"{', '.join(unique_components)}"

        return prompt
```

---

### 4. Prompt Generation Engine

#### A. Visual Prompt Builder
```javascript
class VisualPromptBuilder {
  constructor() {
    this.emotionBlocks = [];
    this.promptPreview = document.getElementById('prompt-preview');
    this.emotionTagLibrary = new EmotionTagLibrary();
  }

  addEmotionBlock(emotion) {
    const block = {
      id: Date.now(),
      emotion: emotion,
      tags: this.emotionTagLibrary.getTagsForEmotion(emotion)
    };

    this.emotionBlocks.push(block);
    this.renderBlocks();
    this.generatePrompt();
  }

  renderBlocks() {
    const container = document.getElementById('emotion-blocks');
    container.innerHTML = '';

    this.emotionBlocks.forEach(block => {
      const blockElement = document.createElement('div');
      blockElement.className = 'emotion-block';
      blockElement.style.backgroundColor = this.getEmotionColor(block.emotion);
      blockElement.innerHTML = `
        <span class="emotion-name">${block.emotion.primary_emotion}</span>
        <button class="remove-block" data-id="${block.id}">×</button>
      `;

      container.appendChild(blockElement);
    });
  }

  generatePrompt() {
    if (this.emotionBlocks.length === 0) {
      this.promptPreview.textContent = 'Add emotions to generate prompt...';
      return;
    }

    // Combine emotions
    const combinedEmotion = this.combineEmotions(this.emotionBlocks);

    // Generate prompt using translator
    const translator = new EmotionToPromptTranslator();
    const prompt = translator.translate_emotion_to_prompt(combinedEmotion, this.selectedGenre);

    // Update preview
    this.promptPreview.textContent = prompt;

    // Calculate quality score
    const score = this.calculateQualityScore(prompt);
    this.displayQualityScore(score);
  }

  combineEmotions(blocks) {
    // Average emotion values
    const n = blocks.length;
    const combined = {
      valence: blocks.reduce((sum, b) => sum + b.emotion.valence, 0) / n,
      arousal: blocks.reduce((sum, b) => sum + b.emotion.arousal, 0) / n,
      dominance: blocks.reduce((sum, b) => sum + b.emotion.dominance, 0) / n,
      tempo: blocks.reduce((sum, b) => sum + b.emotion.tempo, 0) / n
    };

    // Find nearest primary emotion
    const model = new MultiDimensionalEmotionModel();
    const state = model.get_emotion_state(
      combined.valence,
      combined.arousal,
      combined.dominance,
      combined.tempo
    );

    return state;
  }

  calculateQualityScore(prompt) {
    // Simple heuristic: longer prompts with more descriptors tend to be better
    let score = 50;  // Base score

    // Length bonus
    if (prompt.length > 50) score += 10;
    if (prompt.length > 100) score += 10;

    // Descriptor count bonus
    const descriptorCount = (prompt.match(/(adjective|energetic|calm|happy|sad|angry)/gi) || []).length;
    score += descriptorCount * 5;

    // Genre specificity bonus
    if (prompt.includes('song') || prompt.includes('track') || prompt.includes('beat')) {
      score += 10;
    }

    return Math.min(score, 100);
  }
}
```

#### B. Emotion Tag Library
```python
class EmotionTagLibrary:
    """
    Comprehensive library of emotion-specific tags for prompt enhancement
    """

    def __init__(self):
        self.tags = {
            'joy': {
                'primary': ['joyful', 'happy', 'cheerful', 'upbeat', 'bright'],
                'secondary': ['optimistic', 'lighthearted', 'carefree', 'playful'],
                'instrumental': ['major key', 'sparkling', 'warm', 'bouncy'],
                'vocal': ['bright vocals', 'melodic', 'soaring', 'harmonies'],
                'production': ['polished', 'clean', 'punchy', 'radiant']
            },
            'sadness': {
                'primary': ['sad', 'melancholic', 'somber', 'mournful', 'bleak'],
                'secondary': ['sorrowful', 'gloomy', 'despondent', 'wistful'],
                'instrumental': ['minor key', 'slow tempo', 'cello', 'piano'],
                'vocal': ['haunting', 'tender', 'vulnerable', 'raw emotion'],
                'production': ['sparse', 'atmospheric', 'reverb', 'intimate']
            },
            'anger': {
                'primary': ['angry', 'aggressive', 'furious', 'intense', 'hostile'],
                'secondary': ['outraged', 'volatile', 'explosive', 'heated'],
                'instrumental': ['distorted guitars', 'heavy drums', 'power chords'],
                'vocal': ['shouting', 'raspy', 'gritty', 'powerful'],
                'production': ['raw', 'lo-fi', 'compressed', 'in-your-face']
            },
            'fear': {
                'primary': ['fearful', 'anxious', 'tense', 'nervous', 'apprehensive'],
                'secondary': ['unsettling', 'ominous', 'dreadful', 'suspenseful'],
                'instrumental': ['dissonant', 'tremolo', 'unpredictable', 'dark'],
                'vocal': ['whispered', 'trembling', 'urgent', 'breathless'],
                'production': ['creepy', 'atmospheric', 'haunting', 'eerie']
            },
            'love': {
                'primary': ['romantic', 'loving', 'passionate', 'tender', 'affectionate'],
                'secondary': ['devoted', 'sentimental', 'intimate', 'warm'],
                'instrumental': ['soft piano', 'strings', 'acoustic guitar'],
                'vocal': ['sweet', 'gentle', 'soothing', 'sincere'],
                'production': ['lush', 'smooth', 'polished', 'romantic']
            },
            'surprise': {
                'primary': ['surprising', 'unexpected', 'sudden', 'shocking', 'dramatic'],
                'secondary': ['astonishing', 'startling', 'jarring', 'abrupt'],
                'instrumental': ['dynamic shifts', 'unpredictable', 'dramatic pauses'],
                'vocal': ['exclamations', 'dynamic range', 'expressive'],
                'production': ['impactful', 'cinematic', 'dramatic', 'powerful']
            }
        }

        # Polish language emotion tags
        self.polish_tags = {
            'radość': {
                'primary': ['radosny', 'wesoły', 'pogodny', 'radowy', 'ucieszony'],
                'secondary': ['optymistyczny', 'beztroski', 'żywiołowy', 'promienny'],
                'instrumental': ['dur', 'jasny', 'ciepły', 'podskakujący'],
                'vocal': ['jasny wokal', 'melodyjny', 'wzniosły', 'harmonie'],
                'production': ['polerowany', 'czysty', ' energetyczny', 'promienny']
            },
            'smutek': {
                'primary': ['smutny', 'melancholijny', 'ponury', 'żałobny', 'przygnębiony'],
                'secondary': ['smutny', 'tęskniący', 'zasmucony', 'z nostalgii'],
                'instrumental': ['mol', 'wolne tempo', 'wiolonczela', 'fortepian'],
                'vocal': ['przejmujący', 'delikatny', 'bezbronny', 'szczery'],
                'production': ['rzadki', 'atmosferyczny', 'pogłos', 'intymny']
            }
        }

    def get_tags_for_emotion(self, emotion_state: Dict) -> List[str]:
        """
        Returns relevant tags based on emotion state
        """
        primary_emotion = emotion_state['primary_emotion']
        valence = emotion_state['valence']
        arousal = emotion_state['arousal']

        # Select tag category
        if primary_emotion in ['ecstatic', 'joyful', 'content']:
            category = 'joy'
        elif primary_emotion in ['sad', 'grief', 'depressed']:
            category = 'sadness'
        elif primary_emotion in ['angry', 'furious', 'rage']:
            category = 'anger'
        elif primary_emotion in ['anxious', 'fear', 'tense']:
            category = 'fear'
        elif 'love' in primary_emotion.lower():
            category = 'love'
        else:
            category = 'joy'  # Default

        # Select tags based on intensity
        tags = []
        if category in self.tags:
            intensity = abs(valence) + abs(arousal)

            if intensity > 1.0:
                tags.extend(self.tags[category]['primary'])
            elif intensity > 0.5:
                tags.extend(self.tags[category]['secondary'])

            # Add instrumental and vocal tags based on context
            tags.extend(self.tags[category]['instrumental'][:2])
            tags.extend(self.tags[category]['vocal'][:2])

        return tags
```

---

## UI Mockup Description

### Main Interface Layout

```
┌─────────────────────────────────────────────────────────────────────────────┐
│  EMOTION MAPPER v1.0                                    [?] [Settings] [?]  │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│  ┌─────────────────────────────────┐  ┌─────────────────────────────────┐  │
│  │   2D Emotion Plane              │  │   3D Emotion Space              │  │
│  │                                 │  │                                 │  │
│  │      AROUSAL                     │  │         [Interactive 3D]         │  │
│  │        ▲                         │  │                                 │  │
│  │    Joy │  Tension               │  │   Rotate: Mouse drag            │  │
│  │   (+0.8)│ (+0.5)                 │  │   Zoom: Scroll                  │  │
│  │   ─────┼────────▶ VALENCE        │  │   Pan: Right-click drag         │  │
│  │Content │ Neutral                 │  │                                 │  │
│  │ (+0.2)│ (0.0)                    │  │   Current Position:            │  │
│  │   ─────┼────────                 │  │   V: +0.35, A: +0.62, D: -0.12  │  │
│  │ Sadness│ Anger                   │  │   Nearest: Joyful              │  │
│  │  (-0.6)│ (-0.3)                  │  │                                 │  │
│  │        ▼                         │  └─────────────────────────────────┘  │
│  │    (Calm/Relaxed)                │                                      │
│  │                                 │  ┌─────────────────────────────────┐  │
│  │  [◉] Current Position            │  │   Prompt Preview                 │  │
│  │  [─] History Path                │  │                                 │  │
│  └─────────────────────────────────┘  │ "A joyful, upbeat, energetic     │  │
│                                        │  pop song at 120 BPM with        │  │
│  ┌─────────────────────────────────┐  │  bright vocals, polished         │  │
│  │   Timeline Progression           │  │  production, major key"         │  │
│  │                                 │  │                                 │  │
│  │  Intro │ V1  │ Chorus │ V2 │ Br │  │  Quality Score: ████████░░ 82%  │  │
│  │   ●    │ ●   │    ●    │ ●  │ ●  │  │                                 │  │
│  │   └──────┴─────┴────────┴────┴───│  │  [Copy] [Export] [Send to Suno] │  │
│  │                                 │  └─────────────────────────────────┘  │
│  │  [Add Section] [Clear]          │                                      │
│  └─────────────────────────────────┘  ┌─────────────────────────────────┐  │
│                                        │   Emotion Controls              │  │
│  ┌─────────────────────────────────┐  │                                 │  │
│  │   Genre Selector                │  │  Valence: ─────○───── (+0.35)   │  │
│  │                                 │  │  Arousal: ───○────── (+0.62)    │  │
│  │  [Pop] [Rock] [Electronic]      │  │  Dominance: ─────○─── (-0.12)   │  │
│  │  [Hip-Hop] [Jazz] [Classical]   │  │  Tempo: ─────────○─── (120 BPM) │  │
│  │                                 │  │                                 │  │
│  │   Language: [EN] [PL]           │  │  [Reset] [Randomize]            │  │
│  └─────────────────────────────────┘  └─────────────────────────────────┘  │
│                                                                              │
│  ┌──────────────────────────────────────────────────────────────────────┐  │
│  │   Voice/MIDI Controls                                                │  │
│  │  [🎤 Voice: "Make it sadder"]  [🎹 MIDI: Connected]  [⌨️ Shortcuts]  │  │
│  └──────────────────────────────────────────────────────────────────────┘  │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## Integration Points

### 1. Polish Language Support (PLLuM)
```python
class PolishEmotionMapper:
    """
    Polish-specific emotion mapping with cultural considerations
    """

    def __init__(self):
        self.polish_emotion_lexicon = self._load_polish_emotions()

    def _load_polish_emotions(self):
        return {
            'radosny': {'valence': 0.8, 'arousal': 0.6, 'cultural_context': 'traditional polish folk joy'},
            'żal': {'valence': -0.7, 'arousal': -0.4, 'cultural_context': 'polish melancholy (żałoba)'},
            'tęsknota': {'valence': -0.5, 'arousal': -0.2, 'cultural_context': 'nostalgic longing'},
            'złość': {'valence': -0.4, 'arousal': 0.7, 'cultural_context': 'righteous anger'},
            'spokój': {'valence': 0.3, 'arousal': -0.7, 'cultural_context': 'inner peace'}
        }

    def adapt_prompt_for_polish(self, base_prompt: str, emotion_state: Dict) -> str:
        """
        Adapts English prompt to Polish cultural context
        """
        # Translate emotion keywords
        polish_emotions = self._get_polish_emotion_equivalents(emotion_state)

        # Add Polish cultural markers if appropriate
        cultural_markers = self._get_cultural_markers(emotion_state)

        # Construct Polish-optimized prompt
        polish_prompt = f"{base_prompt}, Polish lyrics, {', '.join(polish_emotions)}, {cultural_markers}"

        return polish_prompt
```

---

## Example Use Cases

### Use Case 1: Visual Emotion Exploration
**Scenario:** Songwriter wants to explore emotional landscape for new song

**Workflow:**
1. Open Emotion Mapping Interface
2. Select 2D Emotion Plane view
3. Click and drag to explore emotional space:
   - Start at "Content" (valence: +0.2, arousal: -0.2)
   - Drag towards "Joy" (valence: +0.7, arousal: +0.6)
   - See real-time prompt updates: "A content, gentle pop song at 90 BPM" → "A joyful, upbeat pop song at 120 BPM"
4. Switch to 3D view, add dominance dimension
5. Rotate to explore full emotion space
6. Find optimal position: (V: +0.7, A: +0.5, D: +0.3)
7. Add to timeline as "Chorus" section
8. Repeat for other sections (verse, bridge)

### Use Case 2: Polish Language Love Song
**Scenario:** Create Polish love song with appropriate emotional vocabulary

**Workflow:**
1. Select Language: [PL]
2. Select Genre: [Pop]
3. Set emotion: "Love" (romantic, tender, warm)
4. Add secondary emotion: "Nostalgia" (tęsknota)
5. System generates Polish prompt:
   - "Piosenka romantyczna, sentymentalna, z nutą nostalgii, 90 BPM, ciepły wokal, delikatne pianino"
6. PLLuM optimizes Polish grammar and vocabulary
7. Generate variations with different intensity levels
8. Export to Suno AI for generation

### Use Case 3: Collaborative Emotion Mapping
**Scenario:** Two songwriters collaboratively map out song emotions

**Workflow:**
1. Enable collaboration mode
2. Share unique session URL
3. Both users see same emotion space
4. User 1 sets verse emotions (melancholic)
5. User 2 sets chorus emotions (uplifting)
6. System calculates emotional transition path
7. Both see real-time prompt previews for each section
8. Add bridge section with emotion interpolation
9. Export complete emotional arc to Suno AI

---

## Technical Specifications

### Frontend Stack
- **Framework:** React 18 or Vue 3
- **3D Graphics:** Three.js
- **Visualization:** D3.js, Canvas API
- **UI Components:** Material-UI or Tailwind CSS
- **State Management:** Redux or Pinia

### Backend Stack
- **Framework:** FastAPI (Python) or Express (Node.js)
- **ML Models:** Custom emotion models, VADER, LDA
- **Database:** PostgreSQL (user data), Redis (caching)
- **Real-time:** WebSocket for live updates

### Accessibility
- **WCAG 2.1 AA Compliance**
- **Screen Reader Support:** ARIA labels, semantic HTML
- **Keyboard Navigation:** Full keyboard control
- **High Contrast Mode:** Color-blind friendly
- **Font Scaling:** Resizable text

---

**Document Status:** Complete Architecture Specification
**Next Steps:** UI Prototyping, Emotion Model Training
**Dependencies:** Multi-Dimensional Emotion Model, PLLuM Integration

---

*End of Emotion Mapping Interface Architecture Document*
