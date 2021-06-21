
from django.db import models

# Create your models here.


class Person(models.Model): 
    first_name = models.CharField("First Name", max_length=40, blank=True, null=True)
    last_name = models.CharField("Last Name", max_length=40, blank=True, null=True)
    date_of_birth = models.DateField("Date", max_length=8)
    
    class Meta:  
        db_table = "Person"

    def __str__(self):
        return self.first_name + ', ' + self.last_name
        


class Referral(models.Model):
    referrer = models.CharField("Referrer", max_length=40)
    referral_date = models.DateField("Referral Date", max_length=8)
    note = models.TextField("Text")
    person = models.ForeignKey(Person, on_delete=models.CASCADE);
    
    class Meta:  
        db_table = "Referral"  

    # def __str__(self):
    #     return self.referrer




        


    

