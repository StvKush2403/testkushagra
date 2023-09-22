from rest_framework import serializers

class EmployeeDetails(serializers.Serializer):
    ep_id = serializers.CharField(required = True)
    emp_designation = serializers.CharField(required = True)
    e_age = serializers.IntegerField(required = True)
    e_skills = serializers.CharField(required = True)
    e_softskills = serializers.CharField(required = True)

    class Meta:
        fields = '__all__'

class Kushdetails(serializers.Serializer):
    kush_id = serializers.IntegerField(required = True)
    kush_name = serializers.CharField(required = True)
    kush_designation = serializers.CharField(required = True)
    kush_mob = serializers.IntegerField(required = True)

    class Meta:
        field = '__all__'

class shivadetails(serializers.Serializer):
    shiva_name = serializers.CharField(required = True)
    shiva_designation = serializers.CharField(required = True)

    class Meta:
        field = '__all__'

class updateserializer(serializers.Serializer):
    kush_id = serializers.CharField(required = True)
    kush_name = serializers.CharField(required = False, allow_blank=True, allow_null=True)
    kush_designation = serializers.CharField(required = False, allow_blank=True, allow_null=True)
    kush_mob = serializers.IntegerField(required = False, allow_null=True)

    class Meta:
        field = '__all__'

class funcserializer(serializers.Serializer):
    fun_id = serializers.IntegerField(required = True)
    fun_name = serializers.CharField(required = True)
    fun_work = serializers.CharField(required = True)

    class Meta:
        field = '__all__'

class insertkushagra(serializers.Serializer):
    sun_id = serializers.IntegerField(required = True)
    sun_name = serializers.CharField(required = True)
    sun_designation = serializers.CharField(required = True)
    sun_mob = serializers.IntegerField(required = True)

    class Meta:
        field = '__all__'

class abcserializer(serializers.Serializer):
    murari_id = serializers.IntegerField(required = True)
    murari_name = serializers.CharField(required = True)
    murari_designation = serializers.CharField(required = True)

    class Meta:
        field = '__all__'

class upserializer(serializers.Serializer):
    up_id = serializers.IntegerField(required = True)
    up_name = serializers.CharField(required = True)
    up_designation = serializers.CharField(required = True)

    class Meta:
        field = '__all__'