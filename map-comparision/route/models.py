

# Create your models here.
from django.db import models

import os

from .storage import OverwriteStorage


def actual_path(instance,filename):
    basefilename, file_extension= os.path.splitext(filename)
    str= 'actual'
    return 'images/{string}{ext}'.format(string= str, ext= file_extension)
def expected_path(instance,filename):
    basefilename,file_extension= os.path.splitext(filename)
    str= 'expected'
    return 'images/{string}{ext}'.format(string= str, ext= file_extension)
class Post(models.Model):
    
    Actual = models.ImageField(upload_to=actual_path, storage=OverwriteStorage())
    Expected = models.ImageField(upload_to=expected_path, storage=OverwriteStorage())
    


    






