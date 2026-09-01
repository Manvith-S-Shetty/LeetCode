'''
I nnot did this I just pasted it that's it.
'''
from collections import deque

class Solution:
    def minMoves(self, classroom: List[str], energy: int) -> int:

        rows = len(classroom)
        cols = len(classroom[0])

        # Find starting position and litter positions
        start = None
        litter = {}

        for r in range(rows):
            for c in range(cols):
                if classroom[r][c] == 'S':
                    start = (r, c)

                elif classroom[r][c] == 'L':
                    litter[(r, c)] = len(litter)

        # If there are k litter pieces, 111...111 is our goal
        k = len(litter)
        all_mask = (1 << k) - 1

        # Queue: (row, col, current_energy, mask, moves)
        q = deque()
        q.append((start[0], start[1], energy, 0, 0))

        visited = set()
        visited.add((start[0], start[1], energy, 0))

        directions = [
            (-1, 0),   # up
            (1, 0),    # down
            (0, -1),   # left
            (0, 1)     # right
        ]

        while q:

            r, c, e, mask, moves = q.popleft()

            # All litter collected
            if mask == all_mask:
                return moves

            for dr, dc in directions:

                nr = r + dr
                nc = c + dc

                # Outside the classroom
                if nr < 0 or nr >= rows or nc < 0 or nc >= cols:
                    continue

                # Wall
                if classroom[nr][nc] == 'X':
                    continue

                # No energy to make this move
                if e == 0:
                    continue

                # Moving costs 1 energy
                new_energy = e - 1

                # Reset area
                if classroom[nr][nc] == 'R':
                    new_energy = energy

                # Collect litter
                new_mask = mask

                if classroom[nr][nc] == 'L':
                    litter_id = litter[(nr, nc)]
                    new_mask = mask | (1 << litter_id)

                state = (nr, nc, new_energy, new_mask)

                # Avoid processing the exact same state again
                if state in visited:
                    continue

                visited.add(state)

                q.append(
                    (nr, nc, new_energy, new_mask, moves + 1)
                )

        return -1