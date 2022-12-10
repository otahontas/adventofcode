import * as A from "fp-ts/lib/Array";
import * as E from "fp-ts/lib/Either";
import * as RNEA from "fp-ts/lib/ReadonlyNonEmptyArray";
import { flow } from "fp-ts/function";
import { fromRecord } from "fp-ts/lib/ReadonlyRecord";
import { reduce } from "fp-ts/lib/ReadonlyArray";
import { tuple, number } from "io-ts/Decoder";
import { createSolverError, decodeWithSolverError } from "./errors";
import { runSolver } from "./shared";

runSolver(
  flow(
    RNEA.map(
      flow(
        (line) => line.match(/\d+/g),
        E.fromNullable(
          createSolverError({
            errorName: "EmptyLineError",
            errorMessage: "Line must contain numbers",
          }),
        ),
        E.chain(
          flow(
            A.map(Number),
            decodeWithSolverError(tuple(number, number, number, number)),
          ),
        ),
      ),
    ),
    E.sequenceArray,
    E.map(
      reduce(fromRecord({ first: 0, second: 0 }), (acc, curr) => {
        const [a, b, c, d] = curr;
        const { first, second } = acc;
        const contained = (a <= c && b >= d) || (c <= a && d >= b);
        const overlaps = (a <= c && b >= c) || (c <= a && d >= a);
        return fromRecord({
          first: contained ? first + 1 : first,
          second: overlaps ? second + 1 : second,
        });
      }),
    ),
  ),
)({ day: "04", splitBy: "\n" });
