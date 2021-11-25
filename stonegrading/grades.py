import itertools


class ColorGrades:
    COLORLESS_D = "D"
    COLORLESS_E = "E"
    COLORLESS_F = "F"
    NEARLY_COLORLESS_G = "G"
    NEARLY_COLORLESS_H = "H"
    NEARLY_COLORLESS_I = "I"
    NEARLY_COLORLESS_J = "J"
    NEARLY_COLORLESS_K = "K"
    COLORLESS_D_MINUS = "D-"
    COLORLESS_E_MINUS = "E-"
    COLORLESS_F_MINUS = "F-"
    NEARLY_COLORLESS_G_MINUS = "G-"
    NEARLY_COLORLESS_H_MINUS = "H-"
    NEARLY_COLORLESS_I_MINUS = "I-"
    NEARLY_COLORLESS_J_MINUS = "J-"
    NEARLY_COLORLESS_K_MINUS = "K-"
    COLORLESS_D_PLUS = "D+"
    COLORLESS_E_PLUS = "E+"
    COLORLESS_F_PLUS = "F+"
    NEARLY_COLORLESS_G_PLUS = "G+"
    NEARLY_COLORLESS_H_PLUS = "H+"
    NEARLY_COLORLESS_I_PLUS = "I+"
    NEARLY_COLORLESS_J_PLUS = "J+"
    NEARLY_COLORLESS_K_PLUS = "K+"

    SINGLE_CHOICES = [
        (COLORLESS_D, "D"),
        (COLORLESS_E, "E"),
        (COLORLESS_F, "F"),
        (NEARLY_COLORLESS_G, "G"),
        (NEARLY_COLORLESS_H, "H"),
        (NEARLY_COLORLESS_I, "I"),
        (NEARLY_COLORLESS_J, "J"),
        (NEARLY_COLORLESS_K, "K"),
        (COLORLESS_D_MINUS, "D-"),
        (COLORLESS_E_MINUS, "E-"),
        (COLORLESS_F_MINUS, "F-"),
        (NEARLY_COLORLESS_G_MINUS, "G-"),
        (NEARLY_COLORLESS_H_MINUS, "H-"),
        (NEARLY_COLORLESS_I_MINUS, "I-"),
        (NEARLY_COLORLESS_J_MINUS, "J-"),
        (NEARLY_COLORLESS_K_MINUS, "K-"),
        (COLORLESS_D_PLUS, "D+"),
        (COLORLESS_E_PLUS, "E+"),
        (COLORLESS_F_PLUS, "F+"),
        (NEARLY_COLORLESS_G_PLUS, "G+"),
        (NEARLY_COLORLESS_H_PLUS, "H+"),
        (NEARLY_COLORLESS_I_PLUS, "I+"),
        (NEARLY_COLORLESS_J_PLUS, "J+"),
        (NEARLY_COLORLESS_K_PLUS, "K+"),
    ]

    options = [option[0] for option in SINGLE_CHOICES]
    RANGE_CHOICES = [
        (f"{option[0]}-{option[1]}", f"{option[0]}-{option[1]}") for option in itertools.combinations(options, 2)
    ]

    CHOICES = SINGLE_CHOICES + RANGE_CHOICES


class ClarityGrades:
    INTERNALLY_FLAWLESS_PLUS = "IF+"
    INTERNALLY_FLAWLESS = "IF"
    INTERNALLY_FLAWLESS_MINUS = "IF-"
    VERY_VERY_SLIGHTLY_INCLUDED_DEGREE_1_PLUS = "VVS1+"
    VERY_VERY_SLIGHTLY_INCLUDED_DEGREE_1 = "VVS1"
    VERY_VERY_SLIGHTLY_INCLUDED_DEGREE_1_MINUS = "VVS1-"
    VERY_VERY_SLIGHTLY_INCLUDED_DEGREE_2_PLUS = "VVS2+"
    VERY_VERY_SLIGHTLY_INCLUDED_DEGREE_2 = "VVS2"
    VERY_VERY_SLIGHTLY_INCLUDED_DEGREE_2_MINUS = "VVS2-"
    VERY_SLIGHTLY_INCLUDED_DEGREE_1_PLUS = "VS1+"
    VERY_SLIGHTLY_INCLUDED_DEGREE_1 = "VS1"
    VERY_SLIGHTLY_INCLUDED_DEGREE_1_MINUS = "VS1-"
    VERY_SLIGHTLY_INCLUDED_DEGREE_2_PLUS = "VS2+"
    VERY_SLIGHTLY_INCLUDED_DEGREE_2 = "VS2"
    VERY_SLIGHTLY_INCLUDED_DEGREE_2_MINUS = "VS2-"
    SLIGHTLY_INCLUDED_DEGREE_1_PLUS = "SI1+"
    SLIGHTLY_INCLUDED_DEGREE_1 = "SI1"
    SLIGHTLY_INCLUDED_DEGREE_1_MINUS = "SI1-"
    SLIGHTLY_INCLUDED_DEGREE_2_PLUS = "SI2+"
    SLIGHTLY_INCLUDED_DEGREE_2 = "SI2"
    SLIGHTLY_INCLUDED_DEGREE_2_MINUS = "SI2-"
    INCLUDED_PLUS = "I1+"
    INCLUDED = "I1"
    INCLUDED_MINUS = "I1-"

    CHOICES = (
        (INTERNALLY_FLAWLESS_PLUS, "IF+"),
        (INTERNALLY_FLAWLESS, "IF"),
        (INTERNALLY_FLAWLESS_MINUS, "IF-"),
        (VERY_VERY_SLIGHTLY_INCLUDED_DEGREE_1_PLUS, "VVS1+"),
        (VERY_VERY_SLIGHTLY_INCLUDED_DEGREE_1, "VVS1"),
        (VERY_VERY_SLIGHTLY_INCLUDED_DEGREE_1_MINUS, "VVS1-"),
        (VERY_VERY_SLIGHTLY_INCLUDED_DEGREE_2_PLUS, "VVS2+"),
        (VERY_VERY_SLIGHTLY_INCLUDED_DEGREE_2, "VVS2"),
        (VERY_VERY_SLIGHTLY_INCLUDED_DEGREE_2_MINUS, "VVS2-"),
        (VERY_SLIGHTLY_INCLUDED_DEGREE_1_PLUS, "VS1+"),
        (VERY_SLIGHTLY_INCLUDED_DEGREE_1, "VS1"),
        (VERY_SLIGHTLY_INCLUDED_DEGREE_1_MINUS, "VS1-"),
        (VERY_SLIGHTLY_INCLUDED_DEGREE_2_PLUS, "VS2+"),
        (VERY_SLIGHTLY_INCLUDED_DEGREE_2, "VS2"),
        (VERY_SLIGHTLY_INCLUDED_DEGREE_2_MINUS, "VS2-"),
        (SLIGHTLY_INCLUDED_DEGREE_1_PLUS, "SI1+"),
        (SLIGHTLY_INCLUDED_DEGREE_1, "SI1"),
        (SLIGHTLY_INCLUDED_DEGREE_1_MINUS, "SI1-"),
        (SLIGHTLY_INCLUDED_DEGREE_2_PLUS, "SI2+"),
        (SLIGHTLY_INCLUDED_DEGREE_2, "SI2"),
        (SLIGHTLY_INCLUDED_DEGREE_2_MINUS, "SI2-"),
        (INCLUDED_PLUS, "I1+"),
        (INCLUDED, "I1"),
        (INCLUDED_MINUS, "I1-"),
    )


class GeneralGrades:
    EXCELLENT = "EX"
    VERY_GOOD = "VG"
    GOOD = "GD"
    FAIR = "F"
    POOR = "P"
    EXCELLENT_PLUS = "EX+"
    EXCELLENT_MINUS = "EX-"
    VERY_GOOD_PLUS = "VG+"
    VERY_GOOD_MINUS = "VG-"
    GOOD_PLUS = "GD+"
    GOOD_MINUS = "GD-"
    FAIR_PLUS = "F+"
    FAIR_MINUS = "F-"
    POOR_PLUS = "P+"
    POOR_MINUS = "P-"

    CHOICES = (
        (EXCELLENT, "Excellent"),
        (VERY_GOOD, "Very Good"),
        (GOOD, "Good"),
        (FAIR, "Fair"),
        (POOR, "Poor"),
        (EXCELLENT_PLUS, EXCELLENT_PLUS),
        (EXCELLENT_MINUS, EXCELLENT_MINUS),
        (GOOD_PLUS, GOOD_PLUS),
        (GOOD_MINUS, GOOD_MINUS),
        (POOR_PLUS, POOR_PLUS),
        (POOR_MINUS, POOR_MINUS),
        (VERY_GOOD_PLUS, VERY_GOOD_PLUS),
        (VERY_GOOD_MINUS, VERY_GOOD_MINUS),
        (FAIR_PLUS, FAIR_PLUS),
        (FAIR_MINUS, FAIR_MINUS),
    )


class FluorescenceGrades:
    VERY_STRONG = "VS"
    STRONG = "S"
    MEDIUM = "M"
    FAINT = "F"
    NONE = "N"
    MEDIUM_BLUE = "MB"
    MEDIUM_YELLOW = "MY"
    MEDIUM_WHITE = "MW"
    MEDIUM_GREEN = "MG"

    CHOICES = (
        (VERY_STRONG, "Very Strong"),
        (STRONG, "Strong"),
        (MEDIUM, "Medium"),
        (FAINT, "Faint"),
        (NONE, "None"),
        (MEDIUM_GREEN, "Medium Green"),
        (MEDIUM_WHITE, "Medium White"),
        (MEDIUM_BLUE, "Medium Blue"),
        (MEDIUM_YELLOW, "Medium Yellow"),
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
        (EXTREMELY_THIN_TO_VERY_THIN, "Extremely Thin to Very Thin"),
    )


class GirdleCondition:
    FACETED = "FAC"
    POLISHED = "POL"
    BRUTED = "BRU"

    CHOICES = ((FACETED, "Faceted"), (POLISHED, "Polished"), (BRUTED, "Bruted"))


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
    BEARDED_GIRDLE = "BG"
    POLISH_MARK = "PM"
    ROUGH_GIRDLE = "RG"
    SCRATCH = "S"
    SURFACE_GRAINING = "SGr"
    EXTRA_FACET = "EF"
    ETCH_CHANNELS = "EC"
    LASER_MANUFACTURING_REMNANTS = "LMR"
    BURN_MARKS = "brn"

    CHOICES = (
        (BRUISE, "Bruise"),
        (CAVITY, "Cavity"),
        (CHIP, "Chip"),
        (CLEAVAGE, "Cleavage"),
        (CLOUD, "Cloud"),
        (CRYSTAL, "Crystal"),
        (FEATHER, "Feather"),
        (GRAIN_CENTER, "Grain Center"),
        (INDENTED_NATURAL, "Indented Natural"),
        (INTERNAL_GRAINING, "Internal Graining"),
        (KNOT, "Knot"),
        (LASER_DRILL_HOLE, "Laser Drill Hole"),
        (NEEDLE, "Needle"),
        (PINPOINT, "Pinpoint"),
        (TWINNING_WISP, "Twinning Wisp"),
        (ABRASION, "Abrasion"),
        (NATURAL, "Natural"),
        (NICK, "Nick"),
        (PIT, "Pit"),
        (POLISH_LINE, "Polish Line"),
        (BEARDED_GIRDLE, "Bearded Girdle"),
        (POLISH_MARK, "Polish Mark"),
        (ROUGH_GIRDLE, "Rough Girdle"),
        (SCRATCH, "Scratch"),
        (SURFACE_GRAINING, "Surface Graining"),
        (EXTRA_FACET, "Extra Facet"),
        (BURN_MARKS, "Burn Marks"),
        (ETCH_CHANNELS, "Etch Channels"),
        (LASER_MANUFACTURING_REMNANTS, "Laser Manufacturing Remnants"),
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


class CuletCharacteristics:
    NONE = "N"
    SLIGHTLY_ABRADED = "SAB"
    CHIPPED = "CH"

    CHOICES = (
        (NONE, "None"),
        (SLIGHTLY_ABRADED, "Slightly Abraded"),
        (CHIPPED, "Chipped"),
    )


class DiamondDescription:
    NATURAL = "NATURAL"
    UNNATURAL = "UNNATURAL"

    CHOICES = ((NATURAL, "Natural"), (UNNATURAL, "Unnatural"))
