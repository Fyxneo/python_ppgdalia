from rest_framework import serializers
from prediction.models import Activity

class ActivitySerializer(serializers.Serializer):
    BVP = serializers.FloatField()
    wrist_ACC_X = serializers.FloatField()
    wrist_ACC_Y = serializers.FloatField()
    wrist_ACC_Z = serializers.FloatField()
    EDA = serializers.FloatField()
    chest_ACC_X = serializers.FloatField()
    chest_ACC_Y = serializers.FloatField()
    chest_ACC_Z = serializers.FloatField()
    chest_ECG = serializers.FloatField()
    chest_EMG = serializers.FloatField()
    chest_EDA = serializers.FloatField()
    chest_Temp = serializers.FloatField()
    chest_Resp = serializers.FloatField()
    rpeaks = serializers.FloatField()
    WEIGHT = serializers.FloatField()
    AGE = serializers.FloatField()
    HEIGHT = serializers.FloatField()
    SKIN = serializers.FloatField()
    SPORT = serializers.FloatField()
    f = serializers.FloatField()
    m = serializers.FloatField()
    Activities = serializers.FloatField(allow_null=True)

    def create(self, validated_data):
        return(Activity.objects.create(**validated_data))

    def update(self, instance, validated_date):
        instance.BVP = validated_data.get('BVP', instance.BVP)
        instance.wrist_ACC_X = validated_data.get('wrist_ACC_X', instance.wrist_ACC_X)
        instance.wrist_ACC_Y = validated_data.get('wrist_ACC_Y', instance.wrist_ACC_Y)
        instance.wrist_ACC_Z = validated_data.get('wrist_ACC_Z', instance.wrist_ACC_Z)
        instance.EDA = validated_data.get('EDA', instance.EDA)
        instance.chest_ACC_X = validated_data.get('chest_ACC_X', instance.chest_ACC_X)
        instance.chest_ACC_Y = validated_data.get('chest_ACC_Y', instance.chest_ACC_Y)
        instance.chest_ACC_Z = validated_data.get('chest_ACC_Z', instance.chest_ACC_Z)
        instance.chest_ECG = validated_data.get('chest_ECG', instance.chest_ECG)
        instance.chest_EMG = validated_data.get('chest_EMG', instance.chest_EMG)
        instance.chest_EDA = validated_data.get('chest_EDA', instance.chest_EDA)
        instance.chest_Temp = validated_data.get('chest_Temp', instance.chest_Temp)
        instance.chest_Resp = validated_data.get('chest_Resp', instance.chest_Resp)
        instance.rpeaks = validated_rpeaks.get('rpeaks', instance.rpeaks)
        instance.WEIGHT = validated_data.get('WEIGHT', instance.WEIGHT)
        instance.AGE = validated_data.get('AGE', instance.AGE)
        instance.HEIGHT = validated_data.get('HEIGHT', instance.HEIGHT)
        instance.SKIN = validated_data.get('SKIN', instance.SKIN)
        instance.SPORT = validated_data.get('SPORT', instance.SPORT)
        instance.f = validated_data.get('f', instance.f)
        instance.m = validated_data.get('m', instance.m)
        instance.Activities = validated_data.gey('Activities', instance.Activities)
	
        instance.save()
        
        return(instance)
    
