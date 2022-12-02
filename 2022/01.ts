import * as A from "fp-ts/lib/Array";
import * as E from "fp-ts/lib/Either";
import * as F from "fp-ts/function";
import * as N from "fp-ts/number";
import * as Opt from "fp-ts/lib/Option";
import * as Ord from "fp-ts/Ord";
import * as RA from "fp-ts/lib/ReadonlyArray";
import * as S from "fp-ts/lib/string";
import { sum, range } from "lodash";
import { printAnswers, readInput } from "./helpers";
import type { ArrayType } from "./helpers";

F.pipe(
  readInput("01", "\n\n"),
  E.map(
    F.flow(
      // Parse input
      A.map(S.split("\n")),
      RA.map(RA.map(Number)),
      RA.map(sum),
      RA.sort(Ord.reverse(N.Ord)),
      (nums) => [...range(0, 3).map((index) => RA.lookup(index)(nums))],
      Opt.sequenceArray,
      Opt.fold(
        () => E.left(new Error("There wasn't enough numbers in input array")),
        <Arr extends readonly unknown[], Item = ArrayType<Arr>>(val: Arr) =>
          // we can cast since we know successful case contains 3 elements
          E.right(val as unknown as readonly [Item, Item, Item]),
      ),
    ),
  ),
  E.flatten,
  E.map((threeBiggest) => [threeBiggest[0], sum(threeBiggest)] as const),
  E.fold(
    (error) => console.error("Error happened:", error),
    (result) => printAnswers(result),
  ),
);
