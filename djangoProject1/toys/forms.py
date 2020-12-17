from django import forms

from toys.models import Toys, CommentsOfToys


class ToysForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for (_, field) in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = Toys
        fields = '__all__'


class CommentsOfToysForm(forms.ModelForm):
    class Meta:
        model = CommentsOfToys
        fields = ('text',)
        widgets = {
            'text': forms.Textarea(
                attrs={
                    'class': 'form-control rounded-2',
                    'is_required': True,
                },
            ),
        }
