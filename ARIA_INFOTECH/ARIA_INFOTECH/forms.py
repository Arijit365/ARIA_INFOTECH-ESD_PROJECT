from django import forms
 # define a class of contactpage object
 
class contactformemail(forms.form):
  name = forms.CharField( max_length= 70, required=True)
email = forms.EmailField( require=true)
meassage = forms.forms.CharField( widget = forms.Textarea , max_length= 2000, required=true)
    