import * as E from "fp-ts/lib/Either";
import * as RA from "fp-ts/lib/ReadonlyArray";
import * as RNEA from "fp-ts/lib/ReadonlyNonEmptyArray";
import * as RR from "fp-ts/lib/ReadonlyRecord";
import * as RS from "fp-ts/lib/ReadonlySet";
import * as RT from "fp-ts/lib/ReadonlyTuple";
import * as S from "fp-ts/lib/string";
import { flow } from "fp-ts/function";
import { fromEntries } from "fp-ts/lib/ReadonlyRecord";
import { match } from "ts-pattern";
import { sum } from "lodash";
import { createSolverError } from "./errors";
import { runSolver } from "./helpers";
import type { SolverError } from "./errors";

const half = (s: string) => Math.floor(S.size(s) / 2);
const toSet = (s: string) => RS.fromSet(new Set(s));

const prio = (char: string): E.Either<SolverError, number> =>
  match(char)
    .when(
      (c) => RegExp("[A-Z]").test(c),
      (c) => E.right(c.charCodeAt(0) - 38),
    )
    .when(
      (c) => RegExp("[a-z]").test(c),
      (c) => E.right(c.charCodeAt(0) - 96),
    )
    .otherwise(() =>
      E.left(
        createSolverError({
          errorName: "ConvertToPrioError",
          errorMessage: "Input wasn't alphabetic",
        }),
      ),
    );

const sumOfPrios = flow(
  RNEA.map(
    flow(
      RS.toReadonlyArray(S.Ord),
      RA.head,
      E.fromOption(() =>
        createSolverError({
          errorName: "InputError",
          errorMessage: "There must be one char in intersection",
        }),
      ),
      E.chain(prio),
    ),
  ),
  E.sequenceArray,
  E.map(sum),
);

const toKv = (k: string) => <V>(v: V) => [k, v] as const;

runSolver(
  flow(
    RNEA.map(flow(S.trim, (content) => [content, content] as const)),
    RNEA.unzip,
    RT.bimap(
      flow(
        RNEA.map(toSet),
        RNEA.chunksOf(3),
        RNEA.map((groups) =>
          groups.reduce((acc, curr) => RS.intersection(S.Eq)(acc)(curr)),
        ),
        sumOfPrios,
        toKv("second"),
      ),
      flow(
        RNEA.map(
          flow(
            (s) =>
              [toSet(s.slice(0, half(s))), toSet(s.slice(half(s)))] as const,
            ([left, right]) => RS.intersection(S.Eq)(left)(right),
          ),
        ),
        sumOfPrios,
        toKv("first"),
      ),
    ),
    fromEntries,
    RR.sequence(E.Applicative),
  ),
)({ day: "03", splitBy: "\n" });
