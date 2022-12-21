import * as F from "fp-ts/function";
import * as E from "fp-ts/lib/Either";
import * as O from "fp-ts/lib/Option";
import * as RNEA from "fp-ts/lib/ReadonlyNonEmptyArray";
import * as RA from "fp-ts/lib/ReadonlyArray";
import * as RR from "fp-ts/lib/ReadonlyRecord";
import * as S from "fp-ts/lib/string";
import { createRegExp, digit, oneOrMore, global } from "magic-regexp";
import * as D from "io-ts/Decoder";
import type * as B from "fp-ts/boolean";
import { runSolver, decode } from "./shared";

interface Monkey {
  items: number[];
  operation: (old: number) => number;
  test: (val: number) => boolean;
  toMonkey: typeof B.fold<number>;
}
const readNumbersFromString = F.flow(
  (s: string) => [...s.matchAll(createRegExp(oneOrMore(digit), [global]))],
  RA.map(RR.lookup("0")),
  O.sequenceArray,
  O.map(RA.map(Number)),
);

const toMonkey = F.flow(
  S.split("\n"),
  (s) => s.slice(1),
  decode(D.tuple(D.string, D.string, D.string, D.string, D.string)),
  E.map((id): Monkey => {
    const monkey = {
      items: readNumbersFromString(id[0]),
      operation: F.flow(
        S.split(" = "),
        RA.lookup(1),
        O.map(
          (operation) => (old: number) =>
            eval(operation.replaceAll("old", old.toString())),
        ),
      )(id[1]),
      test: F.flow(readNumbersFromString, O.chain(RA.head), O.map(
        divisor => (val: number) => val % divisor == 0
      ))(id[2]),
      toMonkey: (
        () => "jee",
        () => "jee",

      ) => (value: boolean)
    };

    const toMonkeyIfTrue = F.flow(
      readNumbersFromString,
      O.chain(RA.head),
    )(id[2]);
    const toMonkeyIfFalse = F.flow(
      readNumbersFromString,
      O.chain(RA.head),
    )(id[2]);
    // const toMonkeyIfTrue = safeGetSingleNumber(id[4])
    console.log("items", items);
    console.log("operation", operationStr);
    console.log("test", testDivisor);
    console.log("toMonkeyIfTrue", toMonkeyIfTrue);
    console.log("toMonkeyIfFalse", toMonkeyIfFalse);
    console.log("====");

    return {
      items,
    };
  }),
);

runSolver(
  F.flow((k) => {
    RNEA.map((j: string) => {
      console.log("to monkey res", toMonkey(j));
    })(k);
    k;
    return E.right([0, 0] as const);
  }),
)({ day: "11", splitBy: "\n\n" });
