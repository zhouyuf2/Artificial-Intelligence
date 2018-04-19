# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 11:01:58 2018

@author: Yufeng Zhou

Using Breadth First Search to solve the farmer crosses river with fox, chicken, and grain.
"""

def is_valid(state):
    """
    Check a state is valid or not.
    A state is invalid when only the fox and the chicken or only the chicken and the grain stay together
    param state: input state
    return: True or False
    """
    if state[0] == state[1] and state[0] != state[2] and state[0] != state[3]:
        return False
    if state[1] == state[2] and state[0] != state[1] and state[3] != state[1]:
        return False
    return True


def next_states(state, found):
    """
    From a given state, generate a list of possible next states
    param state: input state
    param found: states already found
    return: a list of new undiscovered states
    """
    res = []
    new_state = (state[0], state[1], state[2], 1 - state[3])
    if is_valid(new_state) and new_state not in found:
        res.append(new_state)

    for i in range(3):
        new_state = list(state)
        if new_state[3] == new_state[i]:
            new_state[i] = 1 - new_state[i]
            new_state[3] = 1 - new_state[3]
            new_state = tuple(new_state)
            if is_valid(new_state) and new_state not in found:
                res.append(new_state)
    return res


def backtrace(parent, start, end):
    """
    Track the path from a BFS searching tree
    param parent: BFS searching tree
    param start: start state
    param end: final state
    return: a path from start state to final state
    """
    path = [end]
    while path[-1] != start:
        path.append(parent[path[-1]])
    path.reverse()
    return path


def bfs(start, end):
    """
    Perform the BFS on the problem
    param start: start state
    param end: final state
    return: a valid path from start state to final state
    """
    parent = {}
    queue = []
    found = []
    queue.append(start)
    found.append(start)
    while queue:
        node = queue.pop(0)
        if node == end:
            return backtrace(parent, start, end)
        for adjacent in next_states(node, found):
            parent[adjacent] = node
            queue.append(adjacent)
            found.append(adjacent)


def visualize(path):
    """
    Represent the result in a meaningful way
    param path: BFS results
    return: None
    """

    names = ['Fox', 'Chicken', 'Grain', 'Farmer']
    sides = ['Start', 'Final']
    for node in path:
        start_side = ''
        final_side = ''
        for i in range(4):
            if node[i] == 0:
                start_side = start_side + names[i] + " "
            else:
                final_side = final_side + names[i] + " "
     
        # Get the actions
        idx = path.index(node)
        if idx > 0:
            changed_item = -1
            for i in range(3):
                if path[idx][0] != path[idx - 1][0]:
                    changed_item = 0
                if path[idx][1] != path[idx - 1][1]:
                    changed_item = 1
                if path[idx][2] != path[idx - 1][2]:
                    changed_item = 2
            if changed_item < 0:
                pass
            else:
                print("move from {} to {} with {}".format(sides[path[idx - 1][3]], sides[path[idx][3]], names[changed_item]))
        else:
            print()


if __name__ == '__main__':
    visualize(bfs((0, 0, 0, 0), (1, 1, 1, 1)))
