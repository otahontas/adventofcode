import * as E from "fp-ts/lib/Either";
import * as RA from "fp-ts/lib/ReadonlyArray";
import * as RNEA from "fp-ts/lib/ReadonlyNonEmptyArray";
import * as RR from "fp-ts/lib/ReadonlyRecord";
import * as RS from "fp-ts/lib/ReadonlySet";
import * as RT from "fp-ts/lib/ReadonlyTuple";
import * as S from "fp-ts/lib/string";
import * as F from "fp-ts/function";
import { Char, prismChar } from "newtype-ts/lib/Char";
import { match } from "ts-pattern";
import { runSolver, createSolverError, toTuple } from "./shared";

const toSet = F.flow((s: string) => new Set(s), RS.fromSet);
const half = (s: string) => Math.floor(S.size(s) / 2);
const prio = F.flow(
  prismChar.reverseGet,
  (s) => s.charCodeAt(0),
  (x) => (x >= 97 ? x - 96 : x - 38),
);

// RR.sequence(E.Applicative),
// const sumOfPrios = F.flow(
//   RNEA.map(
//     F.flow(
//       RS.toReadonlyArray(S.Ord),
//       RA.head,
//       E.fromOption(() =>
//         createSolverError({
//           errorName: "InputError",
//           errorMessage: "There must be one char in intersection",
//         }),
//       ),
//       E.chain(prio),
//     ),
//   ),
//   E.sequenceArray,
//   E.map(sum),
// );

runSolver(
  F.flow(
    RNEA.map(F.flow(S.trim, toTuple)),
    RNEA.unzip,
    RT.bimap(
      F.flow(
        RNEA.map(toSet),
        RNEA.chunksOf(3),
        RNEA.map((groups) =>
          groups.reduce((acc, curr) => RS.intersection(S.Eq)(acc)(curr)),
        ),
      ),
    ),
  ),
)({ day: "03", splitBy: "\n" });
