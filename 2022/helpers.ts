import { readFileSync } from "fs";
export const readInput = (day: string, splitBy: string) =>
	readFileSync(`inputs/${day}.txt`)
		.toString()
		.trimStart()
		.trimEnd()
		.split(splitBy);
export const sum = (nums: number[]) => nums.reduce<number>((a, b) => a + b, 0);
