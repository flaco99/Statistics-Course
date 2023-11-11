original_todolist = input("What is the name of the text file containing an unformatted todo list: ")
output_file_name = input("What is the name of the output file: ")

with open(original_todolist, 'r') as file:
    big_list = file.readlines()

with open(output_file_name, 'w') as file:
    file.write('To-do list\n')
    file.write('\n')
    for line in big_list:
        if not line=='\n':
            first_letter = line[0].upper()
            nice_line = '- '+ first_letter+line[1:]
            file.write(nice_line)