import 'package:plate_core/plate_core.dart';

/// Judges a `3◆203` value: a block digit 1 to 7, then three digits (leading
/// zeros are printed; cancelled blocks were reissued from 000). Reports,
/// never bars a keystroke.
class NorfolkIslandValidator extends RuledPlateValidator {
  const NorfolkIslandValidator() : super('block');

  static const String reasonBlock = 'The block is a digit from 1 to 7.';
  static const String reasonSerial = 'The number is three digits.';

  @override
  List<PlateCheck> get checks => const <PlateCheck>[
    PlateCheck('block', r'[1-7]', reasonBlock),
    PlateCheck('serial', r'[0-9]{3}', reasonSerial),
  ];
}
