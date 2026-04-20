class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = {}
        columns = {}
        boxes = {}
        for r in range(3):
            for c in range(3):
                boxes[(r, c)] = set()
        validation = True

        for i in range(len(board)):
            rows[i] = set()
            columns[i] = set()
            for j in range(len(board)):
                if board[i][j] != '.':
                    if board[i][j] in rows[i]:
                        validation = False
                    rows[i].add(board[i][j])
                if board[j][i] != '.':
                    if board[j][i] in columns[i]:
                        validation = False
                    columns[i].add(board[j][i])
                if board[i][j] != '.':
                    if board[i][j] in boxes[(i//3, j//3)]:
                        validation = False
                    boxes[(i//3, j//3)].add(board[i][j])

        return validation