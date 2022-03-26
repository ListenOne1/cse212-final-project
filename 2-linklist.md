# Linked list
## Introduction:
Linked list is organized and store the data in the random way with in memory, so the data is not next to each other. In order to organized the data, linked list use **node** and **pointer** to organized data. each element is a node. We use thre pointer to point to next value.

![imagine]()

The first node in the linked list is **Head**, the node at the end of the linked list we called **Tail**
Function|Description|Python Code|Performance
-|-|-|-
insert_head(value)|Adds "value" before the head|my_deque.appendleft(value)|O(1)
insert_tail(value)|Adds "value" after the tail|my_deque.append(value)|O(1)
insert(i, value)|Adds "value" after node i|my_deque.insert(i, value)|O(n)

Remove_head(value)|Remove "value" before the head|my_deque.popleft(value)|O(1)
Remove_tail(value)|Remove "value" after the tail|my_deque.pop(value)|O(1)
Remove(i, value)|Remove "value" after node i|my_deque.deque(i, value)|O(n)

Size|Returns the number of items in the linked list|length = len(my_deque)|O(1)
Empty()|Returns true if the length if the linked list is zero|if len(my_deque)==0:|O(1)
