from typing import List

def calculate_grades(scores: List[int]) -> List[str]:
    """
    Calculate grades based on student scores using a relative grading system.

    Args:
        scores (List[int]): List of student scores.

    Returns:
        List[str]: List of grades corresponding to each score.
    """
    # Return an empty list if there are no scores
    if not scores:
        return []

    # Determine the highest score to use as the basis for grade calculation
    best = max(scores)
    grades = []  # Initialize an empty list to store grades

    # Assign grades based on the deviation from the best score
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

        # Debugging output for each score and grade
        print(f"Score: {score}, Best: {best}, Grade: {grades[-1]}")

    return grades