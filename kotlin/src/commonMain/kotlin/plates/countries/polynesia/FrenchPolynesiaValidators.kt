package plates.countries.polynesia

import plates.core.validators.PlateCheck
import plates.core.validators.RuledPlateValidator

/** Judges a French Polynesia plate: six digits and one letter (no I, O, U). */
class FrenchPolynesiaValidator : RuledPlateValidator("number") {
    override val checks = listOf(
        PlateCheck("number", "[0-9]{6}", "The number is six digits."),
        PlateCheck("letter", "[A-HJ-NP-TV-Z]", "The letter is one of A–Z without I, O, U."),
    )
}
