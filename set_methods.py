st = {1, 2, 3, 4, 5, 6, 7, 8, 9}
other_st = {1, 2, 3, 4, 5, 11, 12}
st.discard(10)  # no error
copied_st = st.copy()  # return shallow copy of set
st.add(10)  # {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
copied_st.update([13, 14, 15], [16, 17, 18, 19])  # Update a set with the union of itself and others
st.update(other_st)  # {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12}
# st.remove(13)  # error
# difference = copied_st.difference(other_st)  # Return the difference of two or more sets as a new set
copied_st.difference_update(other_st)  # Remove all elements of another set from this set
# intersection = copied_st.intersection(other_st)  # Return the intersection of two sets as a new set (i.e. all elements that are in both sets)
# copied_st.intersection_update(other_st)  # Update a set with the intersection of itself and another
print(copied_st)
print(other_st)
copied_st = copied_st.union(other_st)  # Return the union of sets as a new set (i.e. all elements that are in either set)
print(copied_st)
