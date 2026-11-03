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

### Install (Python)

Copy `python/plates/countries/polynesia/` into `plate_core/python/plates/countries/`.

Then run the tests from `plate_core/python/`: `pytest`.

### Use

```python
from plates.countries.polynesia.data import SPECS, THEMES

spec = SPECS["ck.car"]
theme = THEMES["CookIslandsThemes.car"]
print(spec.id)
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

- Pick a spec: use another key of `SPECS`.
- Pick a theme: use another key of `THEMES`.
- Validators: `VALIDATORS` maps the names `CookIslandsValidator`, `FrenchPolynesiaValidator`, `NiueValidator`, `NorfolkIslandValidator`, `WallisAndFutunaValidator` to classes.

## License

See [LICENSE](https://github.com/ArAd1Beyranvand/polynesia_plate/blob/main/LICENSE).
