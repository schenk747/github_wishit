from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from wishit.models import Gift
from django.views import generic

def index(request):
	gifts = Gift.objects.all()
	context = {'gift_list' : gifts}
	return render(request, 'wishit/index.html', context)

class IndexView(generic.ListView):
	model = Gift
	template_name = 'wishit/index.html'
	context_object_name = 'gift_list'

	#def get_queryset(self):
	#	"""Return the gift if title if text is 'blue' """
	#	return Gift.objects.filter(text='blue')
"""
def details(request, gift_id):
	gift = get_object_or_404(Gift, pk=gift_id)
	context = {'gift' : gift}
	return render(request, 'wishit/detail.html', context)
"""
class DetailView(generic.DetailView):
	model = Gift #the model the generic view will be acting upon
	#template_name = 'wishit/detail.html'

class ResultsView(generic.DetailView):
	model = Gift
	template_name = 'wishit/result.html'

def results(request, gift_id):
	gift = get_object_or_404(Gift, pk=gift_id)
	context = {'gift' : gift}
	return render(request, 'wishit/result.html', context)

def texts(request, gift_id):
	gift = get_object_or_404(Gift, pk=gift_id)
	context = {'gift' : gift}
	return render(request, 'wishit/text.html', context)

def update_texts(request, gift_id):
	gift = get_object_or_404(Gift, pk=gift_id)
	t = request.POST['text']
	gift.text = t
	gift.save()
	#reverse function helps avoid having to hardcode a URL in the view function
	return HttpResponseRedirect(reverse('wishit:results', args=(gift.id,)))
