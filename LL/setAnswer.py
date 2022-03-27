# from collections import deque

# linked_list = deque()
# linked_list.appendleft(1)
# linked_list.appendleft(2)
# linked_list.appendleft(3)
# linked_list.appendleft(4)

# print(linked_list)


# This is your shopping list in the Set
# After you went to walmart, you bought eggs, ground beef and cucumber.
# The green cabbage and onion were sold out.
# And you also notice that 
item = {"eggs","green cabbage","ground beef","onion","cucumber"}
#####
# Problem there
item.remove("eggs")
item.remove("ground beef")
item.remove("cucumber")
item.add("rice")
item.add("apple")
#####
print(f"This is my new shopping list. {item}")