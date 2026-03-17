import pytest
from _pytest.mark.structures import Mark

DEFAULT_PREFIX: str = "ONLY_"


def pytest_addoption(parser: pytest.Parser) -> None:
    parser.addoption(
        "--only-markers-prefix",
        action="store_true",
        default=False,
        help=(
            "Prefix that triggers the ONLY marker override behaviour. "
            f"Default: {DEFAULT_PREFIX!r}"
        ),
    )


def pytest_configure(config: pytest.Config) -> None:
    if not config.getoption("--only-markers-prefix"):
        return


@pytest.hookimpl(tryfirst=True)
def pytest_collection_modifyitems(config: pytest.Config, items: list[pytest.Item]) -> None:
    """Override markers for every item that carries at least one ONLY_* marker."""

    if not config.getoption("--only-markers-prefix"):
        return

    for item in items:
        only_markers: list[Mark] = [m for m in item.own_markers if m.name.startswith(DEFAULT_PREFIX)]
        if not only_markers:
            continue

        item.own_markers[:] = only_markers
        item.iter_markers = lambda name=None: (
            iter(only_markers) if name is None
            else (m for m in only_markers if m.name == name)
        )
