waiting_list =sorted(['sen','ben','john'])
for index,i in list(enumerate(sorted(waiting_list))):
    print(f"{index+1}.{i.capitalize()}")

waiting_list = ['sen', 'ben', 'john']
formatted_list = [f"{index + 1}.{name.capitalize()}" for index, name in enumerate(sorted(waiting_list))]
print('\n'.join(formatted_list))

for i, j in enumerate("abcd"):
    print(i + 1,j)

buttons = [('John', 'Sen', 'Morro'), ('Lin', 'Ajay', 'Filip')]
for first, second, third in buttons:
    print(first, second)