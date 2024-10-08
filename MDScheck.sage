def is_mds(matrix):
    """
    Check if a given matrix is an MDS matrix.
    
    Parameters:
    matrix (Matrix): A SageMath matrix.
    
    Returns:
    bool: True if the matrix is MDS, False otherwise.
    """
    nrows, ncols = matrix.nrows(), matrix.ncols()
    
    if nrows != ncols:
        return False  # MDS matrices must be square
    
    # Check all square submatrices
    for i in range(1, nrows + 1):
        for row in range(nrows - i + 1):
            for col in range(ncols - i + 1):
                submatrix = matrix.submatrix(row, col, i, i)
                if submatrix.det() == 0:
                    return False
    return True

# Example usage
M = Matrix(GF(2), [[1, 0, 1], [1, 1, 0], [0, 1, 1]])
print(is_mds(M))  # Output: True or False


