class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def reverseList(head, length, k):
            if length < k:
                return head
            pre = None
            mid = head
            after = None
            count = 0
            while mid and count < k:
                after = mid.next
                mid.next = pre
                pre = mid
                mid = after
                count += 1
            if mid:
                head.next = reverseList(mid, length - k, k)
            return pre

        if (not head and not head.next) or k == 1:
            return head

        # get the length of the linked list
        length = 0
        temp = head
        while temp:
            length += 1
            temp = temp.next

        return reverseList(head, length, k)