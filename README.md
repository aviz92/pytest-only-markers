![PyPI version](https://img.shields.io/pypi/v/pytest-only-markers)
![Python](https://img.shields.io/badge/python->=3.12-blue)
![Development Status](https://img.shields.io/badge/status-beta-yellow)
![Maintenance](https://img.shields.io/maintenance/yes/2026)
![PyPI](https://img.shields.io/pypi/dm/pytest-only-markers)
![License](https://img.shields.io/pypi/l/pytest-only-markers)

---

# 💡 pytest-only-markers
A pytest plugin that lets you isolate specific tests using `ONLY_*` markers.
When any test is decorated with a marker prefixed `ONLY_`, only those tests are collected and run — all other tests (and their inherited `pytestmark` markers) are suppressed.

---

## 📦 Installation
```bash
uv add pytest-only-markers
```

---

## 🚀 Features
- ✅ **Selective collection** — only tests carrying an `ONLY_*` marker are collected; all others are deselected
- ✅ **Marker isolation** — non-`ONLY_*` markers (including module-level `pytestmark`) are stripped from matching items
- ✅ **Transparent deselection** — skipped tests appear in pytest's `x deselected` summary, not silently dropped
- ✅ **Instance-level patch** — `iter_markers` is patched per item so downstream plugins see only `ONLY_*` markers
- ✅ **Opt-in via flag** — behaviour is disabled by default; activate with `--only-markers-prefix`

---

## 🛠️ How to Use
1. Install the plugin via `uv add pytest-only-markers`
2. Enable it by adding `--only-markers-prefix` to your `pytest.ini` or passing it on the CLI
3. Decorate any test with `@pytest.mark.ONLY_<name>` to mark it for isolated execution
4. Run pytest — only tests with `ONLY_*` markers will be collected and executed

---

## 🚀 Quick Start

Add to `pytest.ini`:
```ini
[pytest]
addopts = --only-markers-prefix
markers =
    ONLY_smoke: Run only smoke tests
    ONLY_api: Run only API tests
```

Then tag your tests:
```python
pytestmark = [pytest.mark.regression, pytest.mark.slow]

@pytest.mark.ONLY_smoke
def test_health_check():
    ...
# Collected and run — effective markers: ONLY_smoke only

def test_full_flow():
    ...
# Deselected — no ONLY_* marker
```

---

## ▶️ Usage Examples

### Example 1: Single ONLY_ marker
```python
import pytest

pytestmark = [pytest.mark.regression, pytest.mark.slow]

@pytest.mark.ONLY_smoke
def test_ping():
    assert True
# Result: collected, runs with only ONLY_smoke marker
# test_heavy and test_regression are deselected
```

### Example 2: Multiple ONLY_ markers on one test
```python
import pytest

pytestmark = [pytest.mark.dummy]

@pytest.mark.ONLY_api
@pytest.mark.ONLY_smoke
def test_create_user():
    assert True
# Result: collected, effective markers are ONLY_api + ONLY_smoke
# pytestmark (dummy) is stripped
```

### Example 3: CLI usage without modifying pytest.ini
```bash
pytest --only-markers-prefix tests/
```

---

## 🤝 Contributing

If you have a helpful pattern or improvement to suggest:
Fork the repo
Create a new branch
Submit a pull request
I welcome additions that promote clean, productive, and maintainable development.

---

## 📄 License

MIT License — see [LICENSE](LICENSE) for details.

---

## 🙏 Thanks
Thanks for exploring this repository! <br>
Happy coding!

[![GitHub](https://img.shields.io/badge/GitHub-aviz92-181717?logo=github)](https://github.com/aviz92)
&nbsp; [![PyPI](https://img.shields.io/badge/PyPI-aviz-3775A9?logo=pypi)](https://pypi.org/user/aviz/)
&nbsp; [![Blog](https://img.shields.io/badge/Blog-aviz92.github.io-0066CC?logo=googlechrome)](https://aviz92.github.io/)
&nbsp; [![LinkedIn](https://img.shields.io/badge/LinkedIn-avi--zaguri-0A66C2?logo=linkedin)](https://www.linkedin.com/in/avi-zaguri-41869b11b)
