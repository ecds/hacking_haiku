from django import forms
from haiku.apps.people.models import Person, Group

class PersonForm(forms.ModelForm):
    class Meta:
        model = Person

        widgets = {
            'dwelling': forms.SelectMultiple(attrs={'style': "width:482px",
                                                    'width' : '482px'}),
            'schools': forms.SelectMultiple(attrs={'style': "width:482px",
                                                    'width' : '482px'}),
            'notes': forms.Textarea(attrs={'style': "width:850px",
                                                    'width' : '850px'}),

        }

class GroupForm(forms.ModelForm):
    class Meta:
        model = Group

        widgets = {
            'location': forms.Select(attrs={'style': "width:482px",
                                                    'width' : '482px'}),
            'notes': forms.Textarea(attrs={'style': "width:850px",
                                                    'width' : '850px'}),
                                 
        }
