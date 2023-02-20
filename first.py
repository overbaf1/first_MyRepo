    import tabula
    myfile = 'price.pdf'
    tabula.convert_into(myfile,'newFile.csv')
    print('Преобразование прошло успешно')
