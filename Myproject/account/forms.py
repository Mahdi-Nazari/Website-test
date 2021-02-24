from django import forms
from .models import User

class ProfileFrom(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user')
        
        super(ProfileFrom, self).__init__(*args, **kwargs)
        
        self.fields['email'].help_text = "example@domain.com"
        
        if not user.is_superuser:
            self.fields['username'].disabled = True
            self.fields['email'].disabled = True
            self.fields['special_user'].disabled = True
            self.fields['is_author'].disabled = True
    
    
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name',
                'special_user', 'is_author']