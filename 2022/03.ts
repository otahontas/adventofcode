import * as A from "fp-ts/lib/Array";
import * as E from "fp-ts/lib/Either";
import * as F from "fp-ts/function";
import * as RA from "fp-ts/lib/ReadonlyArray";
import * as RS from "fp-ts/lib/ReadonlySet";
import * as S from "fp-ts/lib/string";
import { sum } from "lodash";
import { match } from "ts-pattern";
import { readInput, handleAnswer } from "./helpers";

// Handling parts in different pipelines, since input must be parsed differently
const toSet = (s: string) => RS.fromSet(new Set(s));

const prio = (char: string): E.Either<Error, number> =>
  match(char)
    .when(
      (c) => RegExp("[A-Z]").test(c),
      (c) => E.right(c.charCodeAt(0) - 38),
    )
    .when(
      (c) => RegExp("[a-z]").test(c),
      (c) => E.right(c.charCodeAt(0) - 96),
    )
    .otherwise(() => E.left(new Error("Input wasn't alphabetic")));

// First part
const half = (s: string) => Math.floor(S.size(s) / 2);

F.pipe(
  readInput("03", "\n"),
  E.map(
    F.flow(
      A.map(
        F.flow(
          S.trim,
          (s) => [toSet(s.slice(0, half(s))), toSet(s.slice(half(s)))] as const,
          ([left, right]) => RS.intersection(S.Eq)(left)(right),
          RS.toReadonlyArray(S.Ord),
          RA.head,
          E.fromOption(
            () => new Error("There must be one char in intersection"),
          ),
          E.map(prio),
          E.flatten,
        ),
      ),
      E.sequenceArray,
    ),
  ),
  E.flatten,
  E.map(sum),
  handleAnswer,
);

// Second part
F.pipe(
  readInput("03", "\n"),
  E.map(
    F.flow(
      A.map(F.flow(S.trim, toSet)),
      A.chunksOf(3),
      RA.map(
        F.flow(
          (groups) =>
            groups.reduce((acc, curr) => RS.intersection(S.Eq)(acc)(curr)),
          RS.toReadonlyArray(S.Ord),
          RA.head,
          E.fromOption(
            () => new Error("There must be one char in intersection"),
          ),
          E.map(prio),
          E.flatten,
        ),
      ),
      E.sequenceArray,
    ),
  ),
  E.flatten,
  E.map(sum),
  handleAnswer,
);
