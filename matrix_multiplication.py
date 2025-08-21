def scalar_multiply(matrix: list[list[int|float]], scalar: int|float) -> list[list[int|float]]:
  
  result = [[0] * len(matrix[0]) for _ in range(len(matrix))]
  
  for i in range(len(matrix)):
    for j in range(len(matrix[0])):
      result[i][j] = scalar * matrix[i][j]
  return result
	
