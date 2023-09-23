from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

from common.view import TitleMixin
from .forms import OrdersForm


class OrderCreateView(TitleMixin, CreateView):
    template_name = 'orders/order-create.html'
    form_class = OrdersForm
    success_url = reverse_lazy('order-create')
    title = 'Store - Оформление заказов'

    def form_valid(self, form):
        form.instance.initiator = self.request.user
        return super(OrderCreateView, self).form_valid(form)
