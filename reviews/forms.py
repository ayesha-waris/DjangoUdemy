from django import forms

class ReviewForm(forms.Form):
  user_name = forms.CharField(label="User Name",required=True, max_length=50, error_messages={
    "required": "Please enter your name"
  })
 

