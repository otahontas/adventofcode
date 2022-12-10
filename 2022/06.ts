import { flow } from "fp-ts/function";
import { fromPredicate, map, Applicative } from "fp-ts/lib/Either";
import { fromRecord, sequence } from "fp-ts/lib/ReadonlyRecord";
import { head } from "fp-ts/lib/ReadonlyNonEmptyArray";
import { of, append } from "fp-ts/lib/Array";
import { sum } from "lodash";
import { createSolverError } from "./errors";
import { runSolver } from "./shared";

const findMarker = (length: number) =>
  flow(
    (datastream: string) =>
      Array.from(datastream).findIndex(
        (_val, index) =>
          new Set(datastream.slice(index, index + length)).size === length,
      ),
    fromPredicate(
      (n) => n === -1,
      () =>
        createSolverError({
          errorName: "FindMarkerError",
          errorMessage: "Couldn't find marker",
        }),
    ),
    map(flow(of, append(length), sum)),
  );

runSolver(
  flow(
    head,
    (datastream) =>
      fromRecord({
        first: findMarker(4)(datastream),
        second: findMarker(14)(datastream),
      }),
    sequence(Applicative),
  ),
);
