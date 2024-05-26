# `ocpi-types-typescript`

Auto-generated TypeScript definitions for the OCPI protocol.

At the moment only supporting OCPI 2.1.1.

## Installation

```
npm install --save-dev ocpi-types-typescript
```

## Usage

You can import all defined types as so:

```ts
import type { Location } from 'ocpi-types-typescript/v2.1.1';

const myLocation: Location;
```

You can consult [the documentation](https://gaia-charge.github.io/ocpi-types/typescript/docs) for more information.

## Known issues

As some types have different required fields between OCPI modules, we end up with some seemingly duplicate types. Most prominant case is `Location`, `CdrLocation` and `SessionLocation`. The conversion between each other has to be done manually at the moment.