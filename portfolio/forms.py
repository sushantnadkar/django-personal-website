from django import forms

class ContactForm(forms.Form):
    sender = forms.EmailField(widget=forms.TextInput(attrs={ "id":"email_sender" }))
    cc_myself = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={ "id":"email_cc" }))
    subject = forms.CharField(max_length=100, widget=forms.TextInput(attrs={ "id":"email_subject" }))
    message = forms.CharField(widget=forms.Textarea(attrs={ "id":"email_message" }))

    def send_email(self):
        print(self.changed_data[0])