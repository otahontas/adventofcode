import * as A from "fp-ts/lib/Array";
import * as E from "fp-ts/lib/Either";
import * as F from "fp-ts/function";
import * as Opt from "fp-ts/lib/Option";
import * as RA from "fp-ts/lib/ReadonlyArray";
import { range } from "lodash";
import { readInput, handleAnswer } from "./helpers";
import type { ArrayType } from "./helpers";

F.pipe(
  readInput("04", "\n"),
  E.map(
    F.flow(
      A.map(
        F.flow(
          (line) => line.match(/\d+/g),
          E.fromNullable(new Error("Line must contain numbers")),
          E.map(
            F.flow(
              (nums) => [...range(0, 4).map((index) => A.lookup(index)(nums))],
              Opt.sequenceArray,
              Opt.map(
                RA.traverse(Opt.Applicative)((element) =>
                  isNaN(Number(element)) ? Opt.none : Opt.some(Number(element)),
                ),
              ),
              Opt.flatten,
              Opt.fold(
                () =>
                  E.left(
                    new Error("There wasn't enough numbers in input array"),
                  ),
                <Arr extends readonly unknown[], Item = ArrayType<Arr>>(
                  val: Arr,
                ) =>
                  // we can cast since we know successful case contains 4 elements
                  E.right(val as unknown as readonly [Item, Item, Item, Item]),
              ),
            ),
          ),
          E.flatten,
        ),
      ),
      E.sequenceArray,
      E.map(
        RA.reduce([0, 0] as [number, number], (acc, curr) => {
          const [a, b, c, d] = curr;
          const [first, second] = acc;
          const contained = (a <= c && b >= d) || (c <= a && d >= b);
          const overlaps = (a <= c && b >= c) || (c <= a && d >= a);
          return [
            contained ? first + 1 : first,
            overlaps ? second + 1 : second,
          ] as [number, number];
        }),
      ),
    ),
  ),
  E.flatten,
  handleAnswer,
);
