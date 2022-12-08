import { tryCatch, map, fold, chain } from "fp-ts/lib/Either";
import { flow, pipe } from "fp-ts/lib/function";
import { trim, split } from "fp-ts/lib/string";
import { readFileSync } from "fs";
import type { Either } from "fp-ts/lib/Either";
import type { ReadonlyNonEmptyArray } from "fp-ts/lib/ReadonlyNonEmptyArray";
import type { ReadonlyRecord } from "fp-ts/lib/ReadonlyRecord";
import { createSolverError, formatSolverError } from "./errors";
import type { SolverError } from "./errors";

interface ReadInputProps {
  day: string;
  splitBy: string;
}

const bufToString = (buf: Buffer) => buf.toString("utf-8");

const readInput = ({ day, splitBy }: ReadInputProps) =>
  pipe(
    tryCatch(
      () => readFileSync(`inputs/${day}.txt`),
      () =>
        createSolverError({
          errorName: "InputError",
          errorMessage: "Failed to read input",
        }),
    ),
    map(flow(bufToString, trim, split(splitBy))),
  );

type Ans<V> = ReadonlyRecord<"first" | "second", V>;

const handleAnswer = fold<SolverError, Ans<any>, void>(
  flow(formatSolverError, console.error),
  <V>({ first, second }: Ans<V>) => {
    console.log(`Part 1: ${first}`);
    console.log(`Part 2: ${second}`);
  },
);

export const runSolver = <V>(
  solver: (input: ReadonlyNonEmptyArray<string>) => Either<SolverError, Ans<V>>,
) => flow(readInput, chain(solver), handleAnswer);

export type ArrayType<Arr extends readonly unknown[] | unknown[]> =
  Arr extends readonly (infer Item)[]
    ? Item
    : Arr extends (infer Item)[]
    ? Item
    : Arr;
