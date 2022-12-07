from positional_list import PositionalList

def max(l: PositionalList):
    if l.is_empty():
        return None

    result = l.first().element()

    for e in l:
        if e > result:
            result = e
            
    return result

if __name__ == "__main__":
    l = PositionalList()
    l.add_first(1)
    l.add_first(2)
    l.add_first(7)
    l.add_first(4)

    print(max(l))
    print(l.max())

