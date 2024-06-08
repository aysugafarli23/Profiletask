from django import forms
from .models import Profile


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'
        
    def __init__(self, *args, **kwargs):
       super().__init__(*args, **kwargs)
       
       print(*args, **kwargs)
       for field in self.fields.values():
           field.widget.attrs['class'] = 'form-control'