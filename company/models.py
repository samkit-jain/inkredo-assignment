from django.db import models

class Company(models.Model):
	name = models.CharField(max_length=200)

	def __str__(self):
		return self.name

'''
sqlmigrate company 0001
BEGIN;
--
-- Create model Company
--
CREATE TABLE "company_company" ("id" serial NOT NULL PRIMARY KEY, "name" varchar(200) NOT NULL);
COMMIT;

'''