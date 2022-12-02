import { readFileSync } from "fs";
export const readInput = (day: string, splitBy: string) =>
  readFileSync(`inputs/${day}.txt`)
    .toString()
    .trimStart()
    .trimEnd()
    .split(splitBy);
