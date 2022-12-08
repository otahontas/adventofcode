import * as E from "fp-ts/lib/Either";
import * as RA from "fp-ts/lib/ReadonlyArray";
import * as RNEA from "fp-ts/lib/ReadonlyNonEmptyArray";
import * as RT from "fp-ts/lib/ReadonlyTuple";
import { flow } from "fp-ts/function";
import { fromEntries } from "fp-ts/lib/ReadonlyRecord";
import { match, P } from "ts-pattern";
import { split } from "fp-ts/lib/string";
import { sum } from "lodash";
import { createSolverError } from "./errors";
import { runSolver } from "./helpers";
import type { SolverError } from "./errors";

type Shape = "Rock" | "Paper" | "Scissors";

const sanitize = (char: string): E.Either<SolverError, Shape> =>
  match(char)
    .with(P.union("A", "X"), () => E.right("Rock" as const))
    .with(P.union("B", "Y"), () => E.right("Paper" as const))
    .with(P.union("C", "Z"), () => E.right("Scissors" as const))
    .otherwise((failedInput) =>
      E.left(
        createSolverError({
          errorName: "SanitizeError",
          errorMessage: `Input ${failedInput} wasn't valid`,
        }),
      ),
    );

const toPoints = (
  setup: readonly Shape[],
): E.Either<SolverError, readonly [number, number]> =>
  match(setup)
    .with(["Rock", "Rock"], () => E.right([4, 3] as const))
    .with(["Rock", "Paper"], () => E.right([8, 4] as const))
    .with(["Rock", "Scissors"], () => E.right([3, 8] as const))
    .with(["Paper", "Rock"], () => E.right([1, 1] as const))
    .with(["Paper", "Paper"], () => E.right([5, 5] as const))
    .with(["Paper", "Scissors"], () => E.right([9, 9] as const))
    .with(["Scissors", "Rock"], () => E.right([7, 2] as const))
    .with(["Scissors", "Paper"], () => E.right([2, 6] as const))
    .with(["Scissors", "Scissors"], () => E.right([6, 7] as const))
    .otherwise((failedSetup) =>
      E.left(
        createSolverError({
          errorName: "MatchSetupError",
          errorMessage: `Match setup ${failedSetup} wasn't valid`,
        }),
      ),
    );

const toKSum = (k: "first" | "second") => (val: readonly number[]) =>
  [k, sum(val)] as const;

runSolver(
  flow(
    RNEA.map(
      flow(split(" "), RNEA.map(sanitize), E.sequenceArray, E.chain(toPoints)),
    ),
    E.sequenceArray,
    E.map(
      flow(RA.unzip, RT.bimap(toKSum("second"), toKSum("first")), fromEntries),
    ),
  ),
)({ day: "02", splitBy: "\n" });
