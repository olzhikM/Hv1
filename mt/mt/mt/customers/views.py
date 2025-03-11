from django.shortcuts import render, redirect, get_object_or_404
from .models import Customer
from .forms import CustomerForm

def customer_list(request):
    customers = Customer.objects.all()
    if request.method == "POST":
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("customer_list")
    else:
        form = CustomerForm()
    return render(request, "customers/customer_list.html", {"customers": customers, "form": form})

def customer_detail(request, id):
    customer = get_object_or_404(Customer, id=id)
    return render(request, "customers/customer_detail.html", {"customer": customer})
