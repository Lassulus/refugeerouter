from .models import Group, Refugee
from rest_framework import permissions, serializers, viewsets, routers


class RefugeeSerializer(serializers.ModelSerializer):
    is_adult = serializers.SerializerMethodField()
    is_male = serializers.SerializerMethodField()

    def get_is_adult(self, refugee):
        return refugee.age > 18

    def get_is_male(self, refugee):
        return refugee.gender == Refugee.GENDER_MALE

    class Meta:
        model = Refugee
        fields = '__all__'


class GroupSerializer(serializers.ModelSerializer):
    refugees = RefugeeSerializer(many=True)

    class Meta:
        model = Group
        fields = '__all__'


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
