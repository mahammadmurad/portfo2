from django import forms

class ContactForms(forms.Form):
    name = forms.CharField(
        widget=forms.TextInput(
            attrs={'class':'form-control', 'placeholder': 'name'}
        )
    )
    
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={'class':'form-control', 'placeholder': 'email'}
        )
    )
    
    message = forms.CharField(
        widget=forms.TextInput(
            attrs={'class':'form-control', 'placeholder': 'message'}
        )
    )
    
    # class Meta:
    #     model = Contact
    #     fields = ['name', 'email', 'message']