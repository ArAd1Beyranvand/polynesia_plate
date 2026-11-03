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

### Install (TypeScript)

Copy `typescript/src/countries/polynesia/` into `plate_core/typescript/src/countries/`.

Then run the tests from `plate_core/typescript/`: `npm test`.

### Use

```ts
import country from './countries/polynesia';

const spec = country.specs.get('ck.car');
console.log(country.package);
```

## Specs

The specs are the same in every language (they come from shared data).

- `ck.car`
- `ck.motorcycle`
- `pf.regular`
- `nu.standard`
- `nf.private`
- `wf.private`

## Themes

- `CookIslandsThemes.car`
- `CookIslandsThemes.motorcycle`
- `FrenchPolynesiaThemes.front`
- `FrenchPolynesiaThemes.rear`
- `NiueThemes.standard`
- `NorfolkIslandThemes.private`
- `WallisAndFutunaThemes.rear`

## Change it

- Specs: `country.specs`, by id.
- Themes: `country.themes`.
- Validators: `country.validators` (`CookIslandsValidator`, `FrenchPolynesiaValidator`, `NiueValidator`, `NorfolkIslandValidator`, `WallisAndFutunaValidator`).

## License

See [LICENSE](https://github.com/ArAd1Beyranvand/polynesia_plate/blob/main/LICENSE).
