from math import *


EUR_EEK = input('Kas Sinu summa on eurodes (EUR) või kroonides (EEK)?')
    

summa = input('Sisesta teisendamiseks mõeldud summa:')


if EUR_EEK == 'EUR':
    print ('See teeb ' + str(float(summa) * 15.6466) + ' krooni')
else:
    if EUR_EEK == 'eur':
        print ('See teeb ' + str(float(summa) * 15.6466) + ' krooni')
    else:
        if EUR_EEK == 'EEK':
            print ('See teeb ' + str(float(summa) / 15.6466) + ' eurot')
        else:
            if EUR_EEK == 'eek':
                print ('See teeb ' + str(float(summa) / 15.6466) + ' eurot')
            else:
                print('vale sisend')
