"""Port of polynesia_plate/lib/src/cook_islands/src/cook_islands_validators.dart. Hand-ported; codegen never overwrites this file."""
from __future__ import annotations

import re

from plates.core.validators.plate_validator import GatedPlateValidator, PlateEntry, PlateValidation, is_digits_of_length


class CookIslandsValidator(GatedPlateValidator):
    gate_group = 'serial'

    reason_car = "The number is four digits."
    reason_letters = "The register is three letters."
    reason_motorcycle = "The number is three digits."

    def judge(self, entry: PlateEntry) -> PlateValidation:
        letters, serial = entry.group("letters"), entry.group("serial")
        if len(entry.spec.slots) == 1:
            return (PlateValidation.valid() if is_digits_of_length(serial, 4)
                    else PlateValidation.invalid(self.reason_car))
        if re.fullmatch(r"[A-Z]{3}", letters) is None:
            return PlateValidation.invalid(self.reason_letters)
        if not is_digits_of_length(serial, 3):
            return PlateValidation.invalid(self.reason_motorcycle)
        return PlateValidation.valid()
