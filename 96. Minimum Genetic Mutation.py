from collections import deque

class Solution(object):
    def minMutation(self, startGene, endGene, bank):
        """
        :type startGene: str
        :type endGene: str
        :type bank: List[str]
        :rtype: int
        """
        if endGene not in bank:
            return -1
        
        bank = set(bank)  # Convert to a set for quick lookup
        queue = deque([(startGene, 0)])  # (current gene, mutation steps)
        choices = ['A', 'C', 'G', 'T']
        
        while queue:
            gene, steps = queue.popleft()
            if gene == endGene:
                return steps  # Found the shortest path
            
            # Generate all possible mutations
            for i in range(len(gene)):
                for ch in choices:
                    if ch != gene[i]:  # Only mutate different characters
                        mutated_gene = gene[:i] + ch + gene[i+1:]
                        if mutated_gene in bank:
                            queue.append((mutated_gene, steps + 1))
                            bank.remove(mutated_gene)  # Remove to avoid revisits
        
        return -1  # No valid mutation path found
