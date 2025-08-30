# Whatalang Cursor Rules

This directory contains Cursor AI rules that help maintain consistency and quality across the Whatalang programming language project.

## Rule Files

### 🔧 Core Architecture (`core-architecture.mdc`)
- **Always Applied**: Yes
- **Scope**: All Python files
- **Purpose**: Defines fundamental language principles and component architecture

### 🎨 Code Style (`code-style.mdc`)
- **Always Applied**: Yes
- **Scope**: All Python files
- **Purpose**: Enforces coding standards, documentation, and testing conventions

### ⚡ Reactive System (`reactive-system.mdc`)
- **Always Applied**: Yes
- **Scope**: Reactive system files
- **Purpose**: Defines how reactivity should work and be tested

### 🖥️ CLI & UX (`cli-ux.mdc`)
- **Always Applied**: Yes
- **Scope**: CLI and test files
- **Purpose**: Ensures consistent command-line interface and user experience

### 🚀 Development Workflow (`development-workflow.mdc`)
- **Always Applied**: Yes
- **Scope**: All project files
- **Purpose**: Defines development practices and release processes

## How Rules Work

These rules are automatically applied by Cursor AI when working on Whatalang:

- **Always Applied**: Rules that are always included in AI context
- **Auto Attached**: Rules that trigger based on file patterns
- **Agent Requested**: Rules available for AI to choose from
- **Manual**: Rules that must be explicitly referenced

## Using Rules

1. **Automatic**: Rules apply automatically based on their configuration
2. **Manual Reference**: Use `@ruleName` to explicitly include a rule
3. **File Patterns**: Rules can be scoped to specific file types or directories

## Benefits

- **Consistent Code**: AI follows established patterns and standards
- **Better Suggestions**: AI understands Whatalang's architecture and goals
- **Quality Assurance**: Rules enforce best practices automatically
- **Team Alignment**: Everyone follows the same development guidelines

## Updating Rules

When updating rules:
1. Keep rules focused and actionable
2. Update related documentation
3. Test rule effectiveness
4. Commit rule changes with clear messages

---

*These rules help Cursor AI understand Whatalang and provide better assistance during development.*
