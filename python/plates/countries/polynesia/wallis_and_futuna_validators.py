"""Port of polynesia_plate/lib/src/wallis_and_futuna/src/wallis_and_futuna_validators.dart."""
from __future__ import annotations

from plates.core.validators.plate_validator import GatedPlateValidator, PlateEntry, PlateValidation, is_digits_of_length


class WallisAndFutunaValidator(GatedPlateValidator):
    gate_group = "number"
    reason_number = "The serial is four digits."

    def judge(self, entry: PlateEntry) -> PlateValidation:
        if not is_digits_of_length(entry.group("number"), 4):
            return PlateValidation.invalid(self.reason_number)
        return PlateValidation.valid()
