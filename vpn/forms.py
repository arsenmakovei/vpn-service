from django import forms

from vpn.models import Site


class SiteForm(forms.ModelForm):
    """
    Form for creating or updating a site.
    """

    class Meta:
        model = Site
        fields = ("name", "url")
