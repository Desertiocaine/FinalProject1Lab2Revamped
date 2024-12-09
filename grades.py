from typing import List

def calculate_grades(scores: List[int]) -> List[str]:
    """
    Calculate grades based on student scores using a relative grading system.
    """
    if not scores:
        return []

    best = max(scores)
    grades = []

    for score in scores:
        if score >= best - 10:
            grades.append('A')
        elif score >= best - 20:
            grades.append('B')
        elif score >= best - 30:
            grades.append('C')
        elif score >= best - 40:
            grades.append('D')
        else:
            grades.append('F')

    return grades

def calculate_final_grade(scores):
    """
    Calculate the final grade based on given scores.

    Args:
        scores (List[int]): List of scores.

    Returns:
        tuple: Calculated final grade (float) and corresponding letter grade (str).
    """
    if not scores:
        raise ValueError("Scores list cannot be empty")

    # Filter out redundant placeholder scores
    actual_scores = [score for score in scores if score > 0]

    final_grade = round(sum(actual_scores) / len(actual_scores), 2)  # Format to 2 decimal places
    letter_grade = get_letter_grade(final_grade)
    return final_grade, letter_grade

def get_letter_grade(score):
    """
    Determine the letter grade based on the numerical score.

    Args:
        score (float): Numerical score.

    Returns:
        str: Corresponding letter grade.
    """
    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    elif score >= 60:
        return 'D'
    else:
        return 'F'