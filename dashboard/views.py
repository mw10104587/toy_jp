from django.shortcuts import render
from django.template import Context, loader
from django.shortcuts import render_to_response

# Create your views here.
def dashboard(request):
	# template = loader.get_template('dashboard/dashboard.html')
	# return HttpResponse(template.render())
	# return render_to_response('static/dashboard.html')
	return render(request, 'dashboard/dashboard.html')