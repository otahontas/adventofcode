import * as F from "fp-ts/function";
import * as E from "fp-ts/lib/Either";
import * as RA from "fp-ts/lib/ReadonlyArray";
import * as RNEA from "fp-ts/lib/ReadonlyNonEmptyArray";
import * as RT from "fp-ts/lib/ReadonlyTuple";
import * as S from "fp-ts/lib/string";
import * as D from "io-ts/Decoder";
import { match, P } from "ts-pattern";
import { decode, runSolver, sum } from "./shared";

const strategies = ["A", "B", "C", "X", "Y", "Z"] as const;
type Strategy = typeof strategies[number];
const shapes = ["Rock", "Paper", "Scissors"] as const;
type Shape = typeof shapes[number];

const sanitize = (char: Strategy) =>
  match(char)
    .with(P.union("A", "X"), () => "Rock" as const)
    .with(P.union("B", "Y"), () => "Paper" as const)
    .with(P.union("C", "Z"), () => "Scissors" as const)
    .exhaustive();

const toPoints = (setup: readonly [Shape, Shape]) =>
  match(setup)
    .with(["Rock", "Rock"], () => [4, 3] as const)
    .with(["Rock", "Paper"], () => [8, 4] as const)
    .with(["Rock", "Scissors"], () => [3, 8] as const)
    .with(["Paper", "Rock"], () => [1, 1] as const)
    .with(["Paper", "Paper"], () => [5, 5] as const)
    .with(["Paper", "Scissors"], () => [9, 9] as const)
    .with(["Scissors", "Rock"], () => [7, 2] as const)
    .with(["Scissors", "Paper"], () => [2, 6] as const)
    .with(["Scissors", "Scissors"], () => [6, 7] as const)
    .exhaustive();

runSolver(
  F.flow(
    RNEA.map(
      F.flow(
        S.split(" "),
        RNEA.map(F.flow(decode(D.literal(...strategies)), E.map(sanitize))),
        E.sequenceArray,
        E.chain(
          F.flow(
            decode(D.tuple(D.literal(...shapes), D.literal(...shapes))),
            E.map(toPoints),
          ),
        ),
      ),
    ),
    E.sequenceArray,
    E.map(F.flow(RA.unzip, RT.bimap(sum, sum))),
  ),
)({ day: "02", splitBy: "\n" });
