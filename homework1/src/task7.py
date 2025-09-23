import numpy as np

def calculate_grades(nums):

    """
    Calculate the mean and median of grades in class

    Parameters:
        nums: list of numbers
    
    Returns:
        list: with mean and median

    Raises:
        ValueError: If the input list is empty
    """

    if not nums:
        raise ValueError("No numbers provided")

    num_arr = np.array(nums)
    return [np.mean(num_arr), np.median(num_arr)]


if __name__ == "__main__":
    class_grades = calculate_grades([100, 90, 80, 99, 75, 85])
    print(f"The class average was a {round(class_grades[0],2)}% and the median was {class_grades[1]}")
