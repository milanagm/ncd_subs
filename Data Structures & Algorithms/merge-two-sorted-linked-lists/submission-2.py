# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 and list2: 
            current_head = min(list1, list2) #greift er dann auf list.val zu? 
        elif list1 and not list2:
            current_head = list1
        else:
            current_head = list2
        start_head = current_head

        while list1 and list2: 
            next_min = min(list1.next, list2.next)
            current_head.next = next_min
            if current_head == list1.next: 
                list1 = list1.next
            else: 
                list2 = list2.next
        if list1 and not list2: 
            current_head.next = list1
        else:
            current_head.next = list2

        return start_head
        
        