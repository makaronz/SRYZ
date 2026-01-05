# Claude Workflow Automation Script

## 🚀 Szybki Start

```bash
# Uruchom skrypt
./claude-workflow.sh
```

## 📋 Dostępne Workflow

### 1. Full-Stack Feature Development
Kompletny rozwój funkcji od specyfikacji do deploymentu z wykorzystaniem SPARC methodology.

**Przykład użycia:**
- Nazwa funkcji: `user-authentication`
- Opis: `Implement user authentication with JWT`
- Faza: Wszystkie fazy

**Co robi automatycznie:**
- Research best practices
- Architecture design
- TDD implementation (90% coverage)
- Code review
- Documentation

### 2. GitHub PR Management
Automatyczna recenzja Pull Requestów z multi-agent swarm.

**Przykład użycia:**
- Numer PR: `123`
- Typ review: Comprehensive

**Co robi automatycznie:**
- Pobiera dane PR (jeśli gh CLI dostępne)
- Uruchamia multi-agent review (security, performance, style, architecture)
- Generuje komentarze

### 3. Legacy Code Refactoring
Bezpieczna modernizacja legacy codebase z testami jako safety net.

**Przykład użycia:**
- Cel: `UserService.js`
- Strategia: Pełny refactoring z testami

**Co robi automatycznie:**
- Analiza zależności
- Utworzenie testów (safety net)
- Incremental refactoring
- Verification (truth-score 0.98)

### 4. Research-Driven Innovation
Badania i implementacja innowacyjnych rozwiązań.

**Przykład użycia:**
- Temat: `AI-powered search implementations`
- Zakres: Comprehensive research + innovation

**Co robi automatycznie:**
- Comprehensive research z multiple sources
- Innovation & ideation
- Architecture design
- Knowledge graph building

### 5. Pair Programming Session
Współpraca z AI w trybie pair programming.

**Przykład użycia:**
- Tryb: TDD Mode
- Zadanie: `Implement shopping cart`

**Co robi automatycznie:**
- Uruchamia pair programming session
- TDD workflow (Red-Green-Refactor)
- Real-time verification
- Continuous review

### 6. Multi-Repo Coordination
Koordynacja zmian w wielu repozytoriach.

**Przykład użycia:**
- Repozytoria: `owner/repo1,owner/repo2,owner/repo3`
- Akcja: Coordinated changes

**Co robi automatycznie:**
- Analiza zależności między repo
- Coordinated changes
- Cross-repo PR management
- Synchronized releases

### 7. Quick Swarm Task
Szybkie zadanie z swarm orchestration.

**Przykład użycia:**
- Zadanie: `Add error handling to API`
- Typ: Proste swarm

**Co robi automatycznie:**
- Uruchamia swarm z odpowiednimi agentami
- Wykonuje zadanie
- Pokazuje postęp

### 8. System Status & Memory
Sprawdzenie statusu systemu i pamięci.

**Co pokazuje:**
- Status Claude Flow
- Status Hive Mind
- Ostatnie wpisy w pamięci
- Aktywne sesje

### 9. Brainstorm z Online Research (MCP Web Search)
Badania online z wykorzystaniem MCP tools + kreatywny brainstorming.

**Przykład użycia:**
- Temat: `AI-powered search implementations`
- Zakres: Pełny workflow (Research → Brainstorm → Synteza)
- Głębokość researchu: Comprehensive

**Co robi automatycznie:**
- Online research z wykorzystaniem MCP Web Search (SPARC researcher mode)
- Równoległe wyszukiwanie w internecie (academic, industry, news)
- Kreatywny brainstorming (SPARC innovator mode)
- Synteza wyników
- Tworzenie knowledge graph w pamięci
- Zapis wszystkich wyników w pamięci dla przyszłego użycia

**Funkcje:**
- ✅ Wykorzystuje MCP tools do web search (przez SPARC researcher)
- ✅ Równoległe wyszukiwanie z multiple sources
- ✅ Kreatywne generowanie pomysłów
- ✅ Automatyczna synteza wyników
- ✅ Knowledge graph building
- ✅ Citations i traceability

## 🎯 Przykłady Użycia

### Przykład 1: Nowa funkcja
```bash
./claude-workflow.sh
# Wybierz: 1 (Full-Stack Feature Development)
# Nazwa: user-authentication
# Opis: Implement JWT authentication
# Faza: 1 (Wszystkie fazy)
```

### Przykład 2: Code Review PR
```bash
./claude-workflow.sh
# Wybierz: 2 (GitHub PR Management)
# Numer PR: 123
# Typ review: 1 (Comprehensive)
```

### Przykład 3: Refactoring
```bash
./claude-workflow.sh
# Wybierz: 3 (Legacy Code Refactoring)
# Cel: UserService.js
# Strategia: 1 (Pełny refactoring z testami)
```

### Przykład 4: Szybkie zadanie
```bash
./claude-workflow.sh
# Wybierz: 7 (Quick Swarm Task)
# Zadanie: Add logging to API endpoints
# Typ: 1 (Proste swarm)
```

### Przykład 5: Brainstorm z Online Research
```bash
./claude-workflow.sh
# Wybierz: 9 (Brainstorm z Online Research)
# Temat: AI-powered search implementations
# Zakres: 1 (Pełny workflow)
# Głębokość researchu: 1 (Comprehensive)
```

## ⚙️ Wymagania

- Node.js 18+ (dla npx)
- Claude Flow zainstalowany (`npm install -g claude-flow@alpha`)
- (Opcjonalnie) GitHub CLI (`gh`) dla GitHub workflows

## 🔧 Konfiguracja

Skrypt automatycznie używa:
- `npx claude-flow@alpha` - zawsze najnowsza wersja alpha
- Hooks i memory system - automatycznie skonfigurowane
- MCP servers - automatycznie dostępne

## 📝 Notatki

- Wszystkie operacje są **autonomiczne** - skrypt wykonuje wszystko samodzielnie
- W przypadku błędów, skrypt kontynuuje pracę (używa `|| true`)
- Postęp jest wyświetlany w czasie rzeczywistym
- Możesz przerwać w dowolnym momencie (Ctrl+C)

## 🆘 Troubleshooting

**Problem**: "npx: command not found"
**Rozwiązanie**: Zainstaluj Node.js 18+

**Problem**: "claude-flow: command not found"
**Rozwiązanie**: `npm install -g claude-flow@alpha`

**Problem**: GitHub PR nie działa
**Rozwiązanie**: Zaloguj się przez `gh auth login`

## 🎨 Kolory Outputu

- 🟢 Zielony - Sukces
- 🔵 Niebieski - Informacja
- 🟡 Żółty - Ostrzeżenie/Pytanie
- 🔴 Czerwony - Błąd
- 🔵 Cyan - Postęp

---

**Ostatnia aktualizacja**: 2025-12-25
