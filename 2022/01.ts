import * as F from "fp-ts/function";
import * as E from "fp-ts/lib/Either";
import * as RNEA from "fp-ts/lib/ReadonlyNonEmptyArray";
import * as RT from "fp-ts/lib/ReadonlyTuple";
import * as S from "fp-ts/lib/string";
import * as N from "fp-ts/number";
import * as O from "fp-ts/Ord";
import * as D from "io-ts/Decoder";
import { decode, runSolver, sum, toTuple } from "./shared";

runSolver(
  F.flow(
    RNEA.map(F.flow(S.split("\n"), RNEA.map(Number), sum)),
    RNEA.sort(O.reverse(N.Ord)),
    decode(D.tuple(D.number, D.number, D.number)),
    E.map(F.flow(toTuple, RT.bimap(sum, RNEA.head))),
  ),
)({ day: "01", splitBy: "\n\n" });
