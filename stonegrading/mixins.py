from django.contrib.auth import get_user_model
from django.db import models

from .grades import (
    ClarityGrades,
    ColorGrades,
    CuletGrades,
    FluorescenceGrades,
    GeneralGrades,
    GirdleGrades,
    GirdleCondition,
    DiamondDescription,
)

from .models import Inclusion

User = get_user_model()


class BasicGradingMixin(models.Model):
    diamond_description = models.CharField(choices=DiamondDescription.CHOICES)

    grader_1 = models.ForeignKey(User, on_delete=models.PROTECT, related_name="grader_1_for_stone")
    grader_2 = models.ForeignKey(
        User, on_delete=models.PROTECT, related_name="grader_2_for_stone", blank=True, null=True
    )
    grader_3 = models.ForeignKey(
        User, on_delete=models.PROTECT, related_name="grader_3_for_stone", blank=True, null=True
    )

    basic_carat = models.DecimalField(max_digits=5, decimal_places=3)

    basic_color_1 = models.CharField(choices=ColorGrades.CHOICES, max_length=1)
    basic_color_2 = models.CharField(choices=ColorGrades.CHOICES, max_length=1, null=True)
    basic_color_3 = models.CharField(choices=ColorGrades.CHOICES, max_length=1, null=True)
    basic_final_color = models.CharField(choices=ColorGrades.CHOICES, max_length=1)

    basic_clarity_1 = models.CharField(choices=ClarityGrades.CHOICES, max_length=4)
    basic_clarity_2 = models.CharField(choices=ClarityGrades.CHOICES, max_length=4, null=True)
    basic_clarity_3 = models.CharField(choices=ClarityGrades.CHOICES, max_length=4, null=True)
    basic_final_clarity = models.CharField(choices=ClarityGrades.CHOICES, max_length=4)

    basic_fluorescence_1 = models.CharField(choices=FluorescenceGrades.CHOICES, max_length=4)
    basic_fluorescence_2 = models.CharField(choices=FluorescenceGrades.CHOICES, max_length=4, null=True)
    basic_fluorescence_3 = models.CharField(choices=FluorescenceGrades.CHOICES, max_length=4, null=True)
    basic_final_fluorescence = models.CharField(choices=FluorescenceGrades.CHOICES, max_length=4)

    basic_culet_1 = models.CharField(choices=CuletGrades.CHOICES, max_length=2)
    basic_culet_2 = models.CharField(choices=CuletGrades.CHOICES, max_length=2, null=True)
    basic_culet_3 = models.CharField(choices=CuletGrades.CHOICES, max_length=2, null=True)
    basic_final_culet = models.CharField(choices=CuletGrades.CHOICES, max_length=2)

    basic_culet_characteristic_1 = models.CharField(choices=CuletCharacteristics.CHOICES, max_length=5)
    basic_culet_characteristic_2 = models.CharField(choices=CuletCharacteristics.CHOICES, max_length=5, null=True)
    basic_culet_characteristic_3 = models.CharField(choices=CuletCharacteristics.CHOICES, max_length=5, null=True)
    basic_final_culet_characteristic = models.CharField(choices=CuletCharacteristics.CHOICES, max_length=5)

    basic_girdle_characteristic_1 = models.CharField(choices=GirdleCharacteristics.CHOICES, max_length=3)
    basic_girdle_characteristic_2 = models.CharField(choices=GirdleCharacteristics.CHOICES, max_length=3, null=True)
    basic_girdle_characteristic_3 = models.CharField(choices=GirdleCharacteristics.CHOICES, max_length=3, null=True)
    basic_final_girdle_characteristic = models.CharField(choices=GirdleCharacteristics.CHOICES, max_length=3)

    basic_inclusions_1 = models.ManyToManyField(Inclusion, related_name="basic_inclusions")
    basic_inclusions_2 = models.ManyToManyField(Inclusion, related_name="basic_inclusions", null=True)
    basic_inclusions_3 = models.ManyToManyField(Inclusion, related_name="basic_inclusions", null=True)
    basic_final_inclusions = models.ManyToManyField(Inclusion, related_name="basic_inclusions")

    basic_polish_1 = models.CharField(choices=GeneralGrades.CHOICES, max_length=4)
    basic_polish_2 = models.CharField(choices=GeneralGrades.CHOICES, max_length=4, null=True)
    basic_polish_3 = models.CharField(choices=GeneralGrades.CHOICES, max_length=4, null=True)
    basic_final_polish = models.CharField(choices=GeneralGrades.CHOICES, max_length=4)

    diameter_min = models.DecimalField(max_digits=5, decimal_places=2)
    diameter_max = models.DecimalField(max_digits=5, decimal_places=2)
    height = models.DecimalField(max_digits=5, decimal_places=2)

    table_size = models.DecimalField(max_digits=4, decimal_places=1)
    crown_angle = models.DecimalField(max_digits=4, decimal_places=2)
    pavilion_angle = models.DecimalField(max_digits=4, decimal_places=2)
    star_length = models.DecimalField(max_digits=4, decimal_places=1)
    lower_half = models.DecimalField(max_digits=4, decimal_places=1)

    # there are also descriptions / grades later
    girdle_thickness_number = models.DecimalField(max_digits=4, decimal_places=2)
    girdle_min_number = models.DecimalField(max_digits=4, decimal_places=2)
    girdle_max_number = models.DecimalField(max_digits=4, decimal_places=2)

    culet_size = models.DecimalField(max_digits=4, decimal_places=2)
    crown_height = models.DecimalField(max_digits=4, decimal_places=2)

    pavilion_depth = models.DecimalField(max_digits=4, decimal_places=2)
    total_depth = models.DecimalField(max_digits=4, decimal_places=2)

    table_size_rounded = models.IntegerField()
    table_size_rounded_grade = models.CharField(choices=GeneralGrades.CHOICES, max_length=4)

    crown_angle_rounded = models.DecimalField(max_digits=4, decimal_places=1)
    crown_angle_rounded_grade = models.CharField(choices=GeneralGrades.CHOICES, max_length=4)

    pavilion_angle_rounded = models.DecimalField(max_digits=4, decimal_places=1)
    pavilion_angle_rounded_grade = models.CharField(choices=GeneralGrades.CHOICES, max_length=4)

    star_length_rounded = models.IntegerField(null=True, blank=True)
    star_length_rounded_grade = models.CharField(choices=GeneralGrades.CHOICES, max_length=4, null=True, blank=True)

    lower_half_rounded = models.IntegerField()
    lower_half_rounded_grade = models.CharField(choices=GeneralGrades.CHOICES, max_length=4)

    girdle_thickness_rounded = models.DecimalField(max_digits=4, decimal_places=1)
    girdle_thickness_rounded_grade = models.CharField(
        choices=GeneralGrades.CHOICES, max_length=4, null=True, blank=True
    )
    girdle_min_grade = models.CharField(choices=GirdleGrades.CHOICES, max_length=10)
    girdle_max_grade = models.CharField(choices=GirdleGrades.CHOICES, max_length=10)
    girdle_grade = models.CharField(choices=GeneralGrades.CHOICES, max_length=4)
    girdle_condition = models.CharField(choices=GirdleCondition.CHOICES, max_length=15)

    culet_size_description = models.CharField(choices=CuletGrades.MULTI_CHOICES, max_length=5)

    crown_height_rounded = models.DecimalField(max_digits=4, decimal_places=1)
    crown_height_rounded_grade = models.CharField(choices=GeneralGrades.CHOICES, max_length=4)

    pavilion_depth_rounded = models.DecimalField(max_digits=4, decimal_places=1)

    total_depth_rounded = models.DecimalField(max_digits=4, decimal_places=1)
    total_depth_rounded_grade = models.CharField(choices=GeneralGrades.CHOICES, max_length=4)

    star_length_rounded = models.DecimalField(max_digits=4, decimal_places=1)
    star_length_rounded_grade = models.CharField(choices=GeneralGrades.CHOICES, max_length=4)

    # TODO fix these names
    lowest_individual_cut_grade = models.CharField(choices=GeneralGrades.CHOICES, max_length=4)
    est_table_cut_grade = models.CharField(choices=GeneralGrades.CHOICES, max_length=4)
    gradia_cut_pre_polish_symmetry = models.CharField(choices=GeneralGrades.CHOICES, max_length=4)
    basic_final_cut = models.CharField(choices=GeneralGrades.CHOICES, max_length=4)

    sarine_cut_pre_polish_symmetry = models.CharField(choices=GeneralGrades.CHOICES, max_length=4)
    sarine_cut_post_polish_symmetry = models.CharField(
        choices=GeneralGrades.CHOICES, max_length=4, null=True, blank=True
    )

    # TODO: fix with gradia symmetry
    sarine_symmetry = models.CharField(choices=GeneralGrades.CHOICES, max_length=4)

    roundness = models.DecimalField(max_digits=4, decimal_places=1)
    roundness_grade = models.CharField(choices=GeneralGrades.CHOICES, max_length=4)
    table_size_dev = models.DecimalField(max_digits=4, decimal_places=1)
    table_size_dev_grade = models.CharField(choices=GeneralGrades.CHOICES, max_length=4)

    crown_angle_dev = models.DecimalField(max_digits=4, decimal_places=1)
    crown_angle_dev_grade = models.CharField(choices=GeneralGrades.CHOICES, max_length=4)
    pavilion_angle_dev = models.DecimalField(max_digits=4, decimal_places=1)
    pavilion_angle_dev_grade = models.CharField(choices=GeneralGrades.CHOICES, max_length=4)
    star_length_dev = models.DecimalField(max_digits=4, decimal_places=1)
    star_length_dev_grade = models.CharField(choices=GeneralGrades.CHOICES, max_length=4)
    lower_half_dev = models.DecimalField(max_digits=4, decimal_places=1)
    lower_half_dev_grade = models.CharField(choices=GeneralGrades.CHOICES, max_length=4)

    girdle_thick_dev = models.DecimalField(max_digits=4, decimal_places=1)
    girdle_thick_dev_grade = models.CharField(choices=GeneralGrades.CHOICES, max_length=4)
    crown_height_dev = models.DecimalField(max_digits=4, decimal_places=1)
    crown_height_dev_grade = models.CharField(choices=GeneralGrades.CHOICES, max_length=4)
    pavilion_depth_dev = models.DecimalField(max_digits=4, decimal_places=1)
    pavilion_depth_dev_grade = models.CharField(choices=GeneralGrades.CHOICES, max_length=4)

    misalignment = models.DecimalField(max_digits=4, decimal_places=1)
    misalignment_grade = models.CharField(choices=GeneralGrades.CHOICES, max_length=4)

    table_edge_var = models.DecimalField(max_digits=4, decimal_places=1)
    table_edge_var_grade = models.CharField(choices=GeneralGrades.CHOICES, max_length=4)

    table_off_center = models.DecimalField(max_digits=4, decimal_places=1)
    table_off_center_grade = models.CharField(choices=GeneralGrades.CHOICES, max_length=4)

    culet_off_center = models.DecimalField(max_digits=4, decimal_places=1)
    culet_off_center_grade = models.CharField(choices=GeneralGrades.CHOICES, max_length=4)

    table_off_culet = models.DecimalField(max_digits=4, decimal_places=1)
    table_off_culet_grade = models.CharField(choices=GeneralGrades.CHOICES, max_length=4)

    star_angle = models.DecimalField(max_digits=4, decimal_places=1)
    star_angle_grade = models.CharField(choices=GeneralGrades.CHOICES, max_length=4)

    upper_half_angle = models.DecimalField(max_digits=4, decimal_places=1)
    upper_half_angle_grade = models.CharField(choices=GeneralGrades.CHOICES, max_length=4)
    lower_half_angle = models.DecimalField(max_digits=4, decimal_places=1)
    lower_half_angle_grade = models.CharField(choices=GeneralGrades.CHOICES, max_length=4)

    class Meta:
        abstract = True


class GWAIGradingMixin(models.Model):
    gw_returned_date = models.DateTimeField(null=True, blank=True)
    gw_carat = models.DecimalField(max_digits=5, decimal_places=3, null=True, blank=True)
    gw_repolish_carat = models.DecimalField(max_digits=5, decimal_places=3, null=True, blank=True)
    gw_fluorescence = models.CharField(choices=FluorescenceGrades.CHOICES, max_length=4, null=True, blank=True)
    gw_color = models.CharField(choices=ColorGrades.CHOICES, max_length=1, null=True, blank=True)
    gw_clarity = models.CharField(choices=ClarityGrades.CHOICES, max_length=4, null=True, blank=True)
    gw_culet = models.CharField(choices=CuletGrades.CHOICES, max_length=2, null=True, blank=True)

    class Meta:
        abstract = True


class PostGWGradingMixin(models.Model):
    date_to_gw = models.DateTimeField(null=True, blank=True)
    post_gw_final_carat = models.DecimalField(max_digits=5, decimal_places=3, null=True, blank=True)
    post_gw_final_color = models.CharField(choices=ColorGrades.CHOICES, max_length=1, null=True, blank=True)
    post_gw_final_clarity = models.CharField(choices=ClarityGrades.CHOICES, max_length=4)
    post_gw_fluorescence = models.CharField(choices=FluorescenceGrades.CHOICES, max_length=4, null=True, blank=True)
    post_gw_culet = models.CharField(choices=CuletGrades.CHOICES, max_length=2)

    post_gw_rejection = models.TextField(null=True, blank=True)

    post_gw_inclusions = models.ManyToManyField(Inclusion, related_name="post_gw_inclusions")

    class Meta:
        abstract = True


class GIAGradingMixin(models.Model):
    gia_returned_date = models.DateTimeField(null=True, blank=True)
    gia_color = models.CharField(choices=ColorGrades.CHOICES, max_length=1, null=True, blank=True)
    post_gia_final_color = models.CharField(choices=ColorGrades.CHOICES, max_length=1, null=True, blank=True)
    gia_material_testing = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        abstract = True
