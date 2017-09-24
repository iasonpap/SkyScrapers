def cross(A, B):
    "Cross product of elements in A and elements in B."
    return [a+b for a in A for b in B]

digits   = '1234'
rows     = 'ABCD'
rows_cl  = 'xzyw'
cols     = digits
squares  = cross(rows, cols) #codenames for the squares of the grid
grid_cl   = cross(rows_cl, cols) #codenames for the clues for easier access

"""creating the units (all the squares in the same row and column)
   and peers (all the squares in the same row and column except the key square)
   of the squares"""
unitlist = ([cross(rows, c) for c in cols] +
            [cross(r, cols) for r in rows])
units = dict((s, [u for u in unitlist if s in u])
             for s in squares)
peers = dict((s, set(sum(units[s],[]))-set([s]))
             for s in squares)

"""creating the units and peers of the clues"""
unitlist_cl = ([cross(r,cols) for r in 'xy']  +
               [cross(a,cols) for a in 'zw'])
#units_cl = dict((cl, [u]))

#peers_cl = dict()

print("~~~~~~~~~~~UNITLIST_CL~~~~~~~~")
print(unitlist_cl)
print("~~~~~~~~~~~UNITS~~~~~~~~")
print(units)
print("~~~~~~~~~~~PEERS~~~~~~~~")
print(peers)

def test():
    "A set of unit tests."
    assert len(squares) == 16
    assert len(unitlist) == 8
    assert all(len(units[s]) == 2 for s in squares)
    assert all(len(peers[s]) == 6 for s in squares)
    assert units['C2'] == [['A2', 'B2', 'C2', 'D2'],
                           ['C1', 'C2', 'C3', 'C4']]
    assert peers['C2'] == set(['A2', 'B2', 'D2','C1', 'C3', 'C4'])
    print('All tests pass.')
test()
print()
