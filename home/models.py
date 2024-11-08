from django.db import models
import uuid
from django.contrib.auth.models import User

# Create your models here.
class YoutubeVideo(models.Model):
    video = models.FileField(upload_to = "youtube")

class BaseModel(models.Model):

    # class meta is a inner class or skeleton class which have some attributes which are use to define the strucure of class.
    # -> attribute -> abstract, verbose_name, plural_name , proxy_class or not.

    class Meta:
        # it means consider the basemodel as abstract class, which means you can't create it's object
        # or it is use as a skeleton using which you can make other classes
        abstract = True
    
    uid = models.UUIDField( primary_key = True,
                            default = uuid.uuid4,
                            editable = False)
    created_at = models.DateTimeField(auto_now_add = True)

# because here i am trying to define a relationship from color_code to people, trying to find 
# the people with specific color, by making the object of Colors, but maybe it is not working because it is related
#  by manytomany field, not by foreign key.

class Colors(BaseModel):
    color_code = models.CharField(max_length = 100)

# What does it mean by manytomany field, if multiple logo ke paas same color nahi ho sakta, or how exactly many to many 
# field works or is working here?

class People(BaseModel):
    name = models.CharField(max_length = 100)
    about = models.TextField()
    age = models.IntegerField()
    email = models.EmailField()
    colors = models.ManyToManyField(Colors)

class PeopleAddress(BaseModel):
    
    # related name is saying that if address exist then it is of any people, related to any people/person

    # *** THINGS WE CAN DO ON DELETION/OR AFTER DELETION ***
    # models.CASCADE -> IF YOU DELETE ANY RECORD IF PARENT TABLE, THEN ALSO DELETE THE CORRESPONDING RECORD IN THE CHILD TABLE,
    # IN ORDER TO MAINTAIN REFERENTIAL INTEGRITY CONSTRAINT.

    # models.SET_NULL
    # WHEN YOU DELETE ANY RECORD IN PARENT TABLE THEN SET NULL TO THE FOREIGN KEY COLUMN OF CHILD TABLE

    # models.SET_DEFAULT
    # WHEN YOU DELETE ANY RECORD IN PARENT TABLE THEN SET DEFAULT (ANY DEFAULT) VALUE TO THE FOREIGN KEY OF CHILD TABLE
    
    
    people = models.ForeignKey(People, on_delete = models.CASCADE, related_name = "address", )
    address = models.TextField()