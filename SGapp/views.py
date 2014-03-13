from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.conf import settings

from SGapp.form import MailForm
import sendgrid

def index(request):
    if request.method == 'POST':

        form = MailForm(request.POST)
        if form.is_valid():
            to_mail = str(form.cleaned_data['to_mail'])
            subject_mail = str(form.cleaned_data['subject_mail'])
            content_mail = str(form.cleaned_data['content_mail'])

            sg = sendgrid.SendGridClient(settings.SENDGRID_USERNAME, settings.SENDGRID_PASSWORD)

            message = sendgrid.Mail()
            message.add_to(to_mail)
            message.set_subject(subject_mail)
            message.set_html(content_mail)
            message.set_text(content_mail)
            message.set_from('Nitrous.IO SendGrid <john_doe@example.com>')
            status, msg = sg.send(message)

            if status == 200:
                messages.success(request, 'Your email was successfully sent.')
            else:
                messages.error(request, msg)   
    else:
        form = MailForm()

    return render(request, 'index.html', {
        'form': form,
    })