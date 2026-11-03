import 'package:plate_core/plate_core.dart';

/// Judges a Wallis and Futuna plate: a four-digit serial followed by the
/// printed `WF`. Reports, never bars a keystroke.
class WallisAndFutunaValidator extends RuledPlateValidator {
  const WallisAndFutunaValidator();

  static const String reasonNumber = 'The serial is four digits.';

  @override
  List<PlateCheck> get checks => const <PlateCheck>[
    PlateCheck('number', r'[0-9]{4}', reasonNumber),
  ];
}
