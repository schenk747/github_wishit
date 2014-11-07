from django.shortcuts import render, get_object_or_404, get_list_or_404, redirect, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from wishit.models import Gift, WishList
from django.views import generic
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import csrf_protect
from django.core.context_processors import csrf
import simplejson
from django.template.loader import render_to_string

#def index(request):
#	gifts = Gift.objects.all()
#	context = {'gift_list' : gifts}
#	return render(request, 'wishit/index.html', context)


def index(request, login_failed=False):
	if request.user.is_authenticated():
		return redirect('wishit:home')
	else:
		context = {'login_failed' : login_failed}
		return render(request, 'wishit/index.html')
	#def get_queryset(self):
	#	"""Return the gift if title if text is 'blue' """
	#	return Gift.objects.filter(text='blue')

#def details(request, gift_id):
#	gift = get_object_or_404(Gift, pk=gift_id)
#	context = {'gift' : gift}
#	return render(request, 'wishit/detail.html', context)

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

def home(request):
	if not request.user.is_authenticated():
		return redirect('wishit:index')
	else:
		wishlists = get_list_or_404(WishList)
		wl_id = [wl.id for wl in wishlists]
		gifts = get_list_or_404(Gift, wish_list__in = wl_id)
		#gifts = get_list_or_404(Gift, )
		context = {'wishlist' : wishlists, 'gifts': gifts}
		context.update(csrf(request))
		return render(request, 'wishit/home.html', context)




def login_user(request):
	username = request.POST['username']
	password = request.POST['password']
	user = authenticate(username=username, password=password)
	if user is not None:
		if user.is_active:
			login(request,user)
			#redirect to succes page
			return HttpResponseRedirect(reverse('wishit:home'))
		else:
			pass
			#Return a 'disabled account' error message
	else:
		HttpResponseRedirect(reverse('wishit:index', kwargs={'login_failed':True}))

def logout_user(request):
	logout(request)
	return redirect('wishit:index')

@csrf_protect
def update_wishlist(request):
	#if all (k in request.POST for k in ("title","text")):
	title = request.POST['title']
	text = request.POST['text']
	gift = Gift(title=title, text=text, wisher_id=request.user.id ,wish_list_id=1)
	gift.save()
	wishlists = get_list_or_404(WishList)
	context = {'wishlist' : wishlists}
	#response_dict = {'t' : title, 'text' : text}
	#return HttpResponse(simplejson.dumps(response_dict), mimetype='application/javascript')
	html = render_to_string('wishit/sub_gift.html', context)
	return HttpResponse(html, mimetype='application/javascript')

@csrf_protect
def delete_gift(request):
	#if all (k in request.POST for k in ("title","text")):
	gift_id = request.POST['gift_id']
	gift = Gift.objects.get(pk=gift_id)
	gift.delete()
	wishlists = get_list_or_404(WishList)
	context = {'wishlist' : wishlists}
	#response_dict = {'t' : title, 'text' : text}
	#return HttpResponse(simplejson.dumps(response_dict), mimetype='application/javascript')
	html = render_to_string('wishit/sub_gift.html', context)
	return HttpResponse(html, mimetype='application/javascript')

