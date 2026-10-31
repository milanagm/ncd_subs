# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None: return []

        initial = []
        head = head
        while head.next != []: 
            initial.append(head.value)
            head = head.next
        return reversed(initial)

        
        

        