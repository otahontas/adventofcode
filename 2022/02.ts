import * as A from "fp-ts/lib/Array";
import * as E from "fp-ts/lib/Either";
import * as F from "fp-ts/function";
import * as RA from "fp-ts/lib/ReadonlyArray";
import * as S from "fp-ts/lib/string";
import { sum } from "lodash";
import { match, P } from "ts-pattern";
import { readInput, handleAnswer } from "./helpers";

type Shape = "Rock" | "Paper" | "Scissors";

const sanitize = (char: string): E.Either<Error, Shape> =>
  match(char)
    .with(P.union("A", "X"), () => E.right("Rock" as const))
    .with(P.union("B", "Y"), () => E.right("Paper" as const))
    .with(P.union("C", "Z"), () => E.right("Scissors" as const))
    .otherwise((failedInput) =>
      E.left(new Error(`Input ${failedInput} wasn't valid`)),
    );

// Precalculated point map for both parts
const toPoints = (
  setup: readonly Shape[],
): E.Either<Error, readonly [number, number]> =>
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
      E.left(new Error(`Match setup ${failedSetup} wasn't valid`)),
    );

F.pipe(
  readInput("02", "\n"),
  E.map(
    F.flow(
      A.map(
        F.flow(
          S.split(" "),
          RA.map(sanitize),
          E.sequenceArray,
          E.map(toPoints),
          E.flatten,
        ),
      ),
      E.sequenceArray,
    ),
  ),
  E.flatten,
  E.map(
    F.flow(RA.unzip, ([first, second]) => [sum(first), sum(second)] as const),
  ),
  handleAnswer,
);
