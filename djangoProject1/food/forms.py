from django import forms


# Create your form here
from food.models import Food, CommentsOfFood


class FoodForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for (_, field) in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = Food
        fields = '__all__'


class CommentsOfFoodForm(forms.ModelForm):
    class Meta:
        model = CommentsOfFood
        fields = ('text',)
        widgets = {
            'text': forms.Textarea(
                attrs={
                    'class': 'form-control rounded-2',
                    'is_required': True,
                },
            ),
        }
