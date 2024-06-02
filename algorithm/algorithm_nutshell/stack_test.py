from stack import Stack

st = Stack()
if st.isEmpty():
    print('stack is empty')

st.push(22)
print(st)
st.push(45)
st.push(78)
print(st)
st.pop()
print(st)