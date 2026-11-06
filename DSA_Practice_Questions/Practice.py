import queue;

class Solution:
    def bfs(self, adj):
        queue = deque([0])
        visited = set(0)
        result = []

        while queue:
            node = queue.popleft()
            result.append(node)
            # visited.add(node)

            for neighbor in adj[node]:
                if neighbor not in visited:
                    visited.add(node)
                    queue.append(neighbor)

        return result
                
            

    