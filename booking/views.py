from django.shortcuts import render, redirect
from .models import Repairman, Booking
from django.http import JsonResponse
from django.utils import timezone

# View for the dashboard to search for repairmen
def dashboard(request):
    if request.method == 'POST':
        query = request.POST.get('query')
        repairmen = Repairman.objects.filter(name__icontains=query)
    else:
        repairmen = Repairman.objects.all()

    return render(request, 'booking/dashboard.html', {'repairmen': repairmen})

# View for making a booking
def book_appointment(request, repairman_id):
    repairman = Repairman.objects.get(id=repairman_id)

    if request.method == 'POST':
        customer_name = request.POST['customer_name']
        appointment_date = request.POST['appointment_date']
        customer_location = request.POST['customer_location']

        # Create a new booking
        booking = Booking(
            repairman=repairman,
            customer_name=customer_name,
            appointment_date=appointment_date,
            customer_location=customer_location,
        )
        booking.save()
        return redirect('booking:confirmation', booking_id=booking.id)

    return render(request, 'booking/book_appointment.html', {'repairman': repairman})

# Confirmation page for booking
def booking_confirmation(request, booking_id):
    booking = Booking.objects.get(id=booking_id)
    return render(request, 'booking/confirmation.html', {'booking': booking})


from django.shortcuts import render
from .models import Booking

# View to display the booker's and technician's locations on a map, with directions
def show_location(request, booking_id):
    booking = Booking.objects.get(id=booking_id)
    
    # Split the customer_location into latitude and longitude
    customer_location = booking.customer_location.split(',')
    customer_latitude = customer_location[0]
    customer_longitude = customer_location[1]

    # Fetch the technician's location from the associated repairman
    repairman = booking.repairman

    technician_location = repairman.location.split(',')
    technician_latitude = technician_location[0]
    technician_longitude = technician_location[1]
   

    return render(request, 'booking/show_location.html', {
        'customer_latitude': customer_latitude,
        'customer_longitude': customer_longitude,
        'technician_latitude': technician_latitude,
        'technician_longitude': technician_longitude,
        'booking': booking
    })


