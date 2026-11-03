import { PlateCheck, RuledPlateValidator } from '../../core/validators/plate_validator';

/** Judges a `3◆203` value: a block digit 1 to 7, then three digits (leading
/// zeros are printed; cancelled blocks were reissued from 000). Reports,
/// never bars a keystroke. */
export class NorfolkIslandValidator extends RuledPlateValidator {
  readonly checks = [
    new PlateCheck('block', '[1-7]', 'The block is a digit from 1 to 7.'),
    new PlateCheck('serial', '[0-9]{3}', 'The number is three digits.'),
  ];

  override get gateGroup(): string {
    return 'block';
  }
}
