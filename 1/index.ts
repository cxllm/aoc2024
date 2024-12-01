import fs from "fs";

let file: Array<string> = fs
	.readFileSync(`${__dirname}/input.txt`, "utf-8")
	.split("\r\n");
let left: Array<number> = [];
let right: Array<number> = [];
// Parsing the input file
for (const line of file) {
	let split = line.split("   ");
	let l = split[0];
	let r = split[1];
	left.push(parseInt(l));
	right.push(parseInt(r));
}
// Part 1
left = left.sort();
right = right.sort();

let distances: Array<number> = [];
for (const item in left) distances.push(Math.abs(left[item] - right[item]));

console.log(
	"Part 1:",
	distances.reduce((sum, a) => sum + a, 0)
);

// Part 2
let similarityScore = 0;
for (const leftItem of left) {
	let instances = 0;
	for (const rightItem of right) {
		if (leftItem === rightItem) {
			instances += 1;
		}
	}
	similarityScore += instances * leftItem;
}
console.log("Part 2:", similarityScore);
