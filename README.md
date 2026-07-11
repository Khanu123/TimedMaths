# Timed Maths Challenge

A Python terminal game that generates random arithmetic questions, times the player, and reports accuracy at the end.

## Overview

Timed Maths Challenge is a small command-line project focused on random problem generation, loops, input handling, and simple performance measurement. It is useful as a clean example of Python fundamentals.

## Skills Demonstrated

- Randomized problem generation
- Working with time measurements
- Input validation
- Loops and conditional logic
- Basic terminal UX

## How to Run

```bash
python main.py
```

If the script has a different filename, run that Python file directly.

## What I Would Improve Next

- Replace `eval()` with a safer operator-based calculation function.
- Add difficulty levels.
- Save best times locally.
- Add tests for generated problems and answer checking.

## Portfolio Note

This is an early learning project. The next iteration would focus on safer expression handling and cleaner separation between game logic and user interface.

## Employer Review

| Area | Evidence |
| --- | --- |
| Role relevance | Early Python fundamentals |
| Main programming lesson | Random generation, timing, loops, validation, and simple performance tracking |
| Portfolio value | Shows progression from small terminal programs to tested security automation |
| Best framing | Archive/early-learning project, not a flagship cyber project |

## Refactor Plan

- Replace `eval()` with explicit operator functions.
- Move problem generation into a testable function.
- Add difficulty levels for number ranges and operators.
- Save best scores locally in a simple JSON file.
- Add tests for generated problems and answer checking.

## Interview Talking Points

- Why `eval()` should be avoided with user-controlled input.
- How small projects can be improved with safer design.
- How timing and scoring logic relate to building reliable CLI tools.
