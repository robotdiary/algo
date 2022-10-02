# 연습문제 3
def preorder(root):
    if root:
        ans.append(root)
        preorder(child1[root])
        preorder(child2[root])


def inorder(root):
    if root:
        inorder(child1[root])
        ans.append(root)
        inorder(child2[root])


def postorder(root):
    if root:
        postorder(child1[root])
        postorder(child2[root])
        ans.append(root)


v, e = map(int, input().split())
edges = list(map(int, input().split()))
parent = [0] * (v + 1)
child1 = [0] * (v + 1)
child2 = [0] * (v + 1)
for i in range(0, len(edges), 2):
    # 부모
    parent[edges[i + 1]] = edges[i]
    # 자식
    if not child1[edges[i]]:
        child1[edges[i]] = edges[i + 1]
    else:
        child2[edges[i]] = edges[i + 1]
ans = []
preorder(1)
print('전위 순회 : ', *ans)
ans = []
inorder(1)
print('중위 순회 : ', *ans)
ans = []
postorder(1)
print('후위 순회 : ', *ans)