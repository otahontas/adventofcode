type ChunkedSplit<
  Input extends string,
  Delimiter extends string,
  Output extends string[] = [],
  ChunkSize extends number = 49
> = Output["length"] extends ChunkSize
  ? [Output, Input]
  : Input extends `${infer First}${Delimiter}${infer Rest}`
  ? ChunkedSplit<Rest, Delimiter, [...Output, First], ChunkSize>
  : [[...Output, Input], ""];

// TS handles max 50 elem arrays (exclusive), so chunk input and split by chunks
export type Split<Input extends string> = ChunkedSplit<
  Input,
  "\n"
> extends infer Result
  ? Result extends [string[], string]
    ? Result[1] extends ""
      ? Result[0]
      : [...Result[0], ...Split<Result[1]>]
    : never
  : never;
