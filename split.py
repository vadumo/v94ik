def filter_words(st):
    b = st.lower()
    b = b[1::1]
    a = st[0].upper()
    a = ' '.join(a.split())
    b = ' '.join(b.split())
    return a + b