import json

from django.http import JsonResponse
from django.shortcuts import HttpResponse, render
from django.views.decorators.csrf import csrf_exempt

from .models import (AAP, CAROTENOIDS, EOF, FAP, FSV, MTE, OA, OPPS, PP, PPDF,SIS, WSV)

# Create your views here.

# all given input should be in 100gm if it is not then divide it by 100
# every api will contain name and weight of food.
@csrf_exempt
def AAP_api(request):

    # print(dict(request.POST))
    request_data = json.loads(request.body.decode('utf-8'))
    Name = request_data["name"]
    quant = float(request_data["quantitiy"])
    if AAP.objects.filter(name = Name).count() > 0:
        sd = AAP.objects.get(name = Name)

        data = {
            "Histidine" : sd.Histidine * quant ,
            "Isoleucine" : sd.Isoleucine * quant ,
            "Luecine" : sd.Luecine * quant,
            "Lysine" : sd.Lysine *quant ,
            "Methionine" : sd.Methionine * quant,
            "Cystine" : sd.Cystine *quant,
            "Phenylalanine" : sd.Phenylalanine *quant,
            "Threonine" : sd.Threonine * quant,
            "Tryptophan"  :sd.Tryptophan * quant,
            "Valine"  : sd.Valine *quant,
            "Alanine" : sd.Alanine *quant,
            "Arginine" : sd.Arginine *quant,
            "Aspartic" : sd.Aspartic *quant,
            "Glutamic" : sd.Glutamic *quant,
            "Glycine" : sd.Glycine *quant,
            "Proline" : sd.Proline *quant,
            "Serine" : sd.Serine *quant,
            "Tyrosine" : sd.Tyrosine *quant,
        }

        return JsonResponse(data)

    else:
        data = {"error" : "food name doesn't exist in database"}
        return JsonResponse(data,status= 404)


@csrf_exempt
def PPDF_api(request):

    # print(dict(request.POST))
    request_data = json.loads(request.body.decode('utf-8'))
    Name = request_data["name"]
    quant = float(request_data["quantitiy"])
    if PPDF.objects.filter(name = Name).count() > 0:
        sd = PPDF.objects.get(name = Name)

        data = {
            "water" : sd.water * quant,
            "protein" : sd.protein * quant,
            "ash" : sd.ash * quant,
            "totalfat": sd.totalfat * quant,
            "df_insoluble" : sd.df_insoluble * quant,
            "df_soluble" : sd.df_soluble * quant,
            "carbohydrates" : sd.carbohydrates * quant,
            "energy": sd.energy * quant,
        }

        return JsonResponse(data)

    else:
        data = {"error" : "food name doesn't exist in database"}
        return JsonResponse(data,status= 404)

@csrf_exempt
def WSV_api(request):

    # print(dict(request.POST))
    request_data = json.loads(request.body.decode('utf-8'))
    Name = request_data["name"]
    quant = float(request_data["quantitiy"])
    if WSV.objects.filter(name = Name).count() > 0:
        sd = WSV.objects.get(name = Name)

        data = {
            "Thiamine_B1" : sd.Thiamine_B1 *quant,
            "Riboflavin_B2" : sd.Riboflavin_B2 *quant,
            "Niacin_B3" : sd.Niacin_B3 *quant,
            "Pantothenic_Acid_B5" : sd.Pantothenic_Acid_B5 *quant,
            "B6" : sd.B6 *quant,
            "Biotin_B7" : sd.Biotin_B7 *quant,
            "Folates_B9": sd.Folates_B9 *quant,
            "Ascorbic_Acid" : sd.Ascorbic_Acid *quant,
        }

        return JsonResponse(data)

    else:
        data = {"error" : "food name doesn't exist in database"}
        return JsonResponse(data,status= 404)

@csrf_exempt
def FSV_api(request):

    # print(dict(request.POST))
    request_data = json.loads(request.body.decode('utf-8'))
    Name = request_data["name"]
    quant = float(request_data["quantitiy"])
    if FSV.objects.filter(name = Name).count() > 0:
        sd = FSV.objects.get(name = Name)

        data = {
            "ERGCAL": sd.ERGCAL *quant,
            "TocopherolsA" : sd.TocopherolsA *quant,
            "TocopherolsB" : sd.TocopherolsB *quant,
            "TocopherolsG" : sd.TocopherolsG *quant,
            "TocopherolsD" : sd.TocopherolsD *quant,
            "TocotrienolsA" : sd.TocotrienolsA *quant,
            "TocotrienolsB" : sd.TocotrienolsB *quant,
            "TocotrienolsG" : sd.TocotrienolsG *quant,
            "TocotrienolsD" : sd.TocotrienolsD *quant,
            "RETOL": sd.RETOL *quant,
            "CHOCAL":sd.CHOCAL *quant,
            "OHD3_25" : sd.OHD3_25 *quant,
            "VITE" : sd.VITE *quant,
            "VITK1" : sd.VITK1 *quant,
        }

        return JsonResponse(data)

    else:
        data = {"error" : "food name doesn't exist in database"}
        return JsonResponse(data,status= 404)





@csrf_exempt
def MTE_api(request):

    # print(dict(request.POST))
    request_data = json.loads(request.body.decode('utf-8'))
    Name = request_data["name"]
    quant = float(request_data["quantitiy"])
    if MTE.objects.filter(name = Name).count() > 0:
        sd = MTE.objects.get(name = Name)

        data = {
            "Aluminium": sd.Aluminium *quant,
            "Arsenic": sd.Arsenic *quant,
            "Cadmium" : sd.Cadmium *quant,
            "Calcium" : sd.Calcium *quant,
            "Chromium": sd.Chromium *quant,
            "Cobalt" : sd.Cobalt *quant,
            "Copper" : sd.Copper *quant,
            "Iron": sd.Iron *quant,
            "Lithium" : sd.Lithium *quant,
            "Magnesium": sd.Magnesium *quant,
            "Mercury" : sd.Mercury *quant,
            "Molebdeum" : sd.Molebdeum *quant,
            "Nickel" : sd.Nickel *quant,
            "Phosphorus": sd.Phosphorus *quant,
            "Potassium": sd.Potassium *quant,
            "Selenium": sd.Selenium *quant,
            "Sodium" : sd.Sodium *quant,
            "Zinc": sd.Zinc *quant,
        }

        return JsonResponse(data)

    else:
        data = {"error" : "food name doesn't exist in database"}
        return JsonResponse(data,status= 404)


@csrf_exempt
def CAROTENOIDS_api(request):

    # print(dict(request.POST))
    request_data = json.loads(request.body.decode('utf-8'))
    Name = request_data["name"]
    quant = float(request_data["quantitiy"])
    if CAROTENOIDS.objects.filter(name = Name).count() > 0:
        sd = CAROTENOIDS.objects.get(name = Name)

        data = {
            "Lutein" : sd.Lutein *quant,
            "Zeaxanthin" : sd.Zeaxanthin *quant,
            "Lycopene" : sd.Lycopene *quant,
            "BCryptoxanthin" : sd.BCryptoxanthin *quant,
            "G_Carotene" : sd.G_Carotene *quant,
            "A_Carotene" : sd.A_Carotene *quant,
            "B_Carotene" : sd.B_Carotene *quant,
            "Total_Carotenoids" : sd.Total_Carotenoids *quant,
        }

        return JsonResponse(data)

    else:
        data = {"error" : "food name doesn't exist in database"}
        return JsonResponse(data,status= 404)

@csrf_exempt
def SIS_api(request):

    # print(dict(request.POST))
    request_data = json.loads(request.body.decode('utf-8'))
    Name = request_data["name"]
    print(Name)
    quant = float(request_data["quantitiy"])
    if SIS.objects.filter(name = Name).count() > 0:
        sd = SIS.objects.get(name = Name)

        data = {
            "Starch" : sd.Starch *quant,
            "Fructose" : sd.Fructose *quant,
            "Glucose" : sd.Glucose *quant,
            "Sucrose" : sd.Sucrose *quant,
            "Maltose" : sd.Maltose *quant,
            "Free_Sugars" : sd.Free_Sugars *quant,
            "Total_CHO" : sd.Total_CHO *quant,
        }

        return JsonResponse(data)


    else:
        data = {"error" : "food name doesn't exist in database"}
        return JsonResponse(data,status= 404)



@csrf_exempt
def FAP_api(request):

    # print(dict(request.POST))
    request_data = json.loads(request.body.decode('utf-8'))
    Name = request_data["name"]
    quant = float(request_data["quantitiy"])
    if FAP.objects.filter(name = Name).count() > 0:
        sd = FAP.objects.get(name = Name)

        data = {
            "Eicosaenoic" : sd.Eicosaenoic *quant,
            "Erucic" : sd.Erucic *quant,
            "Nervonic" : sd.Nervonic *quant,
            "Linoleic" : sd.Linoleic *quant,
            "Eicosadienoic" : sd.Eicosadienoic *quant,
            "A_Linolenic" : sd.A_Linolenic *quant,
            "Arachidonic" : sd.Arachidonic *quant,
            "Saturated_Fatty_Acids" : sd.Saturated_Fatty_Acids *quant,
            "Mono_UnSaturated_Fatty_Acids" : sd.Mono_UnSaturated_Fatty_Acids *quant,
            "poly_UnSaturated_Fatty_Acids" : sd.poly_UnSaturated_Fatty_Acids *quant,
            "Capric" : sd.Capric *quant,
            "Lauric" : sd.Lauric *quant,
            "Myristic" : sd.Myristic *quant,
            "Palmitic" : sd.Palmitic *quant,
            "Stearic" : sd.Stearic *quant,
            "Arachidic" : sd.Arachidic *quant,
            "Behenic" : sd.Behenic *quant,
            "Lignoceric" : sd.Lignoceric *quant,
            "Myristoleic" : sd.Myristoleic *quant,
            "Palmitoleic" : sd.Palmitoleic *quant,
            "Oleic" : sd.Oleic *quant,
            "Undecanoic" : sd.Undecanoic *quant,
            "Pentadecanoic" : sd.Pentadecanoic *quant,
            "Docosadienoic" : sd.Docosadienoic *quant,
            "Eicosatrienoic" : sd.Eicosatrienoic *quant,
            "Eicosapentaenoic" : sd.Eicosapentaenoic *quant,
            "Docosapentaenoic" : sd.Docosapentaenoic *quant,
            "Docosahexaenoic" : sd.Docosahexaenoic *quant,
            "Cholestrol" : sd.Cholestrol *quant,
        }

        return JsonResponse(data, safe=False)

    else:
        data = {"error" : "food name doesn't exist in database"}
        return JsonResponse(data,status= 404)

@csrf_exempt
def OA_api(request):

    # print(dict(request.POST))
    request_data = json.loads(request.body.decode('utf-8'))
    Name = request_data["name"]
    quant = float(request_data["quantitiy"])
    if OA.objects.filter(name = Name).count() > 0:
        sd = OA.objects.get(name = Name)

        data = {
            "Oxalate_soluble" : sd.Oxalate_soluble *quant,
            "Oxalate_insoluble" : sd.Oxalate_insoluble *quant,
            "Cis_Aconitic" : sd.Cis_Aconitic *quant,
            "Citric" : sd.Citric *quant,
            "Fumaric" : sd.Fumaric *quant,
            "Mallic" : sd.Mallic *quant,
            "Quinic" : sd.Quinic *quant,
            "Succinic" : sd.Succinic *quant,
            "Tartaric" : sd.Tartaric *quant,
        }

        return JsonResponse(data)

    else:
        data = {"error" : "food name doesn't exist in database"}
        return JsonResponse(data,status= 404)

@csrf_exempt
def PP_api(request):

    # print(dict(request.POST))
    request_data = json.loads(request.body.decode('utf-8'))
    Name = request_data["name"]
    quant = float(request_data["quantitiy"])
    if PP.objects.filter(name = Name).count() > 0:
        sd = PP.objects.get(name = Name)

        data = {
            "Chlorogenic"  : sd.Chlorogenic *quant,
            "Ferulic" : sd.Ferulic *quant,
            "Apigenin" : sd.Apigenin *quant,
            "Apigenin_6_C_gluoside" : sd.Apigenin_6_C_gluoside *quant,
            "Apigenin_7_O_neohesperidoside" : sd.Apigenin_7_O_neohesperidoside *quant,
            "Luteolin" : sd.Luteolin *quant,
            "Kaempferol" : sd.Kaempferol *quant,
            "Quercetin" : sd.Quercetin *quant,
            "Quercetin_3_B_Dglucoside" : sd.Quercetin_3_B_Dglucoside *quant,
            "Quercetin_3_O_rutinoside" : sd.Quercetin_3_O_rutinoside *quant,
            "acid_3_4_Dihydroxy_benzoic" : sd.acid_3_4_Dihydroxy_benzoic *quant,
            "Hydroxy_3_benzaldehyde" : sd.Hydroxy_3_benzaldehyde *quant,
            "Protocatechuic_acid" : sd.Protocatechuic_acid *quant,
            "Vanillic_acid" : sd.Vanillic_acid *quant,
            "Gallic_acid" : sd.Gallic_acid *quant,
            "Cinamic_acid" : sd.Cinamic_acid *quant,
            "O_Coumaric_acid" : sd.O_Coumaric_acid *quant,
            "P_Coumaric_acid" : sd.P_Coumaric_acid *quant,
            "Caffeic_acid" : sd.Caffeic_acid *quant,
            "Quercetin_3_β_galactoside" : sd.Quercetin_3_B_galactoside *quant,
            "Isoramnetin"  : sd.Isoramnetin *quant,
            "Myricetin" : sd.Myricetin *quant,
            "Resvertrol" : sd.Resvertrol *quant,
            "Hesperetin" : sd.Hesperetin *quant,
            "Naringenin" : sd.Naringenin *quant,
            "Hesperdin" : sd.Hesperdin *quant,
            "Daidzein" : sd.Daidzein *quant,
            "Genistein" : sd.Genistein *quant,
            "Epicatechin"  : sd.Epicatechin *quant,
            "Epigallocatechin" : sd.Epigallocatechin *quant,
            "Epigallocatechin_3_gallate" : sd.Epigallocatechin_3_gallate *quant,
            "Catechin" : sd.Catechin *quant,
            "Gallocatechin_gallate" : sd.Gallocatechin_gallate *quant,
            "Gallo_catechin" : sd.Gallo_catechin *quant,
            "Syringic_acid" : sd.Syringic_acid *quant,
            "Sinapinic_acid" : sd.Sinapinic_acid *quant,
            "Ellagic_acid" : sd.Ellagic_acid *quant,
            "Total_polyphenols" : sd.Total_polyphenols *quant,
            "Quercetin_3_B_galactoside" : sd.Quercetin_3_B_galactoside *quant,
        }

        return JsonResponse(data)

    else:
        data = {"error" : "food name doesn't exist in database"}
        return JsonResponse(data,status= 404)

@csrf_exempt
def OPPS_api(request):

    # print(dict(request.POST))
    request_data = json.loads(request.body.decode('utf-8'))
    Name = request_data["name"]
    quant = float(request_data["quantitiy"])
    if OPPS.objects.filter(name = Name).count() > 0:
        sd = OPPS.objects.get(name = Name)

        data = {
            "Raffinose" : sd.Raffinose *quant,
            "Stachyose" : sd.Stachyose *quant,
            "Verbascose"  : sd.Verbascose *quant,
            "Ajugose"  : sd.Ajugose *quant,
            "Campesterol"  : sd.Campesterol *quant,
            "Stigmasterol"  : sd.Stigmasterol *quant,
            "B_Sitosterol" : sd.B_Sitosterol *quant,
            "Phytate" : sd.Phytate *quant,
            "Total_Saponin" : sd.Total_Saponin *quant,
        }

        return JsonResponse(data)

    else:
        data = {"error" : "food name doesn't exist in database"}
        return JsonResponse(data,status= 404)

@csrf_exempt
def EOF_api(request):

    # print(dict(request.POST))
    request_data = json.loads(request.body.decode('utf-8'))
    Name = request_data["name"]
    quant = float(request_data["quantitiy"])

    if EOF.objects.filter(name = Name).count() > 0:
        sd = EOF.objects.get(name = Name)

        data = {
            "Butyric" : sd.Butyric *quant,
            "Caproic" : sd.Caproic *quant,
            "Caprylic" : sd.Caprylic *quant,
            "Capric" : sd.Capric *quant,
            "Lauric" : sd.Lauric *quant,
            "Myristic" : sd.Myristic *quant,
            "Palmitic" : sd.Palmitic *quant,
            "Stearic" : sd.Stearic *quant,
            "Arachidic" : sd.Arachidic *quant,
            "Behenic" : sd.Behenic *quant,
            "Lignoceric" : sd.Behenic *quant,
            "Myristoleic" : sd.Myristoleic *quant,
            "Palmitoleic" : sd.Palmitoleic *quant,
            "Elaidic" : sd.Elaidic *quant,
            "Oleic" : sd.Oleic *quant,
            "Eicosenoic" : sd.Eicosenoic *quant,
            "Erucic" : sd.Eicosenoic *quant,
            "Linoleic" : sd.Linoleic *quant,
            "delta-Linolenic" : sd.Linolenic *quant,
            "Saturated_Fatty_Acids" : sd.Saturated_Fatty_Acids *quant,
            "Mono_Unsaturated_Fatty_Acids" : sd.Mono_Unsaturated_Fatty_Acids *quant,
            "Poly_Unsaturated_Fatty_Acids" : sd.Poly_Unsaturated_Fatty_Acids *quant,

        }

        return JsonResponse(data)

    else:
        data = {"error" : "food name doesn't exist in database"}
        return JsonResponse(data,status= 404)


@csrf_exempt
def ALL(request):
    request_data = json.loads(request.body.decode('utf-8'))
    Name = request_data["name"]
    quant = float(request_data["quantitiy"])

    data = {}
    if FAP.objects.filter(name = Name).count() > 0:
        sd = FAP.objects.get(name = Name)

        data1 = {
            "Eicosaenoic" : sd.Eicosaenoic *quant,
            "Erucic" : sd.Erucic *quant,
            "Nervonic" : sd.Nervonic *quant,
            "Linoleic" : sd.Linoleic *quant,
            "Eicosadienoic" : sd.Eicosadienoic *quant,
            "A_Linolenic" : sd.A_Linolenic *quant,
            "Arachidonic" : sd.Arachidonic *quant,
            "Saturated_Fatty_Acids" : sd.Saturated_Fatty_Acids *quant,
            "Mono_UnSaturated_Fatty_Acids" : sd.Mono_UnSaturated_Fatty_Acids *quant,
            "poly_UnSaturated_Fatty_Acids" : sd.poly_UnSaturated_Fatty_Acids *quant,
            "Capric" : sd.Capric *quant,
            "Lauric" : sd.Lauric *quant,
            "Myristic" : sd.Myristic *quant,
            "Palmitic" : sd.Palmitic *quant,
            "Stearic" : sd.Stearic *quant,
            "Arachidic" : sd.Arachidic *quant,
            "Behenic" : sd.Behenic *quant,
            "Lignoceric" : sd.Lignoceric *quant,
            "Myristoleic" : sd.Myristoleic *quant,
            "Palmitoleic" : sd.Palmitoleic *quant,
            "Oleic" : sd.Oleic *quant,
            "Undecanoic" : sd.Undecanoic *quant,
            "Pentadecanoic" : sd.Pentadecanoic *quant,
            "Docosadienoic" : sd.Docosadienoic *quant,
            "Eicosatrienoic" : sd.Eicosatrienoic *quant,
            "Eicosapentaenoic" : sd.Eicosapentaenoic *quant,
            "Docosapentaenoic" : sd.Docosapentaenoic *quant,
            "Docosahexaenoic" : sd.Docosahexaenoic *quant,
            "Cholestrol" : sd.Cholestrol *quant,
        }
        data.update(data1)


    if EOF.objects.filter(name = Name).count() > 0:
        sd = EOF.objects.get(name = Name)

        data1 = {
            "Butyric" : sd.Butyric *quant,
            "Caproic" : sd.Caproic *quant,
            "Caprylic" : sd.Caprylic *quant,
            "Capric" : sd.Capric *quant,
            "Lauric" : sd.Lauric *quant,
            "Myristic" : sd.Myristic *quant,
            "Palmitic" : sd.Palmitic *quant,
            "Stearic" : sd.Stearic *quant,
            "Arachidic" : sd.Arachidic *quant,
            "Behenic" : sd.Behenic *quant,
            "Lignoceric" : sd.Behenic *quant,
            "Myristoleic" : sd.Myristoleic *quant,
            "Palmitoleic" : sd.Palmitoleic *quant,
            "Elaidic" : sd.Elaidic *quant,
            "Oleic" : sd.Oleic *quant,
            "Eicosenoic" : sd.Eicosenoic *quant,
            "Erucic" : sd.Eicosenoic *quant,
            "Linoleic" : sd.Linoleic *quant,
            "delta-Linolenic" : sd.Linolenic *quant,
            "Saturated_Fatty_Acids" : sd.Saturated_Fatty_Acids *quant,
            "Mono_Unsaturated_Fatty_Acids" : sd.Mono_Unsaturated_Fatty_Acids *quant,
            "Poly_Unsaturated_Fatty_Acids" : sd.Poly_Unsaturated_Fatty_Acids *quant,
        }
        data.update(data1)
    if OPPS.objects.filter(name = Name).count() > 0:
        sd = OPPS.objects.get(name = Name)

        data1 = {
            "Raffinose" : sd.Raffinose *quant,
            "Stachyose" : sd.Stachyose *quant,
            "Verbascose"  : sd.Verbascose *quant,
            "Ajugose"  : sd.Ajugose *quant,
            "Campesterol"  : sd.Campesterol *quant,
            "Stigmasterol"  : sd.Stigmasterol *quant,
            "B_Sitosterol" : sd.B_Sitosterol *quant,
            "Phytate" : sd.Phytate *quant,
            "Total_Saponin" : sd.Total_Saponin *quant,
        }
        data.update(data1)
    if PP.objects.filter(name = Name).count() > 0:
        sd = PP.objects.get(name = Name)

        data1 = {
            "Chlorogenic"  : sd.Chlorogenic *quant,
            "Ferulic" : sd.Ferulic *quant,
            "Apigenin" : sd.Apigenin *quant,
            "Apigenin_6_C_gluoside" : sd.Apigenin_6_C_gluoside *quant,
            "Apigenin_7_O_neohesperidoside" : sd.Apigenin_7_O_neohesperidoside *quant,
            "Luteolin" : sd.Luteolin *quant,
            "Kaempferol" : sd.Kaempferol *quant,
            "Quercetin" : sd.Quercetin *quant,
            "Quercetin_3_B_Dglucoside" : sd.Quercetin_3_B_Dglucoside *quant,
            "Quercetin_3_O_rutinoside" : sd.Quercetin_3_O_rutinoside *quant,
            "acid_3_4_Dihydroxy_benzoic" : sd.acid_3_4_Dihydroxy_benzoic *quant,
            "Hydroxy_3_benzaldehyde" : sd.Hydroxy_3_benzaldehyde *quant,
            "Protocatechuic_acid" : sd.Protocatechuic_acid *quant,
            "Vanillic_acid" : sd.Vanillic_acid *quant,
            "Gallic_acid" : sd.Gallic_acid *quant,
            "Cinamic_acid" : sd.Cinamic_acid *quant,
            "O_Coumaric_acid" : sd.O_Coumaric_acid *quant,
            "P_Coumaric_acid" : sd.P_Coumaric_acid *quant,
            "Caffeic_acid" : sd.Caffeic_acid *quant,
            "Quercetin_3_B_galactoside" : sd.Quercetin_3_B_galactoside *quant,
            "Isoramnetin"  : sd.Isoramnetin *quant,
            "Myricetin" : sd.Myricetin *quant,
            "Resvertrol" : sd.Resvertrol *quant,
            "Hesperetin" : sd.Hesperetin *quant,
            "Naringenin" : sd.Naringenin *quant,
            "Hesperdin" : sd.Hesperdin *quant,
            "Daidzein" : sd.Daidzein *quant,
            "Genistein" : sd.Genistein *quant,
            "Epicatechin"  : sd.Epicatechin *quant,
            "Epigallocatechin" : sd.Epigallocatechin *quant,
            "Epigallocatechin_3_gallate" : sd.Epigallocatechin_3_gallate *quant,
            "Catechin" : sd.Catechin *quant,
            "Gallocatechin_gallate" : sd.Gallocatechin_gallate *quant,
            "Gallo_catechin" : sd.Gallo_catechin *quant,
            "Syringic_acid" : sd.Syringic_acid *quant,
            "Sinapinic_acid" : sd.Sinapinic_acid *quant,
            "Ellagic_acid" : sd.Ellagic_acid *quant,
            "Total_polyphenols" : sd.Total_polyphenols *quant,
            "Quercetin_3_B_galactoside" : sd.Quercetin_3_B_galactoside *quant,
        }
        data.update(data1)
    if OA.objects.filter(name = Name).count() > 0:
        sd = OA.objects.get(name = Name)

        data1 = {
            "Oxalate_soluble" : sd.Oxalate_soluble *quant,
            "Oxalate_insoluble" : sd.Oxalate_insoluble *quant,
            "Cis_Aconitic" : sd.Cis_Aconitic *quant,
            "Citric" : sd.Citric *quant,
            "Fumaric" : sd.Fumaric *quant,
            "Mallic" : sd.Mallic *quant,
            "Quinic" : sd.Quinic *quant,
            "Succinic" : sd.Succinic *quant,
            "Tartaric" : sd.Tartaric *quant,
        }
        data.update(data1)
    if CAROTENOIDS.objects.filter(name = Name).count() > 0:
        sd = CAROTENOIDS.objects.get(name = Name)

        data1 = {
            "Lutein" : sd.Lutein *quant,
            "Zeaxanthin" : sd.Zeaxanthin *quant,
            "Lycopene" : sd.Lycopene *quant,
            "BCryptoxanthin" : sd.BCryptoxanthin *quant,
            "G_Carotene" : sd.G_Carotene *quant,
            "A_Carotene" : sd.A_Carotene *quant,
            "B_Carotene" : sd.B_Carotene *quant,
            "Total_Carotenoids" : sd.Total_Carotenoids *quant,
        }
        data.update(data1)
    if MTE.objects.filter(name = Name).count() > 0:
        sd = MTE.objects.get(name = Name)

        data1 = {
            "Aluminium": sd.Aluminium *quant,
            "Arsenic": sd.Arsenic *quant,
            "Cadmium" : sd.Cadmium *quant,
            "Calcium" : sd.Calcium *quant,
            "Chromium": sd.Chromium *quant,
            "Cobalt" : sd.Cobalt *quant,
            "Copper" : sd.Copper *quant,
            "Iron": sd.Iron *quant,
            "Lithium" : sd.Lithium *quant,
            "Magnesium": sd.Magnesium *quant,
            "Mercury" : sd.Mercury *quant,
            "Molebdeum" : sd.Molebdeum *quant,
            "Nickel" : sd.Nickel *quant,
            "Phosphorus": sd.Phosphorus *quant,
            "Potassium": sd.Potassium *quant,
            "Selenium": sd.Selenium *quant,
            "Sodium" : sd.Sodium *quant,
            "Zinc": sd.Zinc *quant,
        }
        data.update(data1)
    if FSV.objects.filter(name = Name).count() > 0:
        sd = FSV.objects.get(name = Name)

        data1 = {
            "ERGCAL": sd.ERGCAL *quant,
            "TocopherolsA" : sd.TocopherolsA *quant,
            "TocopherolsB" : sd.TocopherolsB *quant,
            "TocopherolsG" : sd.TocopherolsG *quant,
            "TocopherolsD" : sd.TocopherolsD *quant,
            "TocotrienolsA" : sd.TocotrienolsA *quant,
            "TocotrienolsB" : sd.TocotrienolsB *quant,
            "TocotrienolsG" : sd.TocotrienolsG *quant,
            "TocotrienolsD" : sd.TocotrienolsD *quant,
            "RETOL": sd.RETOL *quant,
            "CHOCAL": sd.CHOCAL *quant,
            "OHD3_25" : sd.OHD3_25 *quant,
            "VITE" : sd.VITE *quant,
            "VITK1" : sd.VITK1 *quant,
        }

        data.update(data1)
    if WSV.objects.filter(name = Name).count() > 0:
        sd = WSV.objects.get(name = Name)

        data1 = {
            "Thiamine_B1" : sd.Thiamine_B1 *quant,
            "Riboflavin_B2" : sd.Riboflavin_B2 *quant,
            "Niacin_B3" : sd.Niacin_B3 *quant,
            "Pantothenic_Acid_B5" : sd.Pantothenic_Acid_B5 *quant,
            "B6" : sd.B6 *quant,
            "Biotin_B7" : sd.Biotin_B7 *quant,
            "Folates_B9": sd.Folates_B9 *quant,
            "Ascorbic_Acid" : sd.Ascorbic_Acid *quant,
        }
        data.update(data1)
    if PPDF.objects.filter(name = Name).count() > 0:
        sd = PPDF.objects.get(name = Name)

        data1 = {
            "water" : sd.water * quant,
            "protein" : sd.protein * quant,
            "ash" : sd.ash * quant,
            "totalfat": sd.totalfat * quant,
            "df_insoluble" : sd.df_insoluble * quant,
            "df_soluble" : sd.df_soluble * quant,
            "carbohydrates" : sd.carbohydrates * quant,
            "energy": sd.energy * quant,
        }
        data.update(data1)
    if AAP.objects.filter(name = Name).count() > 0:
        sd = AAP.objects.get(name = Name)

        data1 = {
            "Histidine" : sd.Histidine * quant ,
            "Isoleucine" : sd.Isoleucine * quant ,
            "Luecine" : sd.Luecine * quant,
            "Lysine" : sd.Lysine *quant ,
            "Methionine" : sd.Methionine * quant,
            "Cystine" : sd.Cystine *quant,
            "Phenylalanine" : sd.Phenylalanine *quant,
            "Threonine" : sd.Threonine * quant,
            "Tryptophan"  :sd.Tryptophan * quant,
            "Valine"  : sd.Valine *quant,
            "Alanine" : sd.Alanine *quant,
            "Arginine" : sd.Arginine *quant,
            "Aspartic" : sd.Aspartic *quant,
            "Glutamic" : sd.Glutamic *quant,
            "Glycine" : sd.Glycine *quant,
            "Proline" : sd.Proline *quant,
            "Serine" : sd.Serine *quant,
            "Tyrosine" : sd.Tyrosine *quant,
        }
        data.update(data1)
    if SIS.objects.filter(name = Name).count() > 0:
        sd = SIS.objects.get(name = Name)

        data1 = {
            "Starch" : sd.Starch *quant,
            "Fructose" : sd.Fructose *quant,
            "Glucose" : sd.Glucose *quant,
            "Sucrose" : sd.Sucrose *quant,
            "Maltose" : sd.Maltose *quant,
            "Free_Sugars" : sd.Free_Sugars *quant,
            "Total_CHO" : sd.Total_CHO *quant,
        }
        data.update(data1)

    return JsonResponse(data)




