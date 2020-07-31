from django import forms 
from loanqualification.models import LoanQualification

class LoanQualificationForm(forms.ModelForm):
    class Meta:
        model = LoanQualification
        fields = ['firstname', 'lastname', 'email', 'id_number', 'next_of_kin', 'kra_pin', 'job_done', 'guarantor', 'given_item', 'price_of_item']