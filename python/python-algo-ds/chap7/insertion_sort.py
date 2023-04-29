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


if __name__ == "__main__":
    l = PositionalList()
    l.add_first(1)
    l.add_first(100)
    l.add_first(2)
    l.add_first(3)

    print('size: ', l._size)

    l.print()

    insertion_sort(l)

    l.print()
