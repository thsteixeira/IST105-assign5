from django import forms

class PuzzleForm(forms.Form):
    number = forms.IntegerField(label='Enter a number', min_value=1, max_value=100, required=True)
    text = forms.CharField(label='Enter a Text Message', max_length=100, required=True)

class GuessForm(forms.Form):
    guess = forms.IntegerField(label='Enter your guess', min_value=1, max_value=100, required=True)