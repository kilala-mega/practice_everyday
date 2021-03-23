class Solution(object):
    def maxSatisfied(self, customers, grumpy, X):
        """
        :type customers: List[int]
        :type grumpy: List[int]
        :type X: int
        :rtype: int
        """
        # sliding window
        # len(customers) = len(grumpy)
        # for a window of X maximize the sum(customers[i] where grumpy[i] used to be 1)
        # f(i, j) sum of customers between i ~ j min with grumpy = 1
        n = len(customers)
        satisfied = 0
        for i in range(n):
            if not grumpy[i]:
                satisfied += customers[i]
                customers[i] = 0
        best_satisfied = 0
        current_satisfied = satisfied
        for i in range(n):
            current_satisfied += customers[i]
            if i >= X:
                current_satisfied -= customers[i-X]
            best_satisfied = max(best_satisfied, current_satisfied)
        return best_satisfied
