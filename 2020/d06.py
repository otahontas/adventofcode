from aocd import data


def main() -> None:
    groups = data.split("\n\n")
    first, second = 0, 0

    for answers in groups:
        answer_ids = {answer for answer in answers if answer.isalpha()}
        first += len(answer_ids)
        for person in answers.split("\n"):
            answer_ids &= set(person)
        second += len(answer_ids)
    print("Part 1:", first)
    print("Part 2:", second)


if __name__ == "__main__":
    main()
