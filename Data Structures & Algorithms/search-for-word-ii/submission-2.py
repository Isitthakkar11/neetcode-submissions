class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root ={}
        for word in words:
            node = root
            for ch in word:
                node = node.setdefault(ch, {})
            node['#'] = word
        rows, cols = len(board), len(board[0])
        result = []

        def dfs(r, c, node):
            if (r < 0 or r >= rows or c < 0 or c >= cols):
                return
            ch = board[r][c]
            if ch not in node:
                return
            nxt = node[ch]

            word = nxt.get("#")
            if word:
                result.append(word)
                nxt.pop("#")

            board[r][c] = "*"
            dfs(r - 1, c, nxt)
            dfs(r + 1, c, nxt)
            dfs(r, c + 1, nxt)
            dfs(r, c - 1, nxt)
            board[r][c] = ch

        for r in range(rows):
            for c in range(cols):
                dfs(r, c, root)

        return result