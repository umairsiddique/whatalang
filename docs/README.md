# Whatalang Website

This directory contains the Hugo-based website for Whatalang.

## 🚀 Quick Start

### **For Local Development:**
```bash
# Start local server with development config
hugo server --config hugo.dev.toml --bind 0.0.0.0 --port 1313

# Or use the default config (production settings)
hugo server --bind 0.0.0.0 --port 1313
```

### **For Production Build:**
```bash
# Build with production settings (default)
hugo --minify

# Build with development settings
hugo --config hugo.dev.toml
```

## 📁 Configuration Files

- **`hugo.toml`** - Production configuration (GitHub Pages)
- **`hugo.dev.toml`** - Development configuration (localhost)

## 🔧 Key Differences

| Setting | Production | Development |
|---------|------------|-------------|
| baseURL | `https://umairsiddique.github.io/whatalang/` | `http://localhost:1313/` |
| minify | `true` | `false` |
| buildDrafts | `false` | `true` |
| gc | `true` | `false` |

## 🌐 Access URLs

- **Local Development**: http://localhost:1313/
- **Production**: https://umairsiddique.github.io/whatalang/

## 📝 Content Structure

- **`content/_index.md`** - Homepage
- **`content/features/_index.md`** - Features page
- **`content/getting-started/_index.md`** - Getting started guide
- **`content/examples/_index.md`** - Code examples
- **`content/docs/_index.md`** - Language documentation

## 🎨 Custom Layouts

- **`layouts/section.html`** - Custom layout for content pages
- **`themes/FixIt/`** - Hugo theme (Git submodule)

## 🚀 Deployment

The site is configured for GitHub Pages deployment from the `/docs` folder. Simply push to the main branch and GitHub Pages will automatically build and deploy the site.
