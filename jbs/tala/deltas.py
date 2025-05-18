
def encode(st: str) -> str:
    if not st:
        return ""
    fst = ord(st[0])
    vals = [fst]
    for s in st[1:]:
        vals.append(fst - ord(s))
    return ' '.join(str(v) for v in vals)

def decode(st: str) -> str:
    if not st:
        return ""
    st = st.split()
    fst = int(st[0])
    vals = [chr(fst)]
    for s in st[1:]:
        vals.append(chr(fst - int(s)))
    return ''.join(str(v) for v in vals)
if __name__ == "__main__":
    assert encode("foo") == "102 -9 -9"
    assert decode("102 -9 -9") == "foo"
    assert encode("") == decode("")
