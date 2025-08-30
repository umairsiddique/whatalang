---
title: "Features"
subtitle: "Discover what makes Whatalang powerful"
description: "Explore Whatalang's key features including reactive programming, global state management, and functional operations."
date: 2024-01-01
draft: false
---

# 🚀 Whatalang Features

Whatalang combines the best of reactive programming, functional programming, and state management into one powerful, intuitive language.

---

## 🔄 Reactive Programming

### **Automatic State Monitoring**
Whatalang automatically monitors your state and triggers actions when conditions are met. No more manual event listeners or complex state synchronization.

```whatalang
state { temperature: 20 }

react to temperature when > 30 {
  set ac_status = "on"
  print "AC activated - temperature is high!"
}

react to temperature when < 15 {
  set heater_status = "on"
  print "Heater activated - temperature is low!"
}

# Change temperature and watch reactions happen automatically
set temperature = 35
set temperature = 10
```

### **Multiple Conditions**
Support for various comparison operators and multiple conditions per target.

```whatalang
react to score when > 100 {
  set level = "expert"
}
when > 50 {
  set level = "advanced"
}
when > 10 {
  set level = "intermediate"
}
default {
  set level = "beginner"
}
```

### **Chained Reactions**
Reactions can trigger other reactions, creating powerful workflows.

```whatalang
react to user.login_count when > 10 {
  set user.status = "active"
}

react to user.status when == "active" {
  set user.permissions = ["read", "write", "admin"]
  print "User upgraded to active status!"
}
```

---

## 🌍 Global State Management

### **Single Source of Truth**
Everything in your application lives in one state object, making data flow predictable and easy to debug.

```whatalang
state {
  app: {
    theme: "dark",
    language: "en",
    user: {
      id: 123,
      name: "Alice",
      preferences: {
        notifications: true,
        auto_save: true
      }
    },
    data: {
      items: [1, 2, 3, 4, 5],
      filters: {
        category: "all",
        price_range: [0, 1000]
      }
    }
  }
}
```

### **Path-Based Access**
Access any part of your state using intuitive dot notation and bracket syntax.

```whatalang
# Get values
print app.theme                    # "dark"
print app.user.name               # "Alice"
print app.data.items[0]          # 1
print app.data.filters.category  # "all"

# Set values
set app.theme = "light"
set app.user.preferences.notifications = false
set app.data.filters.price_range = [0, 500]
```

### **Nested Updates**
Update complex nested structures with simple operations.

```whatalang
# Update multiple properties at once
set app.user = {
  id: 123,
  name: "Alice",
  email: "alice@example.com",
  preferences: {
    notifications: true,
    auto_save: true,
    theme: "dark"
  }
}
```

---

## ⚡ Functional Operations

### **Built-in Functional Primitives**
Whatalang comes with powerful functional programming operations built right in.

```whatalang
state {
  numbers: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
}

# Map - transform each element
set doubled = map numbers * 2
# Result: [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

# Filter - keep only elements that match a condition
set evens = filter numbers % 2 == 0
# Result: [2, 4, 6, 8, 10]

# Reduce - combine all elements into a single value
set sum = reduce numbers + 0
# Result: 55

# Concat - combine arrays
set combined = concat numbers [11, 12, 13]
# Result: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
```

### **Complex Transformations**
Chain functional operations for powerful data processing.

```whatalang
state {
  products: [
    { name: "Laptop", price: 999, category: "electronics" },
    { name: "Book", price: 29, category: "books" },
    { name: "Phone", price: 699, category: "electronics" },
    { name: "Pen", price: 2, category: "office" }
  ]
}

# Get expensive electronics
set expensive_electronics = filter products category == "electronics" and price > 500

# Get product names only
set product_names = map expensive_electronics .name

# Calculate total value
set total_value = reduce expensive_electronics .price + 0
```

---

## 🎯 Developer Experience

### **Clean, Readable Syntax**
Whatalang's syntax is designed to be intuitive and easy to understand.

```whatalang
# Natural language-like keywords
state { counter: 0 }

react to counter when > 10 {
  set status = "high"
  print "Counter is high!"
}

# Simple operations
set counter = counter + 1
print "Current count: " + counter
```

### **Comprehensive Error Messages**
Get clear, actionable error messages when something goes wrong.

```whatalang
# Whatalang provides helpful error messages
set nonexistent.key = "value"
# Error: Path 'nonexistent.key' does not exist in state

react to invalid_target when > 10 {
  set status = "error"
}
# Error: Invalid reactive target 'invalid_target'
```

### **Built-in Debugging**
Built-in tools for understanding what's happening in your program.

```whatalang
# Print the entire state
print state

# Print specific paths
print user.preferences
print data.items[0:5]

# Debug reactive statements
print "Reactive statements: " + reactive_count
```

---

## 🔧 CLI and Tooling

### **Command Line Interface**
Run Whatalang programs directly from the command line.

```bash
# Run a Whatalang program
whatalang program.wa

# Run with verbose output
whatalang -v program.wa

# Run programs with different extensions
whatalang program.what
whatalang program  # auto-detects extension
```

### **File Extension Support**
Flexible file extension support for different use cases.

- **`.wa`** - Standard, professional extension
- **`.what`** - Descriptive, branded extension  
- **No extension** - Smart auto-detection

### **Verbose Mode**
Get detailed information about program execution.

```bash
$ whatalang -v example.wa

📁 Loading: example.wa
📝 Source (156 characters):
==================================================
state { counter: 0 }

react to counter when > 5 {
  set status = "active"
}

set counter = 10
print status
==================================================

🔤 LEXICAL ANALYSIS
------------------------------
Generated 25 tokens

🌳 PARSING
------------------------------
Generated AST with 3 statements

⚡ EXECUTION
------------------------------
📝 Registered reactive statement for counter
Set counter = 10
🔄 Reactive trigger: counter > 5
  → Executing: SetStatement
Set status = active
status: active
```

---

## 🚀 Performance Features

### **Efficient State Management**
- Lazy evaluation of reactive conditions
- Optimized path matching algorithms
- Minimal memory overhead
- Fast state updates

### **Scalable Architecture**
- Performance scales with state complexity
- Efficient reactive trigger evaluation
- Optimized for both small and large applications

---

## 🎨 Customization

### **Theme Support**
- Dark and light themes
- Customizable color schemes
- Responsive design for all devices

### **Extensible**
- Plugin system for custom operations
- Custom reactive conditions
- Integration with external systems

---

*Ready to experience these features? [Get started with Whatalang](/getting-started/) or explore our [examples](/examples/).*
