def make_swamp(count, final=False):

    if final:
        right  = ['>' for i in range(count)]
        left   = ['<' for i in range(count)]

    else:    
        left  = ['>' for i in range(count)]
        right = ['<' for i in range(count)]

    return ''.join(left) + '_' + ''.join(right)


def pretty_print(swamp):

    pretty_swamp = " ".join(swamp)
    print(pretty_swamp)

def make_swamp(count, final=False):

    if final:
        right  = ['>' for i in range(count)]
        left   = ['<' for i in range(count)]

    else:    
        left  = ['>' for i in range(count)]
        right = ['<' for i in range(count)]

    return ''.join(left) + '_' + ''.join(right)


def new_states(state):
    new_states = list()

    # Safeguard
    if type(state) is not str:
        raise TypeError("Can't work with non-string.")

    # Get the lilly pad index
    i = state.find('_')

    # Get info about lilly pad position
    leftmost = i == 0
    left_penultimate = i == 1
    rightmost = i == len(state) - 1
    right_penultimate = i == len(state) - 2

    # ========== Get state 1 ==========
    if not leftmost and state[i - 1] == '>':
        nstate = state[:i - 1] + '_' + '>'
        if (i != len(state) - 1):
            nstate += state[i + 1:]

        new_states.append(nstate)
    else:
        new_states.append(None)

    # ========== Get state 2 ==========
    if not left_penultimate and not leftmost and state[i - 2] == '>':
        nstate = state[:i - 2] + '_' + state[i - 1] + '>'
        if (i != len(state) - 1):
            nstate += state[i + 1:]

        new_states.append(nstate)
    else:
        new_states.append(None)

    # ========== Get state 3 ==========
    if not rightmost and state[i + 1] == '<':
        nstate = state[:i] + '<' + '_'
        if (i + 1 != len(state) - 1):
            nstate += state[i + 2:]

        new_states.append(nstate)
    else:
        new_states.append(None)

    # ========== Get state 4 ==========
    if not right_penultimate and not rightmost and state[i + 2] == '<':
        nstate = state[:i] + '<' + state[i + 1] + '_'
        if (i + 2 != len(state) - 1):
            nstate += state[i + 3:]
        new_states.append(nstate)
    else:
        new_states.append(None)

    return new_states


def bfs(end, swamp=None, tocheck=None, checked=None):

    # ==============================

    if tocheck is None:
        if swamp is None:
            return None
        else:
            tocheck = [swamp, ]
    if checked is None:
        checked = []

    # ==============================

    if tocheck == []:
        return None

    state = tocheck[0]
    if state == end:
        checked.append(state)
        return checked

    children = new_states(state)

    for child in children:
        if child is not None and child not in checked and child not in tocheck:
            tocheck.append(child)

    checked.append(state)
    del tocheck[0]

    return bfs(end, tocheck=tocheck, checked=checked)


def dfs(end, swamp=None, tocheck=None, checked=None):

    # ==============================

    if tocheck is None:
        if swamp is None:
            return None
        else:
            tocheck = [swamp, ]
    if checked is None:
        checked = []

    # ==============================

    if tocheck == []:
        return None

    i = len(tocheck) - 1

    state = tocheck[i]
    if state == end:
        checked.append(state)
        return checked

    children = new_states(state)

    for child in children:
        if child is not None and child not in checked and child not in tocheck:
            tocheck.append(child)

    checked.append(state)
    del tocheck[i]

    return dfs(end, tocheck=tocheck, checked=checked)


def frogs_game(half):
    initial = make_swamp(half, final=False)
    final = make_swamp(half, final=True)
    bfs_path = bfs(final, initial)
    dfs_path = dfs(final, initial)
    print(bfs_path)
    print(dfs_path)


if __name__ == '__main__':
    half = input("How many frogs on each side?: ")
    half = int(half)
    frogs_game(half)
