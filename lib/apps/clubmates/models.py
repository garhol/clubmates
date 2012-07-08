from django.db import models
from django.forms import ModelForm

class User(models.Model):
    mail = models.EmailField(max_length=254)   
    
    def __unicode__(self):
        return self.mail

class Location(models.Model):
    parent = models.ForeignKey('self', null=True, blank=True)
    name = models.CharField(max_length=200)
    latitude = models.FloatField(blank = True, null=True)
    longitude = models.FloatField(blank = True, null=True)
    density = models.IntegerField(blank=True, null=True)
    venue = models.BooleanField()
    
    def __unicode__(self):
        return self.name

class LocationForm(ModelForm):
    class Meta:
        model = Location
		
class Message(models.Model):
    user = models.ForeignKey(User)
    location = models.ForeignKey(Location)
    title = models.CharField(max_length=128)
    in_reply_to = models.ForeignKey('self', null=True, blank=True)
    content = models.CharField(max_length=512)
    
    
    def __unicode__(self):
        return self.title

    def is_reply(self):
        return self.reply != null    
