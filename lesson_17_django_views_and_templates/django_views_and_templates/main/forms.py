from django import forms


class SearchServicesForm(forms.Form):
    """
    Form for searching services by customer input
    """
    service_name = forms.CharField(label="Service name", max_length=100)
