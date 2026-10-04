"""
Student Grade Calculator
------------------------
A console-based Python application that calculates and reports student academic
performance. It supports subject-wise marks entry, validation, percentage
calculation, grade assignment based on defined thresholds, and pass/fail evaluation.
"""

from typing import Dict, Tuple

# ==============================================================================
# GRADE CONFIGURATION & THRESHOLDS
# ==============================================================================
# Grade thresholds defined in descending order: (minimum_percentage, grade_label)
# Centralized in one place for ease of maintenance and extensibility.
GRADE_THRESHOLDS: Tuple[Tuple[float, str], ...] = (
    (90.0, "A+"),
    (80.0, "A"),
    (70.0, "B"),
    (60.0, "C"),
    (50.0, "D"),
    (40.0, "E"),
    (0.0, "F"),
)

# Minimum marks required in every subject to achieve a "Pass" status
PASSING_SUBJECT_MARK: float = 40.0


# ==============================================================================
# INPUT VALIDATION FUNCTIONS
# ==============================================================================
def get_non_empty_string(prompt: str, field_name: str = "Input") -> str:
    """
    Prompt the user until a non-empty string (not just whitespace) is entered.

    Args:
        prompt: Message displayed to the user.
        field_name: Descriptive name of the input field for error messages.

    Returns:
        The sanitized non-empty string.
    """
    while True:
        try:
            value = input(prompt).strip()
            if value:
                return value
            print(f"Error: {field_name} cannot be empty. Please enter a valid value.")
        except (KeyboardInterrupt, EOFError):
            print("\nOperation cancelled by user.")
            raise


def get_valid_positive_int(prompt: str, field_name: str = "Number of subjects") -> int:
    """
    Prompt the user until a positive integer (> 0) is entered.

    Args:
        prompt: Message displayed to the user.
        field_name: Descriptive name of the input field for error messages.

    Returns:
        A positive integer.
    """
    while True:
        try:
            user_input = input(prompt).strip()
            value = int(user_input)
            if value > 0:
                return value
            print(f"Error: {field_name} must be a positive integer greater than 0.")
        except ValueError:
            print("Error: Invalid input. Please enter a whole numeric integer (e.g., 3, 5).")
        except (KeyboardInterrupt, EOFError):
            print("\nOperation cancelled by user.")
            raise


def get_valid_marks(prompt: str) -> float:
    """
    Prompt the user until a valid mark between 0 and 100 (inclusive) is entered.

    Validates numeric format (integer or decimal) and range. Does not crash on
    invalid input.

    Args:
        prompt: Message displayed to the user.

    Returns:
        Marks as a float between 0.0 and 100.0.
    """
    while True:
        try:
            user_input = input(prompt).strip()
            marks = float(user_input)
            if 0.0 <= marks <= 100.0:
                return marks
            print("Error: Marks must be between 0 and 100 (inclusive). Please try again.")
        except ValueError:
            print("Error: Invalid input. Marks must be a valid number (e.g., 85 or 92.5).")
        except (KeyboardInterrupt, EOFError):
            print("\nOperation cancelled by user.")
            raise


def get_yes_no_choice(prompt: str) -> bool:
    """
    Prompt the user for a yes/no response.

    Args:
        prompt: Message displayed to the user.

    Returns:
        True if the user responded affirmatively ('y' or 'yes'), False if ('n' or 'no').
    """
    while True:
        try:
            choice = input(prompt).strip().lower()
            if choice in ("y", "yes"):
                return True
            if choice in ("n", "no"):
                return False
            print("Error: Please enter 'y' for yes or 'n' for no.")
        except (KeyboardInterrupt, EOFError):
            print("\nOperation cancelled by user.")
            raise


# ==============================================================================
# COMPUTATION & LOGIC FUNCTIONS
# ==============================================================================
def calculate_percentage(total_marks: float, num_subjects: int) -> float:
    """
    Calculate the percentage score based on total marks and number of subjects.

    Formula: (total_marks / (num_subjects * 100)) * 100

    Args:
        total_marks: Sum of marks obtained across all subjects.
        num_subjects: Total number of subjects evaluated.

    Returns:
        Calculated percentage as a float.
    """
    if num_subjects <= 0:
        return 0.0
    max_possible_marks = num_subjects * 100.0
    return (total_marks / max_possible_marks) * 100.0


def assign_grade(percentage: float) -> str:
    """
    Assign an academic letter grade based on the percentage score.

    Iterates through the centrally defined GRADE_THRESHOLDS.

    Args:
        percentage: The overall percentage scored by the student.

    Returns:
        Grade string (e.g., 'A+', 'A', 'B', 'C', 'D', 'E', 'F').
    """
    for threshold, grade in GRADE_THRESHOLDS:
        if percentage >= threshold:
            return grade
    return "F"


def check_pass_fail(subjects_marks: Dict[str, float]) -> str:
    """
    Determine overall Pass/Fail status.

    A student passes only if marks in EVERY subject are >= PASSING_SUBJECT_MARK (40).
    If any subject score is below 40, the student is marked as 'Fail'.

    Args:
        subjects_marks: Dictionary mapping subject names to marks obtained.

    Returns:
        'Pass' if all subjects meet the minimum threshold, otherwise 'Fail'.
    """
    for marks in subjects_marks.values():
        if marks < PASSING_SUBJECT_MARK:
            return "Fail"
    return "Pass"


# ==============================================================================
# OUTPUT / REPORT DISPLAY FUNCTION
# ==============================================================================
def display_result(
    student_name: str,
    subjects_marks: Dict[str, float],
    total_marks: float,
    percentage: float,
    grade: str,
    status: str,
) -> None:
    """
    Print a neat, structured, and formatted report card for the student.

    Args:
        student_name: Name of the student.
        subjects_marks: Dictionary of subject names and corresponding marks.
        total_marks: Precomputed sum of marks.
        percentage: Precomputed percentage score.
        grade: Assigned letter grade.
        status: Pass/Fail status string.
    """
    max_marks = len(subjects_marks) * 100.0
    divider = "=" * 60
    sub_divider = "-" * 60

    print("\n" + divider)
    print("                  STUDENT RESULT REPORT")
    print(divider)
    print(f" Student Name : {student_name}")
    print(sub_divider)
    print(f" {'#':<4} {'Subject Name':<38} {'Marks / 100':>12}")
    print(sub_divider)

    for index, (subject, marks) in enumerate(subjects_marks.items(), start=1):
        print(f" {index:<4} {subject:<38} {marks:>12.2f}")

    print(sub_divider)
    print(f" Total Marks Obtained : {total_marks:.2f} / {max_marks:.2f}")
    print(f" Percentage           : {percentage:.2f}%")
    print(f" Grade Assigned       : {grade}")
    print(f" Overall Status       : {status}")
    print(divider + "\n")


# ==============================================================================
# MAIN WORKFLOW CONTROLLER
# ==============================================================================
def process_student() -> None:
    """
    Handle the data collection, calculation, and display workflow for a single student.
    """
    print("\n--- Enter Student Details ---")
    student_name = get_non_empty_string(
        prompt="Enter student's name: ",
        field_name="Student name",
    )

    num_subjects = get_valid_positive_int(
        prompt="Enter the number of subjects: ",
        field_name="Number of subjects",
    )

    subjects_marks: Dict[str, float] = {}
    print(f"\nEntering details for {num_subjects} subject(s):")

    for i in range(1, num_subjects + 1):
        # Ensure subject name is not empty and not duplicated
        while True:
            subject_name = get_non_empty_string(
                prompt=f"  Enter name for Subject #{i}: ",
                field_name="Subject name",
            )
            if subject_name in subjects_marks:
                print(f"  Error: '{subject_name}' has already been entered. Use a unique subject name.")
            else:
                break

        marks = get_valid_marks(prompt=f"  Enter marks for '{subject_name}' (out of 100): ")
        subjects_marks[subject_name] = marks

    # Calculations: compute each value once and store for reuse
    total_marks = sum(subjects_marks.values())
    percentage = calculate_percentage(total_marks, num_subjects)
    grade = assign_grade(percentage)
    status = check_pass_fail(subjects_marks)

    # Display the final report
    display_result(
        student_name=student_name,
        subjects_marks=subjects_marks,
        total_marks=total_marks,
        percentage=percentage,
        grade=grade,
        status=status,
    )


def main() -> None:
    """
    Main application loop supporting multiple student assessments until user exits.
    """
    print("=" * 60)
    print("          WELCOME TO STUDENT GRADE CALCULATOR")
    print("=" * 60)

    while True:
        try:
            process_student()
        except (KeyboardInterrupt, EOFError):
            print("\nExiting program...")
            break

        try:
            continue_processing = get_yes_no_choice(
                prompt="Would you like to calculate grades for another student? (y/n): "
            )
            if not continue_processing:
                print("\nThank you for using Student Grade Calculator. Goodbye!")
                break
        except (KeyboardInterrupt, EOFError):
            print("\nExiting program. Goodbye!")
            break


if __name__ == "__main__":
    main()
