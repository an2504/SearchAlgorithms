from collections import deque
import sys
import math

goal_state = [0, 1, 2, 3, 4, 5, 6, 7, 8]


def main():
    start_state = sys.argv[1].split(",")
    start_state = [int(x) for x in start_state]

    print(bfs(start_state))


def bfs(puzzle_state):
    visited = set()
    queue = deque([(puzzle_state, 'START')])
    while queue:
        state, direction = queue.popleft()
        visited.add(to_string(state))
        # print(state)
        if state == goal_state:
            return direction

        children = get_children(state)
        for child, direc in children:
            if to_string(child) not in visited:
                queue.append((child, direction + " " + direc))
                visited.add(to_string(child))


def to_string(puzzle_state):
    return ''.join(str(s) for s in puzzle_state)


def get_children(puzzle_state):
    new_states = []
    board_length = len(puzzle_state)
    side_length = int(math.sqrt(board_length))
    zero_position = puzzle_state.index(0)

    # UP
    if zero_position not in range(0, side_length):
        new_state = puzzle_state[:]
        new_zero_position = zero_position - side_length
        new_state[zero_position], new_state[new_zero_position] = new_state[new_zero_position], new_state[zero_position]
        new_states.append((new_state, 'UP'))

    # DOWN
    if zero_position not in range(board_length - side_length, board_length):
        new_state = puzzle_state[:]
        new_zero_position = zero_position + side_length
        new_state[zero_position], new_state[new_zero_position] = new_state[new_zero_position], new_state[zero_position]
        new_states.append((new_state, 'DOWN'))

    # LEFT
    if zero_position not in range(0, board_length, side_length):
        new_state = puzzle_state[:]
        new_zero_position = zero_position - 1
        new_state[zero_position], new_state[new_zero_position] = new_state[new_zero_position], new_state[zero_position]
        new_states.append((new_state, 'LEFT'))

    # RIGHT
    if zero_position not in range(side_length - 1, board_length, side_length):
        new_state = puzzle_state[:]
        new_zero_position = zero_position + 1
        new_state[zero_position], new_state[new_zero_position] = new_state[new_zero_position], new_state[zero_position]
        new_states.append((new_state, 'RIGHT'))

    return new_states


if __name__ == '__main__':
    main()
