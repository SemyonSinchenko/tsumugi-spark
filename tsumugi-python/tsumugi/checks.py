from typing import Self

from .enums import CheckLevel
from .proto import suite_pb2 as suite


class CheckBuilder:
    def __init__(self) -> None:
        self._level: CheckLevel = CheckLevel.Warning
        self._constraints: list[suite.Check.Constraint] = list()
        self._description: str = ""

    def with_level(self, level: CheckLevel) -> Self:
        self._level = level
        return self

    def with_description(self, decription: str) -> Self:
        self._description = decription
        return self

    def with_constraint(self, constraint: suite.Check.Constraint) -> Self:
        self._constraints.append(constraint)
        return self

    def with_constraints(self, constraints_list: list[suite.Check.Constraint]) -> Self:
        self._constraints = constraints_list
        return self

    def _validate(self) -> None:
        if len(self._constraints) == 0:
            raise ValueError("At least one constraint is required")

    def build(self) -> suite.Check:
        return suite.Check(
            checkLevel=self._level,
            description=self._description,
            constraints=self._constraints,
        )
