from django import forms

from noticeboard.models import Notice

class NoticeForm(forms.ModelForm):
    class Meta:
        model = Notice
        fields = ["title", "text"]