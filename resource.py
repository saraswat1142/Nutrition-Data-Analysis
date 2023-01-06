from import_export import resources
from .models import *

class PPDFAdminResource(resources.ModelResource):

    class Meta:
        model   =  PPDF
        exclude = ('id',)