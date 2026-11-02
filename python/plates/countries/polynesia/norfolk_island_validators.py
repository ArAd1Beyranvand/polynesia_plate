"""Port of polynesia_plate/lib/src/norfolk_island/src/norfolk_island_validators.dart."""
from __future__ import annotations

import re
from plates.core.validators.plate_validator import GatedPlateValidator, PlateEntry, PlateValidation, is_digits_of_length


class NorfolkIslandValidator(GatedPlateValidator):
    gate_group = "block"
    reason_block = "The block is a digit from 1 to 7."
    reason_serial = "The number is three digits."
    _block = re.compile(r"^[1-7]$")

    def judge(self, entry: PlateEntry) -> PlateValidation:
        if not self._block.fullmatch(entry.group("block")):
            return PlateValidation.invalid(self.reason_block)
        if not is_digits_of_length(entry.group("serial"), 3):
            return PlateValidation.invalid(self.reason_serial)
        return PlateValidation.valid()
