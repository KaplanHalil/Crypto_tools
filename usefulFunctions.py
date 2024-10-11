def copy_2d_array(original_array):
    """
    Copies elements from a 2D array to a new array.

    Args:
        original_array (list of lists): The original 2D array.

    Returns:
        list of lists: A new 2D array with the same elements.
    """
    copied_array = []  # Initialize an empty list for the copied array

    for row in original_array:
        # Create a new row (list) with the same elements as the original row
        copied_row = list(row)
        copied_array.append(copied_row)

    return copied_array