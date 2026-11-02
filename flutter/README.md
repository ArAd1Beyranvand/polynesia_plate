FREE PALESTINE 🇮🇷🇵🇸 پاینده ایران

GO VEGAN 🌱

==================================

# polynesia_plate

Licence plates for polynesia members, for the plate_core library.

## Install

```yaml
dependencies:
  plate_core: ^0.12.0
  polynesia_plate: ^0.1.0
```

## Use

```dart
import 'package:plate_core/plate_core.dart';
import 'package:polynesia_plate/polynesia_plate.dart';

PlateCanvas(
  spec: CookIslandsPlates.car,
  theme: CookIslandsThemes.car,
  validator: const CookIslandsValidator(),
  autoValidate: true,
  onChooseCharacter: noCharacterChooser,
);
```

## Contains

- `CookIslandsPlates` — 2 plate specs: `car`, `motorcycle`.
- `FrenchPolynesiaPlates` — 1 plate spec: `regular`.
- `NiuePlates` — 1 plate spec: `standard`.
- `NorfolkIslandPlates` — 1 plate spec: `private`.
- `WallisAndFutunaPlates` — 1 plate spec: `private`.

Each also ships its `…Country` panel, `…Themes` and, where one exists, an advisory `…Validator`.

## Part of plate

Painted by [`plate_core`](https://pub.dev/packages/plate_core); alphabets shared through [`plate_alphabet`](https://pub.dev/packages/plate_alphabet); optional character picker in [`plate_keypad`](https://pub.dev/packages/plate_keypad).

