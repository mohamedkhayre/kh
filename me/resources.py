from import_export import resources
from .models import exceldata

class personresource(resources.ModelResource):
	class meta:
		model=exceldata