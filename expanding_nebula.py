from collections import defaultdict


def solution(g):
    # For this task, let's define such thing as pre-column.
    # In such way we will call the previous state of a column in a grid.
    # All possible 2x2 grids for different current states of cells.
    STATES = {
        0: (
            ((0, 0), (0, 0)),
            ((0, 0), (1, 1)),
            ((1, 0), (1, 0)),
            ((1, 0), (0, 1)),
            ((1, 0), (1, 1)),
            ((1, 1), (0, 0)),
            ((1, 1), (1, 0)),
            ((1, 1), (0, 1)),
            ((1, 1), (1, 1)),
            ((0, 1), (1, 0)),
            ((0, 1), (0, 1)),
            ((0, 1), (1, 1)),
        ),
        1: (
            ((0, 1), (0, 0)),
            ((1, 0), (0, 0)),
            ((0, 0), (1, 0)),
            ((0, 0), (0, 1)),
        ),
    }

    # Merge possible prestates of a cell with possible prestates of previous cells.
    def merge_prestate(pre_img1, pre_img2):
        # List with answer
        arr = []
        # For every prestate in the previous ones we find a possible prestate of a current cell,
        # first row of which merges with the last row of the previous.
        for state1 in pre_img1:
            for state2 in pre_img2:
                # If they are equal, we add them to the list
                if state1[-1] == state2[0]:
                    arr.append(tuple(state1) + (state2[1],))
        return arr

    # Creates all possible pre-columns for a column.
    def create_precolumns(col):
        # Define preimages, as all possible prestates for current state of a first cell.
        prestates = STATES[col[0]]
        # In a cycle we call a function, that merges possible prestates of a cell.
        # with possible prestates of previous cells.
        # After merging we update preimages contain possible prestates of a current cell.
        for i in range(1, len(col)):
            prestates = merge_prestate(prestates, STATES[col[i]])
        # Rearrange the preimages into two columns, which are represented as rows.
        # We need to do this, because we are working with columns, represented as 1D lists.
        return [tuple(zip(*p)) for p in prestates]

    # Rotate the matrix horizontally we do this in order to work with columns, because
    # the possible height of the grid is much smaller than the possible width.
    g = list(zip(*g))
    # Initialize a dictionary, which will store the count of previous pre-columns.
    previous_columns = defaultdict(lambda: 0)
    # Fill the dictionary with pre-columns from a first column.
    for p in create_precolumns(g[0]):
        previous_columns[p[1]] += 1
    # Then iterate through other columns.
    for i in range(1, len(g)):
        # Initialize the current columns.
        columns = defaultdict(lambda: 0)
        for p in create_precolumns(g[i]):
            # If start of a new possible pre-column is the end of some previous pre-columns, then we can continue.
            # Otherwise, we skip these possible pre-column, because it cannot merge with any of previous.
            if previous_columns[p[0]]:
                columns[p[1]] += previous_columns[p[0]]
        # For the next step the current columns will become the previous ones
        previous_columns = columns
    return sum(previous_columns.values())
