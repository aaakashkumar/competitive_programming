# Cheapest Flights Within K Stops
# https://leetcode.com/problems/cheapest-flights-within-k-stops/
# @author Akash Kumar


class Solution(object):
    def findCheapestPrice(self, n, flights, src, dst, K):
        """
        Method to find the cheapest flight price using Dijkstra's algorithm.
        :type n: int
        :type flights: List[List[int]]
        :type src: int
        :type dst: int
        :type K: int
        :rtype: int
        """
        
        import heapq
        
        list_of_flights = dict()
        for edge in flights:
            if edge[0] in list_of_flights:
                list_of_flights[edge[0]].append((edge[1], edge[2]))
            else:
                list_of_flights[edge[0]] = [(edge[1], edge[2])]
                
        unvisited_nodes = [(0, src, 0)]  # priority queue (cost, node, steps)
        
        while unvisited_nodes:
            current_price, current_node, steps_to_current = heapq.heappop(unvisited_nodes)
            
            if current_node == dst:
                return current_price
            
            if steps_to_current <= K:
                try:
                    for neighbor, price_to_neighbor in list_of_flights[current_node]:
                        
                        price_from_src = current_price + price_to_neighbor
                        heapq.heappush(unvisited_nodes, (price_from_src, neighbor, 
                                                             steps_to_current+1))
                except:
                    continue
            
        return -1
            
        