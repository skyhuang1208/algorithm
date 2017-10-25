def _cal_distance_(p1, p2):
    import math
    sqsum= 0
    for x1, x2 in zip(p1, p2):
        sqsum += (x2-x1)**2
    
    return math.sqrt(sqsum)

def naive_n2_nns(target, points): # nearest-neighbor search
    NNdistance= None
    NNpoint= None
    for pt in points:
        dist= _cal_distance_(target, pt)
        if NNdistance==None or dist < NNdistance:
            NNdistance= dist
            NNpoint= pt
    return NNpoint

def build_kd_tree(points, depth= 0):
    N= len(points)
    if N==0: return None
    K= len(points[0])

    axis= depth % K
    points.sort(key= lambda x: x[axis])

    half= N//2
    return {'point': points[half], 
            'left': build_2d_tree(points[:half], depth+1), 
            'right': build_2d_tree(points[half+1:], depth+1)}

def _nns_(target, root, depth= 0): # nearest-neighbor search
    if root==None:
        return None, None
   
    K= len(root['point'])
    axis= depth % K

    if target[axis] < root['point'][axis]:
        next_branch= root['left']
        opposite_branch= root['right']
    else:
        next_branch= root['right']
        opposite_branch= root['left']

    NNdistance= _cal_distance_(target, root['point'])
    NNpoint= root['point']

    NXTdistance, NXTpoint= _nns_(target, next_branch, depth+1)

    if NXTdistance != None and NXTdistance < NNdistance:
        NNdistance= NXTdistance
        NNpoint= NXTpoint

    if NNdistance > abs(target[axis] - root['point'][axis]):
        OPSTdist, OPSTpoint= _nns_(target, opposite_branch, depth +1)
        if OPSTdist != None and OPSTdist < NNdistance:
            NNdistance= OPSTdist
            NNpoint= OPSTpoint

    return NNdistance, NNpoint

def kdtree_nns(target, tree_root):
    nns= _nns_(target, tree_root)
    return nns[1]
