# Set
## Introduction:
The Set data structure is an example of which order is not important. Sets are used to store multiple items in a single variable. Set is able to add, remove, and test for membership in O(1) time. Since Sets are unordered, the order is not important. The output may always look different when you print it, but all of the outputs are considered as the same.
Function|Description|Python Code|Performance
-|-|-|-
Add|Add "value" to the set|my_set.add(value)|O(1)
Remove|Removes the "value" from the set|my_set.remove(value)|O(1)
Member|Determines if "value" is in the set|if value in my_set:|O(1)
Size|Returns the number of items in the set|length = len(my_set)|O(1)

## Example of Set:
How to print a list of set
```python
a_set = {"a","a","b","b","b","c",1,2,2}
print(a_set) # output might be different.

```
Outputs:
```python
{'c', 1, 2, 'b', 'a'}
```
Example for add and remove the Set
```python
one_set = {1,2,3,4,5}
one_set.remove(1)
one_set.remove(3)
one_set.remove(5)
print(one_set)
one_set.add(6)
one_set.add(8)
one_set.add(10)
print(one_set)
```
Output:
```python
{2, 4}
{2, 4, 6, 8, 10}
```
According to the example, we can see the output does not contain any same values, and the set is unordered as well.
## Practice and challenge:
Practice: This is your shopping list in the Set(egg, green cabbage, ground beef, onion and cucumber). You went to walmart, you bought eggs, ground beef and cucumber. The green cabbage and onion were sold out. You also notice that next time you need to buy rice and apple. What would your new shopping list looks like in the Set.
```python
item = {"eggs","green cabbage","ground beef","onion","cucumber"}
###############
# Start there #
###############




#######
# End #
#######

print(f"This is my new shopping list. {item}")
# Answer :
# This is my new shopping list. {'rice', 'apple', 'green cabbage', 'onion'}
# The output might be different.
```
## Answer:
[here](LL/setAnswer.py)
***
[back to title page](https://github.com/ListenOne1/cse212-final-project/blob/main/README.md#programming-with-data-structures-python)
