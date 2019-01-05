# in state: [missionaries, cannibals] and boat position is left = 0, right = 1

# initial state: left: [3, 3], right: [0, 0], boat: 0
# possible actions: 
#   - move 1 missionary right
#   - move 2 missionaries right
#   - move 1 cannibal right
#   - move 2 cannibals right
#   - move 1 missionary and 1 cannibal right
#   - move 1 missionary left
#   - move 2 missionaries left
#   - move 1 cannibal left
#   - move 2 cannibals left
#   - move 1 missionary and 1 cannibal left
# goal test: state is left: [0, 0], right: [3, 3]
# path cost: each step costs 1, so path cost is length of path through tree

    

def goal_check(state):
    if state[0] == [0, 0] and state[1] == [3, 3]:
        return True
    return False

def get_frontier(state, visited_nodes):
    new_boat = 1 if state[2] == 0 else 0
    frontier = []
    current_side = state[state[2]]
    opposite_side = state[new_boat]
    if state[2] == 0:
        if current_side[0] >= 2 and (current_side[0] - 2 >= current_side[1] or current_side[0] - 2 == 0):
            new_state = [[current_side[0] - 2, current_side[1]], [opposite_side[0] + 2, opposite_side[1]], new_boat, state]
            if not new_state in visited_nodes:
                frontier.append(new_state)
                visited_nodes.append(new_state)
        if current_side[0] >= 1 and (current_side[0] - 1 == 0 or current_side[0] - 1 >= current_side[1]):
            new_state = [[current_side[0] - 1, current_side[1]], [opposite_side[0] + 1, opposite_side[1]], new_boat, state]
            if not new_state in visited_nodes:
                frontier.append(new_state)
                visited_nodes.append(new_state)
        if current_side[1] >= 2:
            new_state = [[current_side[0], current_side[1] - 2], [opposite_side[0], opposite_side[1] + 2], new_boat, state]
            if not new_state in visited_nodes:
                frontier.append(new_state)
                visited_nodes.append(new_state)
        if current_side[1] >= 1:
            new_state = [[current_side[0], current_side[1] - 1], [opposite_side[0], opposite_side[1] + 1], new_boat, state]
            if not new_state in visited_nodes:
                frontier.append(new_state)
                visited_nodes.append(new_state)
        if current_side[0] >= 1 and current_side[1] >= 1:
            new_state = [[current_side[0] - 1, current_side[1] - 1], [opposite_side[0] + 1, opposite_side[1] + 1], new_boat, state]
            if not new_state in visited_nodes:
                frontier.append(new_state)
                visited_nodes.append(new_state)
    else:
        if current_side[0] >= 2 and current_side[0] - 2 >= current_side[1]:
            new_state = [[opposite_side[0] + 2, opposite_side[1]], [current_side[0] - 2, current_side[1]], new_boat, state]
            if not new_state in visited_nodes:
                frontier.append(new_state)
                visited_nodes.append(new_state)
        if current_side[0] >= 1 and current_side[1] - 1 >= current_side[1]:
            new_state = [[opposite_side[0] + 1, opposite_side[1]], [current_side[0] - 1, current_side[1]], new_boat, state]
            if not new_state in visited_nodes:
                frontier.append(new_state)
                visited_nodes.append(new_state)
        if current_side[1] >= 2:
            new_state = [[opposite_side[0], opposite_side[1] + 2], [current_side[0], current_side[1] - 2], new_boat, state]
            if not new_state in visited_nodes:
                frontier.append(new_state)
                visited_nodes.append(new_state)
        if current_side[1] >= 1:
            new_state= [[opposite_side[0], opposite_side[1] + 1], [current_side[0], current_side[1] - 1], new_boat, state]
            if not new_state in visited_nodes:
                frontier.append(new_state)
                visited_nodes.append(new_state)
        if current_side[0] >= 1 and current_side[1] >= 1:
            new_state = [[opposite_side[0] + 1, opposite_side[1] + 1], [current_side[0] - 1, current_side[1] - 1], new_boat, state]
            if not new_state in visited_nodes:
                frontier.append(new_state)
                visited_nodes.append(new_state)
    return frontier

def print_solution(last_node):
    current_node = last_node
    nodes_in_order = []
    while not current_node == []:
        nodes_in_order.insert(0, current_node)
        current_node = current_node[3]
    for node in nodes_in_order:
        boat_str = " <> | " if node[2] == 0 else " | <> "
        print(str(node[0][0]) + " missionaries, " + str(node[0][1]) + " cannibals" + boat_str + str(node[1][0]) + " missionaries, " + str(node[1][1]) + " cannibals")

state_queue = [[[3, 3], [0, 0], 0, []]]
visited_nodes = state_queue
cost = 0
while not goal_check(state_queue[0]):
    cost += 1
    frontier = get_frontier(state_queue[0], visited_nodes)
    for node in frontier:
        state_queue.append(node)
    del state_queue[0]
print_solution(state_queue[0])
