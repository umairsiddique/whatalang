---
title: "Whatalang"
subtitle: "The reactive programming language with a single global state"
description: "Whatalang is a modern programming language designed for reactive programming, featuring a single global state, automatic reactivity, and functional operations."
date: 2024-01-01
draft: false
---

# Whatalang

## The reactive programming language with a single global state

**Whatalang** makes reactive programming simple and intuitive. With a single global state that automatically triggers actions when conditions are met, you can build complex, responsive applications with clean, readable code.

<div class="hero-buttons">
<a href="/getting-started/" class="btn btn-primary btn-lg">🚀 Get Started</a>
<a href="/examples/" class="btn btn-secondary btn-lg">📖 View Examples</a>
</div>

---

## ⚡ **NEW: Install Whatalang Globally!**

**Whatalang is now available on PyPI!** Install it globally and run Whatalang programs from anywhere:

```bash
pip install whatalang
```

**Use it immediately:**
```bash
whatalang --version
whatalang program.wa
whatalang --help
```

**Try it online:**
```bash
# Run Whatalang source code directly
whatalang -e "state { message: 'Hello, World!' } print message"
```

---

## ✨ Why Whatalang?

### 🔄 **Reactive by Design**
State changes automatically trigger actions. No more manual event handling or complex state synchronization.

```whatalang
react to counter when > 10 {
  set status = "high"
  print "Counter is high!"
}
```

### 🌍 **Single Global State**
One state object to rule them all. Access any part of your application state with simple path notation.

```whatalang
state {
  user: {
    name: "Alice",
    age: 25,
    preferences: ["dark", "large"]
  }
}

set user.age = 26
print user.preferences[0]
```

### ⚡ **Functional Operations**
Built-in functional programming primitives for powerful state manipulation.

```whatalang
set numbers = [1, 2, 3, 4, 5]
set doubled = map numbers * 2
set evens = filter numbers % 2 == 0
set sum = reduce numbers + 0
```

### 🎯 **Simple Syntax**
Natural language-like syntax that's easy to read and write.

```whatalang
state { counter: 0 }

react to counter when > 5 {
  set status = "active"
}

set counter = 10
print status
```

---

## 🚀 Key Features

<div class="features-grid">

### **Global State Management**
- Single source of truth for all application data
- Nested objects and arrays with path-based access
- Atomic state updates with automatic reactivity

### **Reactive Triggers**
- Automatic action execution when conditions are met
- Support for multiple conditions and operators
- Chained reactions for complex workflows

### **Functional Programming**
- Built-in map, filter, reduce, and concat operations
- Immutable data transformations
- Pure functions for predictable behavior

### **Developer Experience**
- Clean, readable syntax
- Comprehensive error messages
- Built-in debugging and logging
- **Global CLI installation**

</div>

---

## 📱 Try It Now

Experience Whatalang in your browser with our interactive playground:

<div class="code-playground">
```whatalang
state {
  counter: 0,
  status: "normal"
}

react to counter when > 10 {
  set status = "high"
}

set counter = 15
print status
```
</div>

---

## 🎯 Perfect For

- **Event-driven applications**
- **Real-time dashboards**
- **Data transformation pipelines**
- **Reactive user interfaces**
- **State management systems**
- **Prototyping and experimentation**

---

## 🚀 Get Started in Minutes

1. **Install Whatalang**: `pip install whatalang`
2. **Create your first program**: `whatalang hello.wa`
3. **Explore examples**: Check out our [examples gallery](/examples/)
4. **Join the community**: [GitHub](https://github.com/umairsiddique/whatalang)

<div class="cta-section">
<a href="/getting-started/" class="btn btn-primary btn-lg">Start Building with Whatalang</a>
</div>

---

## 🌟 **Whatalang is Now on PyPI!**

- **📦 Package**: [PyPI](https://pypi.org/project/whatalang/)
- **🌐 Website**: [whatalang.org](https://whatalang.org) (coming soon)
- **📚 Documentation**: [Getting Started](/getting-started/)
- **💻 CLI**: Global `whatalang` command
- **🚀 Features**: Reactive programming with single global state

---

*Whatalang is open source and built with ❤️ by developers, for developers.*
