from django.views.generic import View,TemplateView,ListView,DetailView,CreateView,DeleteView,UpdateView
from bills.models import Category,Creditor,PaymentMethod,PaymentProvider,Schedule
from django.urls import reverse,reverse_lazy

# INDEX VIEW
class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Home Page"
        return context

# LIST VIEWS
class CreditorListView(ListView):
    context_object_name = 'creditors'
    model = Creditor
    template_name = 'bills/creditor_list.html'

class CategoryListView(ListView):
    context_object_name = 'categories'
    model = Category
    template_name = 'bills/category_list.html'

class PaymentMethodListView(ListView):
    context_object_name = 'methods'
    model = PaymentMethod
    template_name = 'bills/payment_method_list.html'

class PaymentProviderListView(ListView):
    context_object_name = 'providers'
    model = PaymentProvider
    template_name = 'bills/payment_provider_list.html'

class ScheduleListView(ListView):
    context_object_name = 'schedules'
    model = Schedule
    template_name = 'bills/schedule_list.html'

# CREATE VIEWS
class CreditorCreateView(CreateView):
    fields = '__all__'
    model = Creditor

# DELETE VIEWS
class CreditorDeleteView(DeleteView):
    model = Creditor
    success_url = reverse_lazy("bills:creditors")

# UPDATE VIEWS
class CreditorUpdateView(UpdateView):
    fields = '__all__'
    model = Creditor

# DETAIL VIEWS
class PaymentMethodDetailView(DetailView):
    context_object_name = 'payment_method_detail'
    model = PaymentMethod
    template_name = 'bills/payment_method_detail.html'

class CreditorDetailView(DetailView):
    context_object_name = 'creditor_detail'
    model = Creditor
    template_name = 'bills/creditor_detail.html'
