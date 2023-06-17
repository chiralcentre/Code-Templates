def get_bit(num, bit):
    temp = (1 << bit) & num
    return 0 if temp == 0 else 1
        
def get_all_subsets(v, sets):
    for i in range(1 << len(v)):
      st = []
      for j in range(len(v)):
         if get_bit(i, j) == 1:
            st.append(v[j])
      sets.append(st)
