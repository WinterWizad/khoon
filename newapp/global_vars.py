
from users.models import Doners

def donor_processor(request):
    if request.user.is_authenticated:  # Ensure user is logged in
        donors = Doners.objects.filter(username__username=request.user.username)
        
    else:
        donors = None  # Handle unauthenticated users
        
    return {'donor': donors}