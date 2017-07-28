from django.http import Http404, JsonResponse
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render
from users.models import Users
from company.models import Company
from users.forms import LoginForm


#Get details of a specific user
#example: http://127.0.0.1:8000/users/get/?id=1
def getUsers(request):
	try:
		userid = request.GET.get('id')

		if userid is None:
			return JsonResponse({'message': 'id parameter missing'})

		userid = str(userid).strip()

		try:
			if int(userid) <= 0:
				return JsonResponse({'message': 'id must be a positive integer'})
		except ValueError:
			return JsonResponse({'message': 'id must be a positive integer'})

		try:
			u = Users.objects.get(pk=int(userid))
			
			if u.id:
				if u.company_val: #if company exists
					return JsonResponse({
						'id': u.id,
						'name': u.name,
						'job_title': u.job_title,
						'age': u.age,
						'gender': u.gender,
						'company': {
							'id': u.company_val.id,
							'name': u.company_val.name,
						}
					})
				else:
					return JsonResponse({
						'id': u.id,
						'name': u.name,
						'job_title': u.job_title,
						'age': u.age,
						'gender': u.gender,
						'company': 'not set'
					})
		except ObjectDoesNotExist:
			return JsonResponse({'message': 'user does not exist'})
	except:
		return JsonResponse({'message': 'some error'})


#To create a new user
#example: http://127.0.0.1:8000/users/create with required POST parameters
def createUsers(request):
	try:
		username = request.POST.get('name')
		userjob = request.POST.get('job_title')
		userage = request.POST.get('age')
		usergender = request.POST.get('gender')
		companyid = request.POST.get('company_id')

		#Checking if conditions are met
		if username is None:
			return JsonResponse({'message': 'name parameter missing'})

		username = str(username).strip()

		if username == "":
			return JsonResponse({'message': 'empty name given'})

		if userjob is None:
			return JsonResponse({'message': 'job_title parameter missing'})

		userjob = str(userjob).strip()

		if userjob == "":
			return JsonResponse({'message': 'empty job_title given'})

		if userage is None:
			return JsonResponse({'message': 'age parameter missing'})

		userage = str(userage).strip()

		try:
			if int(userage) <= 0:
				return JsonResponse({'message': 'age must be a positive integer'})
		except ValueError:
			return JsonResponse({'message': 'age must be a positive integer'})

		if usergender is None:
			return JsonResponse({'message': 'gender parameter missing'})

		usergender = str(usergender).strip()

		if not (usergender == "M" or usergender == "F"):
			return JsonResponse({'message': 'gender should be M or F'})

		if companyid is None:
			return JsonResponse({'message': 'company_id parameter missing'})

		companyid = str(companyid).strip()

		try:
			if int(companyid) <= 0:
				return JsonResponse({'message': 'company_id should be a positive integer'})
		except ValueError:
			return JsonResponse({'message': 'company_id should be a positive integer'})

		try:
			#Creating the user
			c = Company.objects.get(pk=int(companyid))		
			u = Users(name=username, age=int(userage), gender=usergender, job_title=userjob, company_val=c)
			u.save()

			if u.id:
				return JsonResponse({
					'id': u.id,
					'name': u.name,
					'job_title': u.job_title,
					'age': u.age,
					'gender': u.gender,
					'company name': u.company_val.name,
				})

			return JsonResponse({'message': 'not saved'})
		except ObjectDoesNotExist:
			return JsonResponse({'message': 'company does not exist'})
	except:
		return JsonResponse({'message': 'some error'})


#To update a user's info
#example: http://127.0.0.1:8000/users/update with optional POST parameters
def updateUsers(request):
	try:
		#To check if session is set
		try:
			del request.session['userid']
		except:
			pass

		userid = request.POST.get('id') #required
		username = request.POST.get('name') #optional
		userjob = request.POST.get('job_title') #optional
		userage = request.POST.get('age') #optional
		usergender = request.POST.get('gender') #optional
		companyid = request.POST.get('company_id') #optional

		if userid is None:
			return JsonResponse({'message': 'id parameter missing'})

		userid = str(userid).strip()

		try:
			if int(userid) <= 0:
				return JsonResponse({'message': 'id must be a positive integer'})
		except ValueError:
			return JsonResponse({'message': 'id must be a positive integer'})

		try:
			u = Users.objects.get(pk=int(userid))
			
			if u.id: #mandatory condition

				#optional parameters hence, ignoring incorrect values
				if (not username is None) and (not str(username).strip() == ""):
					u.name = username

				if (not userjob is None) and (not str(userjob).strip() == ""):
					u.job_title = userjob

				if (not userage is None) and (not str(userage).strip() == ""):
					try:
						if int(userage) > 0:
							u.age = int(userage)
					except ValueError:
						pass

				if (not usergender is None) and (str(usergender).strip() == "M" or str(usergender).strip() == "F"):
					u.gender = usergender

				if (not companyid is None) and (not str(companyid).strip() == ""):
					companyid = str(companyid).strip()

					try:
						if int(companyid) > 0:
							try:
								c = Company.objects.get(pk=int(companyid))
								u.company_val = c
							except ObjectDoesNotExist:
								pass
					except ValueError:
						pass

				u.save()

				if u.id:
					if u.company_val: #if company exists
						return JsonResponse({
							'id': u.id,
							'name': u.name,
							'job_title': u.job_title,
							'age': u.age,
							'gender': u.gender,
							'company': {
								'id': u.company_val.id,
								'name': u.company_val.name,
							}
						})
					else:
						return JsonResponse({
							'id': u.id,
							'name': u.name,
							'job_title': u.job_title,
							'age': u.age,
							'gender': u.gender,
							'company': 'not set'
						})

				return JsonResponse({'message': 'not saved'})
		except ObjectDoesNotExist:
			return JsonResponse({'message': 'user does not exist'})
	except:
		return JsonResponse({'message': 'some error'})


#To delete a user
#example: http://127.0.0.1:8000/users/delete with required id POST parameters
def deleteUsers(request):
	try:
		userid = request.POST.get('id')

		if userid is None:
			return JsonResponse({'message': 'id parameter missing'})

		userid = str(userid).strip()

		try:
			if int(userid) <= 0:
				return JsonResponse({'message': 'id must be a positive integer'})
		except ValueError:
			return JsonResponse({'message': 'id must be a positive integer'})

		try:
			#deleting user
			u = Users.objects.get(pk=int(userid))
			u.delete()

			return JsonResponse({'message': 'delete done'})
		except ObjectDoesNotExist:
			return JsonResponse({'message': 'user not found'})
	except:
		return JsonResponse({'message': 'some error'})


#Get complete list of users
#example: http://127.0.0.1:8000/users/all
def allUsers(request):
	try:
		retval = {'result': []}

		for u in Users.objects.all():
			if u.company_val:
				retval['result'].append({
					'id': u.id,
					'name': u.name,
					'job_title': u.job_title,
					'age': u.age,
					'gender': u.gender,
					'company': {
						'id': u.company_val.id,
						'name': u.company_val.name,
					}
				})
			else:
				retval['result'].append({
					'id': u.id,
					'name': u.name,
					'job_title': u.job_title,
					'age': u.age,
					'gender': u.gender,
					'company': 'not set'
				})
		
		return JsonResponse(retval)
	except:
		return JsonResponse({'message': 'some error'})


#When http://127.0.0.1:8000/users/login is called 
def loginView(request):
	#if user is already logged in then move to next page
	#else show login page
	if request.session.has_key('userid'):
		u = Users.objects.get(pk=int(request.session['userid']))
		
		#for the select tag in HTML to contain all companies name
		allcompanylist = []

		for co in Company.objects.all():
			allcompanylist.append({
				'id': co.id,
				'name': co.name,
			})

		if u.company_val:
			return render(request, 'loggedin.html', {
				'id': u.id,
				'name': u.name,
				'job_title': u.job_title,
				'age': u.age,
				'gender': u.gender,
				'company': {
					'id': u.company_val.id,
					'name': u.company_val.name,
				},
				'allcompany': allcompanylist,
			})
		else:
			return render(request, 'loggedin.html', {
				'id': u.id,
				'name': u.name,
				'job_title': u.job_title,
				'age': u.age,
				'gender': u.gender,
				'company': {
					'id': -1,
					'name': 'whatever',
				},
				'allcompany': allcompanylist,
			})

	return render(request, 'login.html')


#Attempt to access http://127.0.0.1:8000/users/dashboard
def loginUser(request):
	userid = -1

	if request.method == "POST":
		MyLoginForm = LoginForm(request.POST)

		if MyLoginForm.is_valid():
			userid = MyLoginForm.cleaned_data['userid']
			passw = MyLoginForm.cleaned_data['password']

			#Password is password for all users
			if passw == "password":
				try:
					#if valid userid
					u = Users.objects.get(pk=int(userid))

					allcompanylist = []

					for co in Company.objects.all():
						allcompanylist.append({
							'id': co.id,
							'name': co.name,
						})

					request.session['userid'] = userid
					request.session.set_expiry(60)

					return render(request, 'loggedin.html', {
						'id': u.id,
						'name': u.name,
						'job_title': u.job_title,
						'age': u.age,
						'gender': u.gender,
						'company': {
							'id': u.company_val.id,
							'name': u.company_val.name,
						},
						'allcompany': allcompanylist,
					})
				except:
					return render(request, 'login.html')
	else:
		MyLoginForm = LoginForm()

	#details don't match
	return render(request, 'login.html')