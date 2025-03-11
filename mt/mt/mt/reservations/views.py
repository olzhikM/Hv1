from django.shortcuts import render, redirect, get_object_or_404
from .models import Reservation
from .forms import ReservationForm, ReservationStatusForm

def reservation_list(request):
    reservations = Reservation.objects.all()
    if request.method == "POST":
        form = ReservationForm(request.POST)
        if form.is_valid():
            customer = form.cleaned_data["customer"]
            table = form.cleaned_data["table"]
            date = form.cleaned_data["date"]
            
            if Reservation.objects.filter(table=table, date=date).exists():
                form.add_error('table', "Данный стлик уже забронирован")
            elif Reservation.objects.filter(customer=customer, date=date).exists():
                form.add_error("customer", "Данный клиент уже забронировал стлик")
            else:
                form.save()
                return redirect('reservation_list')
    else:
        form = ReservationForm()
        
    return render(request, 'reservations/reservation_list.html', {"reservations": reservations, "form": form})

def reservation_detail(request, id):
    reservation = get_object_or_404(Reservation, id=id)
    return render(request, "reservations/reservation_detail.html", {"reservation": reservation})

def reservation_update(request, id):
    reservation = get_object_or_404(Reservation, id=id)
    if request.method == "POST":
        form = ReservationStatusForm(request.POST, instance=reservation)
        if form.is_valid():
            form.save()
            return redirect('reservation_list')
    else:
        form = ReservationStatusForm(instance=reservation)
        
    return render(request, "reservations/reservation_update.html", {'form': form, 'reservation': reservation})

def reservation_delete(request, id):
    reservation = get_object_or_404(Reservation, id=id)
    if request.method == "POST":
        reservation.delete()
        return redirect("reservation_list")
    return render(request, 'reservations/reservation_delete.html', {'reservation': reservation})