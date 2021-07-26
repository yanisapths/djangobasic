from django.db import models

# Create your models here. Look for model datatype fieldand how to create--> https://docs.djangoproject.com/en/3.2/ref/models/fields/

#สร้างตารางPost ประกอบไปด้วย2 columns คือ name:มีdatatypeเป็นchar,desc:,มีdatatypeเป็นtext
class Post(models.Model):
    name = models.CharField(max_length=200) #ตั้งชื่อข้อมูลในคอลัมน์nameได้ 200ตัวอักษร
    desc = models.TextField() #ไม่กำหนดความยาว
    
#increamental ID is created automatically, we don't need to do anything about it.
#after created model, use command in terminal  : python manage.py makemigrations nut iit will says no change detected, we have to go to settings.py to specify where to build this migrations file and in thiscase it's in addBlog
#in case we have many apps, we need to tell whether which models will be working with which apps, so they map to each other correctly
#-->settings.py---> add 'blogs' in installed_apps then run ' python manage.py makemigrations'