from django.conf import settings
from django import forms
from django.core.mail import send_mail, get_connection

class ContactForm(forms.Form):
    sender = forms.EmailField(label="", widget=forms.TextInput(attrs={ "id":"email_sender", "placeholder": "Email..." }))
    cc_myself = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={ "id":"email_cc" }))
    subject = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={ "id":"email_subject", "placeholder": "Subject..." }))
    message = forms.CharField(label="", widget=forms.Textarea(attrs={ "id":"email_message", "placeholder": "Your message..." }))

    def send_email(self):
        recipients = ["nadkarsushant@gmail.com"]
        if self.cleaned_data["cc_myself"]:
            recipients.append(self.cleaned_data["sender"])

        if settings.DEBUG:
            con = get_connection('django.core.mail.backends.console.EmailBackend')
        else:
            con = None

        send_mail(
            self.cleaned_data["subject"],
            self.cleaned_data["message"],
            self.cleaned_data["sender"],
            recipients,
            fail_silently=True,
            connection=con,
        )