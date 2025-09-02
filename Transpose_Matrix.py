class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        

        m = len(matrix)
        n = len(matrix[0])
        result = [[0] *m for _ in range(n)]



        if m>=1 and n<=1000 and m*n>=1 and n<=100000:
            for i in range(m):
                for j in range(n):
                    result[j][i] = matrix[i][j]
            
         

        return result
        
