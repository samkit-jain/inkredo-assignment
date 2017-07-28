from django.http import Http404, JsonResponse
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render
from company.models import Company


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


def allCompany(request):
	try:
		retval = {'result': []}

		for c in Company.objects.all():
			retval['result'].append({'id': c.id, 'name': c.name})
		
		return JsonResponse(retval)
	except:
		return JsonResponse({'message': 'some error'})