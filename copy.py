def copy_file(file_name, copy_name=None):
    #Если имя файла не задано
	if copy_name == None:
		#убираем расширение с названия, прибавляем "1" и добавляем расирение
        copy_name = file_name.replace('.txt', '') + '1' + '.txt'
    #откроем первый файл для чтения и создадим второй
	file_for_copy = open(file_name, "r")
    file_copy = open(copy_name, "a")
    #берем строку из исходного файла и добаим в новый файл
	for line in file_for_copy:
        file_copy.write(line)
	#закроем файлы
    file_for_copy.close()
    file_copy .close()

copy_file("log.txt")
