class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

def merge_sorted_lists(headA, headB):
    dummy = ListNode()
    current = dummy

    while headA is not None and headB is not None:
        if headA.value < headB.value:
            current.next = headA
            headA = headA.next
        else:
            current.next = headB
            headB = headB.next
        current = current.next

    if headA is not None:
        current.next = headA
    elif headB is not None:
        current.next = headB

    return dummy.next

def print_linked_list(head):
    while head is not None:
        print(head.value)
        head = head.next
n1 = int(input())
values1 = [int(input()) for _ in range(n1)]

n2 = int(input())
values2 = [int(input()) for _ in range(n2)]

# Create linked lists
headA = ListNode(values1[0])
currentA = headA
for value in values1[1:]:
    currentA.next = ListNode(value)
    currentA = currentA.next

headB = ListNode(values2[0])
currentB = headB
for value in values2[1:]:
    currentB.next = ListNode(value)
    currentB = currentB.next

# Merge and print result
result_ex1 = merge_sorted_lists(headA, headB)
print_linked_list(result_ex1)
