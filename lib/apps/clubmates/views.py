from django.shortcuts import render_to_response
from django.template import RequestContext
from models import Location, Message

def index(request):
	context = {}
	context['lumpy'] = "scrumpy"
	return render_to_response('www/index.html', context, context_instance=RequestContext(request))
	
def show_location(request, loc):
	context = {}
	
	try:
		my_location = Location.objects.get(name=loc)
		context['parent'] = my_location.parent
		context['curr_location'] = my_location
		context['lat'] = my_location.latitude
		context['lon'] = my_location.longitude
	except:
		context['curr_location'] = loc
		context['new_location'] = True

	try:
		siblings = Location.objects.filter(parent=my_location.parent).exclude(name=loc)
		context['siblings'] = siblings
	except:
		pass

	
	context['curr_location'] = loc
	return render_to_response('www/places/index.html', context, context_instance=RequestContext(request))
	