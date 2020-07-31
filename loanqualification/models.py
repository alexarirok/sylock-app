from django.db import models

class LoanQualification(models.Model):
    firstname = models.CharField(max_length=30, help_text='optional')
    lastname = models.CharField(max_length=30, help_text='optional')
    email = models.EmailField(max_length=100, help_text='required')
    id_number = models.IntegerField( help_text='required')
    next_of_kin = models.CharField(max_length=100, help_text='optional')
    kra_pin = models.CharField(max_length=100, help_text='required')
    job_done = models.CharField(max_length=255, help_text='optional')
    guarantor = models.CharField(max_length=255, help_text='optional')
    given_item = models.CharField(max_length=255, help_text='optional')
    price_of_item = models.CharField(max_length=255, help_text='optional') 

    def __str__(self):
        return f"My name is {self.name}"