from positional_list import PositionalList


def insertion_sort(L: PositionalList):
    """Sort PositionalList of comparable elements"""
    if len(L) > 1:
        marker = L.first()

        while marker != L.last():
            pivot = L.after(marker)

            value = pivot.element()

            if value > marker.element():  # pivot is already sorted
                marker = pivot  # pivot becomes new marker
            else:
                walk = marker
                while walk != L.first() and L.before(walk).element() > value:
                    walk = L.before(walk)
                L.delete(pivot)
                L.add_before(walk, value)
