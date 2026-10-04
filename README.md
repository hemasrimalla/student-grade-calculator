# Student Grade Calculator

A robust, console-based Python application that calculates and reports student academic performance. It collects subject-wise marks, rigorously validates user inputs, computes percentage and grade metrics, enforces passing thresholds, and prints neat, formatted report cards.

---

## Table of Contents
1. [Features](#features)
2. [Project Structure](#project-structure)
3. [Grade Criteria Table](#grade-criteria-table)
4. [How to Run the Application](#how-to-run-the-application)
5. [Sample Execution & Results](#sample-execution--results)
   - [Student 1: Distinction (Grade A+, Pass)](#student-1-distinction-alice-johnson)
   - [Student 2: Average (Grade C, Pass)](#student-2-average-bob-smith)
   - [Student 3: Failing - Subject Failure (Grade C, Fail)](#student-3-failing---subject-failure-charlie-brown)
   - [Student 4: Failing - Low Aggregate (Grade F, Fail)](#student-4-failing---low-aggregate-david-lee)
6. [Core Conceptual Questions & Answers](#core-conceptual-questions--answers)
   - [a) How would you validate user input?](#a-how-would-you-validate-user-input)
   - [b) How does Python evaluate multiple conditions (if/elif/else, and/or)?](#b-how-does-python-evaluate-multiple-conditions-ifelifelse-andor)
   - [c) What happens if a user enters a value outside the expected range?](#c-what-happens-if-a-user-enters-a-value-outside-the-expected-range)
7. [Code Quality & Architecture](#code-quality--architecture)

---

## Features

- **Robust Input Validation**:
  - Ensures student and subject names are non-empty and stripped of leading/trailing whitespace.
  - Ensures number of subjects is a positive integer greater than zero.
  - Ensures marks are numeric values strictly within the range of `0.0` to `100.0`.
  - Catches `ValueError` to prevent crashes when non-numeric data is supplied.
  - Automatically re-prompts until valid input is received.
- **Accurate Calculations**:
  - Calculates total marks and percentage (`(total_marks / (num_subjects * 100)) * 100`).
  - Follows the DRY (Don't Repeat Yourself) principle by computing each metric once and reusing it.
- **Configurable Grade Thresholds**:
  - Grades are defined in a centralized constant tuple (`GRADE_THRESHOLDS`), making adjustments easy and maintainable.
- **Pass/Fail Evaluation**:
  - Checks every subject against the minimum passing threshold (`PASSING_SUBJECT_MARK = 40.0`).
  - Flags a student as **Fail** if any subject score drops below 40, regardless of the overall percentage.
- **Formatted Tabular Report**:
  - Prints an aligned ASCII report card displaying subject marks, totals, 2-decimal percentage, assigned grade, and Pass/Fail status.
- **Batch Student Processing**:
  - Loop allows analyzing multiple students in one session until the user chooses to exit.
- **Zero External Dependencies**:
  - Built strictly using the Python Standard Library.

---

## Project Structure

```text
student_grade_calculator/
├── grade_calculator.py   # Main Python application
└── README.md             # Project documentation, sample runs, and technical Q&A
```

---

## Grade Criteria Table

Grades are assigned based on the overall percentage calculated across all enrolled subjects. In addition, an overall **Pass** status requires obtaining at least **40 marks** in every individual subject.

| Percentage Range | Grade | Classification | Pass / Fail Condition |
| :--- | :---: | :--- | :--- |
| **90.0% – 100.0%** | **A+** | Outstanding / Distinction | Pass (all subjects $\ge 40$) |
| **80.0% – 89.99%** | **A**  | Excellent | Pass (all subjects $\ge 40$) |
| **70.0% – 79.99%** | **B**  | Very Good | Pass (all subjects $\ge 40$) |
| **60.0% – 69.99%** | **C**  | Average / Good | Pass (all subjects $\ge 40$) |
| **50.0% – 59.99%** | **D**  | Satisfactory | Pass (all subjects $\ge 40$) |
| **40.0% – 49.99%** | **E**  | Marginal Pass | Pass (all subjects $\ge 40$) |
| **Below 40.0%**    | **F**  | Fail | Fail |

> **Important Passing Rule:** If a student scores less than 40 in *any* subject, their overall status is marked as **Fail**, even if their aggregate percentage would otherwise qualify for a passing letter grade.

---

## How to Run the Application

### Prerequisites
- Python 3.8 or later installed on your system.

### Running from Terminal / Command Prompt / PowerShell

1. Navigate to the project directory:
   ```bash
   cd C:\Users\HEMA\.gemini\antigravity\scratch\student_grade_calculator
   ```

2. Run the script:
   ```bash
   python grade_calculator.py
   ```

3. Follow the on-screen prompts to enter student details. To exit when prompted, enter `n`.

---

## Sample Execution & Results

Below is an authentic sample run containing edge-case input validation (handling empty strings, negative numbers, out-of-bounds scores, non-numeric values) followed by reports for distinct student performance profiles:

### Input Validation in Action
```text
============================================================
          WELCOME TO STUDENT GRADE CALCULATOR
============================================================

--- Enter Student Details ---
Enter student's name: 
Error: Student name cannot be empty. Please enter a valid value.
Enter student's name: Alice Johnson
Enter the number of subjects: 0
Error: Number of subjects must be a positive integer greater than 0.
Enter the number of subjects: -2
Error: Number of subjects must be a positive integer greater than 0.
Enter the number of subjects: three
Error: Invalid input. Please enter a whole numeric integer (e.g., 3, 5).
Enter the number of subjects: 3

Entering details for 3 subject(s):
  Enter name for Subject #1: Mathematics
  Enter marks for 'Mathematics' (out of 100): -5
Error: Marks must be between 0 and 100 (inclusive). Please try again.
  Enter marks for 'Mathematics' (out of 100): 105
Error: Marks must be between 0 and 100 (inclusive). Please try again.
  Enter marks for 'Mathematics' (out of 100): xyz
Error: Invalid input. Marks must be a valid number (e.g., 85 or 92.5).
  Enter marks for 'Mathematics' (out of 100): 95
```

---

### Student 1: Distinction (Alice Johnson)
- **Profile**: Scores 90+ in all subjects.
```text
============================================================
                  STUDENT RESULT REPORT
============================================================
 Student Name : Alice Johnson
------------------------------------------------------------
 #    Subject Name                            Marks / 100
------------------------------------------------------------
 1    Mathematics                                   95.00
 2    Physics                                       92.00
 3    Chemistry                                     98.00
------------------------------------------------------------
 Total Marks Obtained : 285.00 / 300.00
 Percentage           : 95.00%
 Grade Assigned       : A+
 Overall Status       : Pass
============================================================
```

---

### Student 2: Average (Bob Smith)
- **Profile**: Scores between 60% and 70% with all subjects passed.
```text
============================================================
                  STUDENT RESULT REPORT
============================================================
 Student Name : Bob Smith
------------------------------------------------------------
 #    Subject Name                            Marks / 100
------------------------------------------------------------
 1    History                                       68.00
 2    Political Science                             62.00
 3    Economics                                     65.00
------------------------------------------------------------
 Total Marks Obtained : 195.00 / 300.00
 Percentage           : 65.00%
 Grade Assigned       : C
 Overall Status       : Pass
============================================================
```

---

### Student 3: Failing - Subject Failure (Charlie Brown)
- **Profile**: High overall percentage (63.33%, Grade C), but scored 35 (< 40) in Mathematics.
- **Result**: Overall Status is correctly flagged as **Fail**.
```text
============================================================
                  STUDENT RESULT REPORT
============================================================
 Student Name : Charlie Brown
------------------------------------------------------------
 #    Subject Name                            Marks / 100
------------------------------------------------------------
 1    Mathematics                                   35.00
 2    English                                       80.00
 3    Science                                       75.00
------------------------------------------------------------
 Total Marks Obtained : 190.00 / 300.00
 Percentage           : 63.33%
 Grade Assigned       : C
 Overall Status       : Fail
============================================================
```

---

### Student 4: Failing - Low Aggregate (David Lee)
- **Profile**: Low scores across all subjects resulting in an aggregate below 40%.
```text
============================================================
                  STUDENT RESULT REPORT
============================================================
 Student Name : David Lee
------------------------------------------------------------
 #    Subject Name                            Marks / 100
------------------------------------------------------------
 1    Mathematics                                   32.00
 2    Physics                                       28.00
 3    Chemistry                                     35.00
------------------------------------------------------------
 Total Marks Obtained : 95.00 / 300.00
 Percentage           : 31.67%
 Grade Assigned       : F
 Overall Status       : Fail
============================================================
```

---

## Core Conceptual Questions & Answers

### a) How would you validate user input?

To ensure a program is robust, user-friendly, and fault-tolerant, input validation should follow a multi-stage approach:

1. **Defensive Parsing with Exception Handling (`try...except`)**:
   Never assume the user will enter valid data types. Parsing functions such as `int()` or `float()` should be wrapped inside a `try...except ValueError` block. This prevents unexpected application crashes when users enter letters, special characters, or empty strings where numbers are expected.

2. **String Sanitization & Emptiness Verification**:
   Strip extraneous whitespace using `.strip()` on string inputs. Check whether the resulting string is non-empty (`if not value:`) so users cannot submit blank names or whitespace-only inputs.

3. **Domain / Boundary Range Validation**:
   Check that converted values conform to real-world domain rules using comparison expressions (e.g., `0.0 <= marks <= 100.0` for examination marks, or `subjects > 0` for subject counts).

4. **Continuous Feedback Loop (`while True`)**:
   Encapsulate prompt logic inside an infinite loop that terminates (`return` or `break`) only when all validation checks pass. If validation fails, provide an informative, polite error message detailing what was expected and re-prompt immediately without discarding previous progress.

5. **Graceful Termination Handling**:
   Catch `KeyboardInterrupt` and `EOFError` so that if a user presses `Ctrl+C` or closes the input stream, the program exits gracefully rather than dumping an unhandled stack trace.

---

### b) How does Python evaluate multiple conditions (if/elif/else, and/or)?

Python evaluates conditional logic using sequential branching and Boolean short-circuit evaluation:

1. **Sequential Branching (`if / elif / else`)**:
   - Python tests conditions in strict order from top to bottom.
   - As soon as an expression evaluates to `True`, Python executes that block and **immediately skips all subsequent `elif` and `else` blocks**.
   - If none of the conditions evaluate to `True`, the optional `else` block executes.
   - For threshold-based evaluations (like grades), ordering thresholds from highest to lowest (e.g., `>= 90`, `>= 80`, etc.) ensures mutually exclusive, predictable categorization.

2. **Logical Operators (`not`, `and`, `or`) and Precedence**:
   - `not` has the highest precedence (inverts truth value).
   - `and` has the second highest precedence (evaluates to true only if all operands are true).
   - `or` has the lowest precedence (evaluates to true if at least one operand is true).
   - Explicit parentheses should be used to make complex evaluation order clear (e.g., `(a or b) and c`).

3. **Short-Circuit Evaluation**:
   Python evaluates logical expressions lazily from left to right:
   - **`and` Short-Circuit**: If the left operand is falsy, Python stops immediately and returns that falsy value without evaluating the right operand. For example, in `count > 0 and (total / count) > 50`, if `count` is 0, the division is never executed, preventing a `ZeroDivisionError`.
   - **`or` Short-Circuit**: If the left operand is truthy, Python stops immediately and returns that truthy value without evaluating the right operand. For example, in `is_admin or has_permission()`, if `is_admin` is `True`, `has_permission()` is never called.

---

### c) What happens if a user enters a value outside the expected range?

When a user enters a value outside the expected range (for instance, `-15` or `125` for marks):

1. **Without Input Validation**:
   - If the code converts the input to `float` and proceeds without checking bounds, the calculation will process erroneous numbers.
   - A student could end up with an impossible percentage (such as `125%` or negative values) or an incorrect grade.
   - In other scenarios (like entering `0` or negative numbers for subject counts), division by zero (`ZeroDivisionError`) or invalid loop counters could crash the program.

2. **With the Implemented Validation in this Project**:
   - The input is parsed into a numeric type (`float` or `int`).
   - The conditional check evaluates to `False` (e.g., `0.0 <= marks <= 100.0` is `False` for `105`).
   - The program intercepts this before any calculation takes place.
   - A descriptive error message is displayed:
     ```text
     Error: Marks must be between 0 and 100 (inclusive). Please try again.
     ```
   - The input loop does not advance; instead, it re-prompts the user for the same subject until a valid mark in the range `[0, 100]` is supplied.
   - As a result, the application state remains valid, calculations remain correct, and the program never crashes.

---

## Code Quality & Architecture

- **Modular Functions**:
  - `get_non_empty_string(prompt, field_name)`: Enforces non-empty string entry.
  - `get_valid_positive_int(prompt, field_name)`: Validates positive non-zero integers.
  - `get_valid_marks(prompt)`: Validates marks between 0 and 100 with exception handling.
  - `calculate_percentage(total_marks, num_subjects)`: Computes percentage accurately.
  - `assign_grade(percentage)`: Maps percentage to letter grade using `GRADE_THRESHOLDS`.
  - `check_pass_fail(subjects_marks)`: Evaluates if any subject mark is below 40.
  - `display_result(student_name, subjects_marks, total_marks, percentage, grade, status)`: Renders the formatted result report.
  - `process_student()`: Orchestrates single student assessment.
  - `main()`: Controls the multi-student session loop.
- **Single Source of Truth**:
  - Grade criteria and minimum passing mark are defined as constants at the top of the file.
- **No Redundant Computations**:
  - `total_marks` is computed once using `sum()`.
  - `percentage` is computed once using `calculate_percentage()`.
  - Computed values are passed directly to `display_result()`.
- **Standards & Best Practices**:
  - Fully typed with Python type hints (`typing.Dict`, `typing.Tuple`).
  - Comprehensive docstrings for every function following PEP 257.
  - Protected entry point via `if __name__ == "__main__":`.
