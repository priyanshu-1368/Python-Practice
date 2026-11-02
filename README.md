# Python Practice

A comprehensive collection of Python practice programs, structured lab exercises, data structure implementations, and algorithmic problems developed by [priyanshu-1368](https://github.com/priyanshu-1368) in the [Python-Practice](https://github.com/priyanshu-1368/Python-Practice) repository.

---

## Overview

This repository serves as a progressive learning track for Python programming, spanning basic console I/O and conditional control flow to multi-dimensional data structures, custom functions, array sorting, and algorithmic pattern printing. 

The curriculum aligns with practical coursework completed through **red & white multimedia education**, focusing on hands-on fundamentals, data type manipulation, and computational logic.

---

## Repository Structure

```text
Python-Practice/
├── Basics/
│   ├── 2integer_input.py
│   ├── Voter eligible.py
│   ├── age data.py
│   ├── compare_numbers.py
│   ├── divisibility_check.py
│   ├── even_and_divisable_by_3.py
│   ├── even_numbers.py
│   ├── first.py
│   ├── input_until_zero.py
│   ├── isProgram.py
│   ├── larger_or_equal2.py
│   ├── multiples_of_five.py
│   ├── odd_numbers.py
│   ├── positive_or_negative.py
│   ├── reverse_countdown.py
│   ├── square_numbers.py
│   └── temperature input.py
├── Datatypes in Detail/
│   ├── Lab Work - 5.1/
│   │   ├── F-String Variables.py
│   │   ├── Find, Replace & Count.py
│   │   ├── Input & Formatting.py
│   │   ├── Palindrome Check.py
│   │   ├── Split & Join.py
│   │   ├── String Cases.py
│   │   └── String Checking & Cleanup.py
│   ├── Lab Work - 5.2/
│   │   ├── List Comprehensions.py
│   │   ├── List Operations.py
│   │   ├── List vs Tuple.py
│   │   └── Tuple Basics and Mutability.py
│   └── Lab Work - 5.3/
│       ├── Constructing Dictionaries.py
│       ├── Deleting with.py
│       ├── Dictionary Manipulation.py
│       ├── Mathematical Set Operations.py
│       ├── Set Operations.py
│       └── Type Conversion (Casting).py
├── Extra Tasks/
├── Function, Array & Sorting/
└── Patterns/
```

---

## Detailed Directory Breakdown

### 1. Basics

The `Basics/` directory contains 17 introductory scripts focusing on core Python syntax, conditional branching, comparison logic, and fundamental iterative constructs:

| Script Name | Concepts Covered | Summary |
| :--- | :--- | :--- |
| `2integer_input.py` | `input()`, `int()`, `if-else` | Takes two integers and evaluates numerical equality. |
| `Voter eligible.py` | Relational operators, `if-else` | Evaluates whether a user is at least 18 years old to determine voting eligibility. |
| `age data.py` | Multi-way branching (`elif`) | Categorizes ages into invalid, child (1–12), teenager (13–19), adult (20–59), and senior citizen (60+). |
| `compare_numbers.py` | Relational & logical operators | Performs extensive multi-variable comparison (equality and inequality) across 4 numbers (`a`, `b`, `c`, `d`). |
| `divisibility_check.py` | `for` loop, modulo (`%`), nested conditions | Evaluates divisibility by 2, 3, or both across numbers 1 through 50. |
| `even_and_divisable_by_3.py` | Modulo operator, compound logic | Checks whether an input number satisfies divisibility by 3 and even number conditions. |
| `even_numbers.py` | `while` loop, incrementation | Generates and prints even numbers from 2 up to 50. |
| `first.py` | String variables, formatted output | Displays foundational institution mission, vision, and core values. |
| `input_until_zero.py` | Sentinel loop (`while True`), `break` | Continuously prompts for user input until the sentinel value `0` is entered. |
| `isProgram.py` | String methods (`lower()`, `index()`) | Demonstrates substring search and case manipulation. |
| `larger_or_equal2.py` | Sign determination | Assigns binary indicator values based on non-negative thresholding (`>= 0`). |
| `multiples_of_five.py` | Step iteration (`range(start, stop, step)`) | Iterates through multiples of 5 from 5 up to 50. |
| `odd_numbers.py` | Modulo filtering | Filters and displays odd integers in the interval [1, 20]. |
| `positive_or_negative.py` | Floating-point conversion, branching | Classifies floating-point inputs as positive or negative. |
| `reverse_countdown.py` | Negative step ranges | Produces a reverse numerical countdown from 10 to 1. |
| `square_numbers.py` | Exponentiation / arithmetic multiplication | Calculates and prints square numbers from 1 to 10. |
| `temperature input.py` | Celsius temperature thresholds | Maps Celsius temperatures into distinct qualitative weather descriptors. |

---

### 2. Datatypes in Detail

This module explores Python built-in data types through progressive laboratory assignments:

#### Lab Work - 5.1: Strings & String Manipulation
* **`F-String Variables.py`**: Formatted string literals (`f"..."`) incorporating variable expressions and price formatting.
* **`Find, Replace & Count.py`**: Practical application of substring search with `.find()`, replacement with `.replace()`, and frequency analysis via `.count()`.
* **`Input & Formatting.py`**: Dynamic user input capture and formatted personalized greeting output.
* **`Palindrome Check.py`**: String reversal via step slicing (`[::-1]`) and boolean equality validation.
* **`Split & Join.py`**: Delimiter-based splitting (`.split(",")`), argument unpacking (`*words, sep=" "`), and line-by-line parsing (`.splitlines()`).
* **`String Cases.py`**: Text transformation utilizing `.upper()`, `.lower()`, and `.title()`.
* **`String Checking & Cleanup.py`**: Boundary verification (`.startswith()`, `.endswith()`), character cleaning using list comprehension and `.isalpha()`, and string slicing.

#### Lab Work - 5.2: Lists & Tuples
* **`List Comprehensions.py`**: Concise syntax for generating numerical squares, filtering even numbers, and lowercasing string sequences.
* **`List Operations.py`**: Indexing, negative indexing, `.append()`, item deletion with `.remove()`, in-place ordering with `.sort()`, and reversal via `.reverse()`.
* **`List vs Tuple.py`**: Direct contrast of mutable sequence reassignment versus immutable collections.
* **`Tuple Basics and Mutability.py`**: Index access within tuples alongside explicit conceptual documentation regarding object mutability.

#### Lab Work - 5.3: Dictionaries & Sets
* **`Constructing Dictionaries.py`**: Pairing parallel key and value lists dynamically using `zip()` inside `dict()`.
* **`Deleting with.py`**: Explicit item removal from collections using the `del` statement.
* **`Dictionary Manipulation.py`**: Key and value extraction (`.keys()`, `.values()`), adding new pairs, updating existing records, and key removal.
* **`Mathematical Set Operations.py`**: Set algebra operations including union (`.union()`), intersection (`.intersection()`), and difference (`.difference()`).
* **`Set Operations.py`**: Element addition (`.add()`), removal (`.remove()`), and constant-time membership testing (`in`).
* **`Type Conversion (Casting).py`**: Type casting between strings, integers, lists, tuples, and pairing lists to dictionaries.

---

### 3. Extra Tasks

A curated suite of supplementary practice exercises designed to consolidate procedural problem-solving skills, handle edge cases, and apply logic across varied scenarios.

---

### 4. Function, Array & Sorting

Programs dedicated to modular programming, data sequence processing, and classic algorithmic techniques:
* **Functions**: Modular code encapsulation, parameter passing, return values, and reusable routines.
* **Arrays & Sequences**: Homogeneous and heterogeneous list processing.
* **Sorting Algorithms**: Sorting mechanisms and in-place sequence ordering.

---

### 5. Patterns

Iterative console output programs using nested loops to render geometric and numerical shapes:
* Nested `for` and `while` loop logic.
* Right-angled triangles, inverted pyramids, and symmetric patterns.
* Character, symbol (`*`), and incremental number matrices.

---

## Original Notes and Explanations

The following conceptual explanations and institutional declarations are preserved verbatim from the repository's original source code comments and program definitions:

### Explanation of Mutability

> If we try to set numbers[1] = 25
> Python will display an error saying that a tuple object does not allow item assignment.
> Tuples are not changeable.
> On the hand lists are mutable meaning they can be changed after they are created.
> This means that once a tuple is created
> its elements can't be changed, added or removed.

### Institutional Mission, Vision & Core Values

From `first.py`:

> red & white multimedia education

* **Mission :**
  > To become a globally leading institute in preparing every student for the industry.

* **Vision :**
  > We empower the student to achieve a global career, by providing skills according to their potential through modern education.

* **Core Values (ISIU):**
  * **Integrity:**
    > Adherence to strong ethical principles, honesty, and fairness in all actions and decisions, creating trust among students, staff, and partners.
  * **Student-Centered Focus:**
    > Putting students first. Every decision and action is taken to benefit the students, helping them learn and succeed.
  * **Innovation:**
    > Coming up with new ideas and better ways of doing things. It's about thinking creatively and making education more effective.

---

## Getting Started

### Prerequisites

* Python 3.8 or higher installed on your system.

### Running Any Program

1. Clone the repository:
   ```bash
   git clone https://github.com/priyanshu-1368/Python-Practice.git
   cd Python-Practice
   ```

2. Run a script from the command line:
   ```bash
   python "Basics/even_and_divisable_by_3.py"
   ```

3. To run scripts with spaces in folder or file names, wrap the path in quotes:
   ```bash
   python "Datatypes in Detail/Lab Work - 5.1/Palindrome Check.py"
   ```
