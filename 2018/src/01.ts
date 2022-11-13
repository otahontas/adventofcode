import type { Add, Subtract } from "ts-arithmetic";
import type { Split, StringToNumber } from "./helpers";
import type { Input } from "././01_input";

type ParseRow<Input extends string> =
  Input extends `${infer Sign}${infer Value}`
    ? [Sign, StringToNumber<Value>]
    : never;

type ParseRows<Input extends string[]> = Input extends [
  infer Row,
  ...infer Rest
]
  ? Row extends string
    ? Rest extends string[]
      ? [ParseRow<Row>, ...ParseRows<Rest>]
      : never
    : never
  : Input extends [infer Row]
  ? Row extends string
    ? [ParseRow<Row>]
    : never
  : [];

type Row = ["+" | "-", number];

type RowToOutput<R extends Row, Output extends number> = R[0] extends "+"
  ? Add<Output, R[1]>
  : Subtract<Output, R[1]>;

type SolveFirst<
  Input extends Row[],
  Output extends number = 0
> = Input extends [infer First, ...infer Rest]
  ? First extends Row
    ? Rest extends Row[]
      ? SolveFirst<Rest, RowToOutput<First, Output>>
      : never
    : never
  : Input extends [infer First]
  ? First extends Row
    ? RowToOutput<First, Output>
    : never
  : Output;

// TODO: run whole split -> parse -> solve chunked per 49 inputs
type Splitted = Split<Input>;

// type FirstAnswer = TODO
