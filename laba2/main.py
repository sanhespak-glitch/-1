from typing import Tuple
Result=Tuple[int,int]
def _validate_inputs(target:int,low,high):
    if low>high:
        raise ValueError("invalide range")
    if not(low<=target<=high):
        raise ValueError("target must be within")
def guess_number(target:int,low,high)->Result:
    _validate_inputs(target,low,high)
    attempts=0
    left,right=low,high
    while left <= right:
        attempts+=1
        mid=(left+right)//2
        if mid==target:
            return mid, attempts
        if mid<target:
            left=mid+1
        else:
            right=mid-1
