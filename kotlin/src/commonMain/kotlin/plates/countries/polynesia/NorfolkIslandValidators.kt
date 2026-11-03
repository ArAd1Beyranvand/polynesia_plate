package plates.countries.polynesia

import plates.core.validators.PlateCheck
import plates.core.validators.RuledPlateValidator

/** Judges a `3◆203` value: a block digit 1 to 7, then three digits (leading zeros are printed; cancelled blocks were reissued from 000). Reports, never bars a keystroke. */
class NorfolkIslandValidator : RuledPlateValidator("block") {
    override val checks = listOf(
        PlateCheck("block", "[1-7]", "The block is a digit from 1 to 7."),
        PlateCheck("serial", "[0-9]{3}", "The number is three digits."),
    )
}
