from collections import defaultdict
import sys, threading
def main():
 

    def farcity():


        visited = set()
        def dfs(person, visited):

            visited.add(person)

            for neighbour in graph[person]:
                if neighbour not in visited:
                    dfs(neighbour, visited)
            # print(person, visited)


        n , m = map(int, input().split())

        gold = list(map(int, input().split()))

        for i, val in enumerate(gold):
            gold[i] = [i+1, val]
        gold.sort(key = lambda x: x[1])


        graph = defaultdict(list)
        for i in range(m):
            node, neighbour = map(int, input().split())
            graph[node].append(neighbour)
            graph[neighbour].append(node)


        cost = 0    
        # print(gold)
        for person in gold:
            if person[0] not in visited:
                cost += person[1]
                dfs(person[0], visited)

        return cost


    print(farcity())







sys.setrecursionlimit(1 << 30)
threading.stack_size(1 << 27)
main_thread = threading.Thread(target= main )
main_thread.start()
main_thread.join()






