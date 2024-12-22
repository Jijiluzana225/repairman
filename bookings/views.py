from django.shortcuts import render, redirect
from .models import Repairman, Appointment
from .forms import AppointmentForm
# from django.contrib.gis.geoip2 import GeoIP2
# from django.contrib.gis.geos import Point

def repairman_search(request):
    repairmen = Repairman.objects.all()
    return render(request, 'bookings/repairman_search.html', {'repairmen': repairmen})

def book_appointment(request, repairman_id):
    repairman = Repairman.objects.get(id=repairman_id)
    
    if request.method == "POST":
        form = AppointmentForm(request.POST)
        if form.is_valid():
            location = form.cleaned_data['location']
            latitude = request.POST.get('latitude')
            longitude = request.POST.get('longitude')
            
            appointment = form.save(commit=False)
            appointment.repairman = repairman
            appointment.location = f"{latitude}, {longitude}"  # Save GPS coordinates
            appointment.save()
            return redirect('appointment_detail', appointment_id=appointment.id)
    else:
        form = AppointmentForm()

    return render(request, 'bookings/book_appointment.html', {'repairman': repairman, 'form': form})



from geopy.geocoders import Nominatim

def get_location_from_gps(request):
    # Example of getting the user's location based on a specific address
    geolocator = Nominatim(user_agent="repair_booking")
    location = geolocator.geocode("User current location address or GPS coordinates")
    if location:
        return location.latitude, location.longitude
    return None