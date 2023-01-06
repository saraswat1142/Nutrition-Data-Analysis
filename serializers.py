from rest_framework import serializers

from .models import (AAP, CAROTENOIDS, EOF, FAP, FSV, MTE, OA, OPPS, PP, PPDF,
                     SIS, WSV)


class AAPSerializer(serializers.ModelSerializer):

    class Meta:
        model = AAP
        exclude = ('name',)

class CAROTENOIDSSerializer(serializers.ModelSerializer):

    class Meta:
        model = CAROTENOIDS
        exclude = ('name',)

class EOFSerializer(serializers.ModelSerializer):

    class Meta:
        model = EOF
        exclude = ('name',)

class FAPSerializer(serializers.ModelSerializer):

    class Meta:
        model = FAP
        exclude = ('name',)

class FSVSerializer(serializers.ModelSerializer):

    class Meta:
        model = FSV
        exclude = ('name',)

class MTESerializer(serializers.ModelSerializer):

    class Meta:
        model = MTE
        exclude = ('name',)

class OASerializer(serializers.ModelSerializer):

    class Meta:
        model = OA
        exclude = ('name',)

class OPPSSerializer(serializers.ModelSerializer):

    class Meta:
        model = OPPS
        exclude = ('name',)

class PPSerializer(serializers.ModelSerializer):

    class Meta:
        model = PP
        exclude = ('name',)

class WSVerializer(serializers.ModelSerializer):

    class Meta:
        model = WSV
        exclude = ('name',)

class SISSerializer(serializers.ModelSerializer):

    class Meta:
        model = SIS
        exclude = ('name',)

class PPDFSerializer(serializers.ModelSerializer):

    class Meta:
        model = PPDF
        exclude = ('name',)


