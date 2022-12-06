import * as A from "fp-ts/lib/Array";
import * as E from "fp-ts/lib/Either";
import * as F from "fp-ts/function";
import { readInput, handleAnswer } from "./helpers";

const findMarker = (datastream: string) => (length: number) =>
  Array.from(datastream).findIndex(
    (_val, index) =>
      new Set(datastream.slice(index, index + length)).size === length,
  ) + length;

F.pipe(
  readInput("06", "\n"),
  E.map(
    F.flow(
      A.head,
      E.fromOption(() => new Error("Input must be at least one line")),
      E.map((datastream) => [4, 14].map(findMarker(datastream))),
    ),
  ),
  E.flatten,
  handleAnswer,
);
