from django.shortcuts import render, redirect
from .models import Table
from .forms import TableForm
from datetime import datetime
from reservations.models import Reservation

def table_list(request):
    tables = Table.objects.all()
    if request.method == "POST":
        form = TableForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('table_list')
    else:
        form = TableForm()
    return render(request, "tables/table_list.html", {"tables": tables, "form": form})

def available_tables(request):
    date_str = request.GET.get("date", datetime.today().strftime("%Y-%m-%d"))
    date = datetime.strptime(date_str, "%Y-%m-%d").date()
    
    reserved_tables = Reservation.objects.filter(date=date).values_list("table_id", flat=True)
    tables = Table.objects.exclude(id__in=reserved_tables)
    
    return render(request, "tables/available_tables.html", {"tables": tables, "date": date_str})