from math import inf


# The dijkstra algorithm
def dijkstra(nodes, connections, start):
    # Set up the priority queue
    priority_queue = {node: inf for node in nodes}
    priority_queue[start] = 0

    # set up the visited elements as an empty dict
    visited = {}

    # continue as long as there are items in the priority queue
    while priority_queue:
        # find the priority queue item with the lowest value
        next_node = min(priority_queue, key=priority_queue.get)
        next_dist = priority_queue.pop(next_node)

        # Add this node to the visited list
        visited[next_node] = next_dist

        # Find the neighbours of the newly added node
        neighbours = {nd for nd in priority_queue if {nd, next_node} in set(connections.keys())}
        #  For each unvisited neighbour of the new node check and if necessary update the distance to that neighbour
        for neighbour in neighbours:
            min_dist = min(priority_queue[neighbour], next_dist + connections[frozenset({next_node, neighbour})])
            priority_queue[neighbour] = min_dist

        print(f'visited: {visited}')
        print(f'priority queue', [priority_queue])

    return visited


if __name__ == "__main__":
    nodes_in = {'A', 'B', 'C', 'D', 'E'}
    connections_in = {frozenset({'A', 'B'}): 7,
                      frozenset({'A', 'D'}): 3,
                      frozenset({'B', 'D'}): 2,
                      frozenset({'B', 'C'}): 3,
                      frozenset({'B', 'E'}): 6,
                      frozenset({'C', 'D'}): 4,
                      frozenset({'D', 'E'}): 7,
                      frozenset({'C', 'E'}): 1}

    min_paths = dijkstra(nodes_in, connections_in, 'A')
    print(min_paths)
