# C.O.B.R.A Architecture

## Current State (v1.0)

- Engine handles command execution
- main.py handles input/output and command registration

## Goal (v1.1)

- Separate command logic into modules
- Introduce modular system:
  - system
  - network
  - security

## Next Steps

- Move commands from main.py to modules
- Create command registry
- Introduce parser layer

## New Component

### Command Registry

Responsible for:
- Centralizing command registration
- Decoupling modules from engine
- Preparing for modular loading
