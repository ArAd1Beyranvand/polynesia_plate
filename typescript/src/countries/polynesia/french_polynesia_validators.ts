import { PlateCheck, RuledPlateValidator } from '../../core/validators/plate_validator';

/**
 * Judges a French Polynesia plate: six digits and one letter, as in
 * `233051 P`. The letter leaves out I, O and U. Reports, never bars a
 * keystroke.
 */
export class FrenchPolynesiaValidator extends RuledPlateValidator {
  readonly checks = [
    new PlateCheck('number', '[0-9]{6}', 'The number is six digits.'),
    new PlateCheck('letter', '[A-HJ-NP-TV-Z]', 'The letter is one of A–Z without I, O, U.'),
  ];

  override get gateGroup(): string {
    return 'number';
  }
}
