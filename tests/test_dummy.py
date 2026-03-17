import pytest

from custom_python_logger import get_logger, build_logger

logger = build_logger(__name__)

pytestmark = [
    pytest.mark.dummy_x,
    pytest.mark.dummy_y,
]

@pytest.mark.ONLY_dummy_x
@pytest.mark.ONLY_dummy_y
def test_dummy():
    logger.info("Running test_dummy")
    assert True


class TestDummyClass:
    @pytest.mark.only_dummy_x
    def test_dummy_method(self):
        logger.info("Running test_dummy_method")
        assert True


class TestDummyClassWithFixture:
    def test_dummy_with_fixture(self):
        logger.info("Running test_dummy_with_fixture")
        assert True
