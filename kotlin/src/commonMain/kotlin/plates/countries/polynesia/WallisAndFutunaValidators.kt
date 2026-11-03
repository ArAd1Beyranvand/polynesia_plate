package plates.countries.polynesia

import plates.core.validators.PlateCheck
import plates.core.validators.RuledPlateValidator

/** Judges a Wallis and Futuna plate: a four-digit serial followed by the printed `WF`. Reports, never bars a keystroke. */
class WallisAndFutunaValidator : RuledPlateValidator() {
    override val checks = listOf(
        PlateCheck("number", "[0-9]{4}", "The serial is four digits."),
    )
}
