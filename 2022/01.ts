import { sum } from "lodash"
import { readInput } from "./helpers";

const descendingSums = readInput("01", "\n\n")
	.reduce<number[]>(
		(acc, curr) => [...acc, sum(curr.split("\n").map(Number))],
		[],
	)
	.sort((a, b) => b - a);

console.log(`Part 1: ${descendingSums[0]}`);
console.log(`Part 2: ${sum(descendingSums.slice(0, 3))}`);
