"""Port of polynesia_plate/lib/src/french_polynesia/src/french_polynesia_validators.dart. Hand-ported; codegen never overwrites this file."""
from __future__ import annotations

import re

from plates.core.validators.plate_validator import GatedPlateValidator, PlateEntry, PlateValidation, is_digits_of_length


class FrenchPolynesiaValidator(GatedPlateValidator):
    gate_group = 'number'

    reason_number = "The number is six digits."
    reason_letter = "The letter is one of A\u2013Z without I, O, U."

    def judge(self, entry: PlateEntry) -> PlateValidation:
        if not is_digits_of_length(entry.group("number"), 6):
            return PlateValidation.invalid(self.reason_number)
        if re.fullmatch(r"[A-HJ-NP-TV-Z]", entry.group("letter")) is None:
            return PlateValidation.invalid(self.reason_letter)
        return PlateValidation.valid()
