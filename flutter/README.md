FREE PALESTINE 🇮🇷🇵🇸 پاینده ایران

GO VEGAN 🌱

==================================

# polynesia_plate

Licence plates for polynesia members, for the plate_core library.

## Languages

| Language | Folder | Example |
| --- | --- | --- |
| Flutter / Dart | [`flutter/`](https://github.com/ArAd1Beyranvand/polynesia_plate/tree/main/flutter) | — |
| Kotlin | [`kotlin/`](https://github.com/ArAd1Beyranvand/polynesia_plate/tree/main/kotlin) | — |
| Python | [`python/`](https://github.com/ArAd1Beyranvand/polynesia_plate/tree/main/python) | — |
| TypeScript | [`typescript/`](https://github.com/ArAd1Beyranvand/polynesia_plate/tree/main/typescript) | — |

## Quick start

### Install

```yaml
dependencies:
  plate_core: ^0.12.0
  polynesia_plate: ^0.1.0
```

### Use

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

## Specs

Each spec is one plate layout.

- none listed

## Themes

- none listed

## Change it

`PlateCanvas` takes `spec:` (an entry of `None`) and `theme:` (an entry of `None`).

## Also included

- none

## Part of plate

Painted by [`plate_core`](https://pub.dev/packages/plate_core); alphabets shared through [`plate_alphabet`](https://pub.dev/packages/plate_alphabet); optional character picker in [`plate_keypad`](https://pub.dev/packages/plate_keypad).

## License

See [LICENSE](https://github.com/ArAd1Beyranvand/polynesia_plate/blob/main/LICENSE).
