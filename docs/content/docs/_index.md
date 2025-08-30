---
title: "Documentation"
subtitle: "Complete language reference and API documentation"
description: "Comprehensive documentation covering Whatalang syntax, language features, and advanced concepts."
date: 2024-01-01
draft: false
---

# 📚 Whatalang Documentation

Complete reference for the Whatalang programming language.

---

## 🏗️ Language Overview

### **What is Whatalang?**
Whatalang is a reactive programming language designed around a single global state. It combines the simplicity of declarative programming with the power of automatic reactivity.

### **Core Principles**
- **Single Global State**: All data lives in one place
- **Reactive by Design**: Automatic responses to state changes
- **Functional Operations**: Built-in data transformation tools
- **Simple Syntax**: Natural language-like keywords

---

## 📝 Syntax Reference

### **Program Structure**
A Whatalang program consists of:
1. **State declarations** - Define initial state
2. **Reactive statements** - Define automatic behaviors
3. **Imperative statements** - Direct state changes and output

```whatalang
state {
  // Initial state
}

react to target when condition {
  // Reactive actions
}

// Imperative statements
set variable = value
print expression
```

---

## 🏛️ State Declaration

### **Basic State**
```whatalang
state {
  key: value
}
```

### **Nested Objects**
```whatalang
state {
  user: {
    name: "Alice",
    age: 25,
    preferences: {
      theme: "dark",
      notifications: true
    }
  }
}
```

### **Arrays**
```whatalang
state {
  numbers: [1, 2, 3, 4, 5],
  users: [
    { name: "Alice", age: 25 },
    { name: "Bob", age: 30 }
  ]
}
```

### **Mixed Types**
```whatalang
state {
  string_value: "Hello",
  number_value: 42,
  boolean_value: true,
  null_value: null,
  object_value: { key: "value" },
  array_value: [1, 2, 3]
}
```

---

## 🔄 Reactive Statements

### **Basic React Statement**
```whatalang
react to target when condition {
  action1
  action2
}
```

### **Multiple Conditions**
```whatalang
react to target when > 10 {
  action1
}
when < 0 {
  action2
}
default {
  action3
}
```

### **Supported Operators**
- `==` - Equal to
- `!=` - Not equal to
- `>` - Greater than
- `<` - Less than
- `>=` - Greater than or equal to
- `<=` - Less than or equal to

### **Complex Conditions**
```whatalang
react to user.age when >= 18 and user.status == "active" {
  set user.permissions = ["read", "write"]
}
```

---

## ⚙️ Imperative Statements

### **Set Statement**
```whatalang
set path = expression
```

**Examples:**
```whatalang
set counter = 10
set user.name = "Bob"
set user.preferences.theme = "light"
set data.items[0] = "new_value"
```

### **Print Statement**
```whatalang
print expression
```

**Examples:**
```whatalang
print "Hello, World!"
print counter
print user.name
print state  # Print entire state
```

---

## 🛤️ Path Expressions

### **Basic Paths**
```whatalang
variable_name
user.name
user.preferences.theme
```

### **Array Access**
```whatalang
items[0]        # First element
items[1]        # Second element
items[-1]       # Last element
```

### **Nested Paths**
```whatalang
user.profile.settings.notifications
data.items[0].price
```

---

## ⚡ Functional Operations

### **Map Operation**
Transform each element in an array.

```whatalang
set doubled = map numbers * 2
set names = map users .name
set prices = map products .price
```

### **Filter Operation**
Keep only elements that match a condition.

```whatalang
set evens = filter numbers % 2 == 0
set active_users = filter users .status == "active"
set expensive_items = filter products .price > 100
```

### **Reduce Operation**
Combine all elements into a single value.

```whatalang
set sum = reduce numbers + 0
set total_price = reduce products .price + 0
set concatenated = reduce strings + ""
```

### **Concat Operation**
Combine multiple arrays.

```whatalang
set combined = concat array1 array2
set all_items = concat items new_items
```

---

## 📊 Data Types

### **Primitive Types**
- **String**: `"Hello, World!"`
- **Number**: `42`, `3.14`, `-10`
- **Boolean**: `true`, `false`
- **Null**: `null`

### **Composite Types**
- **Object**: `{ key: value }`
- **Array**: `[1, 2, 3]`

### **Type Coercion**
Whatalang automatically converts between compatible types:
- Numbers can be used as strings
- Strings can be concatenated with numbers
- Booleans can be used in numeric contexts

---

## 🔧 Built-in Functions

### **len() - Array Length**
```whatalang
set count = len(items)
set user_count = len(users)
```

### **String Operations**
```whatalang
set message = "Hello" + " " + "World"
set full_name = user.first_name + " " + user.last_name
```

### **Numeric Operations**
```whatalang
set sum = a + b
set difference = a - b
set product = a * b
set quotient = a / b
set remainder = a % b
```

---

## 🚨 Error Handling

### **Common Errors**
1. **Invalid Path**: Trying to access non-existent state
2. **Type Mismatch**: Using incompatible types in operations
3. **Syntax Error**: Invalid language syntax
4. **Runtime Error**: Errors during program execution

### **Error Messages**
Whatalang provides clear, actionable error messages:
```
Error: Path 'user.email' does not exist in state
Error: Cannot perform operation '+' on types 'string' and 'number'
Error: Invalid syntax at line 5
```

---

## 🎯 Best Practices

### **State Organization**
- Group related data together
- Use descriptive names for keys
- Keep nesting levels reasonable (max 3-4 levels)

### **Reactive Design**
- Keep reactive conditions simple
- Avoid complex chained reactions
- Use default actions for fallback behavior

### **Performance**
- Minimize unnecessary state changes
- Use efficient path expressions
- Avoid deeply nested reactive statements

---

## 🔍 Debugging

### **Print Debugging**
```whatalang
print "Debug: counter = " + counter
print "Debug: user = " + user
print "Debug: state = " + state
```

### **Verbose Mode**
Use the `-v` flag for detailed execution information:
```bash
whatalang -v program.wa
```

### **State Inspection**
```whatalang
# Print entire state
print state

# Print specific sections
print user
print data.items
```

---

## 📚 Examples

### **Simple Counter**
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

### **User Management**
```whatalang
state {
  user: {
    name: "Alice",
    age: 25,
    status: "active"
  }
}

react to user.age when >= 18 {
  set user.adult = true
}

react to user.status when == "active" {
  set user.permissions = ["read", "write"]
}

set user.age = 26
print user
```

---

## 🚀 Advanced Features

### **Chained Reactions**
```whatalang
react to user.login_count when > 10 {
  set user.status = "active"
}

react to user.status when == "active" {
  set user.permissions = ["read", "write", "admin"]
}
```

### **Conditional Logic**
```whatalang
react to temperature when > 30 and humidity > 80 {
  set ac_status = "on"
  set dehumidifier_status = "on"
}
```

### **Dynamic Paths**
```whatalang
react to user.preferences.theme when == "dark" {
  set user.preferences.auto_save = true
}
```

---

## 📖 Language Grammar

### **BNF Notation**
```
program ::= statement*
statement ::= state_decl | react_statement | set_statement | print_statement
state_decl ::= 'state' '{' key_value_pair* '}'
react_statement ::= 'react' 'to' target (when_condition | default_actions)*
when_condition ::= 'when' comparison_operator expression '{' action* '}'
set_statement ::= 'set' path '=' expression
print_statement ::= 'print' expression
```

---

## 🔗 Related Resources

- **[Getting Started](/getting-started/)**: Quick start guide
- **[Examples](/examples/)**: Code examples and tutorials
- **[Features](/features/)**: Language feature overview
- **[GitHub](https://github.com/umairsiddique/whatalang)**: Source code and issues

---

*This documentation covers the core Whatalang language. For specific examples and use cases, check out our [examples page](/examples/).*
