# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        if len(lists) == 1:
            return lists[0]
        def merge(list1, list2):
            dummy = node = ListNode(0)

            while list1 and list2:
                if list1.val <= list2.val:
                    node.next = list1
                    list1 = list1.next
                    node = node.next
                else:
                    node.next = list2
                    list2 = list2.next
                    node = node.next
            
            node.next = list1 or list2
            return dummy.next
        
        for i in range(1, len(lists)):
            l1, l2 = lists[i - 1], lists[i]
            lists[i] = merge(l1, l2)
        
        return lists[- 1]

