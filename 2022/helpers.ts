import * as E from "fp-ts/lib/Either";
import { readFileSync } from "fs";

export const unSafeReadInput = (day: string, splitBy: string) =>
  readFileSync(`inputs/${day}.txt`)
    .toString()
    .trimStart()
    .trimEnd()
    .split(splitBy);

export const readInput = (day: string, splitBy: string) =>
  E.tryCatch(
    () => unSafeReadInput(day, splitBy),
    () => new Error("Failed to read input"),
  );

export const handleAnswer = E.fold(
  (error) => {
    console.error("Error happened:", error);
  },
  (answer) => {
    if (Array.isArray(answer)) {
      const [first, second] = answer;
      console.log(`Part 1: ${first}`);
      console.log(`Part 2: ${second}`);
    } else {
      console.log(`Answer: ${answer}`);
    }
  },
);

export type ArrayType<Arr extends readonly unknown[] | unknown[]> =
  Arr extends readonly (infer Item)[]
    ? Item
    : Arr extends (infer Item)[]
    ? Item
    : Arr;
