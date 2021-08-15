from django.shortcuts  import render  
from ARIA_INFOTECH import contactformemail
from django.core.mail import send_mail

def contactsendemail(request):
    if request.method == 'GET':
        form = contactformemail()
         else:
             form = contactformemail(request.POST )
             if form.is_valid():
                 name = form.cleaned_data[' name']
                 email = form.cleaned_data[ ' email ']
                 message = form.cleaned_data [ ' meassage ']
                 send_mail(name , email , message , ['arijitnegative009@gmail.com' , email])
        return render(request, 'index.html' , {'form': form })