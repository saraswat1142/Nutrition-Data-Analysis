from django.contrib import admin

from .models import (AAP, CAROTENOIDS, EOF, FAP, FSV, MTE, OA, OPPS, PP, PPDF,
                     SIS, WSV)



from django.contrib import admin

from import_export.admin import ImportExportModelAdmin
from import_export import resources

class PPDFAdminResource(resources.ModelResource):

    class Meta:
        model = PPDF

        import_id_fields = ('name',)

class PPDFModelAdmin(ImportExportModelAdmin):
    resource_class = PPDFAdminResource


admin.site.register(PPDF, PPDFModelAdmin)

class WSVAdminResource(resources.ModelResource):

    class Meta:
        model = WSV

        import_id_fields = ('name',)

class WSVModelAdmin(ImportExportModelAdmin):
    resource_class = WSVAdminResource

admin.site.register(WSV, WSVModelAdmin)

class FSVAdminResource(resources.ModelResource):

    class Meta:
        model = FSV

        import_id_fields = ('name',)

class FSVModelAdmin(ImportExportModelAdmin):
    resource_class = FSVAdminResource

admin.site.register(FSV, FSVModelAdmin)



class EOFAdminResource(resources.ModelResource):

    class Meta:
        model = EOF

        import_id_fields = ('name',)

class EOFModelAdmin(ImportExportModelAdmin):
    resource_class = EOFAdminResource

admin.site.register(EOF, EOFModelAdmin)


class AAPAdminResource(resources.ModelResource):

    class Meta:
        model = AAP

        import_id_fields = ('name',)

class AAPModelAdmin(ImportExportModelAdmin):
    resource_class = AAPAdminResource

admin.site.register(AAP, AAPModelAdmin)


class FAPAdminResource(resources.ModelResource):

    class Meta:
        model = FAP

        import_id_fields = ('name',)

class FAPModelAdmin(ImportExportModelAdmin):
    resource_class = FAPAdminResource

admin.site.register(FAP, FAPModelAdmin)


class MTEAdminResource(resources.ModelResource):

    class Meta:
        model = MTE

        import_id_fields = ('name',)

class MTEModelAdmin(ImportExportModelAdmin):
    resource_class = MTEAdminResource

admin.site.register(MTE, MTEModelAdmin)


class OAAdminResource(resources.ModelResource):

    class Meta:
        model = OA

        import_id_fields = ('name',)

class OAModelAdmin(ImportExportModelAdmin):
    resource_class = OAAdminResource

admin.site.register(OA, OAModelAdmin)


class PPAdminResource(resources.ModelResource):

    class Meta:
        model = PP

        import_id_fields = ('name',)

class PPModelAdmin(ImportExportModelAdmin):
    resource_class = PPAdminResource

admin.site.register(PP, PPModelAdmin)


class OPPSAdminResource(resources.ModelResource):

    class Meta:
        model = OPPS

        import_id_fields = ('name',)

class OPPSModelAdmin(ImportExportModelAdmin):
    resource_class = OPPSAdminResource

admin.site.register(OPPS, OPPSModelAdmin)


class SISAdminResource(resources.ModelResource):

    class Meta:
        model = SIS

        import_id_fields = ('name',)

class SISModelAdmin(ImportExportModelAdmin):
    resource_class = SISAdminResource

admin.site.register(SIS, SISModelAdmin)


class CAROTENOIDSAdminResource(resources.ModelResource):

    class Meta:
        model = CAROTENOIDS

        import_id_fields = ('name',)

class CAROTENOIDSModelAdmin(ImportExportModelAdmin):
    resource_class = CAROTENOIDSAdminResource

admin.site.register(CAROTENOIDS, CAROTENOIDSModelAdmin)

# admin.site.register(PostCommePP