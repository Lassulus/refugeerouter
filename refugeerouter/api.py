from .models import Flat, Group, Refugee
from rest_framework import permissions, serializers, viewsets, routers


class RefugeeSerializer(serializers.ModelSerializer):
    is_adult = serializers.SerializerMethodField()
    is_male = serializers.SerializerMethodField()

    def get_is_adult(self, refugee):
        return refugee.age > 17

    def get_is_male(self, refugee):
        return refugee.gender == Refugee.GENDER_MALE

    class Meta:
        model = Refugee
        exclude = [ 'group' ]


class GroupSerializer(serializers.ModelSerializer):
    refugees = RefugeeSerializer(many=True)
    num_children = serializers.SerializerMethodField()
    num_adults = serializers.SerializerMethodField()

    def get_num_children(self, group):
        return len(group.refugees.filter(age__gt=17))

    def get_num_adults(self, group):
        return len(group.refugees.exclude(age__gt=17))

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


class FlatSerializer(serializers.ModelSerializer):

    class Meta:
        model = Flat
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


class FlatViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Flat.objects.all()
    serializer_class = FlatSerializer
    permission_classes = [permissions.IsAuthenticated]


router = routers.DefaultRouter()
router.register(r'refugees', RefugeeViewSet)
router.register(r'groups', GroupViewSet)
router.register(r'flats', FlatViewSet)
