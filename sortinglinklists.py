class ListNode:
    def __init__(self, val = 0, next=None):
        self.val = val
        self.next = next

class Solution:

    def sorting_lists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1: return l2
        if not l2: return l1
        
        dummy = ListNode()
        tail = dummy

        while l1 and l2:
            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next


            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next

        if l1: tail.next = l1
        if l2: tail.next = l2

        return dummy.next

sol_instance = Solution()    

List1 = ListNode(5, ListNode(15, ListNode(25)))
List2 = ListNode(10, ListNode(20, ListNode(30)))

result_list = sol_instance.sorting_lists(List1, List2)

print("Merged List: ", end=" ")

while result_list:
    print(result_list.val, end=" ")
    if result_list.next:
        print("->", end=" ")
    result_list = result_list.next