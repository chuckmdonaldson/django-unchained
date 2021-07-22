from django import forms
from bills.models import Category,Creditor,PaymentMethod,PaymentProvider,Schedule

class AddCategoryForm(forms.ModelForm):
    class Meta():
        model = Category
        fields = '__all__'

class AddCreditorForm(forms.ModelForm):
     class Meta():
         model = Creditor
         fields = '__all__'

class AddPaymentMethodForm(forms.ModelForm):
    exp_date = forms.DateField(widget=forms.SelectDateWidget())

    class Meta():
        model = PaymentMethod
        fields = '__all__'

class AddPaymentProviderForm(forms.ModelForm):
    class Meta():
        model = PaymentProvider
        fields = '__all__'

class AddScheduleForm(forms.ModelForm):
    class Meta():
        model = Schedule
        fields = '__all__'
