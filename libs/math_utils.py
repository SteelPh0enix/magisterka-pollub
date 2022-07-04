from numpy import number, random
from typing import cast, Tuple, Mapping, Any, Generator

# for interpolation, use numpy.interp:
# >>> from numpy import interp
# >>> interp(256,[1,512],[5,10])
# 7.4951076320939336

ValueOrRange = float | Mapping[int, float]

_module_rng = random.default_rng()


def _to_float(value: Any) -> float:
    return float(cast(float, value))


def _extract_range(range: ValueOrRange) -> Tuple[float, float]:
    """This function extracts range from ValueOrRange value.

    The rules are simple:
        * If range is float or 1-element collection, return (-range, range);
        * If range is 2-element collection, return (range[0], range[1])

    If range has more than 2 elements, only first two are used, and the rest is ignored"""

    if isinstance(range, float) or isinstance(range, int) or isinstance(range, number):
        return (-float(range), float(range))
    elif len(cast(Mapping, range)) == 1:
        range_collection = cast(Mapping, range)
        return (-_to_float(range_collection[0]), _to_float(range_collection[0]))
    elif len(cast(Mapping, range)) >= 2:
        range_collection = cast(Mapping, range)
        return (_to_float(range_collection[0]), _to_float(range_collection[1]))

    raise RuntimeError(f"Invalid range {range}. Range must have at least 1 element.")


def random_uniform_float(
    range: ValueOrRange, generator: random.Generator | None = None
) -> float:
    """Returns a random float in specified range, generated with uniform distribution.
    Uses internal generator defined in this module by default.
    If you pass a single float as a range, it'll be translated to [-range, range).
    If you want full control over the range, just pass it as a tuple."""
    if generator is None:
        generator = _module_rng

    normalized_range = _extract_range(range)
    return generator.uniform(normalized_range[0], normalized_range[1])


def random_normal_float(
    mean: float = 0.0,
    deviation: float = 1.0,
    generator: random.Generator | None = None,
) -> float:
    """Returns a random float, generated with normal distribution.
    Uses internal generator defined in this module by default.
    You can adjust the distribution characteristics via mu and sigma arguments."""
    if generator is None:
        generator = _module_rng

    return generator.normal(mean, deviation)


def add_noise(
    value: float,
    mean: float = 0.0,
    deviation: float = 1.0,
    generator: random.Generator | None = None,
) -> float:
    """Returns the passed value with random gaussian noise.
    You can tweak the distribution settings with mu and sigma arguments.
    By default it uses default_rng created in this module scope, you can pass different Generator if you want"""

    if generator is None:
        generator = _module_rng

    noise = generator.normal(mean, deviation)

    return value + noise


def noisy_numbers_generator(
    range: ValueOrRange,
    bias_mean: float,
    bias_variance: float,
    generator: random.Generator | None = None,
) -> Generator[Tuple[float, float, float], None, None]:
    """This generator creates random numbers with bias, variance, and bias variance to represent realistic, noisy measurements

    Returns a tuple with (noised number, original number, noise value)"""
    if generator is None:
        generator = _module_rng

    while True:
        original = random_uniform_float(range, generator)
        noise = random_normal_float(bias_mean, bias_variance, generator)
        yield original + noise, original, noise
