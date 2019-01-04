from zipfile import ZipFile

if __name__ == '__main__':
    print '04 Unzip file\n'
    pwd = ''
    found = False
    try:
        with open('english.txt', 'rU') as infile:
            wordSet = set(line.strip() for line in infile)
    except IOError:
        print 'error opening file'

    for word in wordSet:
        if found == False:
            try:
                with ZipFile('test_zip.zip') as zf:
                    print "trying word: ", word
                    zf.extractall(pwd=word)
                    pwd = word
                    found = True

            except:
                print 'error opening file'

    print "password: ", pwd
