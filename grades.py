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


def calculate_final_grade(scores: List[int]) -> float:
    """
    Calculate the final grade based on given scores.

    Args:
        scores (List[int]): List of scores.

    Returns:
        float: Calculated final grade based on average.
    """
    if not scores:
        raise ValueError("Scores list cannot be empty")

    return sum(scores) / len(scores)  # Example: average score