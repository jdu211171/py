old_dct = dict(Abdugaffor=4, NurIslom=5)
old_dct.update(dict(Abdugaffor=5, NurIslom=3, Munisa=4))
sorted_dct = dict(sorted(old_dct.items(), key=lambda item: item[1], reverse=True))
# copied_dictionary = old_dct.copy()

# old_dct.clear()

# print(old_dct.get('Munisa'))

# print(old_dct.pop('Nur Islom'))

# lowest_grade_student = sorted_dct.popitem()
# print(lowest_grade_student)
# print(sorted_dct)
