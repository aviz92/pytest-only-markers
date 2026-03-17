import pytest

from custom_python_logger import get_logger, build_logger

logger = build_logger(__name__)

pytestmark = [
    pytest.mark.regular,
    pytest.mark.dummy,
]

@pytest.mark.ONLY_X
@pytest.mark.ONLY_Y
def test_dummy():
    logger.info("Running test_dummy")
    assert True
