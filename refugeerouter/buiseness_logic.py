from django.db.models import Max, Min

from refugeerouter.models import Group, Flat, Refugee


def group_fits_in_flat(group: Group, flat: Flat) -> bool:
    refugees_in_group = group.refugee_set.all()
    num_adults = refugees_in_group.filter(age__gte=18).count()

    if flat.max_adults < num_adults:
        return False

    num_males = refugees_in_group.filter(gender=Refugee.GENDER_MALE).count()
    if flat.max_male < num_males:
        return False

    num_kids = refugees_in_group.filter(age__lte=17).count()
    if flat.max_kids < num_kids:
        return False

    if num_kids > 0:
        max_age_kids = refugees_in_group.filter(age__lte=17).aggregate(Max('age')).get('age__max')
        min_age_kids = refugees_in_group.filter(age__lte=17).aggregate(Min('age')).get('age__min')
        if flat.max_kids_age < max_age_kids:
            return False
        if flat.min_kids_age > min_age_kids:
            return False

    return True