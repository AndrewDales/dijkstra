from math import inf


# The dijkstra algorithm
def dijkstra(nodes, edges, start=None, end=None, detail=False, show_route=True):
    if not start:
        start = nodes[0]

    # Set up the priority queue
    priority_queue = {node: inf for node in nodes}
    priority_queue[start] = 0

    # set up the visited elements as an empty dict
    visited = {}

    # Set up the routes dictionary - this will hold the quickest route found to each node
    routes = {start: [start]}

    # continue as long as there are items in the priority queue
    while priority_queue:
        # find the priority queue item with the lowest value
        next_node = min(priority_queue, key=priority_queue.get)
        next_dist = priority_queue.pop(next_node)

        # Add this node to the visited list
        visited[next_node] = next_dist

        # If full details are not required and the end point has been reached return the minimum distance and the route
        if next_node == end and (not detail):
            if not show_route:
                return next_dist
            else:
                return next_dist, routes[next_node]

        # Find the neighbours of the newly added node
        neighbours = {nd for nd in priority_queue if {nd, next_node} in set(edges.keys())}
        # For each unvisited neighbour of the new node check if the total distance to the neighbour, via the
        # new node is less than distance to the neighbour that is already in the priority queue
        for neighbour in neighbours:
            new_dist = next_dist + edges[frozenset({next_node, neighbour})]
            if new_dist < priority_queue[neighbour]:
                # If the new distance is less than the existing distance, update the priority queue
                priority_queue[neighbour] = new_dist
                # update the routes to include the newly found distance
                routes[neighbour] = routes[next_node] + [neighbour]

    if show_route:
        return visited, routes
    else:
        return visited


if __name__ == "__main__":
    nodes_in = {'A', 'B', 'C', 'D', 'E'}
    edges_in = {frozenset({'A', 'B'}): 7,
                frozenset({'A', 'D'}): 3,
                frozenset({'B', 'D'}): 2,
                frozenset({'B', 'C'}): 3,
                frozenset({'B', 'E'}): 6,
                frozenset({'C', 'D'}): 4,
                frozenset({'D', 'E'}): 7,
                frozenset({'C', 'E'}): 1}

    start_node = 'A'
    end_node = 'E'

    min_dist, route = dijkstra(nodes_in, edges_in, start=start_node, end=end_node, show_route=True)

    print(f"The minimum distance from {start_node} to {end_node} is {min_dist}")
    print(f"The quickest route is {' -> '.join(route)}")
