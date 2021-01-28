class ColorGrades:
    COLORLESS_D = "D"
    COLORLESS_E = "E"
    COLORLESS_F = "F"
    NEARLY_COLORLESS_G = "G"
    NEARLY_COLORLESS_H = "H"
    NEARLY_COLORLESS_I = "I"
    NEARLY_COLORLESS_J = "J"

    CHOICES = (
        (COLORLESS_D, "Colorless D"),
        (COLORLESS_E, "Colorless E"),
        (COLORLESS_F, "Colorless F"),
        (NEARLY_COLORLESS_G, "Nearly Colorless G"),
        (NEARLY_COLORLESS_H, "Nearly Colorless H"),
        (NEARLY_COLORLESS_I, "Nearly Colorless I"),
        (NEARLY_COLORLESS_J, "Nearly Colorless J"),
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
        (INTERNALLY_FLAWLESS, "Internally Flawless"),
        (VERY_VERY_SLIGHTLY_INCLUDED_DEGREE_1, "Very Very Slightly Included Degree 1"),
        (VERY_VERY_SLIGHTLY_INCLUDED_DEGREE_2, "Very Very Slightly Included Degree 2"),
        (VERY_SLIGHTLY_INCLUDED_DEGREE_1, "Very Slightly Included Degree 1"),
        (VERY_SLIGHTLY_INCLUDED_DEGREE_2, "Very Slightly Included Degree 2"),
        (SLIGHTLY_INCLUDED_DEGREE_1, "Slightly Included Degree 1"),
        (SLIGHTLY_INCLUDED_DEGREE_2, "Slightly Included Degree 2"),
        (INCLUDED, "Included"),
    )


class GeneralGrades:
    EXCELLENT = "EX"
    VERY_GOOD = "VG"
    GOOD = "GOOD"
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
    EXTREMELY_THIN = "EXT"
    VERY_THIN = "VTN"
    THIN = "THIN"
    MEDIUM = "MED"
    SLIGHTLY_THICK = "STK"
    THICK = "THK"
    VERY_THICK = "VTK"
    EXTREMELY_THICK = "EXT"
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
    BRUISE = "BR"
    CAVITY = "CV"
    CHIP = "CH"
    CLOUD = "CL"
    FEATHER = "F"
    INCLUDED_CRYSTAL = "IC"
    INDENTED_NATURAL = "IN"
    INTERNAL_GRAINING = "IG"
    KNOT = "KN"
    NEEDLE = "ND"
    PINPOINT = "PP"
    ABRASION = "AB"
    SCRATCH = "SC"
    NICK = "NK"
    POLISH_LINE = "PL"
    PIT = "PT"
    NATURAL = "N"
    EXTRA_FEET = "EF"
    SURFACE_GRAINING = "SG"

    CHOICES = (
        (BRUISE, "Bruise"),
        (CAVITY, "Cavity"),
        (CHIP, "Chip"),
        (CLOUD, "Cloud"),
        (FEATHER, "Feather"),
        (INCLUDED_CRYSTAL, "Included crystal"),
        (INDENTED_NATURAL, "Indented natural"),
        (INTERNAL_GRAINING, "Internal graining"),
        (KNOT, "knot"),
        (NEEDLE, "Needle"),
        (PINPOINT, "Pinpoint"),
        (ABRASION, "Abrasion"),
        (SCRATCH, "Scratch"),
        (NICK, "Nick"),
        (POLISH_LINE, "Polish Line"),
        (PIT, "Pit"),
        (NATURAL, "Natural"),
        (EXTRA_FEET, "Extra Feet"),
        (SURFACE_GRAINING, "Surface Graining"),
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
