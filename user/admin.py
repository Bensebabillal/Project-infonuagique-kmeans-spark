import csv

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.http import HttpResponse
from django.utils.translation import ugettext_lazy as _
from import_export.admin import ImportMixin

from user.models import CustomUser


class ExportCsvMixin:
    def export_as_csv(self, request, queryset):
        meta = self.model._meta
        field_names = [field.name for field in meta.fields]

        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename={}.csv'.format(meta)
        writer = csv.writer(response)

        writer.writerow(field_names)
        for obj in queryset:
            row = writer.writerow([getattr(obj, field) for field in field_names])

        return response

    export_as_csv.short_description = "Export Selected"


class UserProfileAdmin(UserAdmin, ExportCsvMixin, ImportMixin):
    list_display = ['id', 'username', 'email', 'first_name', 'last_name',
                    'date_joined']
    list_filter = ("email", "first_name",)
    fieldsets = (
        (None, {'fields': ('username', 'email', 'password')}),
        (_('Personal info'),
         {'fields': ('first_name', 'last_name', 'avatar')}),
        (_('Permissions'), {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )

    search_fields = ('email', 'first_name', 'last_name',)

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'username', 'password1', 'password2'),
        }),
    )
    actions = ["export_as_csv", ]
    ordering = ('email',)

    # exclude = ['username']

    class Meta:
        model = CustomUser


admin.site.register(CustomUser, UserProfileAdmin)
