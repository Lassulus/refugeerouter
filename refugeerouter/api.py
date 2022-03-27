from django.urls import reverse
from .models import Group, Refugee
from rest_framework import permissions, serializers, viewsets, routers


class RefugeeSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(allow_null=True)
    is_adult = serializers.SerializerMethodField()
    is_male = serializers.SerializerMethodField()

    def get_is_adult(self, refugee):
        return refugee.age > 17

    def get_is_male(self, refugee):
        return refugee.gender == Refugee.GENDER_MALE

    class Meta:
        model = Refugee
        exclude = ['group']


class GroupSerializer(serializers.ModelSerializer):
    refugees = RefugeeSerializer(many=True)
    children = serializers.SerializerMethodField()
    adults = serializers.SerializerMethodField()
    url = serializers.SerializerMethodField()

    def get_children(self, group):
        return len(group.refugees.filter(age__lte=17))

    def get_adults(self, group):
        return len(group.refugees.exclude(age__lte=17))

    def get_url(self, group):
        return f"<a href=\"{reverse('GroupUpdate', args=[group.id])}\">Link</a>"

    class Meta:
        model = Group
        fields = '__all__'

    def create(self, validated_data):
        print(validated_data)
        refugees_data = validated_data.pop('refugees')
        group = Group.objects.create(**validated_data)
        for refugee_data in refugees_data:
            Refugee.objects.create(group=group, **refugee_data)
        return group


class RefugeeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Refugee.objects.all()
    serializer_class = RefugeeSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]


router = routers.DefaultRouter()
router.register(r'refugees', RefugeeViewSet)
router.register(r'groups', GroupViewSet)
