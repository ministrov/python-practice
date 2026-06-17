# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a structured Python learning repository tracking progression from Junior (beginner) to Senior (advanced) backend developer. It's organized as a course with theory, practical exercises, and assessments for each topic.

**Duration estimate:** 18-24 months at 10-15 hours/week
**Current progress:** Junior Level, Block 2.1 mostly complete (fundamentals), Block 2.2 (data structures) ready
**Target stack:** Python 3.8+, FastAPI, PostgreSQL, SQLAlchemy, Docker, Kubernetes

## Directory Structure & Patterns

The repository follows a strict organizational pattern:

```
01_junior/
├── 2.1_fundamentals/        # Completed: types, variables, references, conditionals, loops, strings, IO
│   ├── 01_types_demo.py + 02_types_task.py
│   ├── 03_variables_demo.py + 03b_variables_task.py
│   ├── 03c_references_and_objects_demo.py + 03c_references_and_objects_task.py
│   ├── ... (pattern continues)
│   └── 16_io_and_files_tasks.py    # Latest topic
├── 2.2_data_structures/     # Prepared: lists, tuples, dicts, sets, comprehensions
│   ├── 01_list_demo.py + 02_list_task.py
│   ├── ... (12 files total)
│   └── 12_choosing_structures_task.py
├── 2.3_functions/           # Upcoming: function basics, *args/**kwargs, decorators
│   └── (guide files available)
├── assessments/
│   ├── ASSESSMENT_Block_2_1.md
│   ├── REASSESSMENT_Block_2_1.md
│   └── ASSESSMENT_Block_2_2.md
└── ...
02_middle/          # Planned: OOP, async/await, databases, Flask/FastAPI, testing
03_senior/          # Planned: architecture, distributed systems, DevOps
README.md           # Course overview and structure
PROGRESS.md         # Detailed learning progress tracker
PYTHON_BACKEND_ROADMAP.md  # Full 18-24 month learning plan with resources
```

## Key Patterns

### File Naming Convention

**`NN_topic_demo.py`** — Theory file with:

- Concept explanations
- Code examples demonstrating the concept
- Output of examples
- Often includes edge cases or tricky situations

**`NN_topic_task.py`** — Practice file with:

- `# YOUR CODE HERE:` placeholders where user fills in solutions
- Usually 6-12 exercises per file
- Exercises progress from basic to complex within the topic
- No expected imports; user writes pure code in functions

Files are **numbered sequentially** (01, 02, 03...) to maintain learning order.

### Assessment Pattern

After each topic block, there are two assessment types:

1. **Micro-questions** (usually 4-8 questions in `*_task.py`):
   - Quick conceptual checks
   - ≥80% = ready to move on

2. **Block assessments** (`ASSESSMENT_Block_X.md`):
   - Combine knowledge from multiple topics
   - 4 problems of increasing difficulty
   - Run them and verify output matches expected results

## How to Work with New Content

When adding or modifying learning materials:

1. **Theory files (`*_demo.py`):**
   - Run them first to show what the output should be
   - Comments explain the WHY, not just the WHAT
   - Progressively introduce complexity (basics → edge cases)

2. **Task files (`*_task.py`):**
   - Keep exercises independent where possible
   - Order them by difficulty (easier first)
   - Solution goes inside the provided `# YOUR CODE HERE:` block
   - Verify all 8-12 exercises have clear expected outputs

3. **Assessments:**
   - File must be runnable with `python assessments/ASSESSMENT_*.md` converted to `.py`
   - Include a clear final score calculation
   - Minimum passing score is explicitly stated (usually ≥80%)

## Code Style & Standards

- **PEP 8 Compliance:** All code must follow [PEP8_STYLE_GUIDE.md](PEP8_STYLE_GUIDE.md) for consistent, readable Python
- Key rules: 4-space indents, `snake_case` for variables, `PascalCase` for classes, max 79 chars/line
- Always add docstrings to functions and classes
- Use `isinstance()` for type checks, `is None` for None comparisons

## Common Commands

### Running a learning file

```bash
# Run theory (read + study output)
python 01_junior/2.1_fundamentals/03_variables_demo.py

# Run practice (solve, then check output)
python 01_junior/2.1_fundamentals/03b_variables_task.py

# Run assessment
python 01_junior/assessments/ASSESSMENT_Block_2_1.md  # (or convert to .py first)
```

### Progress and planning

- **Track current progress:** See `PROGRESS.md` (updated after each session)
- **View full learning roadmap:** See `PYTHON_BACKEND_ROADMAP.md`
- **Check assessments:** Look in `assessments/` folder

### Git workflow (homework branches)

This repo uses feature branches for homework:

```bash
# View recent commits (see homework history)
git log --oneline

# Checkout a homework branch to review
git checkout feature/homework-2_operations

# Switch back to main
git checkout master
```

## Important Conventions

### Code style

- **PEP 8 compliance** (snake_case for variables/functions, CAPS_LOCK for constants)
- No complex abstractions; straightforward, readable code
- Comments only explain the WHY for non-obvious decisions
- Functions have docstrings (one line or proper multi-line)

### Learning progression

The **critical rule for structure:**

- All files in a block must be numbered sequentially (`01_`, `02_`, ...)
- Demo files must exist before task files (user reads theory first)
- Each topic must have both demo and task (except assessments)
- This discipline enables progress tracking and scaling to future blocks

### Assessment criteria

- **Micro-questions:** ≥80% = pass, ready to proceed to next topic
- **Block assessments:** ≥80% = pass the full block, ready for next level
- If < 80%: review the specific failed topics and reattempt

## Critical File Updates

When session work completes:

1. **PROGRESS.md** — Update with:
   - Date and block/topic completed
   - Checkmarks for completed sections
   - Any revised understanding
   - Next recommended topic

2. **Recent commits** — Use clear commit messages:
   ```
   feat: implement expense tracker with average calculation
   homework: complete <block>_<topic> exercises
   ```

## Key Context for Future Sessions

- User is learning Python 3.8+ systematically following a structured curriculum
- The goal is backend developer proficiency (Python + SQL + web frameworks)
- Each session typically covers 1 topic (demo + practice + micro-assessment)
- Progress is deliberately paced: 4-6 months for Junior level, not rushed
- Emphasis on understanding fundamentals deeply before moving up
- Git history shows homework branches for major milestones

## Questions This CLAUDE.md Answers

- **Where do I add new content?** → Follow the numbered pattern in the appropriate block folder
- **How do I run code?** → `python path/to/file.py` (both demo and task)
- **What does a complete topic look like?** → `*_demo.py` + `*_task.py` pair + micro-questions
- **When should I create an assessment?** → After all 6-7 topics in a block are complete
- **How do I track progress?** → Update `PROGRESS.md` after each session
- **What's the learning order?** → Follow numbered files sequentially; see roadmap for block order
