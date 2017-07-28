from django.db import models
from company.models import Company

class Users(models.Model):
	name = models.CharField(max_length=50)
	job_title = models.CharField(max_length=50)
	age = models.IntegerField()
	company_val = models.ForeignKey(Company, on_delete=models.SET_NULL,null=True) #NOT CASCADE BECAUSE A USER CAN CHANGE COMPANY
	
	GENDER_CHOICES = (
		('M', 'Male'),
		('F', 'Female'),
	)
	gender = models.CharField(max_length=1, choices=GENDER_CHOICES)

	def __str__(self):
		return self.name

'''
BEGIN;
--
-- Create model Users
--
CREATE TABLE "users_users" ("id" serial NOT NULL PRIMARY KEY, "name" varchar(50) NOT NULL, "job_title" varchar(50) NOT NULL, "age" integer NOT NULL, "gender" varchar(1) NOT NULL, "company_val_id" integer NOT NULL);
ALTER TABLE "users_users" ADD CONSTRAINT "users_users_company_val_id_eceaddf5_fk_company_company_id" FOREIGN KEY ("company_val_id") REFERENCES "company_company" ("id") DEFERRABLE INITIALLY DEFERRED;
CREATE INDEX "users_users_company_val_id_eceaddf5" ON "users_users" ("company_val_id");
COMMIT;
'''