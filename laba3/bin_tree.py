from __future__ import annotations
from typing import TypedDict
class Node(TypedDict,total=False):
    value: int|float
    left: Node|None
    right: Node|None
def _left(root):
    return 2-(root-1)
def _right(root):
    return root*2
def bintree(height,root) -> Node:
    def build(x,level) -> Node:
        node:Node={"value":x,"left":None,"right":None}
        if level==1:
            return node
        node["left"]=build(_left(x),level-1)
        node["right"] = build(_right(x), level - 1)
        return node
    return build(root,height)
print(bintree(4,14))



