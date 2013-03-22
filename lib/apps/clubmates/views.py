from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect

from models import Location, Message, LocationForm


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
        my_location = Location.objects.get(id=loc)
        context['parent'] = my_location.parent
        context['curr_location'] = my_location
        context['lat'] = my_location.latitude
        context['lon'] = my_location.longitude
        context['zoom'] = my_location.density
    except:
        context['curr_location'] = loc
        context['new_location'] = True

    try:
        siblings = Location.objects.filter(parent=my_location.parent).exclude(id=loc).order_by('name')
        context['siblings'] = siblings
    except:
        pass
    
    try:
        children = Location.objects.filter(parent=my_location).exclude(venue=True).order_by('name')
        context['children'] = children
    except:
        pass

    venues = Location.objects.filter(parent=my_location, venue=True).order_by('name')
    context['venues'] = venues
    
    context['crumbs'] = get_crumbs_by_id(loc)
   

    return render_to_response('www/place/index.html', context, context_instance=RequestContext(request))

def show_venue(request, loc):
    context = {}
    try:
        my_location = Location.objects.get(id=loc)
        context['curr_location'] = my_location
        context['parent'] = my_location.parent
        context['lat'] = my_location.latitude
        context['lon'] = my_location.longitude
        context['zoom'] = 19
        #context['sat']= True
    except:
        context['curr_location'] = loc
        context['new_location'] = True
        
    try:
        siblings = Location.objects.filter(parent=my_location.parent).exclude(id=loc).order_by('name')
        context['siblings'] = siblings
    except:
        pass
        
    context['crumbs'] = get_crumbs_by_id(loc)
    
    return render_to_response('www/venue/index.html', context, context_instance=RequestContext(request))


def add_location(request, loc):
    context = {}
    my_location = Location.objects.get(id=loc)
    context['curr_location'] = my_location
    context['parent'] = my_location.parent
    context['lat'] = my_location.latitude
    context['lon'] = my_location.longitude
    context['zoom'] = my_location.density   
    if request.method == 'POST': # If the form has been submitted...
        form = LocationForm(request.POST) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            name = form.cleaned_data['name']
            latitude = form.cleaned_data['latitude']
            longitude = form.cleaned_data['longitude']
            density = form.cleaned_data['density']
            venue = form.cleaned_data['venue']
            parent = form.cleaned_data['parent']
            l = Location(name=name, parent=parent, latitude=latitude, longitude=longitude, density=density, venue=venue)
            l.save()

            return HttpResponseRedirect('/') # Redirect after POST
    else:
        context['form'] = LocationForm(initial={'parent':my_location.id}) # An unbound form


    return render_to_response('www/place/add.html', context, context_instance=RequestContext(request))
 
def get_crumbs_by_id(id):
    obj = Location.objects.get(id=id)
    if obj.parent:
        return [obj] + get_crumbs_by_id(obj.parent.id)    
    return [obj]
