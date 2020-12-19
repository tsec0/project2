from django import forms


# Create your form here
from userfeedback.models import UserFeedBack


class UserFeedBackForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for (_, field) in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = UserFeedBack
        exclude = ('publisher',)
