import * as E from "fp-ts/lib/Either";
import * as RNEA from "fp-ts/lib/ReadonlyNonEmptyArray";
import { Ord } from "fp-ts/number";
import { flow } from "fp-ts/function";
import { fromRecord } from "fp-ts/lib/ReadonlyRecord";
import { reverse } from "fp-ts/Ord";
import { split } from "fp-ts/lib/string";
import { sum } from "lodash";
import { tuple, number } from "io-ts/Decoder";
import { decodeWithSolverError } from "./errors";
import { runSolver } from "./helpers";

runSolver(
  flow(
    RNEA.map(flow(split("\n"), RNEA.map(Number), sum)),
    RNEA.sort(reverse(Ord)),
    decodeWithSolverError(tuple(number, number, number)),
    E.map((threeBiggest) =>
      fromRecord({ first: threeBiggest[0], second: sum(threeBiggest) }),
    ),
  ),
)({ day: "01", splitBy: "\n\n" });
