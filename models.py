from django.db import models


# Create your models here.
class PPDF(models.Model):
    name = models.CharField(max_length=50, blank=False,unique = True,primary_key=True)
    water = models.FloatField(null = True)
    protein =  models.FloatField(null = True)
    ash =  models.FloatField(null = True)
    totalfat = models.FloatField(null = True)
    df_insoluble =  models.FloatField(null = True)
    df_soluble = models.FloatField(null = True)
    carbohydrates = models.FloatField(null = True)
    energy = models.FloatField(null = True)

    def __str__(self):
        return self.name

class WSV(models.Model):
    name = models.CharField(max_length=50, blank=False,unique = True,primary_key=True)
    Thiamine_B1 = models.FloatField(null = True)
    Riboflavin_B2 = models.FloatField(null = True)
    Niacin_B3 = models.FloatField(null = True)
    Pantothenic_Acid_B5 = models.FloatField(null = True)
    B6 = models.FloatField(null = True)
    Biotin_B7 = models.FloatField(null = True)
    Folates_B9 = models.FloatField(null = True)
    Ascorbic_Acid = models.FloatField(null = True)

    def __str__(self):
        return self.name

class FSV(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False,primary_key=True,unique = True)
    ERGCAL = models.FloatField(null = True)
    TocopherolsA = models.FloatField(null = True)
    TocopherolsB = models.FloatField(null = True)
    TocopherolsG = models.FloatField(null = True)
    TocopherolsD = models.FloatField(null = True)
    TocotrienolsA = models.FloatField(null = True)
    TocotrienolsB = models.FloatField(null = True)
    TocotrienolsG = models.FloatField(null = True)
    TocotrienolsD = models.FloatField(null = True)
    RETOL= models.FloatField(null = True)
    CHOCAL= models.FloatField(null = True)
    OHD3_25 = models.FloatField(null = True)
    VITE = models.FloatField(null = True)
    VITK1 = models.FloatField(null = True)

    def __str__(self):
        return self.name


class CAROTENOIDS(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False,primary_key=True,unique = True)
    Lutein = models.FloatField(null = True)
    Zeaxanthin = models.FloatField(null = True)
    Lycopene = models.FloatField(null = True)
    BCryptoxanthin = models.FloatField(null = True)
    G_Carotene = models.FloatField(null = True)
    A_Carotene = models.FloatField(null = True)
    B_Carotene = models.FloatField(null = True)
    Total_Carotenoids = models.FloatField(null = True)

    def __str__(self):
        return self.name

class MTE(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False,primary_key=True,unique = True)
    Aluminium = models.FloatField(null = True)
    Arsenic = models.FloatField(null = True)
    Cadmium = models.FloatField(null = True)
    Calcium = models.FloatField(null = True)
    Chromium = models.FloatField(null = True)
    Cobalt = models.FloatField(null = True)
    Copper = models.FloatField(null = True)
    Iron = models.FloatField(null = True)
    Lead = models.FloatField(null = True)
    Lithium = models.FloatField(null = True)
    Magnesium  = models.FloatField(null = True)
    Manganese  = models.FloatField(null = True)
    Mercury = models.FloatField(null = True)
    Molebdeum = models.FloatField(null = True)
    Nickel = models.FloatField(null = True)
    Phosphorus = models.FloatField(null = True)
    Potassium = models.FloatField(null = True)
    Selenium = models.FloatField(null = True)
    Sodium = models.FloatField(null = True)
    Zinc = models.FloatField(null = True)

    def __str__(self):
        return self.name


class SIS(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False,primary_key=True,unique = True)
    Starch = models.FloatField(null = True)
    Fructose = models.FloatField(null = True)
    Glucose = models.FloatField(null = True)
    Sucrose = models.FloatField(null = True)
    Maltose = models.FloatField(null = True)
    Free_Sugars = models.FloatField(null = True)
    Total_CHO = models.FloatField(null = True)

    def __str__(self):
        return self.name

class FAP(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False,primary_key=True,unique = True)
    Eicosaenoic = models.FloatField(null = True)
    Erucic = models.FloatField(null = True)
    Nervonic = models.FloatField(null = True)
    Linoleic = models.FloatField(null = True)
    Eicosadienoic = models.FloatField(null = True)
    A_Linolenic = models.FloatField(null = True)
    Arachidonic = models.FloatField(null = True)
    Saturated_Fatty_Acids = models.FloatField(null = True)
    Mono_UnSaturated_Fatty_Acids = models.FloatField(null = True)
    poly_UnSaturated_Fatty_Acids = models.FloatField(null = True)
    Capric = models.FloatField(null = True)
    Lauric = models.FloatField(null = True)
    Myristic = models.FloatField(null = True)
    Palmitic = models.FloatField(null = True)
    Stearic = models.FloatField(null = True)
    Arachidic = models.FloatField(null = True)
    Behenic = models.FloatField(null = True)
    Lignoceric = models.FloatField(null = True)
    Myristoleic = models.FloatField(null = True)
    Palmitoleic = models.FloatField(null = True)
    Oleic = models.FloatField(null = True)
    Undecanoic = models.FloatField(null = True)
    Pentadecanoic = models.FloatField(null = True)
    Docosadienoic = models.FloatField(null = True)
    Eicosatrienoic = models.FloatField(null = True)
    Eicosapentaenoic = models.FloatField(null = True)
    Docosapentaenoic = models.FloatField(null = True)
    Docosahexaenoic = models.FloatField(null = True)
    Cholestrol = models.FloatField(null = True)

    def __str__(self):
        return self.name

class AAP(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False,primary_key=True,unique = True)
    Histidine = models.FloatField(null = True)
    Isoleucine = models.FloatField(null = True)
    Luecine = models.FloatField(null = True)
    Lysine = models.FloatField(null = True)
    Methionine = models.FloatField(null = True)
    Cystine = models.FloatField(null = True)
    Phenylalanine = models.FloatField(null = True)
    Threonine = models.FloatField(null = True)
    Tryptophan = models.FloatField(null = True)
    Valine = models.FloatField(null = True)
    Alanine = models.FloatField(null = True)
    Arginine = models.FloatField(null = True)
    Aspartic = models.FloatField(null = True)
    Glutamic = models.FloatField(null = True)
    Glycine = models.FloatField(null = True)
    Proline = models.FloatField(null = True)
    Serine = models.FloatField(null = True)
    Tyrosine = models.FloatField(null = True)

    def __str__(self):
        return self.name

class OA(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False,primary_key=True,unique = True)
    Oxalate_soluble = models.FloatField(null = True)
    Oxalate_insoluble = models.FloatField(null = True)
    Cis_Aconitic = models.FloatField(null = True)
    Citric = models.FloatField(null = True)
    Fumaric = models.FloatField(null = True)
    Mallic = models.FloatField(null = True)
    Quinic = models.FloatField(null = True)
    Succinic = models.FloatField(null = True)
    Tartaric = models.FloatField(null = True)

    def __str__(self):
        return self.name

class PP(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False,primary_key=True,unique = True)
    Chlorogenic  = models.FloatField(null = True)
    Ferulic = models.FloatField(null = True)
    Apigenin = models.FloatField(null = True)
    Apigenin_6_C_gluoside = models.FloatField(null = True)
    Apigenin_7_O_neohesperidoside = models.FloatField(null = True)
    Luteolin = models.FloatField(null = True)
    Kaempferol = models.FloatField(null = True)
    Quercetin = models.FloatField(null = True)
    Quercetin_3_B_Dglucoside = models.FloatField(null = True)
    Quercetin_3_O_rutinoside = models.FloatField(null = True)
    acid_3_4_Dihydroxy_benzoic = models.FloatField(null = True)
    Hydroxy_3_benzaldehyde = models.FloatField(null = True)
    Protocatechuic_acid = models.FloatField(null = True)
    Vanillic_acid = models.FloatField(null = True)
    Gallic_acid = models.FloatField(null = True)
    Cinamic_acid = models.FloatField(null = True)
    O_Coumaric_acid = models.FloatField(null = True)
    P_Coumaric_acid = models.FloatField(null = True)
    Caffeic_acid = models.FloatField(null = True)
    Quercetin_3_B_galactoside = models.FloatField(null = True)
    Isoramnetin  = models.FloatField(null = True)
    Myricetin = models.FloatField(null = True)
    Resvertrol = models.FloatField(null = True)
    Hesperetin = models.FloatField(null = True)
    Naringenin = models.FloatField(null = True)
    Hesperdin = models.FloatField(null = True)
    Daidzein = models.FloatField(null = True)
    Genistein = models.FloatField(null = True)
    Epicatechin  = models.FloatField(null = True)
    Epigallocatechin = models.FloatField(null = True)
    Epigallocatechin_3_gallate = models.FloatField(null = True)
    Catechin = models.FloatField(null = True)
    Gallocatechin_gallate = models.FloatField(null = True)
    Gallo_catechin = models.FloatField(null = True)
    Syringic_acid = models.FloatField(null = True)
    Sinapinic_acid = models.FloatField(null = True)
    Ellagic_acid = models.FloatField(null = True)
    Total_polyphenols = models.FloatField(null = True)
    Quercetin_3_B_galactoside = models.FloatField(null = True)
    name,acid_3_4_Dihydroxy_benzoic,Hydroxy_3_benzaldehyde,Protocatechuic_acid,Vanillic_acid,Gallic_acid,Cinamic_acid,O_Coumaric_acid,P_Coumaric_acid,Caffeic_acid,Chlorogenic,Ferulic,Apigenin,Apigenin_6_C_gluoside,Apigenin_7_O_neohesperidoside,Luteolin,Kaempferol,Quercetin,Quercetin_3_B_Dglucoside,Quercetin_3_O_rutinoside,Isoramnetin,Myricetin,Resvertrol,Hesperetin,Naringenin,Hesperdin,Daidzein,Genistein,Epicatechin
    def __str__(self):
        return self.name

class OPPS(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False,primary_key=True,unique = True)
    Raffinose = models.FloatField(null = True)
    Stachyose = models.FloatField(null = True)
    Verbascose  = models.FloatField(null = True)
    Ajugose  = models.FloatField(null = True)
    Campesterol  = models.FloatField(null = True)
    Stigmasterol  = models.FloatField(null = True)
    B_Sitosterol = models.FloatField(null = True)
    Phytate = models.FloatField(null = True)
    Total_Saponin = models.FloatField(null = True)

    def __str__(self):
        return self.name

class EOF(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False,primary_key=True,unique = True)
    Butyric = models.FloatField(null = True)
    Caproic = models.FloatField(null = True)
    Caprylic = models.FloatField(null = True)
    Capric = models.FloatField(null = True)
    Lauric = models.FloatField(null = True)
    Myristic = models.FloatField(null = True)
    Palmitic = models.FloatField(null = True)
    Stearic = models.FloatField(null = True)
    Arachidic = models.FloatField(null = True)
    Behenic = models.FloatField(null = True)
    Lignoceric = models.FloatField(null = True)
    Myristoleic = models.FloatField(null = True)
    Palmitoleic = models.FloatField(null = True)
    Elaidic = models.FloatField(null = True)
    Oleic = models.FloatField(null = True)
    Eicosenoic = models.FloatField(null = True)
    Erucic = models.FloatField(null = True)
    Linoleic = models.FloatField(null = True)
    Linolenic = models.FloatField(null = True)
    Saturated_Fatty_Acids = models.FloatField(null = True)
    Mono_Unsaturated_Fatty_Acids = models.FloatField(null = True)
    Poly_Unsaturated_Fatty_Acids = models.FloatField(null = True)

    def __str__(self):
        return self.name