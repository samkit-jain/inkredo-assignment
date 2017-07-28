from django.http import Http404, JsonResponse
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render
from company.models import Company


#Get details of a single company
#example: http://127.0.0.1:8000/company/get/?id=2
def getCompany(request):
	try:
		companyid = request.GET.get('id')

		if companyid is None:
			return JsonResponse({'message': 'id parameter missing'})

		if str(companyid).strip() == "":
			return JsonResponse({'message': 'empty id given'})

		try:
			c = Company.objects.get(pk=int(str(companyid).strip()))
			return JsonResponse({'id': c.id, 'name': c.name})
		except ObjectDoesNotExist:
			return JsonResponse({'message': 'company not found'})
	except:
		return JsonResponse({'message': 'some error'})



#Create a single company
#example: http://127.0.0.1:8000/company/create with just a single 'name' parameter
def createCompany(request):
	try:
		companyname = request.POST.get('name')

		if companyname is None:
			return JsonResponse({'message': 'name parameter missing'})

		if str(companyname).strip() == "":
			return JsonResponse({'message': 'empty name given'})

		c = Company(name=str(companyname).strip())
		c.save()

		if c.id:
			return JsonResponse({'id': c.id, 'name': c.name})

		return JsonResponse({'message': 'not saved'})
	except:
		return JsonResponse({'message': 'some error'})


#Update details of a single company
#example: http://127.0.0.1:8000/company/update with required ID and NAME post parameters
def updateCompany(request):
	try:
		companyid = request.POST.get('id')
		companyname = request.POST.get('name')

		if companyid is None:
			return JsonResponse({'message': 'id parameter missing'})

		if str(companyid).strip() == "":
			return JsonResponse({'message': 'empty id given'})

		if companyname is None:
			return JsonResponse({'message': 'name parameter missing'})

		if str(companyname).strip() == "":
			return JsonResponse({'message': 'empty name given'})

		try:
			c = Company.objects.get(pk=int(str(companyid).strip()))
			c.name = str(companyname).strip()
			c.save()

			if c.id:
				return JsonResponse({'id': c.id, 'name': c.name})

			return JsonResponse({'message': 'not saved'})
		except ObjectDoesNotExist:
			return JsonResponse({'message': 'company not found'})
	except:
		return JsonResponse({'message': 'some error'})


#Delete a single company
#example: http://127.0.0.1:8000/company/delete with a required id POST parameter
def deleteCompany(request):
	try:
		companyid = request.POST.get('id')

		if companyid is None:
			return JsonResponse({'message': 'id parameter missing'})

		if str(companyid).strip() == "":
			return JsonResponse({'message': 'empty id given'})

		try:
			c = Company.objects.get(pk=int(str(companyid).strip()))
			c.delete()

			return JsonResponse({'message': 'delete done'})
		except ObjectDoesNotExist:
			return JsonResponse({'message': 'company not found'})
	except:
		return JsonResponse({'message': 'some error'})


#Get details of all companies
#example: http://127.0.0.1:8000/company/get/?id=2
def allCompany(request):
	try:
		retval = {'result': []}

		for c in Company.objects.all():
			retval['result'].append({'id': c.id, 'name': c.name})
		
		return JsonResponse(retval)
	except:
		return JsonResponse({'message': 'some error'})