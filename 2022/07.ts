import * as RA from "fp-ts/lib/ReadonlyArray";
import { not, and } from "fp-ts/lib/predicate";
import * as Opt from "fp-ts/lib/Option";
// import * as E from "fp-ts/lib/Either";
import * as Tree from "fp-ts/lib/Tree";
import * as S from "fp-ts/lib/String";
import { flow, pipe } from "fp-ts/function";
// import { fromPredicate, map, Applicative } from "fp-ts/lib/Either";
import { fromPredicate } from "fp-ts/lib/Either";
// import { fromRecord, sequence } from "fp-ts/lib/ReadonlyRecord";
import { fromRecord } from "fp-ts/lib/ReadonlyRecord";
// import { head } from "fp-ts/lib/ReadonlyNonEmptyArray";
// import { of, append } from "fp-ts/lib/Array";
import { sum, min } from "lodash";
// import { match } from "ts-pattern";
import { createSolverError } from "./errors";
import { runSolver } from "./shared";

type Node =
  | {
      type: "folder";
      name: string;
    }
  | {
      type: "file";
      name: string;
      size: number;
    };

runSolver(
  flow(
    // Folders and their content are listed certain order so we can just chop over them
    RA.filter(and(not(S.includes("$ cd ..")))(not(S.includes("$ ls")))),
    (j) => {
      const res = pipe(
        j,
        RA.chop((p: readonly string[]) => {
          return pipe(
            p,
            RA.tail,
            Opt.map((o) => {
              const { init, rest } = pipe(
                o,
                RA.spanLeft(not(S.startsWith("$ cd"))),
              );
              return [init, rest] as const;
            }),
            Opt.fold(
              () => [[] as string[], [] as string[]],
              (result) => {
                // console.log("result", result);
                return result;
              },
            ),
          );
        }),
      );
      // console.log("res", res);
      let ind = 0;

      const root: Node = {
        type: "folder",
        name: "/",
      };

      const t = Tree.unfoldTree(root, (node: Node) => {
        let children: Node[] = [];
        if (node.type === "folder") {
          const arr = res[ind]!;
          // console.log("incoming dir", node);
          const mapped = arr.map((elem): Node => {
            if (elem.includes("dir")) {
              const [_, name] = elem.split(" ");
              return {
                type: "folder",
                name: name!,
              };
            }
            const [sizeRaw, name] = elem.split(" ");
            return {
              type: "file",
              size: Number(sizeRaw!),
              name: name!,
            };
          });
          children = mapped;
          // console.log("returning childen", children);
          // console.log("=======");
          ind++;
        }
        return [node, children];
      });

      // console.log("t tree", t);

      // console.log("folding tree");

      const sums: number[] = [];

      const res2 = Tree.fold((node: Node, children: Node[]): Node => {
        // console.log("node", node);
        // console.log("children:");
        // children.forEach((child) => console.log(child));
        children.forEach((child) => {
          if (child.type === "file" && child.name.includes("dir")) {
            sums.push(child.size);
          }
        });
        return node.type === "file"
          ? node
          : {
              type: "file",
              name: `dir ${node.name}`,
              size: sum(children.map((k) => (k as any).size)),
            };
      })(t);
      sums.push((res2 as any).size);
      const ans1 = sum(sums.filter((n) => n <= 100000));
      console.log("ans1", ans1);

      const total = 70000000;
      // const needed = 30000000;
      const filled = (res2 as any).size as number;
      const unused = total - filled;
      const needed = 30000000 - 19177471;
      console.log("unused", unused);
      console.log("needed", needed);
      console.log("ans2", min(sums.filter((n) => n >= needed)));

      return j;
    },
    () =>
      fromRecord({
        first: 0,
        second: 0,
      }),
    fromPredicate(
      () => false,
      () => createSolverError({ errorName: "paske", errorMessage: "poske" }),
    ),
  ),
)({ day: "07", splitBy: "\n" });
