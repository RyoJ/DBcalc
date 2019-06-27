from django import forms


class ANSForm(forms.Form):
    answer = forms.IntegerField(
        label='answer',
        required=True,
        #widget=forms.TextInput() #数値の場合は必要ない？
    )