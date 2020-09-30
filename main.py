

whileloop=0
while whileloop == 0:
    input('Click Enter to reset and create files')
    file_builder = open("numberslog.txt", "w+")
    def count():
        whilecounting = 1
        while whatnum+1 > whilecounting:
            print(whilecounting)
            file_builder.write(str(whilecounting))
            file_builder.write('\n')
            whilecounting=whilecounting+1
        file_builder.close()


    whatnum=int(input('What num to count up to '))
    shouldstart=input('ok type yes to start(this program will take a while on how big the number is and may lag) ')

    if shouldstart == "yes":
        print ('ok')
        count()
    elif shouldstart == 'no':
        print ('ok will not start')
        exit()
    else:
        print ("Error: could no process value")


