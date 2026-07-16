# PyPI Publishing Checklist

Complete this checklist before publishing your package to PyPI.

## Code Quality

- [ ] All functions have proper docstrings
- [ ] Type hints are added to all functions
- [ ] Code follows PEP 8 style guidelines
- [ ] Run linter: `flake8 easy_to_maths/`
- [ ] Run formatter: `black easy_to_maths/`
- [ ] Code type-checked: `mypy easy_to_maths/`

## Testing

- [ ] Unit tests written for all functions
- [ ] All tests pass: `pytest tests/ -v`
- [ ] Test coverage is adequate (>80%): `pytest tests/ --cov=easy_to_maths`
- [ ] Edge cases tested (zero, negatives, floats)
- [ ] Error cases tested (ZeroDivisionError, etc.)

## Documentation

- [ ] README.md is complete and accurate
- [ ] Docstrings include examples
- [ ] Installation instructions are clear
- [ ] Usage examples are provided
- [ ] Contributing guidelines included
- [ ] License mentioned in README

## File Structure

- [ ] `pyproject.toml` configured correctly
- [ ] `packages = ["easy_to_maths"]` in pyproject.toml
- [ ] `easy_to_maths/` directory exists
- [ ] `easy_to_maths/__init__.py` exists with exports
- [ ] `easy_to_maths/maths.py` exists with functions
- [ ] `tests/` directory with test files
- [ ] `LICENSE` file (MIT)
- [ ] `readme.md` file (lowercase)

## Package Metadata

- [ ] Package name is valid (lowercase, hyphens only)
- [ ] Version number follows semantic versioning (0.2.0)
- [ ] Author name and email filled in
- [ ] Description is clear and concise
- [ ] Keywords are relevant
- [ ] Python version requirement is correct (>=3.9)
- [ ] License is specified (MIT)
- [ ] Classifiers are appropriate

## Build & Validation

- [ ] Build tools installed: `pip install build twine`
- [ ] Package builds successfully: `python -m build`
- [ ] No build warnings or errors
- [ ] Package contents are correct: check `dist/` directory
- [ ] Validation passes: `twine check dist/*`
- [ ] Wheel and source distributions created

## PyPI Setup

- [ ] PyPI account created (https://pypi.org/account/register/)
- [ ] Email verified on PyPI
- [ ] 2FA enabled on PyPI account
- [ ] API token generated
- [ ] API token saved securely (not in code)
- [ ] Username/token for twine configured

## Pre-Publication Testing

- [ ] Test on TestPyPI first: `twine upload --repository testpypi dist/*`
- [ ] Install from TestPyPI: `pip install -i https://test.pypi.org/simple/ easy-to-maths`
- [ ] Verify installation works correctly
- [ ] Test all functions in test installation
- [ ] Clean up TestPyPI version

## Git & Version Control

- [ ] Code committed to git repository
- [ ] Branch is clean (no uncommitted changes)
- [ ] Version updated in `pyproject.toml`
- [ ] Git tag created: `git tag v0.2.0`
- [ ] Tag pushed to remote: `git push origin v0.2.0`
- [ ] CHANGELOG updated (if applicable)

## Final Checks

- [ ] Removed test builds: `rm -rf dist/ build/ *.egg-info`
- [ ] Rebuilt package: `python -m build`
- [ ] Final validation: `twine check dist/*`
- [ ] No sensitive data in files
- [ ] No large binary files
- [ ] No relative imports causing issues
- [ ] Dependencies are minimal (zero for this package)

## Publishing

- [ ] Ready to upload: `python -m twine upload dist/*`
- [ ] Entered credentials correctly (__token__ username)
- [ ] Upload completed successfully
- [ ] Package appears on PyPI: https://pypi.org/project/easy-to-maths/

## Post-Publication

- [ ] Verified package on PyPI
- [ ] Tested installation from PyPI: `pip install easy-to-maths`
- [ ] Created GitHub release with changelog
- [ ] Announced release (if applicable)
- [ ] Updated documentation links
- [ ] Monitored for issues

## Notes

```
Version: 0.2.0
Release Date: [DATE]
PyPI URL: https://pypi.org/project/easy-to-maths/
GitHub URL: https://github.com/Arpitsoni89/maths-tools
```

---

## Quick Commands Reference

```bash
# Install tools
pip install build twine

# Build package
python -m build

# Validate package
twine check dist/*

# Upload to TestPyPI
twine upload --repository testpypi dist/*

# Upload to PyPI
twine upload dist/*

# Clean up
rm -rf dist/ build/ *.egg-info
```

## Troubleshooting

| Problem | Solution |
|---------|----------|
| "Invalid distribution" | Run `twine check dist/*` to see errors |
| "File already exists" | Increment version number in pyproject.toml |
| "Unauthorized" | Check API token is correct, username is `__token__` |
| "Not found" | Package name must be unique on PyPI |
| Import fails | Check `packages = ["easy_to_maths"]` in pyproject.toml |

---

✅ **All set? You're ready to publish!**
