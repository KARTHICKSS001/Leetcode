
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        arr = []

        # Convert linked list to array
        while head:
            arr.append(head.val)
            head = head.next

        # Sort the array
        arr.sort()

        dummy = ListNode(0)
        cur = dummy

        for num in arr:
            cur.next = ListNode(num)
            cur = cur.next

        return dummy.next
