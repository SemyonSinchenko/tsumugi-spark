from typing_extensions import Self

from tsumugi.analyzers import AnalyzerOptions, Completeness, ConstraintBuilder, Size

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

    def has_size(
        self, expected_size: float, hint: str = "", name: str | None = None
    ) -> Self:
        """Add a constraint that the DataFrame has size like expected."""
        return self.with_constraint(
            ConstraintBuilder()
            .for_analyzer(Size())
            .with_hint(hint)
            .with_name(name or "Size")
            .should_be_eq_to(expected_size)
            .build()
        )

    def is_complete(
        self,
        column: str,
        hint: str = "",
        name: str | None = None,
        where: str | None = None,
        options: AnalyzerOptions | None = None,
    ) -> Self:
        """Add a constraint that the column doesn not have missings."""
        return self.has_completeness(column, 1.0, hint, name, where, options)

    def has_completeness(
        self,
        column: str,
        expected_value: float,
        hint: str = "",
        name: str | None = None,
        where: str | None = None,
        options: AnalyzerOptions | None = None,
    ) -> Self:
        """Add a constraint the the column has an expected part of missings."""
        return self.with_constraint(
            ConstraintBuilder()
            .for_analyzer(
                Completeness(
                    column=column,
                    where=where,
                    options=options or AnalyzerOptions.default(),
                )
            )
            .with_hint(hint)
            .with_name(name or f"Completeness({column})")
            .should_be_eq_to(expected_value)
            .build()
        )

    def are_complete(
        self,
        columns: list[str],
        hint: str = "",
        name: str | None = None,
        where: str | None = None,
        options: AnalyzerOptions | None = None,
    ) -> Self:
        """Add a constraint that columns have an expected part of missings."""
        return self.have_completeness(columns, 1.0, hint, name, where, options)

    def have_completeness(
        self,
        columns: list[str],
        expected_value: float,
        hint: str = "",
        name: str | None = None,
        where: str | None = None,
        options: AnalyzerOptions | None = None,
    ) -> Self:
        """Add a constraint that columns have an expected level of completeness."""
        return self.with_constraints(
            [
                ConstraintBuilder()
                .for_analyzer(
                    Completeness(
                        column=col,
                        where=where,
                        options=options or AnalyzerOptions.default(),
                    )
                )
                .with_name(name or f"Completeness({col})")
                .with_hint(hint)
                .should_be_eq_to(expected_value)
                .build()
                for col in columns
            ]
        )

    def _validate(self) -> None:
        if len(self._constraints) == 0:
            raise ValueError("At least one constraint is required")

    def build(self) -> suite.Check:
        return suite.Check(
            checkLevel=self._level,
            description=self._description,
            constraints=self._constraints,
        )
