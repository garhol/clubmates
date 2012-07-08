from django.shortcuts import render_to_response
from django.template import RequestContext
from models import Location, Message

def index(request):
    context = {}
    try:
        children = Location.objects.filter(parent=6).exclude(venue=True).order_by('name')
        context['children'] = children
    except:
        pass
    return render_to_response('www/index.html', context, context_instance=RequestContext(request))
	
def show_location(request, loc):
	context = {}

	try:
		my_location = Location.objects.get(name=loc)
		context['parent'] = my_location.parent
		context['curr_location'] = my_location
		context['lat'] = my_location.latitude
		context['lon'] = my_location.longitude
		context['zoom'] = my_location.density
	except:
		context['curr_location'] = loc
		context['new_location'] = True

	try:
		siblings = Location.objects.filter(parent=my_location.parent).exclude(name=loc).order_by('name')
		context['siblings'] = siblings
	except:
		pass
	
	try:
		children = Location.objects.filter(parent=my_location).exclude(venue=True).order_by('name')
		context['children'] = children
	except:
		pass
        
	try:
		venues = Location.objects.filter(parent=my_location, venue=True).order_by('name')
		context['venues'] = venues
	except:
		pass
    	
	context['curr_location'] = loc
	return render_to_response('www/place/index.html', context, context_instance=RequestContext(request))

def show_venue(request, loc):
    context = {}
    try:
        my_location = Location.objects.get(id=loc)
        context['curr_location'] = my_location
        context['parent'] = my_location.parent
        context['lat'] = my_location.latitude
        context['lon'] = my_location.longitude
        context['zoom'] = 17
    except:
        context['curr_location'] = loc
        context['new_location'] = True
        
    try:
        siblings = Location.objects.filter(parent=my_location.parent).exclude(id=loc).order_by('name')
        context['siblings'] = siblings
    except:
        pass
    
    return render_to_response('www/venue/index.html', context, context_instance=RequestContext(request))
    