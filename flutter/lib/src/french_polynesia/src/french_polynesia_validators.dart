import 'package:plate_core/plate_core.dart';

/// Judges a French Polynesia plate: six digits and one letter, as in
/// `233051 P`. The letter leaves out I, O and U. Reports, never bars a
/// keystroke.
class FrenchPolynesiaValidator extends RuledPlateValidator {
  const FrenchPolynesiaValidator() : super('number');

  static const String reasonNumber = 'The number is six digits.';
  static const String reasonLetter =
      'The letter is one of A–Z without I, O, U.';

  @override
  List<PlateCheck> get checks => const <PlateCheck>[
    PlateCheck('number', r'[0-9]{6}', reasonNumber),
    PlateCheck('letter', r'[A-HJ-NP-TV-Z]', reasonLetter),
  ];
}
