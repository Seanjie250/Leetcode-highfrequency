class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:

        if endGene not in bank:
            return -1
        
        choice = set(bank)
        options = ['A' , 'C' , 'G' , 'T']

        queue = deque()
        queue.append(startGene)

        visited = set()
        visited.add(startGene)
        
        count = 0

        while queue:
            for i in range(len(queue)):
                gene = queue.popleft()
                if gene == endGene:
                    return count
                for i in range(8):
                    for option in options:
                        new_gen = gene[:i] + option + gene[i + 1:]
                        if new_gen in choice and new_gen not in visited:
                            queue.append(new_gen)
                            visited.add(new_gen)
            count += 1
        return -1

                            