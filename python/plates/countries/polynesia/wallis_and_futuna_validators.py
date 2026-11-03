"""Port of polynesia_plate/lib/src/wallis_and_futuna/src/wallis_and_futuna_validators.dart."""

from plates.core.validators.plate_validator import PlateCheck, RuledPlateValidator


class WallisAndFutunaValidator(RuledPlateValidator):
    checks = (
        PlateCheck("number", r"[0-9]{4}", "The serial is four digits."),
    )
