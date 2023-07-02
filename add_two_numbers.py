# Definition for singly-linked list.
class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

class Solution:

    @staticmethod
    def getNumber(l):
        p, num, ctr = l, 0, 0
        while p is not None:
            num = p.val * (10 ** ctr) + num
            p = p.next
            ctr += 1
        return num

    @staticmethod
    def makeLinkedList(num):
        val = num
        head, curr = None, None
        if val:
            while val:
                digit = val % 10
                if head is None:
                    head = ListNode(digit)
                    curr = head
                else:
                    newNode = ListNode(digit)
                    curr.next = newNode
                    curr = newNode
                val = val // 10
        else:
            head = ListNode()
        return head

    def addTwoNumbers(self, l1, l2):
        num1, num2 = self.getNumber(l1), self.getNumber(l2)
        return self.makeLinkedList(num1 + num2)


