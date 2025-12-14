# Agent Management Tools

This directory contains automation scripts for managing the Agent Knowledge System.

## Scripts

### 1. `create_agent.py`
Create a new agent from a template.

**Usage:**
```bash
python tools/create_agent.py <template_id> <agent_name> [--domain DOMAIN]
```

**Example:**
```bash
python tools/create_agent.py backend-developer rust-backend --domain rust
```

**What it does:**
- Reads the specified template
- Replaces `{{DOMAIN}}` placeholders
- Creates `agents/AGENTS.<agent_name>.md`
- Prints next steps for manual updates

---

### 2. `validate_data.py`
Validate all data YAML files for consistency.

**Usage:**
```bash
python tools/validate_data.py
```

**What it checks:**
- ✅ All template files referenced in `lineage.yaml` exist
- ✅ All agent files referenced in `lineage.yaml` exist
- ✅ All agents have entries in `capabilities.yaml`
- ✅ All agents have entries in `versions.yaml`
- ✅ Swarm definitions reference valid agents

**Exit codes:**
- `0` = All validations passed
- `1` = Validation failed

---

### 3. `update_version.py`
Add a new version entry to an agent's history.

**Usage:**
```bash
python tools/update_version.py <agent_name> <new_version> <change_description>
```

**Example:**
```bash
python tools/update_version.py python-backend 1.2.0 "Added async support"
```

**What it does:**
- Appends a new version entry to `data/versions.yaml`
- Updates `current_version`
- Sets date to today

---

## Dependencies

All dependencies are provided by the Nix development environment (`flake.nix`). You do not need to install anything manually.

## Workflow

### Creating a New Agent
1. Run `invoke create-agent` (or `python tools/create_agent.py`) to generate the file
2. Edit the agent file to customize
3. Manually add entries to:
   - `data/lineage.yaml`
   - `data/capabilities.yaml`
4. Run `invoke update-version` to create v1.0.0
5. Run `invoke validate` to ensure consistency

### Updating an Existing Agent
1. Edit the agent markdown file
2. Run `invoke update-version` to record the change
3. Run `invoke validate` to verify

---

## Future Enhancements
- Auto-update `lineage.yaml` on agent creation
- Auto-generate `capabilities.yaml` stubs
- Interactive prompts for all required fields
