from allauth.account.adapter import DefaultAccountAdapter


# from allauth_2fa.utils import user_has_valid_totp_device


class CustomUserAdapter(DefaultAccountAdapter):

    def save_user(self, request, user, form, commit=False):
        user = super().save_user(request, user, form, commit)
        data = form.cleaned_data
        # print(request.FILES['document_file'])
        # print(data)
        # user.identity_number = data.get('identity_number')
        # print(user.identity_number, data.get('identity_number'))
        user.first_name = data.get('first_name')
        user.last_name = data.get('last_name')
        # user.document_file = request.FILES['document_file']

        user.save()
        return user
