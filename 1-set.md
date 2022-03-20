# Set
## Introduction:
The set data structure is an example of one for which order is not important. The set allow no duplicates. The set is able to add, remove, and test for memnership in O(1) time.
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
Example:
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
## Answer: