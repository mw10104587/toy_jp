from django.shortcuts import render
from django.template import Context, loader
from django.shortcuts import render_to_response

from orders.models import Order

# Create your views here.
def dashboard(request):
	# template = loader.get_template('dashboard/dashboard.html')
	# return HttpResponse(template.render())
	# return render_to_response('static/dashboard.html')

	# get data here
	orders = Order.objects.filter(company_name="Apple")
	t = orders[0].json_object()

	return render(request, 'dashboard/dashboard.html', {'apple': t})