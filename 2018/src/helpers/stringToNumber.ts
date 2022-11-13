import type { Add, Multiply, Pow, Subtract } from "ts-arithmetic";

type Digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9];
type CharToDigit<Char extends string> = Extract<
  Char extends keyof Digits ? Digits[Char] : never,
  number
>;

type RecursivelyConvert<
  Input extends string[],
  PowOf10 extends number,
  Output extends number = 0
> = Input extends [infer Digit, ...infer Rest]
  ? Digit extends string
    ? Rest extends string[]
      ? RecursivelyConvert<
          Rest,
          Subtract<PowOf10, 1>,
          Add<Output, Multiply<CharToDigit<Digit>, Pow<10, PowOf10>>>
        >
      : never
    : never
  : Input extends [infer Digit]
  ? Digit extends string
    ? Add<Output, Multiply<CharToDigit<Digit>, Pow<10, PowOf10>>>
    : never
  : Output;

type StringToChars<
  Input extends string,
  List extends string[] = []
> = Input extends `${infer Char}${infer Rest}`
  ? StringToChars<Rest, [...List, Char]>
  : List;

export type StringToNumber<Input extends string> =
  StringToChars<Input> extends infer Chars
    ? Chars extends string[]
      ? RecursivelyConvert<Chars, Subtract<Chars["length"], 1>>
      : never
    : never;
