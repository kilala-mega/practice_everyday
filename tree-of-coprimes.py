"""
represent a graph with edges:
graph[node1] = node2
graph[node2] = node1

root node is node 0 -> start from node 0

note the number is between 1 and 50
DFS
use a list (parent node) path to store: value -> (node index, depth) to exclude duplicate search on the gcd of the same value
"""
class Solution:
    def getCoprimes(self, nums: List[int], edges: List[List[int]]) -> List[int]:
        # final output, initialized to -1
        ans = [-1] * len(nums)
        path = [[] for _ in range(51)] # 1 <= nums[i] <= 50
        seen = set() # if i-th is visited
        
        graph = defaultdict(list)
        for node1, node2 in edges:
            graph[node1].append(node2)
            graph[node2].append(node1)
            
        
        def dfs(node: int, depth: int) -> None:
            if node in seen:
                return
            seen.add(node)
            largest_depth = -1
            for i in range(len(path)):
                if gcd(nums[node], i) == 1:
                    # find a coprimes
                    if len(path[i]) > 0:
                        top_i, top_depth = path[i][-1]
                        if top_depth > largest_depth:
                            largest_depth = top_depth
                            ans[node] = top_i
            path[nums[node]].append((node, depth))
            for neighbor in graph[node]:
                dfs(neighbor, depth+1)
            path[nums[node]].pop()
                    
        
        dfs(0, 0) # start with node 0 and say it's depth is 0
        return ans
        
