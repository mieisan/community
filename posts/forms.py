from django import forms
from .models import Post


class PostForm(forms.ModelForm):
    tag_names = forms.CharField(
        required=False,
        label="タグ",
        help_text="カンマ区切りで入力 例: Python,Django,Linux"
    )

    class Meta:
        model = Post
        fields = [
            "title",
            "content",
            "image",
        ]
