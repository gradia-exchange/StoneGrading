from stonegrading.models import Inclusion, Inclusions


def inclusion_fixtures():
    """
    Initial data for inclusions
    :return:
    """
    for inc_db_name, inc_display_name in Inclusions.CHOICES:
        Inclusion.objects.create(inclusion=inc_db_name)
