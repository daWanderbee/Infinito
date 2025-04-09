from django.shortcuts import render, redirect
from .forms import StudentRegistrationForm
from django.db.models import Q
from .models import Student
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def register_student(request):
    if request.method == 'POST':
        form = StudentRegistrationForm(request.POST)
        if form.is_valid():
            registration = form.save()
            
            # Save registration data to session for the success page
            request.session['registration_data'] = {
                'id': registration.id,
                'name': registration.name,
                'game_playing': registration.game_playing
            }
            
            return redirect('success')
    else:
        form = StudentRegistrationForm()
    
    return render(request, 'registration_form.html', {'form': form})
def success(request):
    # Get the latest registration for this user (you might need to adjust this logic)
    registration = request.session.get('registration_data', None)
    
    # If there's no registration data in the session (direct access to success page)
    if not registration:
        # You could redirect to home or get the latest registration for this user
        # This is just a fallback option
        return redirect('register')  # or handle as appropriate
        
    return render(request, 'success.html', {'registration': registration})

def registrations_list(request):
    registrations_list = Student.objects.all().order_by('-id')  # Most recent first
    
    # Search functionality
    search_query = request.GET.get('search', '')
    if search_query:
        registrations_list = registrations_list.filter(
            Q(name__icontains=search_query) | 
            Q(registration_number__icontains=search_query) |
            Q(vit_email__icontains=search_query) |
            Q(phone__icontains=search_query) |
            Q(game_playing__icontains=search_query)
        )
    
    # Pagination
    page = request.GET.get('page', 1)
    paginator = Paginator(registrations_list, 10)  # Show 10 registrations per page
    
    try:
        registrations = paginator.page(page)
    except PageNotAnInteger:
        registrations = paginator.page(1)
    except EmptyPage:
        registrations = paginator.page(paginator.num_pages)
    
    context = {
        'registrations': registrations,
        'total_count': registrations_list.count(),
        'search_query': search_query,
    }
    
    return render(request, 'registrations_list.html', context)