marks = {"Physics": 678, "Maths": 90}

internal_marks = {'Practical':100}

marks.update(internal_marks)
marks.update({'example':100})

# print(marks)
print(len(marks))
# print(marks.get('example'))
# print(marks.keys())
# print(marks.values())
#print(marks.items())

print(marks.pop('example'))
print(len(marks))


marks.clear()
print(len(marks))
