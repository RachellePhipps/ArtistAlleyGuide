from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text', 'rating']  

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['text'].widget.attrs.update({
            'class': 'form-control',
            'rows': 4,
            'placeholder': 'Write your comment here...'
        })

        self.fields['rating'].widget = forms.Select(choices=[(i, f'{i} Stars') for i in range(1, 6)])
        self.fields['rating'].widget.attrs.update({
            'class': 'form-select',
        })
