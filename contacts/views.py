from django.shortcuts import redirect
from django.contrib import messages
from .models import Contact

def contacts(request):
    if request.method == 'POST':
        user_id = request.POST['user_id']
        realtor_email = request.POST['realtor_email']
        listing_id = request.POST['listing_id']
        listing = request.POST['listing']
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']

        if request.user.is_authenticated:
            has_contacted = Contact.objects.all().filter(user_id=user_id, listing_id=listing_id)
            if has_contacted:
                messages.add_message(request, messages.ERROR, 'You made an enquiry for this listing earlier')
                return redirect('/listings/' + listing_id)

        contact = Contact(listing_id=listing_id, user_id=user_id,message=message,email=email,phone=phone,listing=listing,name=name)
        contact.save()
        messages.add_message(request, messages.SUCCESS, 'Your request has been submitted, a realtor will contact you soon')
        return redirect('/listings/' + listing_id)
    return redirect('index')