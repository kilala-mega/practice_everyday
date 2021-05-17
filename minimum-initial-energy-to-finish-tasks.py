class Solution:
    def minimumEffort(self, tasks: List[List[int]]) -> int:
        tasks = sorted(tasks, key=lambda x: x[1]-x[0], reverse=True)
        
        #print(tasks)
        energy = tasks[0][1]
        total = energy
        for i in range(1, len(tasks)):
            energy -= tasks[i-1][0]
            if energy < tasks[i][1]:
                total += (tasks[i][1]-energy)
                energy = tasks[i][1]
        return total
