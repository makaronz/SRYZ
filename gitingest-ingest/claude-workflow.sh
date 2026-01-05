#!/bin/bash

# Claude Flow Workflow Automation Script
# Automatycznie wykonuje wybrane workflow na podstawie interakcji użytkownika

set -e

# Kolory dla outputu
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
CYAN='\033[0;36m'
NC='\033[0m' # No Color

# Funkcja timeout dla macOS (timeout nie jest dostępne domyślnie)
run_with_timeout() {
    local timeout_seconds=$1
    shift
    local cmd="$@"
    
    # Sprawdź czy timeout jest dostępne
    if command -v timeout &> /dev/null; then
        timeout $timeout_seconds $cmd
    elif command -v gtimeout &> /dev/null; then
        # GNU timeout z Homebrew
        gtimeout $timeout_seconds $cmd
    else
        # Fallback dla macOS: użyj perl do timeout
        perl -e 'alarm shift; exec @ARGV' $timeout_seconds $cmd
    fi
}

# Logo i powitanie
echo -e "${CYAN}"
echo "╔═══════════════════════════════════════════════════════════╗"
echo "║         🌊 Claude Flow Workflow Automation 🌊            ║"
echo "║              v2.7.47 - Autonomous Execution              ║"
echo "╚═══════════════════════════════════════════════════════════╝"
echo -e "${NC}"

# Funkcja do wyświetlania menu
show_menu() {
    echo -e "\n${BLUE}Wybierz workflow do wykonania:${NC}\n"
    echo "1) 🚀 Full-Stack Feature Development (SPARC + Swarm)"
    echo "   → Kompletny rozwój funkcji od specyfikacji do deploymentu"
    echo ""
    echo "2) 🔍 GitHub PR Management (Multi-Agent Review)"
    echo "   → Automatyczna recenzja i zarządzanie Pull Requestami"
    echo ""
    echo "3) 🔧 Legacy Code Refactoring (Hive Mind + Memory)"
    echo "   → Bezpieczna modernizacja legacy codebase"
    echo ""
    echo "4) 🔬 Research-Driven Innovation (Researcher + Innovator)"
    echo "   → Badania i implementacja innowacyjnych rozwiązań"
    echo ""
    echo "5) 👥 Pair Programming Session (TDD + Verification)"
    echo "   → Współpraca z AI w trybie pair programming"
    echo ""
    echo "6) 🔗 Multi-Repo Coordination (GitHub Multi-Repo)"
    echo "   → Koordynacja zmian w wielu repozytoriach"
    echo ""
    echo "7) ⚡ Quick Swarm Task (Szybkie zadanie)"
    echo "   → Proste zadanie z swarm orchestration"
    echo ""
    echo "8) 📊 System Status & Memory"
    echo "   → Sprawdzenie statusu systemu i pamięci"
    echo ""
    echo "9) 💡 Brainstorm z Online Research (MCP Web Search)"
    echo "   → Badania online + kreatywny brainstorming z wykorzystaniem MCP"
    echo ""
    echo "0) ❌ Wyjście"
    echo ""
}

# Funkcja do pobierania inputu
get_input() {
    local prompt="$1"
    local default="$2"
    local input
    local prompt_text
    
    # Przygotuj tekst promptu
    if [ -n "$default" ]; then
        prompt_text="${YELLOW}$prompt${NC} [${CYAN}$default${NC}]: "
    else
        prompt_text="${YELLOW}$prompt${NC}: "
    fi
    
    # Wyświetl prompt na stderr (nie będzie w output funkcji)
    echo -ne "$prompt_text" >&2
    
    # Przeczytaj input
    read -r input
    
    # Usuń białe znaki z początku i końca
    input=$(echo "$input" | sed 's/^[[:space:]]*//;s/[[:space:]]*$//')
    
    # Zwróć wartość (tylko input, bez promptu)
    if [ -z "$input" ] && [ -n "$default" ]; then
        echo "$default"
    else
        echo "$input"
    fi
}

# Funkcja do wyświetlania postępu
show_progress() {
    local message="$1"
    echo -e "\n${GREEN}▶${NC} ${CYAN}$message${NC}"
}

# Funkcja do wyświetlania błędu
show_error() {
    local message="$1"
    echo -e "${RED}✗${NC} ${RED}$message${NC}"
}

# Funkcja do wyświetlania sukcesu
show_success() {
    local message="$1"
    echo -e "${GREEN}✓${NC} ${GREEN}$message${NC}"
}

# Workflow 1: Full-Stack Feature Development
workflow_fullstack() {
    show_progress "Inicjalizacja Full-Stack Feature Development workflow..."
    
    local feature_name=$(get_input "Nazwa funkcji do implementacji" "user-authentication")
    local description=$(get_input "Opis funkcji" "Implement user authentication with JWT")
    
    echo -e "\n${BLUE}Wybierz fazy do wykonania:${NC}"
    echo "1) Wszystkie fazy (Specification → Deployment)"
    echo "2) Specification & Research"
    echo "3) Architecture Design"
    echo "4) TDD Implementation"
    echo "5) Review & Quality"
    echo "6) Documentation & Deployment"
    
    local phase=$(get_input "Wybierz fazę" "1")
    
    show_progress "Uruchamianie workflow dla: $feature_name"
    
    case $phase in
        1|"")
            # Wszystkie fazy
            show_progress "Faza 1: Specification & Research"
            npx --yes claude-flow@alpha swarm "Research best practices for $description" --claude || true
            
            show_progress "Faza 2: Architecture Design"
            npx --yes claude-flow@alpha swarm "Design architecture for $description. Create system design, component structure, and technical specifications." \
                --strategy development --max-agents 2 || true
            
            show_progress "Faza 3: TDD Implementation"
            npx --yes claude-flow@alpha swarm "Implement $description using Test-Driven Development. Write tests first, then implement features. Target 90% code coverage." \
                --strategy testing --max-agents 3 --parallel || true
            
            show_progress "Faza 4: Review & Quality"
            npx --yes claude-flow@alpha swarm "Review code quality and security for $description. Check for bugs, security vulnerabilities, code smells, and best practices." \
                --strategy analysis --max-agents 2 || true
            
            show_progress "Faza 5: Documentation"
            npx --yes claude-flow@alpha swarm "Create comprehensive documentation for $description. Include API docs, usage examples, architecture diagrams, and setup instructions." \
                --strategy research --max-agents 1 || true
            ;;
        2)
            npx --yes claude-flow@alpha swarm "Research best practices for $description" --claude || true
            npx --yes claude-flow@alpha swarm "Analyze requirements for $description. Identify functional and non-functional requirements, constraints, and dependencies." \
                --strategy research --max-agents 2 || true
            ;;
        3)
            npx --yes claude-flow@alpha swarm "Design architecture for $description. Create system design, component structure, and technical specifications." \
                --strategy development --max-agents 2 || true
            ;;
        4)
            npx --yes claude-flow@alpha swarm "Implement $description using Test-Driven Development. Write tests first, then implement features. Target 90% code coverage." \
                --strategy testing --max-agents 3 --parallel || true
            ;;
        5)
            npx --yes claude-flow@alpha swarm "Review code quality and security for $description. Check for bugs, security vulnerabilities, code smells, and best practices." \
                --strategy analysis --max-agents 2 || true
            ;;
        6)
            npx --yes claude-flow@alpha swarm "Create comprehensive documentation for $description. Include API docs, usage examples, architecture diagrams, and setup instructions." \
                --strategy research --max-agents 1 || true
            ;;
    esac
    
    show_success "Workflow Full-Stack Feature Development zakończony!"
}

# Workflow 2: GitHub PR Management
workflow_github_pr() {
    show_progress "Inicjalizacja GitHub PR Management workflow..."
    
    local pr_number=$(get_input "Numer Pull Request" "")
    
    if [ -z "$pr_number" ]; then
        show_error "Numer PR jest wymagany!"
        return 1
    fi
    
    echo -e "\n${BLUE}Wybierz typ review:${NC}"
    echo "1) Comprehensive (wszystkie agenty)"
    echo "2) Security Focus"
    echo "3) Performance Focus"
    echo "4) Style & Architecture"
    
    local review_type=$(get_input "Typ review" "1")
    
    local agents="security,performance,style,architecture"
    case $review_type in
        2) agents="security" ;;
        3) agents="performance" ;;
        4) agents="style,architecture" ;;
    esac
    
    show_progress "Pobieranie danych PR #$pr_number..."
    
    # Sprawdź czy gh CLI jest dostępne
    if command -v gh &> /dev/null; then
        PR_DATA=$(gh pr view $pr_number --json files,title,body,labels 2>/dev/null || echo "")
        PR_DIFF=$(gh pr diff $pr_number 2>/dev/null || echo "")
        
        if [ -n "$PR_DATA" ]; then
            show_progress "Uruchamianie multi-agent code review..."
            npx --yes claude-flow@alpha github code-review --pr $pr_number --agents "$agents" || true
        else
            show_error "Nie można pobrać danych PR. Sprawdź czy jesteś zalogowany: gh auth login"
        fi
    else
        show_progress "GitHub CLI nie znaleziony. Uruchamianie review bez kontekstu PR..."
        npx --yes claude-flow@alpha github code-review --pr $pr_number --agents "$agents" || true
    fi
    
    show_success "GitHub PR Review zakończony!"
}

# Workflow 3: Legacy Code Refactoring
workflow_refactoring() {
    show_progress "Inicjalizacja Legacy Code Refactoring workflow..."
    
    local target=$(get_input "Plik/moduł do refactoringu" "")
    
    if [ -z "$target" ]; then
        show_error "Cel refactoringu jest wymagany!"
        return 1
    fi
    
    echo -e "\n${BLUE}Wybierz strategię:${NC}"
    echo "1) Pełny refactoring z testami"
    echo "2) Tylko analiza i plan"
    echo "3) Incremental refactoring"
    
    local strategy=$(get_input "Strategia" "1")
    
    show_progress "Inicjalizacja Hive Mind dla refactoringu: $target"
    npx --yes claude-flow@alpha hive-mind spawn "Refactor $target to modern patterns" --claude || true
    
    case $strategy in
        1)
            show_progress "Krok 1: Analiza i safety net"
            npx --yes claude-flow@alpha swarm "Analyze $target dependencies, coupling, and code structure. Identify refactoring opportunities and risks." \
                --strategy analysis --max-agents 2 || true
            npx --yes claude-flow@alpha swarm "Create comprehensive test suite for $target. Target 80% code coverage. Include unit, integration, and regression tests." \
                --strategy testing --max-agents 2 --parallel || true
            
            show_progress "Krok 2: Refactoring"
            npx --yes claude-flow@alpha swarm "Refactor $target to modern patterns while maintaining functionality. Verify with tests. Maintain 98% test pass rate." \
                --strategy development --max-agents 3 --parallel || true
            ;;
        2)
            npx --yes claude-flow@alpha swarm "Analyze $target dependencies, coupling, and code structure. Identify refactoring opportunities and risks." \
                --strategy analysis --max-agents 2 || true
            npx --yes claude-flow@alpha swarm "Plan refactoring strategy for $target. Create step-by-step plan with risk assessment and rollback strategy." \
                --strategy research --max-agents 2 || true
            ;;
        3)
            show_progress "Incremental refactoring..."
            npx --yes claude-flow@alpha swarm "Refactor $target incrementally. Maintain all existing tests. Apply modern patterns and best practices step by step." \
                --strategy development --max-agents 2 || true
            ;;
    esac
    
    show_success "Legacy Code Refactoring workflow zakończony!"
}

# Workflow 4: Research-Driven Innovation
workflow_research() {
    show_progress "Inicjalizacja Research-Driven Innovation workflow..."
    
    local topic=$(get_input "Temat badań" "")
    
    if [ -z "$topic" ]; then
        show_error "Temat badań jest wymagany!"
        return 1
    fi
    
    echo -e "\n${BLUE}Wybierz zakres:${NC}"
    echo "1) Comprehensive research + innovation"
    echo "2) Tylko research"
    echo "3) Innovation based on existing research"
    
    local scope=$(get_input "Zakres" "1")
    
    case $scope in
        1|"")
            show_progress "Faza 1: Comprehensive Research"
            echo -e "${YELLOW}⏱️  Research może zająć 3-8 minut...${NC}\n"
run_with_timeout 900 npx --yes claude-flow@alpha swarm "Research $topic comprehensively with web search. Find latest information, best practices, examples, trends, and academic sources. Use web_search tool extensively." \
                --strategy research --max-agents 3 --parallel --monitor || true
            
            show_progress "Faza 2: Innovation & Ideation"
            echo -e "${YELLOW}⏱️  Innovation może zająć 2-5 minut...${NC}\n"
run_with_timeout 600 npx --yes claude-flow@alpha swarm "Propose innovative solutions for $topic based on research findings. Think creatively, propose novel approaches, and combine insights with innovation." \
                --strategy research --max-agents 2 --parallel || true
            
            show_progress "Faza 3: Architecture Design"
            echo -e "${YELLOW}⏱️  Architecture design może zająć 2-5 minut...${NC}\n"
run_with_timeout 600 npx --yes claude-flow@alpha swarm "Design system architecture for $topic. Create component structure, technical specifications, and implementation plan." \
                --strategy development --max-agents 2 || true
            ;;
        2)
            echo -e "${YELLOW}⏱️  Research może zająć 3-8 minut...${NC}\n"
run_with_timeout 900 npx --yes claude-flow@alpha swarm "Research $topic comprehensively with web search. Find latest information, best practices, examples, trends, and academic sources." \
                --strategy research --max-agents 3 --parallel --monitor || true
            ;;
        3)
            echo -e "${YELLOW}⏱️  Innovation może zająć 2-5 minut...${NC}\n"
run_with_timeout 600 npx --yes claude-flow@alpha swarm "Propose innovative solutions for $topic. Think creatively, propose novel approaches, and generate innovative concepts." \
                --strategy research --max-agents 2 --parallel || true
            ;;
    esac
    
    show_success "Research-Driven Innovation workflow zakończony!"
}

# Workflow 5: Pair Programming
workflow_pair_programming() {
    show_progress "Inicjalizacja Pair Programming workflow..."
    
    echo -e "\n${BLUE}Wybierz tryb:${NC}"
    echo "1) TDD Mode (Test-Driven Development)"
    echo "2) Driver Mode (Ty piszesz, AI pomaga)"
    echo "3) Navigator Mode (AI pisze, Ty kierujesz)"
    echo "4) Switch Mode (Automatyczne przełączanie)"
    echo "5) Debug Mode"
    echo "6) Review Mode"
    
    local mode=$(get_input "Tryb" "1")
    
    local mode_flag=""
    case $mode in
        1) mode_flag="--mode tdd --test-first --coverage 90" ;;
        2) mode_flag="--mode driver" ;;
        3) mode_flag="--mode navigator" ;;
        4) mode_flag="--mode switch" ;;
        5) mode_flag="--mode debug --verbose" ;;
        6) mode_flag="--mode review --strict" ;;
    esac
    
    local task=$(get_input "Zadanie do wykonania" "")
    
    if [ -n "$task" ]; then
        show_progress "Uruchamianie pair programming: $task"
        npx --yes claude-flow@alpha pair --start $mode_flag --verify --threshold 0.95 || true
    else
        show_progress "Uruchamianie pair programming..."
        npx --yes claude-flow@alpha pair --start $mode_flag --verify || true
    fi
    
    show_success "Pair Programming session rozpoczęta!"
    echo -e "${YELLOW}Użyj komend w sesji: /help, /test, /review, /commit${NC}"
}

# Workflow 6: Multi-Repo Coordination
workflow_multirepo() {
    show_progress "Inicjalizacja Multi-Repo Coordination workflow..."
    
    local repos=$(get_input "Repozytoria (oddzielone przecinkami)" "")
    
    if [ -z "$repos" ]; then
        show_error "Repozytoria są wymagane!"
        return 1
    fi
    
    echo -e "\n${BLUE}Wybierz akcję:${NC}"
    echo "1) Analiza zależności"
    echo "2) Coordinated changes"
    echo "3) Cross-repo PR management"
    echo "4) Synchronized release"
    
    local action=$(get_input "Akcja" "1")
    
    case $action in
        1)
            npx --yes claude-flow@alpha github multi-repo --repos "$repos" --analyze-dependencies || true
            ;;
        2)
            local change=$(get_input "Opis zmian" "")
            npx --yes claude-flow@alpha swarm "$change" --repos "$repos" --strategy parallel || true
            ;;
        3)
            npx --yes claude-flow@alpha github multi-repo --repos "$repos" --create-prs --link-prs || true
            ;;
        4)
            local version=$(get_input "Wersja" "v1.0.0")
            npx --yes claude-flow@alpha github release-management --repos "$repos" --version "$version" --synchronize || true
            ;;
    esac
    
    show_success "Multi-Repo Coordination workflow zakończony!"
}

# Workflow 7: Quick Swarm Task
workflow_quick_swarm() {
    show_progress "Inicjalizacja Quick Swarm Task..."
    
    local task=$(get_input "Opis zadania" "")
    
    if [ -z "$task" ]; then
        show_error "Zadanie jest wymagane!"
        return 1
    fi
    
    echo -e "\n${BLUE}Wybierz typ:${NC}"
    echo "1) Proste swarm (szybkie)"
    echo "2) Swarm z Hive Mind (kompleksowe)"
    echo "3) Swarm z SPARC mode"
    
    local type=$(get_input "Typ" "1")
    
    case $type in
        1)
            show_progress "Uruchamianie swarm: $task"
            npx --yes claude-flow@alpha swarm "$task" --claude || true
            ;;
        2)
            show_progress "Uruchamianie Hive Mind swarm: $task"
            npx --yes claude-flow@alpha hive-mind spawn "$task" --claude || true
            ;;
        3)
            local mode=$(get_input "Swarm strategy (research/development/testing/analysis)" "development")
            show_progress "Uruchamianie swarm z strategy $mode: $task"
            npx --yes claude-flow@alpha swarm "$task" \
                --strategy $mode --max-agents 3 --parallel || true
            ;;
    esac
    
    show_success "Quick Swarm Task zakończony!"
}

# Workflow 8: System Status
workflow_status() {
    show_progress "Sprawdzanie statusu systemu..."
    
    echo -e "\n${BLUE}Status Claude Flow:${NC}"
    npx --yes claude-flow@alpha status || true
    
    echo -e "\n${BLUE}Status Hive Mind:${NC}"
    npx --yes claude-flow@alpha hive-mind status || true
    
    echo -e "\n${BLUE}Pamięć (ostatnie 10 wpisów):${NC}"
    npx --yes claude-flow@alpha memory list --limit 10 || true
    
    echo -e "\n${BLUE}Aktywne sesje:${NC}"
    npx --yes claude-flow@alpha hive-mind sessions || true
    
    show_success "Status sprawdzony!"
}

# Workflow 9: Brainstorm z Online Research (MCP Web Search)
workflow_brainstorm() {
    show_progress "Inicjalizacja Brainstorm z Online Research workflow..."
    
    local topic=$(get_input "Temat do brainstormingu i researchu" "")
    
    if [ -z "$topic" ]; then
        show_error "Temat jest wymagany!"
        return 1
    fi
    
    echo -e "\n${BLUE}Wybierz zakres brainstormingu:${NC}"
    echo "1) Pełny workflow (Research → Brainstorm → Synteza)"
    echo "2) Tylko Online Research (MCP Web Search)"
    echo "3) Tylko Brainstorming (kreatywne pomysły)"
    echo "4) Research + Innovation (badania + innowacyjne rozwiązania)"
    
    local scope=$(get_input "Zakres" "1")
    
    echo -e "\n${BLUE}Wybierz głębokość researchu:${NC}"
    echo "1) Comprehensive (głębokie, wszystkie źródła)"
    echo "2) Quick (szybki przegląd)"
    echo "3) Academic (akademickie źródła)"
    echo "4) Industry (przemysłowe źródła)"
    
    local depth=$(get_input "Głębokość researchu" "1")
    
    local depth_flag=""
    local sources_flag=""
    case $depth in
        1|"")
            depth_flag="--depth comprehensive"
            sources_flag="--sources academic,industry,news"
            ;;
        2)
            depth_flag="--depth quick"
            ;;
        3)
            depth_flag="--depth comprehensive"
            sources_flag="--sources academic"
            ;;
        4)
            depth_flag="--depth comprehensive"
            sources_flag="--sources industry"
            ;;
    esac
    
    # Utwórz katalog tymczasowy dla wyników
    local temp_dir=$(mktemp -d)
    local research_output="$temp_dir/research_output.txt"
    local brainstorm_output="$temp_dir/brainstorm_output.txt"
    local synthesis_output="$temp_dir/synthesis_output.txt"
    
    # Cleanup function
    cleanup() {
        rm -rf "$temp_dir"
    }
    trap cleanup EXIT
    
    show_progress "Zapisywanie tematu w pamięci..."
    npx --yes claude-flow@alpha memory store "brainstorm-topic" "$topic" --namespace brainstorm --reasoningbank || true
    
    case $scope in
        1|"")
            # Pełny workflow: Research → Brainstorm → Synteza
            show_progress "Faza 1: Online Research z wykorzystaniem MCP Web Search..."
            echo -e "${CYAN}Uruchamianie swarm z research strategy (wykorzystuje MCP tools do web search)...${NC}"
            echo -e "${YELLOW}To może zająć kilka minut - swarm wykonuje faktyczny research online...${NC}\n"
            
            # Użyj swarm bez --claude (używa built-in executor i faktycznie wykonuje)
            # Przechwyć output do pliku
            echo -e "${CYAN}Wykonuję research... (output zapisywany)${NC}"
            echo -e "${YELLOW}⏱️  To może zająć 3-8 minut...${NC}\n"
            # Timeout 15 minut dla researchu
run_with_timeout 900 npx --yes claude-flow@alpha swarm "Research $topic comprehensively with web search using MCP tools. Find latest information, best practices, examples, and trends. Use web_search tool to find real sources and information. Provide detailed findings with sources and links." \
                --strategy research \
                --max-agents 3 \
                --parallel \
                --monitor > "$research_output" 2>&1 || true
            
            # Odczytaj wyniki researchu
            show_progress "Odczytywanie wyników researchu..."
            local research_results=""
            if [ -f "$research_output" ] && [ -s "$research_output" ]; then
                research_results=$(cat "$research_output")
                echo -e "${GREEN}✓ Research zakończony (${#research_results} znaków wyników)${NC}"
                
                # Wyświetl podsumowanie (pierwsze 500 znaków) - bezpiecznie
                echo -e "\n${BLUE}📋 Podsumowanie researchu:${NC}"
                echo "$research_results" | head -c 500 2>/dev/null || echo "$research_results" | cut -c1-500 2>/dev/null || echo "${research_results:0:500}"
                if [ ${#research_results} -gt 500 ]; then
                    echo -e "\n${YELLOW}... (więcej w pamięci)${NC}"
                fi
                echo ""
            else
                research_results="Research completed but no detailed output captured. Check memory for results."
                echo -e "${YELLOW}⚠ Brak szczegółowego outputu, sprawdzam pamięć...${NC}"
            fi
            
            # Zapisz pełne wyniki w pamięci
            show_progress "Zapisywanie wyników researchu w pamięci..."
            npx --yes claude-flow@alpha memory store "research-$topic" \
                "$research_results" \
                --namespace research --reasoningbank || true
            
            show_progress "Faza 2: Kreatywny Brainstorming..."
            echo -e "${CYAN}Uruchamianie swarm z kreatywnym brainstormingiem...${NC}"
            echo -e "${YELLOW}Generowanie innowacyjnych pomysłów na podstawie researchu...${NC}\n"
            
            # Przygotuj prompt z wynikami researchu (ograniczony kontekst dla wydajności)
            local brainstorm_prompt="Brainstorm innovative solutions and creative ideas for $topic. "
            if [ -n "$research_results" ] && [ ${#research_results} -gt 100 ]; then
                # Użyj pierwszych 5000 znaków researchu jako kontekstu (zamiast 2000 dla lepszego kontekstu, ale nie więcej)
                local research_context="${research_results:0:5000}"
                # Jeśli to JSON/logi, wyciągnij tylko kluczowe informacje
                if echo "$research_context" | grep -q "type.*system\|Running in"; then
                    # Wyciągnij tylko faktyczne wyniki researchu (pomiń logi techniczne)
                    research_context=$(echo "$research_results" | grep -v "type.*system\|Running in\|Command:" | head -c 5000 2>/dev/null || echo "${research_results:0:5000}")
                fi
                brainstorm_prompt="${brainstorm_prompt}Based on the following research findings (summary): ${research_context}... Now think outside the box, propose multiple approaches, and generate creative concepts. Consider different perspectives and unconventional solutions that build on the research."
            else
                brainstorm_prompt="${brainstorm_prompt}Think outside the box, propose multiple approaches, and generate creative concepts. Consider different perspectives and unconventional solutions."
            fi
            
            echo -e "${CYAN}Wykonuję brainstorming... (output zapisywany)${NC}"
            echo -e "${YELLOW}⏱️  To może zająć 2-5 minut...${NC}\n"
            # Timeout 10 minut dla brainstormingu
run_with_timeout 600 npx --yes claude-flow@alpha swarm "$brainstorm_prompt" \
                --strategy research \
                --max-agents 2 \
                --parallel > "$brainstorm_output" 2>&1 || true
            
            # Odczytaj wyniki brainstormingu
            show_progress "Odczytywanie wyników brainstormingu..."
            local brainstorm_results=""
            if [ -f "$brainstorm_output" ] && [ -s "$brainstorm_output" ]; then
                brainstorm_results=$(cat "$brainstorm_output")
                echo -e "${GREEN}✓ Brainstorming zakończony (${#brainstorm_results} znaków wyników)${NC}"
                
                # Wyświetl podsumowanie - bezpiecznie
                echo -e "\n${BLUE}💡 Podsumowanie pomysłów:${NC}"
                echo "$brainstorm_results" | head -c 500 2>/dev/null || echo "$brainstorm_results" | cut -c1-500 2>/dev/null || echo "${brainstorm_results:0:500}"
                if [ ${#brainstorm_results} -gt 500 ]; then
                    echo -e "\n${YELLOW}... (więcej w pamięci)${NC}"
                fi
                echo ""
            else
                brainstorm_results="Brainstorming completed but no detailed output captured."
            fi
            
            show_progress "Zapisywanie pomysłów w pamięci..."
            npx --yes claude-flow@alpha memory store "brainstorm-ideas-$topic" \
                "$brainstorm_results" \
                --namespace brainstorm --reasoningbank || true
            
            show_progress "Faza 3: Synteza i Analiza..."
            echo -e "${CYAN}Analizowanie wyników researchu i brainstormingu...${NC}"
            echo -e "${YELLOW}Tworzenie kompleksowej syntezy...${NC}\n"
            
            # Przygotuj prompt z pełnymi wynikami researchu i brainstormingu (ograniczone dla wydajności)
            local synthesis_prompt="Analyze and synthesize the following research findings and brainstorm ideas for $topic. "
            if [ -n "$research_results" ] && [ -n "$brainstorm_results" ]; then
                # Ogranicz do 3000 znaków każdego (zamiast 1500 dla lepszego kontekstu)
                local research_summary="${research_results:0:3000}"
                local brainstorm_summary="${brainstorm_results:0:3000}"
                # Jeśli to JSON/logi, wyciągnij tylko kluczowe informacje
                if echo "$research_summary" | grep -q "type.*system\|Running in"; then
                    research_summary=$(echo "$research_results" | grep -v "type.*system\|Running in\|Command:" | head -c 3000 2>/dev/null || echo "${research_results:0:3000}")
                fi
                synthesis_prompt="${synthesis_prompt}Research findings (summary): ${research_summary}... Brainstorm ideas (summary): ${brainstorm_summary}... Now create a comprehensive summary with actionable insights, recommendations, and next steps. Combine research data with creative ideas into a cohesive plan."
            else
                synthesis_prompt="${synthesis_prompt}Create comprehensive summary with actionable insights, recommendations, and next steps. Combine research data with creative ideas."
            fi
            
            echo -e "${CYAN}Wykonuję syntezę... (output zapisywany)${NC}"
            echo -e "${YELLOW}⏱️  To może zająć 2-5 minut...${NC}\n"
            # Timeout 10 minut dla syntezy
run_with_timeout 600 npx --yes claude-flow@alpha swarm "$synthesis_prompt" \
                --strategy analysis \
                --max-agents 2 > "$synthesis_output" 2>&1 || true
            
            # Odczytaj wyniki syntezy
            show_progress "Odczytywanie wyników syntezy..."
            local synthesis_results=""
            if [ -f "$synthesis_output" ] && [ -s "$synthesis_output" ]; then
                synthesis_results=$(cat "$synthesis_output")
                echo -e "${GREEN}✓ Synteza zakończona (${#synthesis_results} znaków wyników)${NC}"
                
                # Wyświetl pełną syntezę
                echo -e "\n${BLUE}📊 Kompleksowa synteza:${NC}"
                echo "$synthesis_results"
                echo ""
            else
                synthesis_results="Synthesis completed. Research and brainstorm results are available in memory."
            fi
            
            show_progress "Faza 4: Tworzenie Knowledge Graph..."
            npx --yes claude-flow@alpha memory store "brainstorm-synthesis-$topic" \
                "$synthesis_results" \
                --namespace knowledge --reasoningbank || true
            ;;
        2)
            # Tylko Online Research
            show_progress "Online Research z wykorzystaniem MCP Web Search..."
            echo -e "${CYAN}Swarm wykorzystuje MCP tools do równoległego web search...${NC}"
            echo -e "${YELLOW}To może zająć kilka minut - wykonuję faktyczny research online...${NC}\n"
            
            echo -e "${CYAN}Wykonuję research... (output zapisywany)${NC}"
            echo -e "${YELLOW}⏱️  To może zająć 3-8 minut...${NC}\n"
run_with_timeout 900 npx --yes claude-flow@alpha swarm "Research $topic with comprehensive web search using MCP tools. Find latest information, trends, best practices, and real examples. Use web_search tool extensively to gather information from multiple sources. Provide detailed findings with sources and links." \
                --strategy research \
                --max-agents 3 \
                --parallel \
                --monitor > "$research_output" 2>&1 || true
            
            # Odczytaj wyniki researchu
            show_progress "Odczytywanie wyników researchu..."
            local research_results=""
            if [ -f "$research_output" ] && [ -s "$research_output" ]; then
                research_results=$(cat "$research_output")
                echo -e "${GREEN}✓ Research zakończony (${#research_results} znaków wyników)${NC}"
                echo -e "\n${BLUE}📋 Podsumowanie researchu:${NC}"
                echo "$research_results" | head -c 1000 2>/dev/null || echo "$research_results" | cut -c1-1000 2>/dev/null || echo "${research_results:0:1000}"
                if [ ${#research_results} -gt 1000 ]; then
                    echo -e "\n${YELLOW}... (więcej w pamięci)${NC}"
                fi
                echo ""
            else
                research_results="Research completed but no detailed output captured."
            fi
            
            show_progress "Zapisywanie wyników w pamięci..."
            npx --yes claude-flow@alpha memory store "research-$topic" \
                "$research_results" \
                --namespace research --reasoningbank || true
            ;;
        3)
            # Tylko Brainstorming
            show_progress "Kreatywny Brainstorming..."
            echo -e "${YELLOW}Generowanie kreatywnych pomysłów...${NC}\n"
            
            echo -e "${CYAN}Wykonuję brainstorming... (output zapisywany)${NC}"
            echo -e "${YELLOW}⏱️  To może zająć 2-5 minut...${NC}\n"
run_with_timeout 600 npx --yes claude-flow@alpha swarm "Brainstorm creative ideas and solutions for $topic. Generate multiple innovative approaches, think creatively, and propose unconventional solutions. Consider different perspectives and angles." \
                --strategy research \
                --max-agents 2 \
                --parallel > "$brainstorm_output" 2>&1 || true
            
            # Odczytaj wyniki brainstormingu
            show_progress "Odczytywanie wyników brainstormingu..."
            local brainstorm_results=""
            if [ -f "$brainstorm_output" ] && [ -s "$brainstorm_output" ]; then
                brainstorm_results=$(cat "$brainstorm_output")
                echo -e "${GREEN}✓ Brainstorming zakończony (${#brainstorm_results} znaków wyników)${NC}"
                echo -e "\n${BLUE}💡 Podsumowanie pomysłów:${NC}"
                echo "$brainstorm_results" | head -c 1000 2>/dev/null || echo "$brainstorm_results" | cut -c1-1000 2>/dev/null || echo "${brainstorm_results:0:1000}"
                if [ ${#brainstorm_results} -gt 1000 ]; then
                    echo -e "\n${YELLOW}... (więcej w pamięci)${NC}"
                fi
                echo ""
            else
                brainstorm_results="Brainstorming completed but no detailed output captured."
            fi
            
            show_progress "Zapisywanie pomysłów w pamięci..."
            npx --yes claude-flow@alpha memory store "brainstorm-ideas-$topic" \
                "$brainstorm_results" \
                --namespace brainstorm --reasoningbank || true
            ;;
        4)
            # Research + Innovation
            show_progress "Faza 1: Online Research..."
            echo -e "${YELLOW}Wykonuję research online...${NC}\n"
            
            echo -e "${CYAN}Wykonuję research... (output zapisywany)${NC}"
            echo -e "${YELLOW}⏱️  To może zająć 3-8 minut...${NC}\n"
run_with_timeout 900 npx --yes claude-flow@alpha swarm "Research $topic using web search. Find latest information, best practices, and real examples. Use web_search tool to gather comprehensive information. Provide detailed findings." \
                --strategy research \
                --max-agents 2 \
                --parallel > "$research_output" 2>&1 || true
            
            # Odczytaj wyniki researchu
            show_progress "Odczytywanie wyników researchu..."
            local research_results=""
            if [ -f "$research_output" ] && [ -s "$research_output" ]; then
                research_results=$(cat "$research_output")
                echo -e "${GREEN}✓ Research zakończony (${#research_results} znaków wyników)${NC}"
            else
                research_results="Research completed."
            fi
            
            show_progress "Faza 2: Innovation based on Research..."
            echo -e "${YELLOW}Generowanie innowacyjnych rozwiązań na podstawie researchu...${NC}\n"
            
            # Użyj wyników researchu jako kontekstu
            local innovation_prompt="Propose innovative solutions for $topic based on the following research findings: "
            if [ -n "$research_results" ] && [ ${#research_results} -gt 100 ]; then
                local research_context="${research_results:0:5000}"
                # Jeśli to JSON/logi, wyciągnij tylko kluczowe informacje
                if echo "$research_context" | grep -q "type.*system\|Running in"; then
                    research_context=$(echo "$research_results" | grep -v "type.*system\|Running in\|Command:" | head -c 5000 2>/dev/null || echo "${research_results:0:5000}")
                fi
                innovation_prompt="${innovation_prompt}${research_context}... Now think creatively, propose novel approaches, and combine research insights with innovation."
            else
                innovation_prompt="Propose innovative solutions for $topic. Think creatively, propose novel approaches, and combine research insights with innovation."
            fi
            
            echo -e "${CYAN}Wykonuję innovation... (output zapisywany)${NC}"
            echo -e "${YELLOW}⏱️  To może zająć 2-5 minut...${NC}\n"
run_with_timeout 600 npx --yes claude-flow@alpha swarm "$innovation_prompt" \
                --strategy research \
                --max-agents 2 > "$brainstorm_output" 2>&1 || true
            
            # Odczytaj wyniki innovation
            show_progress "Odczytywanie wyników innovation..."
            local innovation_results=""
            if [ -f "$brainstorm_output" ] && [ -s "$brainstorm_output" ]; then
                innovation_results=$(cat "$brainstorm_output")
                echo -e "${GREEN}✓ Innovation zakończone (${#innovation_results} znaków wyników)${NC}"
                echo -e "\n${BLUE}💡 Podsumowanie innowacyjnych rozwiązań:${NC}"
                echo "$innovation_results" | head -c 1000 2>/dev/null || echo "$innovation_results" | cut -c1-1000 2>/dev/null || echo "${innovation_results:0:1000}"
                if [ ${#innovation_results} -gt 1000 ]; then
                    echo -e "\n${YELLOW}... (więcej w pamięci)${NC}"
                fi
                echo ""
            else
                innovation_results="Innovation completed."
            fi
            
            show_progress "Zapisywanie w pamięci..."
            npx --yes claude-flow@alpha memory store "innovation-$topic" \
                "$innovation_results" \
                --namespace innovation --reasoningbank || true
            ;;
    esac
    
    show_progress "Pobieranie zapisanych wyników z pamięci..."
    echo -e "\n${BLUE}Wyniki zapisane w pamięci:${NC}"
    npx --yes claude-flow@alpha memory query "$topic" --namespace research --reasoningbank || true
    npx --yes claude-flow@alpha memory query "$topic" --namespace brainstorm --reasoningbank || true
    npx --yes claude-flow@alpha memory query "$topic" --namespace knowledge --reasoningbank || true
    
    show_success "Brainstorm z Online Research zakończony!"
    echo -e "${YELLOW}Wyniki zostały zapisane w pamięci. Użyj 'claude-flow memory query' aby je odczytać.${NC}"
}

# Główna pętla
main() {
    while true; do
        show_menu
        local choice=$(get_input "Twój wybór" "")
        # Usuń białe znaki i sprawdź czy nie jest puste
        choice=$(echo "$choice" | sed 's/^[[:space:]]*//;s/[[:space:]]*$//')
        
        # Jeśli puste, spróbuj ponownie
        if [ -z "$choice" ]; then
            show_error "Wybór nie może być pusty. Spróbuj ponownie."
            continue
        fi
        
        case "$choice" in
            1)
                workflow_fullstack
                ;;
            2)
                workflow_github_pr
                ;;
            3)
                workflow_refactoring
                ;;
            4)
                workflow_research
                ;;
            5)
                workflow_pair_programming
                ;;
            6)
                workflow_multirepo
                ;;
            7)
                workflow_quick_swarm
                ;;
            8)
                workflow_status
                ;;
            9)
                workflow_brainstorm
                ;;
            0|q|exit|Q)
                echo -e "\n${GREEN}Do widzenia! 👋${NC}\n"
                exit 0
                ;;
            *)
                show_error "Nieprawidłowy wybór: '$choice'. Wpisz liczbę od 0-9."
                ;;
        esac
        
        echo -e "\n${CYAN}─────────────────────────────────────────────────────────${NC}"
        local continue=$(get_input "Czy chcesz wykonać kolejne zadanie? (t/n)" "t")
        if [[ ! "$continue" =~ ^[TtYy] ]]; then
            echo -e "\n${GREEN}Do widzenia! 👋${NC}\n"
            exit 0
        fi
    done
}

# Sprawdzenie czy claude-flow jest dostępne
if ! command -v npx &> /dev/null; then
    show_error "Node.js/npx nie jest zainstalowane. Zainstaluj Node.js 18+"
    exit 1
fi

# Uruchomienie głównej pętli
main
