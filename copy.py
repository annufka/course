def copy_file(file_name, copy_name=None):
    if copy_name == None:
        copy_name = file_name.replace('.txt', '') + '1' + '.txt'
    file_for_copy = open(file_name, "r")
    file_copy = open(copy_name, "a")
    for line in file_for_copy:
        file_copy.write(line)
    file_for_copy.close()
    file_copy .close()

copy_file("log.txt")
