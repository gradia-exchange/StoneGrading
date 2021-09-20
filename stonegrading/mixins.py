from django.contrib.auth import get_user_model
from django.db import models

from .grades import (
    ClarityGrades,
    ColorGrades,
    CuletGrades,
    FluorescenceGrades,
    GeneralGrades,
    GirdleGrades,
    CuletCharacteristics,
    GirdleCondition,
    DiamondDescription,
)

from .models import Inclusion

User = get_user_model()


class BasicGradingMixin(models.Model):
    basic_diamond_description = models.CharField(
        choices=DiamondDescription.CHOICES, max_length=15, blank=True, null=True
    )

    basic_grader_1 = models.ForeignKey(
        User, on_delete=models.PROTECT, related_name="basic_grader_1", blank=True, null=True
    )
    basic_grader_2 = models.ForeignKey(
        User, on_delete=models.PROTECT, related_name="basic_grader_2", blank=True, null=True
    )
    basic_grader_3 = models.ForeignKey(
        User, on_delete=models.PROTECT, related_name="basic_grader_3", blank=True, null=True
    )

    basic_carat = models.DecimalField(max_digits=5, decimal_places=3, blank=True, null=True)

    basic_color_1 = models.CharField(choices=ColorGrades.CHOICES, max_length=2, blank=True, null=True)
    basic_color_2 = models.CharField(choices=ColorGrades.CHOICES, max_length=2, blank=True, null=True)
    basic_color_3 = models.CharField(choices=ColorGrades.CHOICES, max_length=2, blank=True, null=True)
    basic_color_final = models.CharField(choices=ColorGrades.CHOICES, max_length=2, blank=True, null=True)

    basic_clarity_1 = models.CharField(choices=ClarityGrades.CHOICES, max_length=5, blank=True, null=True)
    basic_clarity_2 = models.CharField(choices=ClarityGrades.CHOICES, max_length=5, blank=True, null=True)
    basic_clarity_3 = models.CharField(choices=ClarityGrades.CHOICES, max_length=5, blank=True, null=True)
    basic_clarity_final = models.CharField(choices=ClarityGrades.CHOICES, max_length=5, blank=True, null=True)

    basic_fluorescence_1 = models.CharField(choices=FluorescenceGrades.CHOICES, max_length=4, blank=True, null=True)
    basic_fluorescence_2 = models.CharField(choices=FluorescenceGrades.CHOICES, max_length=4, blank=True, null=True)
    basic_fluorescence_3 = models.CharField(choices=FluorescenceGrades.CHOICES, max_length=4, blank=True, null=True)
    basic_fluorescence_final = models.CharField(
        choices=FluorescenceGrades.CHOICES, max_length=4, blank=True, null=True
    )

    basic_culet_1 = models.CharField(choices=CuletGrades.CHOICES, max_length=2, blank=True, null=True)
    basic_culet_2 = models.CharField(choices=CuletGrades.CHOICES, max_length=2, blank=True, null=True)
    basic_culet_3 = models.CharField(choices=CuletGrades.CHOICES, max_length=2, blank=True, null=True)
    basic_culet_final = models.CharField(choices=CuletGrades.CHOICES, max_length=2, blank=True, null=True)

    basic_culet_characteristic_1 = models.CharField(
        choices=CuletCharacteristics.CHOICES, max_length=5, blank=True, null=True
    )
    basic_culet_characteristic_2 = models.CharField(
        choices=CuletCharacteristics.CHOICES, max_length=5, blank=True, null=True
    )
    basic_culet_characteristic_3 = models.CharField(
        choices=CuletCharacteristics.CHOICES, max_length=5, blank=True, null=True
    )
    basic_culet_characteristic_final = models.CharField(
        choices=CuletCharacteristics.CHOICES, max_length=5, blank=True, null=True
    )

    basic_girdle_condition_1 = models.CharField(choices=GirdleCondition.CHOICES, max_length=3, blank=True, null=True)
    basic_girdle_condition_2 = models.CharField(choices=GirdleCondition.CHOICES, max_length=3, blank=True, null=True)
    basic_girdle_condition_3 = models.CharField(choices=GirdleCondition.CHOICES, max_length=3, blank=True, null=True)
    basic_girdle_condition_final = models.CharField(
        choices=GirdleCondition.CHOICES, max_length=3, blank=True, null=True
    )

    basic_inclusions_1 = models.ManyToManyField(Inclusion, related_name="basic_inclusions_1", blank=True)
    basic_inclusions_2 = models.ManyToManyField(Inclusion, related_name="basic_inclusions_2", blank=True)
    basic_inclusions_3 = models.ManyToManyField(Inclusion, related_name="basic_inclusions_3", blank=True)
    basic_inclusions_final = models.ManyToManyField(Inclusion, related_name="basic_inclusions_final", blank=True)

    basic_polish_1 = models.CharField(choices=GeneralGrades.CHOICES, max_length=4, blank=True, null=True)
    basic_polish_2 = models.CharField(choices=GeneralGrades.CHOICES, max_length=4, blank=True, null=True)
    basic_polish_3 = models.CharField(choices=GeneralGrades.CHOICES, max_length=4, blank=True, null=True)
    basic_polish_final = models.CharField(choices=GeneralGrades.CHOICES, max_length=4, blank=True, null=True)

    basic_girdle_min_grade_final = models.CharField(
        choices=GirdleGrades.CHOICES, max_length=10, blank=True, null=True
    )

    basic_remarks = models.TextField(blank=True, null=True, default="")

    class Meta:
        abstract = True


class SarineGradingMixin(models.Model):
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
    crown_angle_rounded = models.DecimalField(max_digits=4, decimal_places=1)

    pavilion_angle_rounded = models.DecimalField(max_digits=4, decimal_places=1)
    star_length_rounded = models.IntegerField(null=True, blank=True)

    lower_half_rounded = models.IntegerField()
    girdle_thickness_rounded = models.DecimalField(max_digits=4, decimal_places=1)

    girdle_min_grade = models.CharField(choices=GirdleGrades.CHOICES, max_length=10)
    girdle_max_grade = models.CharField(choices=GirdleGrades.CHOICES, max_length=10)

    culet_size_description = models.CharField(choices=CuletGrades.MULTI_CHOICES, max_length=5)

    crown_height_rounded = models.DecimalField(max_digits=4, decimal_places=1)

    pavilion_depth_rounded = models.DecimalField(max_digits=4, decimal_places=1)

    total_depth_rounded = models.DecimalField(max_digits=4, decimal_places=1)

    sarine_cut_pre_polish_symmetry = models.CharField(choices=GeneralGrades.CHOICES, max_length=4)

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


class GWGradingMixin(models.Model):
    date_from_gw = models.DateTimeField(null=True, blank=True)
    gw_return_reweight = models.DecimalField(max_digits=5, decimal_places=3, null=True, blank=True)
    gw_color = models.CharField(choices=ColorGrades.CHOICES, max_length=2, null=True, blank=True)
    gw_clarity = models.CharField(choices=ClarityGrades.CHOICES, max_length=5, null=True, blank=True)
    gw_fluorescence = models.CharField(choices=FluorescenceGrades.CHOICES, max_length=5, null=True, blank=True)
    gw_remarks = models.TextField(blank=True, null=True, default="")

    class Meta:
        abstract = True


class GWGradingAdjustMixin(models.Model):
    gw_adjust_grader_1 = models.ForeignKey(
        User, on_delete=models.PROTECT, related_name="gw_adjust_grader_1", blank=True, null=True
    )
    gw_adjust_grader_2 = models.ForeignKey(
        User, on_delete=models.PROTECT, related_name="gw_adjust_grader_2", blank=True, null=True
    )
    gw_adjust_grader_3 = models.ForeignKey(
        User, on_delete=models.PROTECT, related_name="gw_adjust_grader_3", blank=True, null=True
    )
    gw_color_adjusted_1 = models.CharField(choices=ColorGrades.CHOICES, max_length=2, null=True, blank=True)
    gw_color_adjusted_2 = models.CharField(choices=ColorGrades.CHOICES, max_length=2, null=True, blank=True)
    gw_color_adjusted_3 = models.CharField(choices=ColorGrades.CHOICES, max_length=2, null=True, blank=True)
    gw_color_adjusted_final = models.CharField(choices=ColorGrades.CHOICES, max_length=2, null=True, blank=True)

    gw_clarity_adjusted_1 = models.CharField(choices=ClarityGrades.CHOICES, max_length=5, null=True, blank=True)
    gw_clarity_adjusted_2 = models.CharField(choices=ClarityGrades.CHOICES, max_length=5, null=True, blank=True)
    gw_clarity_adjusted_3 = models.CharField(choices=ClarityGrades.CHOICES, max_length=5, null=True, blank=True)
    gw_clarity_adjusted_final = models.CharField(choices=ClarityGrades.CHOICES, max_length=5, null=True, blank=True)

    gw_fluorescence_adjusted_1 = models.CharField(
        choices=FluorescenceGrades.CHOICES, max_length=4, null=True, blank=True
    )
    gw_fluorescence_adjusted_2 = models.CharField(
        choices=FluorescenceGrades.CHOICES, max_length=4, null=True, blank=True
    )
    gw_fluorescence_adjusted_3 = models.CharField(
        choices=FluorescenceGrades.CHOICES, max_length=4, null=True, blank=True
    )
    gw_fluorescence_adjusted_final = models.CharField(
        choices=FluorescenceGrades.CHOICES, max_length=4, null=True, blank=True
    )

    gw_adjust_remarks = models.TextField(blank=True, null=True, default="")

    class Meta:
        abstract = True


class GIAGradingMixin(models.Model):
    date_from_gia = models.DateTimeField(null=True, blank=True)
    gia_color = models.CharField(choices=ColorGrades.CHOICES, max_length=2, null=True, blank=True)
    post_gia_final_color = models.CharField(choices=ColorGrades.CHOICES, max_length=2, null=True, blank=True)
    gia_material_testing = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        abstract = True


class GIAGradingAdjustMixin(models.Model):
    gia_adjust_grader_1 = models.ForeignKey(
        User, on_delete=models.PROTECT, related_name="gia_adjust_grader_1", blank=True, null=True
    )
    gia_adjust_grader_2 = models.ForeignKey(
        User, on_delete=models.PROTECT, related_name="gia_adjust_grader_2", blank=True, null=True
    )
    gia_adjust_grader_3 = models.ForeignKey(
        User, on_delete=models.PROTECT, related_name="gia_adjust_grader_3", blank=True, null=True
    )
    gia_color_adjusted_1 = models.CharField(choices=ColorGrades.CHOICES, max_length=2, null=True, blank=True)
    gia_color_adjusted_2 = models.CharField(choices=ColorGrades.CHOICES, max_length=2, null=True, blank=True)
    gia_color_adjusted_3 = models.CharField(choices=ColorGrades.CHOICES, max_length=2, null=True, blank=True)
    gia_color_adjusted_final = models.CharField(choices=ColorGrades.CHOICES, max_length=2, null=True, blank=True)

    gia_polish_adjusted_1 = models.CharField(choices=GeneralGrades.CHOICES, max_length=4, null=True, blank=True)
    gia_polish_adjusted_2 = models.CharField(choices=GeneralGrades.CHOICES, max_length=4, null=True, blank=True)
    gia_polish_adjusted_3 = models.CharField(choices=GeneralGrades.CHOICES, max_length=4, null=True, blank=True)
    gia_polish_adjusted_final = models.CharField(choices=GeneralGrades.CHOICES, max_length=4, null=True, blank=True)

    gia_culet_adjusted_1 = models.CharField(choices=CuletGrades.CHOICES, max_length=2, blank=True, null=True)
    gia_culet_adjusted_2 = models.CharField(choices=CuletGrades.CHOICES, max_length=2, blank=True, null=True)
    gia_culet_adjusted_3 = models.CharField(choices=CuletGrades.CHOICES, max_length=2, blank=True, null=True)
    gia_culet_adjusted_final = models.CharField(choices=CuletGrades.CHOICES, max_length=2, blank=True, null=True)

    gia_culet_characteristic_1 = models.CharField(
        choices=CuletCharacteristics.CHOICES, max_length=5, blank=True, null=True
    )
    gia_culet_characteristic_2 = models.CharField(
        choices=CuletCharacteristics.CHOICES, max_length=5, blank=True, null=True
    )
    gia_culet_characteristic_3 = models.CharField(
        choices=CuletCharacteristics.CHOICES, max_length=5, blank=True, null=True
    )
    gia_culet_characteristic_final = models.CharField(
        choices=CuletCharacteristics.CHOICES, max_length=5, blank=True, null=True
    )

    gia_adjust_remarks = models.TextField(blank=True, null=True, default="")

    class Meta:
        abstract = True


class AutoGradeMixin(models.Model):
    auto_table_size_rounded_grade = models.CharField(
        choices=GeneralGrades.CHOICES, max_length=4, null=True, blank=True
    )
    auto_crown_angle_rounded_grade_grade = models.CharField(
        choices=GeneralGrades.CHOICES, max_length=4, null=True, blank=True
    )
    auto_pavilion_angle_rounded_grade = models.CharField(
        choices=GeneralGrades.CHOICES, max_length=4, null=True, blank=True
    )
    auto_star_length_rounded_grade = models.CharField(
        choices=GeneralGrades.CHOICES, max_length=4, null=True, blank=True
    )
    auto_lower_half_rounded_grade = models.CharField(
        choices=GeneralGrades.CHOICES, max_length=4, null=True, blank=True
    )
    auto_girdle_thick_rounded_grade = models.CharField(
        choices=GeneralGrades.CHOICES, max_length=4, null=True, blank=True
    )
    auto_girdle_grade = models.CharField(choices=GeneralGrades.CHOICES, max_length=4, null=True, blank=True)
    auto_crown_height_rounded_grade = models.CharField(
        choices=GeneralGrades.CHOICES, max_length=4, null=True, blank=True
    )
    auto_total_depth_rounded_grade = models.CharField(
        choices=GeneralGrades.CHOICES, max_length=4, null=True, blank=True
    )
    auto_individual_cut_grade_grade = models.CharField(
        choices=GeneralGrades.CHOICES, max_length=4, null=True, blank=True
    )
    auto_est_table_cut_grade_grade = models.CharField(
        choices=GeneralGrades.CHOICES, max_length=4, null=True, blank=True
    )
    auto_gradia_cut_grade_grade = models.CharField(
        choices=GeneralGrades.CHOICES, max_length=4, null=True, blank=True
    )
    auto_final_sarine_cut_grade = models.CharField(
        choices=GeneralGrades.CHOICES, max_length=4, null=True, blank=True
    )
    auto_final_gradia_cut_grade = models.CharField(
        choices=GeneralGrades.CHOICES, max_length=4, null=True, blank=True
    )

    class Meta:
        abstract = True
