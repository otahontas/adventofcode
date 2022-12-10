import * as E from "fp-ts/lib/Either";
import * as F from "fp-ts/lib/function";
import * as I from "fp-ts/lib/Identity";
import * as RA from "fp-ts/lib/ReadonlyArray";
import type * as RNEA from "fp-ts/lib/ReadonlyNonEmptyArray";
import * as RT from "fp-ts/lib/ReadonlyTuple";
import * as S from "fp-ts/lib/string";
import * as N from "fp-ts/number";
import { readFileSync } from "fs";
import * as D from "io-ts/Decoder";
import type { Newtype } from "newtype-ts";
import { iso } from "newtype-ts";

interface SolverErrorProps {
  errorName: string;
  errorMessage: string;
}

interface SolverError
  extends Newtype<{ readonly SolverError: unique symbol }, SolverErrorProps> {}

const isoSolverError = iso<SolverError>();

export const createSolverError = ({
  errorName,
  errorMessage,
}: SolverErrorProps): SolverError =>
  isoSolverError.wrap({
    errorName,
    errorMessage,
  });

const formatSolverError = (error: SolverError) => {
  const { errorName, errorMessage } = isoSolverError.unwrap(error);
  return `${errorName}: ${errorMessage}`;
};

interface ReadInputProps {
  day: string;
  splitBy: string;
}

const bufToString = (buf: Buffer) => buf.toString("utf-8");

const readInput = ({ day, splitBy }: ReadInputProps) =>
  F.pipe(
    E.tryCatch(
      () => readFileSync(`inputs/${day}.txt`),
      () =>
        createSolverError({
          errorName: "InputError",
          errorMessage: "Failed to read input",
        }),
    ),
    E.map(F.flow(bufToString, S.trim, S.split(splitBy))),
  );

const handleAnswer = E.fold<SolverError, readonly [unknown, unknown], void>(
  F.flow(formatSolverError, console.error),
  <A, B>([first, second]: readonly [A, B]) => {
    console.log(`Part 1: ${first}`);
    console.log(`Part 2: ${second}`);
  },
);

export const runSolver = <A, B>(
  solver: (
    input: RNEA.ReadonlyNonEmptyArray<string>,
  ) => E.Either<SolverError, readonly [A, B]>,
) => F.flow(readInput, E.chain(solver), handleAnswer);

export const toTuple = <V>(val: V) => RT.flap(val)([I.of, I.of(val)]);

export const decode = <Decoder extends D.Decoder<unknown, D.TypeOf<Decoder>>,>(
  decoder: Decoder,
) =>
  F.flow(
    decoder.decode,
    E.mapLeft((decodeError) =>
      createSolverError({
        errorName: "DecodeError",
        errorMessage: D.draw(decodeError),
      }),
    ),
  );

export const sum = RA.foldMap(N.MonoidSum)(I.of<number>);
