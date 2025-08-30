---
title: "Examples"
subtitle: "See Whatalang in action with real code examples"
description: "Explore practical examples of Whatalang programs, from simple state management to complex reactive systems."
date: 2024-01-01
draft: false
---

# 📚 Whatalang Examples

Explore these examples to see how Whatalang makes reactive programming simple and powerful.

---

## 🎯 Basic Examples

### **Hello World**
The simplest Whatalang program.

```whatalang
state {
  message: "Hello, World!"
}

print message
```

**Output:**
```
Hello, World!
```

### **Simple Counter**
A basic counter with reactive status updates.

```whatalang
state {
  counter: 0,
  status: "normal"
}

react to counter when > 10 {
  set status = "high"
}

react to counter when < 0 {
  set status = "negative"
}

set counter = 15
set counter = -5
print "Counter: " + counter + ", Status: " + status
```

**Output:**
```
Counter: -5, Status: negative
```

---

## 🔄 Reactive Examples

### **Temperature Control System**
A smart thermostat that automatically controls heating and cooling.

```whatalang
state {
  temperature: 22,
  ac_status: "off",
  heater_status: "off",
  mode: "auto"
}

react to temperature when > 28 {
  set ac_status = "on"
  set heater_status = "off"
  print "🌡️ AC activated - cooling down"
}

react to temperature when < 18 {
  set ac_status = "off"
  set heater_status = "on"
  print "🔥 Heater activated - warming up"
}

react to temperature when >= 18 and <= 28 {
  set ac_status = "off"
  set heater_status = "off"
  print "✅ Temperature is comfortable"
}

# Simulate temperature changes
set temperature = 32
set temperature = 15
set temperature = 24
```

### **User Authentication System**
A reactive user management system with automatic security measures.

```whatalang
state {
  user: {
    login_attempts: 0,
    status: "active",
    permissions: ["read"],
    last_login: null
  },
  security: {
    lockout_threshold: 3,
    lockout_duration: 300
  }
}

react to user.login_attempts when > security.lockout_threshold {
  set user.status = "locked"
  print "🔒 Account locked due to too many failed attempts"
}

react to user.status when == "locked" {
  set user.permissions = []
  print "❌ All permissions revoked"
}

react to user.status when == "active" {
  set user.permissions = ["read", "write"]
  print "✅ User has full access"
}

# Simulate failed login attempts
set user.login_attempts = 4
set user.status = "active"
```

---

## 🌍 State Management Examples

### **Shopping Cart**
A reactive shopping cart that automatically calculates totals and applies discounts.

```whatalang
state {
  cart: {
    items: [],
    total: 0,
    discount: 0,
    final_total: 0
  },
  discounts: {
    free_shipping_threshold: 50,
    bulk_discount_threshold: 100
  }
}

react to cart.total when >= discounts.free_shipping_threshold {
  set cart.discount = cart.discount + 10
  print "🚚 Free shipping applied!"
}

react to cart.total when >= discounts.bulk_discount_threshold {
  set cart.discount = cart.discount + 15
  print "🎉 Bulk discount applied!"
}

react to cart.discount {
  set cart.final_total = cart.total - cart.discount
}

# Add items to cart
set cart.items = [
  { name: "Laptop", price: 999 },
  { name: "Mouse", price: 25 }
]

set cart.total = 1024
print "Final total: $" + cart.final_total
```

### **User Profile Management**
A comprehensive user profile system with reactive updates.

```whatalang
state {
  user: {
    profile: {
      name: "Alice",
      age: 25,
      email: "alice@example.com",
      preferences: {
        theme: "dark",
        notifications: true,
        language: "en"
      }
    },
    stats: {
      login_count: 0,
      last_active: null,
      status: "inactive"
    }
  }
}

react to user.stats.login_count when > 0 {
  set user.stats.status = "active"
  set user.stats.last_active = "now"
}

react to user.profile.age when >= 18 {
  set user.profile.adult = true
  print "🎉 User is now an adult!"
}

react to user.profile.preferences.theme when == "dark" {
  set user.profile.preferences.auto_save = true
  print "🌙 Dark theme enabled - auto-save activated"
}

# Simulate user activity
set user.stats.login_count = 5
set user.profile.age = 26
set user.profile.preferences.theme = "dark"
```

---

## ⚡ Functional Programming Examples

### **Data Processing Pipeline**
Using Whatalang's built-in functional operations for data transformation.

```whatalang
state {
  data: {
    numbers: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    processed: [],
    statistics: {}
  }
}

# Process the data using functional operations
set data.processed = map data.numbers * 2
set evens = filter data.numbers % 2 == 0
set odds = filter data.numbers % 2 == 1
set sum = reduce data.numbers + 0
set average = sum / len(data.numbers)

# Update statistics
set data.statistics = {
  doubled: data.processed,
  even_numbers: evens,
  odd_numbers: odds,
  total_sum: sum,
  average: average
}

print "Statistics: " + data.statistics
```

### **Product Catalog Filtering**
Advanced filtering and transformation of product data.

```whatalang
state {
  products: [
    { name: "Laptop", price: 999, category: "electronics", rating: 4.5 },
    { name: "Book", price: 29, category: "books", rating: 4.2 },
    { name: "Phone", price: 699, category: "electronics", rating: 4.8 },
    { name: "Pen", price: 2, category: "office", rating: 3.9 },
    { name: "Tablet", price: 399, category: "electronics", rating: 4.3 }
  ],
  filtered: [],
  recommendations: []
}

# Filter expensive electronics with high ratings
set expensive_electronics = filter products category == "electronics" and price > 500 and rating >= 4.5

# Get product names only
set product_names = map expensive_electronics .name

# Calculate total value
set total_value = reduce expensive_electronics .price + 0

# Update filtered results
set filtered = {
  expensive_electronics: expensive_electronics,
  product_names: product_names,
  total_value: total_value
}

print "Filtered results: " + filtered
```

---

## 🎮 Interactive Examples

### **Game State Management**
A simple game with reactive state management.

```whatalang
state {
  game: {
    player: {
      health: 100,
      level: 1,
      experience: 0,
      status: "alive"
    },
    world: {
      difficulty: "normal",
      enemies_defeated: 0
    }
  }
}

react to game.player.health when <= 0 {
  set game.player.status = "dead"
  print "💀 Game Over!"
}

react to game.player.experience when >= 100 {
  set game.player.level = game.player.level + 1
  set game.player.experience = 0
  print "🎉 Level up! You are now level " + game.player.level
}

react to game.world.enemies_defeated when >= 10 {
  set game.world.difficulty = "hard"
  print "🔥 Difficulty increased to hard mode!"
}

# Simulate gameplay
set game.player.health = 50
set game.player.experience = 150
set game.world.enemies_defeated = 12
```

---

## 🔧 Advanced Examples

### **Multi-Level Reactive System**
A complex system with chained reactions and multiple conditions.

```whatalang
state {
  system: {
    status: "normal",
    alerts: [],
    maintenance_mode: false
  },
  sensors: {
    temperature: 25,
    humidity: 60,
    pressure: 1013
  },
  thresholds: {
    temp_high: 30,
    temp_low: 15,
    humidity_high: 80,
    pressure_low: 1000
  }
}

# Primary sensor reactions
react to sensors.temperature when > thresholds.temp_high {
  set system.status = "warning"
  set system.alerts = concat system.alerts ["High temperature detected"]
}

react to sensors.temperature when < thresholds.temp_low {
  set system.status = "warning"
  set system.alerts = concat system.alerts ["Low temperature detected"]
}

# Secondary system reactions
react to system.status when == "warning" {
  set system.maintenance_mode = true
  print "⚠️ System entering maintenance mode"
}

react to system.alerts when len(system.alerts) > 5 {
  set system.status = "critical"
  print "🚨 Critical system status - too many alerts!"
}

# Simulate sensor readings
set sensors.temperature = 35
set sensors.humidity = 85
set sensors.pressure = 990
```

---

## 📖 How to Run These Examples

1. **Copy the code** into a `.wa` or `.what` file
2. **Run with Whatalang**: `whatalang example.wa`
3. **Use verbose mode** to see the execution details: `whatalang -v example.wa`
4. **Experiment** by modifying values and watching reactions

---

## 🎯 Next Steps

- **Try the examples** above to understand the concepts
- **Modify the code** to experiment with different scenarios
- **Create your own** reactive programs
- **Explore the documentation** for more advanced features
- **Join the community** to share your creations

---

*These examples showcase the power and simplicity of Whatalang. Start simple and build up to complex reactive systems! 🚀*
