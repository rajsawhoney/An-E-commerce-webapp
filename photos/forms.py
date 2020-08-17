from django.forms import models
from django import forms
from .models import Photo, Meme

from django.forms.fields import MultipleChoiceField


class CustomModelChoiceIterator(models.ModelChoiceIterator):
    def choice(self, obj):
        return (self.field.prepare_value(obj),
                self.field.label_from_instance(obj), obj)


class CustomModelChoiceField(models.ModelMultipleChoiceField):
    def _get_choices(self):
        if hasattr(self, '_choices'):
            return self._choices
        return CustomModelChoiceIterator(self)
    choices = property(_get_choices, MultipleChoiceField._set_choices)


class Memeform(forms.ModelForm):
    meme = CustomModelChoiceField(widget=forms.CheckboxSelectMultiple,
                                  queryset=Photo.objects.all()
                                  )

    class Meta:
        model = Meme
        fields = ('meme', 'text', 'description',)

        widgets = {
            'text': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Give your article a title...'}),
            'description': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Write here...'}),

        }
