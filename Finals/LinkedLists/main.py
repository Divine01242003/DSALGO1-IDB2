# Mahusay, Divine Mars G
#11/22/2024
# IDB2 DSALGO1
# Finals Activity #2

from LinkedStack import LinkedStack as Stack, into_postfix
from PositionalList import PositionalList as PositionalList


#1 Infix to Postfix
S = Stack()
print("Problem No. 1")
print()
infix_expression = input("Enter an Arithmetic expression: ")

postfix_expression = into_postfix(infix_expression)

print(f"PostFix Expression in order: {postfix_expression}")

print()

#2 Sort positional list
print("Problem No. 2")
P = PositionalList()

numbers = [1, 72, 81, 25, 65, 91, 11]
for number in numbers:
    P.add_last(number)

# Define the insertion sort function (ascending order)
def insertion_sort(L):
    """Sort the PositionalList in ascending order using insertion sort."""
    if len(L) > 1:
        marker = L.first()
        while marker != L.last():
            pivot = L.after(marker)
            value = pivot.element()
            if value >= marker.element():
                marker = pivot
            else:
                walk = marker
                while walk != L.first() and L.before(walk).element() > value:
                    walk = L.before(walk)
                L.delete(pivot)
                L.add_before(walk, value)

# Define the insertion sort function (descending order)
def insertion_sort_descending(L):
    """Sort the PositionalList in descending order using insertion sort."""
    if len(L) > 1:
        marker = L.first()
        while marker != L.last():
            pivot = L.after(marker)
            value = pivot.element()
            if value <= marker.element():
                marker = pivot
            else:
                walk = marker
                while walk != L.first() and L.before(walk).element() < value:
                    walk = L.before(walk)
                L.delete(pivot)
                L.add_before(walk, value)
                
# Ascending order
insertion_sort(P)
print("Ascending order:")
print("")
for x in P:
    print(x, end=" ")
print()

# Descending order
insertion_sort_descending(P)
print("Descending order:")
print("")
for x in P:
    print(x, end=" ")
print()