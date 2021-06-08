import itertools


class ColorGrades:
    COLORLESS_D = "D"
    COLORLESS_E = "E"
    COLORLESS_F = "F"
    NEARLY_COLORLESS_G = "G"
    NEARLY_COLORLESS_H = "H"
    NEARLY_COLORLESS_I = "I"
    NEARLY_COLORLESS_J = "J"

    CHOICES = (
        (COLORLESS_D, "D"),
        (COLORLESS_E, "E"),
        (COLORLESS_F, "F"),
        (NEARLY_COLORLESS_G, "G"),
        (NEARLY_COLORLESS_H, "H"),
        (NEARLY_COLORLESS_I, "I"),
        (NEARLY_COLORLESS_J, "J"),
    )


class ClarityGrades:
    INTERNALLY_FLAWLESS = "IF"
    VERY_VERY_SLIGHTLY_INCLUDED_DEGREE_1 = "VVS1"
    VERY_VERY_SLIGHTLY_INCLUDED_DEGREE_2 = "VVS2"
    VERY_SLIGHTLY_INCLUDED_DEGREE_1 = "VS1"
    VERY_SLIGHTLY_INCLUDED_DEGREE_2 = "VS2"
    SLIGHTLY_INCLUDED_DEGREE_1 = "SI1"
    SLIGHTLY_INCLUDED_DEGREE_2 = "SI2"
    INCLUDED = "I1"

    CHOICES = (
        (INTERNALLY_FLAWLESS, "IF"),
        (VERY_VERY_SLIGHTLY_INCLUDED_DEGREE_1, "VVS1"),
        (VERY_VERY_SLIGHTLY_INCLUDED_DEGREE_2, "VVS2"),
        (VERY_SLIGHTLY_INCLUDED_DEGREE_1, "VS1"),
        (VERY_SLIGHTLY_INCLUDED_DEGREE_2, "VS2"),
        (SLIGHTLY_INCLUDED_DEGREE_1, "SI1"),
        (SLIGHTLY_INCLUDED_DEGREE_2, "SI2"),
        (INCLUDED, "I1"),
    )


class GeneralGrades:
    EXCELLENT = "EX"
    VERY_GOOD = "VG"
    GOOD = "GD"
    FAIR = "F"
    POOR = "P"

    CHOICES = ((EXCELLENT, "Excellent"), (VERY_GOOD, "Very Good"), (GOOD, "Good"), (FAIR, "Fair"), (POOR, "Poor"))


class FluorescenceGrades:
    VERY_STRONG = "VS"
    STRONG = "S"
    MEDIUM = "M"
    FAINT = "F"
    NONE = "N"

    CHOICES = (
        (VERY_STRONG, "Very Strong"),
        (STRONG, "Strong"),
        (MEDIUM, "Medium"),
        (FAINT, "Faint"),
        (NONE, "None"),
    )


class GirdleGrades:
    EXTREMELY_THIN = "ETN"
    VERY_THIN = "VTN"
    THIN = "THN"
    MEDIUM = "MED"
    SLIGHTLY_THICK = "STK"
    THICK = "THK"
    VERY_THICK = "VTK"
    EXTREMELY_THICK = "ETK"
    FACETED = "F"
    SMOOTH = "SM"
    EXTREMELY_THIN_TO_VERY_THIN = "ETN TO VTN"

    CHOICES = (
        (EXTREMELY_THIN, "Extremely Thin"),
        (VERY_THIN, "Very Thin"),
        (THIN, "Thin"),
        (MEDIUM, "Medium"),
        (SLIGHTLY_THICK, "Slightly Thick"),
        (THICK, "Thick"),
        (VERY_THICK, "Very Thick"),
        (EXTREMELY_THICK, "Extremely Thick"),
        (FACETED, "Faceted"),
        (SMOOTH, "Smooth"),
        (EXTREMELY_THIN_TO_VERY_THIN, "Extremely thin - very thin"),
    )


class Inclusions:
    BRUISE = "Br"
    CAVITY = "Cv"
    CHIP = "Ch"
    CLEAVAGE = "Clv"
    CLOUD = "Cld"
    CRYSTAL = "Xtl"
    FEATHER = "Ftr"
    GRAIN_CENTER = "GrCnt"
    INDENTED_NATURAL = "IndN"
    INTERNAL_GRAINING = "IntGr"
    KNOT = "K"
    LASER_DRILL_HOLE = "LDH"
    NEEDLE = "Ndl"
    PINPOINT = "Pp"
    TWINNING_WISP = "W"
    ABRASION = "Abr"
    NATURAL = "N"
    NICK = "Nk"
    PIT = "Pit"
    POLISH_LINE = "PL"
    BURN_MASK = "Brn"
    SCRATCH = "S"
    SURFACE_GRAINING = "SGr"
    EXTRA_FEET = "EF"

    CHOICES = (
        (BRUISE, "Bruise"),
        (CAVITY, "Cavity"),
        (CHIP, "Chip"),
        (CLEAVAGE, "Cleavage"),
        (CLOUD, "Cloud"),
        (CRYSTAL, "Xtl"),
        (FEATHER, "Feather"),
        (GRAIN_CENTER, "Grain Center"),
        (INDENTED_NATURAL, "Indented natural"),
        (INTERNAL_GRAINING, "Internal graining"),
        (KNOT, "knot"),
        (LASER_DRILL_HOLE, "Laser Drill Hole"),
        (NEEDLE, "Needle"),
        (PINPOINT, "Pinpoint"),
        (TWINNING_WISP, "Twinning Wisp"),
        (ABRASION, "Abrasion"),
        (NATURAL, "Natural"),
        (NICK, "Nick"),
        (PIT, "Pit"),
        (POLISH_LINE, "Polish Line"),
        (BURN_MASK, "Burn Mask"),
        (SCRATCH, "Scratch"),
        (SURFACE_GRAINING, "Surface Graining"),
        (EXTRA_FEET, "Extra Feet"),
    )


class CuletGrades:
    NONE = "N"
    VERY_SMALL = "VS"
    SMALL = "S"
    MEDIUM = "M"
    SLIGHTLY_LARGE = "SL"
    LARGE = "L"
    VERY_LARGE = "VL"
    EXTREMELY_LARGE = "XL"

    CHOICES = (
        (NONE, "None"),
        (VERY_SMALL, "Very Small"),
        (SMALL, "Small"),
        (MEDIUM, "Medium"),
        (SLIGHTLY_LARGE, "Slightly Large"),
        (LARGE, "Large"),
        (VERY_LARGE, "Very Large"),
        (EXTREMELY_LARGE, "Extremely Large"),
    )

    MULTI_CHOICES = list(itertools.combinations(CHOICES, 2))
    MULTI_CHOICES = [list(item) for item in MULTI_CHOICES]
    MULTI_CHOICES = [sorted(item) for item in MULTI_CHOICES]
    MULTI_CHOICES = tuple((f"{a[0]}/{b[0]}", f"{a[1]} / {b[1]}") for (a, b) in MULTI_CHOICES)
