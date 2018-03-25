from django import forms
from models import UserDB

class NameForm(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=100)

# class AccountInfo(forms.ModelForm):
#     class Meta:
#         model = UserDB
#         fields = ('user_first_name', 'user_last_name', 'user_email',
#                   'user_phone',)
