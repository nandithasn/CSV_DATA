from django.shortcuts import render

# Create your views here.

from app.models import *
from django.http import HttpResponse


def insert_data(request):
    with open('C:\\Users\\devuf\\OneDrive\\Desktop\\DJANGO\\nandu\\Scripts\\CSV_DATA\\Business-employment-data-september-2022-quarter-csv.csv','r')as fobj:
        import csv
        GO=csv.reader(fobj)
        next(GO)
        for i in GO:
            MO=BusinessEmployeMentData(Series_reference=i[0],Period=i[1],Data_value=i[2],Suppressed=i[3],STATUS=i[4],UNITS=i[5],Magnitude=i[6],Subject=i[7],Group=i[8],Series_title_1=i[9])
            MO.save()
        
        return HttpResponse('data inserted Successfully')




'''reader function usage
    reader() is used to read the file, which returns 
    an iterable reader object. The reader object is
     then iterated using a for loop to print the 
     contents of each row.
     '''