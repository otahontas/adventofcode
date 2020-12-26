import re
from aocd import lines
from collections import defaultdict

Node = str
Edge = tuple[Node, int]
Graph = dict[Node, list[Edge]]


def create_graphs(rules: list[str]) -> tuple[Graph, Graph]:
    graph: dict[str, list[Edge]] = defaultdict(list)
    reversed_graph: dict[str, list[Edge]] = defaultdict(list)
    for rule in rules:
        container, content = rule.split(" bags contain ")
        content = re.findall(r"(\d+) ([\w\s]+(?= ))", content)
        for amount, bag in content:
            graph[container].append((bag, int(amount)))
            reversed_graph[bag].append((container, int(amount)))
    return graph, reversed_graph


def first(graph: Graph) -> int:
    def dfs(bag: str) -> None:
        if bag in seen:
            return
        seen.add(bag)
        for content, _ in graph[bag]:
            dfs(content)

    seen = set()
    dfs("shiny gold")
    return len(seen) - 1


def second(graph: Graph) -> int:
    def dfs(bag: str, amount: int) -> int:
        if bag not in graph:
            return amount
        new = 0 if bag == "shiny gold" else amount
        for content, num in graph[bag]:
            new += dfs(content, num * amount)
        return new

    return dfs("shiny gold", 1)


def main() -> None:
    graph, reversed_graph = create_graphs(rules=lines)
    print("Part 1:", first(graph=reversed_graph))
    print("Part 2:", second(graph=graph))


if __name__ == "__main__":
    main()
