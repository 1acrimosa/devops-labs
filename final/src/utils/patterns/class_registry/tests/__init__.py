"""Tests."""

import typing


class Pokemon:
    """A basic class with some attributes that we can use to test out class registries."""

    element: typing.Optional[str]

    def __init__(self, name: typing.Optional[str] = None):
        """Initialize a new pokémon."""
        super().__init__()

        self.name: typing.Optional[str] = name


# Define some classes that we can register.
class Charmander(Pokemon):
    """A fire-type pokémon."""

    element: typing.Optional[str] = "fire"


class Charmeleon(Pokemon):
    """A fire-type pokémon."""

    element: typing.Optional[str] = "fire"


class Squirtle(Pokemon):
    """A water-type pokémon."""

    element: typing.Optional[str] = "water"


class Wartortle(Pokemon):
    """A water-type pokémon."""

    element: typing.Optional[str] = "water"


class Bulbasaur(Pokemon):
    """A grass-type pokémon."""

    element: typing.Optional[str] = "grass"


class Ivysaur(Pokemon):
    """A grass-type pokémon."""

    element: typing.Optional[str] = "grass"


class Mew(Pokemon):
    """A psychic-type pokémon."""

    element: typing.Optional[str] = "psychic"


class PokemonFactory:
    """A factory that can produce new pokémon on demand.  Used to test how registries behave when a method/function is registered instead of a class."""

    @classmethod
    def create_psychic_pokemon(cls, name: typing.Optional[str] = None):
        """Create a new psychic-type pokémon."""
        return Mew(name)  # pragma: no cover
