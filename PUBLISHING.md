# 📦 Publishing Whatalang to PyPI

This guide explains how to publish new versions of Whatalang to PyPI.

## 🚀 Quick Publish Checklist

- [ ] Update version in `pyproject.toml`
- [ ] Update version in `whatalang/cli.py`
- [ ] Test the package locally
- [ ] Build distribution packages
- [ ] Upload to PyPI
- [ ] Verify installation

## 📝 Step-by-Step Process

### **Step 1: Update Version Numbers**

**In `pyproject.toml`:**
```toml
[project]
version = "1.0.1"  # Increment version number
```

**In `whatalang/cli.py`:**
```python
parser.add_argument(
    "--version", 
    action="version", 
    version="Whatalang 1.0.1"  # Update version here too
)
```

### **Step 2: Test Locally**

```bash
# Activate virtual environment
source venv/bin/activate

# Install in editable mode
pip install -e .

# Test the CLI
whatalang --version
whatalang --help
```

### **Step 3: Build Distribution Packages**

```bash
# Clean previous builds
rm -rf dist/ build/ *.egg-info/

# Build new packages
python -m build

# Verify packages
twine check dist/*
```

### **Step 4: Upload to PyPI**

```bash
# Upload to PyPI
twine upload dist/*

# You'll be prompted for:
# Username: __token__
# Password: pypi-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
```

### **Step 5: Verify Installation**

```bash
# Test installation from PyPI
pip uninstall whatalang -y
pip install whatalang
whatalang --version
```

## 🔑 PyPI Authentication

### **API Token Setup:**
1. Go to https://pypi.org/manage/account/token/
2. Create new token with "Entire account" scope
3. Copy the token (starts with `pypi-`)

### **Environment Variables (Optional):**
```bash
export TWINE_USERNAME=__token__
export TWINE_PASSWORD=pypi-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
twine upload dist/*
```

## 📋 Version Numbering

Follow [Semantic Versioning](https://semver.org/):
- **MAJOR.MINOR.PATCH**
- **1.0.0** → **1.0.1** (patch: bug fixes)
- **1.0.0** → **1.1.0** (minor: new features)
- **1.0.0** → **2.0.0** (major: breaking changes)

## 🧹 Cleanup

After publishing:
```bash
# Remove build artifacts
rm -rf dist/ build/ *.egg-info/

# Commit version changes
git add pyproject.toml whatalang/cli.py
git commit -m "bump version to 1.0.1"
git push origin main
```

## 🚨 Common Issues

### **Package Already Exists:**
- PyPI doesn't allow overwriting existing versions
- Always increment version number before publishing

### **Authentication Failed:**
- Ensure username is `__token__` (not your PyPI username)
- Check that API token is correct and not expired

### **Build Errors:**
- Ensure all dependencies are installed
- Check `pyproject.toml` syntax
- Verify package structure

## 📚 Useful Commands

```bash
# Check package info
pip show whatalang

# List installed packages
pip list | grep whatalang

# Uninstall package
pip uninstall whatalang

# Install specific version
pip install whatalang==1.0.0

# Upgrade to latest
pip install --upgrade whatalang
```

## 🌐 PyPI Links

- **Whatalang on PyPI**: https://pypi.org/project/whatalang/
- **PyPI Account**: https://pypi.org/manage/account/
- **API Tokens**: https://pypi.org/manage/account/token/

## 🎯 Publishing Workflow Summary

1. **Update versions** in config files
2. **Test locally** with editable install
3. **Build packages** with `python -m build`
4. **Upload to PyPI** with `twine upload dist/*`
5. **Verify installation** from PyPI
6. **Commit changes** and push to GitHub

---

**Happy Publishing! 🚀**
