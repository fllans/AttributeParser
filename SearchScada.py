import glob
#qwerty = glob.glob('D:/*/*me*')
#print(qwerty)



import os
#import datetime
#def modification_date(filename):
#    t = os.path.getmtime(filename)
#    return datetime.datetime.fromtimestamp(t)
#print (modification_date("D:/pmsm_ideal.mdl"))



testpath = input('D:/pmsm_ideal.mdl')
 

print(os.path.isfile(testpath))


import exifread
 
 
def is_lzw(filename):
    with open(filename, 'rb') as f:
        return 'LZW' in exifread.process_file(f)['Image Compression'].printable
 
print(is_lzw('D:/pmsm_ideal.mdl'))
