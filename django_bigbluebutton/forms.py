from django import forms


class MeetingCreateLinkForm(forms.Form):
    fullname = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    USER_TYPES = (
        ('moderator', 'Moderator'),
        ('attendee', 'Attendee')
    )
    user_type = forms.ChoiceField(
        required=True,
        choices=USER_TYPES,
    )

    def create_link(self, meeting):
        fullname = self.cleaned_data.get('fullname')
        email = self.cleaned_data.get('email')
        user_type = self.cleaned_data.get('user_type', 'attendee')
        return meeting.create_join_link(fullname, user_type,email)
