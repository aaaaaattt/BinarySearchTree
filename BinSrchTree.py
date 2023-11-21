class BSTNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.left = None
        self.right = None

#탐색연산(순환 구조)
def search_bst(n,key) : #key값이 찾으려는 값 , n은 root노드
    if n == None :
        return None
    elif key == n.key:
        return n
    elif key < n.key :
        return search_bst(n.left, key)
    else:
        return search_bst(n.right, key)

#탐색연산(반복 구조)
def search_bst_iter(n,key) :
    while n != None :
        if key == n.key:
            return n
        elif key < n.key:
            n = n.left
        else:
            n = n.right
    return None         #찾는 키의 노드가 없으면 None반환


#최대와 최소 키를 가지는 노드 탐색 연산(반복 구조)
def search_max_bst(n):
    while n != None and n.right != None:
        n = n.right
    return n

def search_min_bst(n) :
    while n != None and n.left != None:
        n = n.left
    return n