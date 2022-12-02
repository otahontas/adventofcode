import { match } from "ts-pattern";
import { readInput } from "./helpers";

const inputError = new Error("Wrong input");

type Choice = 0 | 1 | 2;

const CHOICE_AMOUNT = 3 as const;

const scores = {
	lose: 0,
	draw: 3,
	win: 6,
} as const;

const actUponPart2 = {
	0: "lose",
	1: "draw",
	2: "win",
} as const;

// JS mod doesn't flip negative inputs around :(
const mod = (x: number, m: number) => ((x % m) + m) % m;

const sanitize = (char: string): Choice =>
	match(char)
		.with("A", () => 0 as const)
		.with("B", () => 1 as const)
		.with("C", () => 2 as const)
		.with("X", () => 0 as const)
		.with("Y", () => 1 as const)
		.with("Z", () => 2 as const)
		.otherwise(() => {
			throw inputError;
		});

// take double mod so remainder ends up being positive
const get_my_score = (opp: number, me: number) =>
	match([opp, me] as const)
		.when(
			([opp, me]) => opp === me,
			() => scores["draw"],
		)
		.otherwise(([opp, me]) =>
			mod(mod(opp - me, CHOICE_AMOUNT), CHOICE_AMOUNT) < CHOICE_AMOUNT / 2
				? scores["lose"]
				: scores["win"],
		);

const getMePt2 = (opp: Choice, me: Choice) =>
	match(actUponPart2[me])
		.with("lose", () => mod(opp - 1, CHOICE_AMOUNT))
		.with("draw", () => opp)
		.with("win", () => mod(opp + 1, CHOICE_AMOUNT))
		.otherwise(() => {
			throw inputError;
		});

const [first, second] = readInput("02", "\n").reduce<[number, number]>(
	([first, second], curr) => {
		const [opp, me] = curr.split(" ").map((char) => sanitize(char));
		if (opp !== undefined && me !== undefined) {
			const mePt2 = getMePt2(opp, me);
			return [
				first + get_my_score(opp, me) + (me + 1),
				second + get_my_score(opp, mePt2) + (mePt2 + 1),
			];
		}
		throw inputError;
	},
	[0, 0],
);

console.log("Part 1:", first);
console.log("Part 2:", second);
