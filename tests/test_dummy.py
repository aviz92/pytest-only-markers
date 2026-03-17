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


class TestDummyClass:
    @pytest.mark.ONLY_X
    def test_dummy_method(self):
        logger.info("Running test_dummy_method")
        assert True


class TestDummyClassWithFixture:
    def test_dummy_with_fixture(self):
        logger.info("Running test_dummy_with_fixture")
        assert True
