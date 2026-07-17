class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        result = []
        queens = []
        cols = set()
        diag1 = set()
        diag2 = set()

        def backtrack(row):
            if row == n:
                result.append(build_board())
                return 

            for col in range(n):
                if col in cols or (row - col) in diag1 or (row + col) in diag2:
                    continue

                queens.append(col)
                cols.add(col)
                diag1.add(row - col)
                diag2.add(row + col)
                backtrack(row + 1)

                queens.pop()
                cols.remove(col)
                diag1.remove(row - col)
                diag2.remove(row + col)

        def build_board():
            return ["." * c + "Q" + "." * (n - c - 1) for c in queens]
        
        backtrack(0)
        return result