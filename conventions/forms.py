from django import forms
from .models import Comment


# create a form for commenting
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text', 'rating']  

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # basic attributes
        self.fields['text'].widget.attrs.update({
            'class': 'form-control',
            'rows': 4,
            'placeholder': 'Write your comment here...'
        })

        # select stars
        self.fields['rating'].widget = forms.Select(choices=[(i, f'{i} Stars') for i in range(1, 6)])
        self.fields['rating'].widget.attrs.update({
            'class': 'form-select',
        })
