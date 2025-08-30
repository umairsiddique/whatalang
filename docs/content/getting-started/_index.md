---
title: "Getting Started"
subtitle: "Get up and running with Whatalang in minutes"
description: "Learn how to install Whatalang, write your first program, and understand the basics of reactive programming."
date: 2024-01-01
draft: false
---

# 🚀 Getting Started with Whatalang

Welcome to Whatalang! This guide will get you up and running with the reactive programming language in just a few minutes.

---

## 📦 Installation

### **Prerequisites**
- Python 3.8 or higher
- pip (Python package installer)

### **Install Whatalang**
```bash
pip install whatalang
```

### **Verify Installation**
```bash
whatalang --version
```

You should see the Whatalang version number displayed.

---

## 🎯 Your First Whatalang Program

Let's start with a simple example that demonstrates the core concepts.

### **Step 1: Create a File**
Create a file called `hello.wa` with the following content:

```whatalang
state {
  counter: 0,
  message: "Hello, Whatalang!"
}

react to counter when > 5 {
  set message = "Counter is high!"
  print "🎉 Counter reached " + counter
}

set counter = 10
print message
```

### **Step 2: Run the Program**
```bash
whatalang hello.wa
```

### **Step 3: Understand What Happened**
1. **State Declaration**: We created a global state with `counter` and `message`
2. **Reactive Statement**: We set up a reaction that triggers when `counter > 5`
3. **State Changes**: We changed the counter value to 10
4. **Automatic Reaction**: The reactive statement automatically triggered
5. **Output**: The program printed the updated message

---

## 🔄 Understanding Reactive Programming

### **What is Reactivity?**
Reactive programming means your program automatically responds to changes in data. In Whatalang, when you change a value in the global state, any reactive statements watching that value automatically execute.

### **Key Concepts**

#### **1. Global State**
```whatalang
state {
  user: {
    name: "Alice",
    age: 25
  },
  settings: {
    theme: "dark",
    notifications: true
  }
}
```

#### **2. Reactive Statements**
```whatalang
react to user.age when >= 18 {
  set user.adult = true
  print "User is now an adult!"
}
```

#### **3. State Changes**
```whatalang
set user.age = 26
# This automatically triggers the reactive statement above
```

---

## 📚 Basic Syntax

### **State Declaration**
```whatalang
state {
  key1: value1,
  key2: value2,
  nested: {
    deep: "value"
  }
}
```

### **Setting Values**
```whatalang
set counter = 10
set user.name = "Bob"
set settings.theme = "light"
```

### **Printing Values**
```whatalang
print counter
print user.name
print state  # Print entire state
```

### **Reactive Statements**
```whatalang
react to target when condition {
  action1
  action2
}
```

---

## 🎮 Interactive Examples

### **Example 1: Temperature Monitor**
```whatalang
state {
  temperature: 20,
  ac_status: "off",
  heater_status: "off"
}

react to temperature when > 30 {
  set ac_status = "on"
  print "🌡️ AC activated - it's hot!"
}

react to temperature when < 15 {
  set heater_status = "on"
  print "🔥 Heater activated - it's cold!"
}

# Test the reactions
set temperature = 35
set temperature = 10
```

### **Example 2: User Authentication**
```whatalang
state {
  user: {
    login_attempts: 0,
    status: "active",
    permissions: ["read"]
  }
}

react to user.login_attempts when > 3 {
  set user.status = "locked"
  print "🔒 Account locked due to too many attempts"
}

react to user.status when == "locked" {
  set user.permissions = []
  print "❌ All permissions revoked"
}

# Simulate failed login attempts
set user.login_attempts = 5
```

---

## 🔧 CLI Options

### **Basic Usage**
```bash
whatalang <file>
```

### **Verbose Mode**
```bash
whatalang -v <file>
```

Shows detailed information about:
- Lexical analysis (tokens)
- Parsing (AST)
- Execution steps
- Reactive triggers

### **File Extensions**
Whatalang supports multiple file extensions:
- `program.wa` - Standard extension
- `program.what` - Descriptive extension
- `program` - Auto-detection

---

## 🚨 Common Pitfalls

### **1. Forgetting to Declare State**
```whatalang
# ❌ Wrong - trying to set undeclared state
set counter = 10

# ✅ Correct - declare state first
state { counter: 0 }
set counter = 10
```

### **2. Incorrect Reactive Syntax**
```whatalang
# ❌ Wrong - missing 'react to'
when counter > 10 {
  set status = "high"
}

# ✅ Correct - proper reactive syntax
react to counter when > 10 {
  set status = "high"
}
```

### **3. Invalid Paths**
```whatalang
# ❌ Wrong - path doesn't exist
set user.profile.email = "test@example.com"

# ✅ Correct - create the path first
set user.profile = { email: "test@example.com" }
```

---

## 📖 Next Steps

Now that you understand the basics:

1. **Explore Examples**: Check out our [examples gallery](/examples/)
2. **Read Documentation**: Dive deeper into [language features](/docs/)
3. **Try Your Own Ideas**: Experiment with reactive programming concepts
4. **Join the Community**: Share your creations on [GitHub](https://github.com/umairsiddique/whatalang)

---

## 🆘 Need Help?

- **Documentation**: Check our [comprehensive docs](/docs/)
- **Examples**: Browse working code in our [examples](/examples/)
- **GitHub**: Report issues or ask questions on [GitHub](https://github.com/umairsiddique/whatalang)
- **Community**: Join discussions and share your experiences

---

*Ready to build something amazing? Start with the examples and let your creativity flow! 🎉*
