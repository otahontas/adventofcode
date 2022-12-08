import { draw } from "io-ts/Decoder";
import { flow } from "fp-ts/lib/function";
import { iso } from "newtype-ts";
import { mapLeft } from "fp-ts/lib/Either";
import type { Decoder as GenericDecoder, TypeOf } from "io-ts/Decoder";
import type { Newtype } from "newtype-ts";

interface SolverErrorProps {
  errorName: string;
  errorMessage: string;
}

export interface SolverError
  extends Newtype<{ readonly SolverError: unique symbol }, SolverErrorProps> {}

export const createSolverError = ({
  errorName,
  errorMessage,
}: SolverErrorProps): SolverError =>
  iso<SolverError>().wrap({
    errorName,
    errorMessage,
  });

export const formatSolverError = (error: SolverError) => {
  // actual runtime type is SolverErrorProps, since this is opaque type for ts
  const { errorName, errorMessage } = error as unknown as SolverErrorProps;
  return `${errorName}: ${errorMessage}`;
};

export const decodeWithSolverError = <
  Decoder extends GenericDecoder<unknown, TypeOf<Decoder>>,
>(
  decoder: Decoder,
) =>
  flow(
    decoder.decode,
    mapLeft((decodeError) =>
      createSolverError({
        errorName: "DecodeError",
        errorMessage: draw(decodeError),
      }),
    ),
  );
