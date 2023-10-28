arr_inp = input('Default: ')
arr_inp = list(arr_inp)
separated = []

for i in arr_inp:
  if i.strip():
    separated.append(i)

string_list = []
integer_list = []

for i in separated:
  try:
    i = int(i)
    integer_list.append(i)
  except ValueError:
    string_list.append(i)

def toString(n):
  return str(n)

print('\n')
print('String: ', ''.join(sorted(string_list)))
print('Integer: ', ''.join(sorted(map(toString, integer_list))))
