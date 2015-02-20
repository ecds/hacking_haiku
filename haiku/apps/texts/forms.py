from django import forms
from haiku.apps.texts.models import Work, Verse


class WorkForm(forms.ModelForm):
    class Meta:
        model = Work

        widgets = {
            'authors': forms.SelectMultiple(attrs={'style': "width:482px",
                                                    'width' : '482px'}),
            'notes': forms.Textarea(attrs={'style': "width:850px",
                                                    'width' : '850px'}),
        }
      

class VerseForm(forms.ModelForm):
    class Meta:
        model = Verse

        widgets = {
            'other_works': forms.SelectMultiple(attrs={'style': "width:482px",
                                                    'width' : '482px'}),
            'encounters': forms.SelectMultiple(attrs={'style': "width:482px",
                                                    'width' : '482px'}),
            'structures': forms.SelectMultiple(attrs={'style': "width:482px",
                                                    'width' : '482px'}),
            'cities': forms.SelectMultiple(attrs={'style': "width:482px",
                                                    'width' : '482px'}),
            'allusions': forms.SelectMultiple(attrs={'style': "width:482px",
                                                    'width' : '482px'}),
            'notes': forms.Textarea(attrs={'style': "width:850px",
                                                    'width' : '850px'}),
            'japanese_text': forms.TextInput(attrs={'style': "width:850px",
                                                    'width' : '850px'}),
            'english_text': forms.Textarea(attrs={'style': "width:850px",
                                                    'width' : '850px'}),
            'romanization': forms.Textarea(attrs={'style': "width:850px",
                                                    'width' : '850px'}),

        }
        
class KigoForm(forms.ModelForm):
    class Meta:
        model = Work

        widgets = {
            'authors': forms.SelectMultiple(attrs={'style': "width:482px",
                                                    'width' : '482px'}),
            'notes': forms.Textarea(attrs={'style': "width:850px",
                                                    'width' : '850px'}),
        }
