class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = defaultdict(list)
        for scr, dst in sorted(tickets, reverse = True):
            graph[scr].append(dst)

        result = []

        def dfs(airport):
            while graph[airport]:
                next_stop = graph[airport].pop()
                dfs(next_stop)
            result.append(airport)

        dfs("JFK")

        return result[::-1]


        