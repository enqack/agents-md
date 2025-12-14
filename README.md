# Agent Knowledge System

A comprehensive, metadata-driven system for creating, managing, and orchestrating specialized AI agents. Features cognitive architecture, swarm coordination, and reproducible development environments.

## 🌟 Features

- **📚 Knowledge Base**: Centralized guidelines (security, engineering standards, cloud architecture)
- **🎨 Template System**: Reusable agent templates with cognitive architecture
- **🤖 Agent Registry**: Production-ready agents with full lineage tracking
- **📊 Metadata System**: Capabilities, swarm definitions, and version history
- **🛠️ Automation Tools**: Python scripts for agent creation and validation
- **🔧 Build System**: Nix Flakes + Invoke for reproducible development

---

## 📂 Directory Structure

```
.
├── knowledge/          # Foundational guidelines and protocols
│   ├── core-directives.md
│   ├── artifact-protocol.md
│   ├── engineering-standards.md
│   ├── security-baseline.md
│   ├── cloud-architecture.md
│   └── technical-writing-guide.md
├── templates/          # Reusable agent templates
│   ├── tech-writer.md
│   └── software-development/
│       ├── backend-developer.md
│       ├── frontend-developer.md
│       ├── devops-engineer.md
│       ├── orchestrator-agent.md
│       └── ... (9 total)
├── agents/             # Instantiated, production-ready agents
│   ├── AGENTS.golang-techwriter.md
│   ├── AGENTS.python-backend.md
│   ├── AGENTS.react-frontend.md
│   ├── AGENTS.aws-devops.md
│   ├── AGENTS.gcp-engineer.md
│   └── AGENTS.gcp-fast-engineer.md
├── data/               # System registry and metadata
│   ├── lineage.yaml        # Agent pedigree and template mapping
│   ├── capabilities.yaml   # What each agent can/cannot do
│   ├── swarms.yaml         # Pre-defined agent teams
│   └── versions.yaml       # Version history tracking
└── tools/              # Automation scripts
    ├── create_agent.py     # Generate agent from template
    ├── validate_data.py    # Validate YAML consistency
    ├── update_version.py   # Manage version history
    └── README.md
```

---

## 🚀 Quick Start

### Prerequisites
- **Nix** with Flakes enabled

### 1. Enter Development Environment
```bash
nix develop
```

This provides:
- Python 3.11
- pip, virtualenv
- Invoke (task runner)

### 2. Initial Setup
```bash
invoke setup
```

Creates a virtual environment and installs dependencies (PyYAML).

### 3. Validate the System
```bash
invoke validate
```

Ensures all data files are consistent.

---

## 🛠️ Common Workflows

### Creating a New Agent

**Option 1: Using Tools**
```bash
invoke create-agent --template=backend-developer --name=rust-backend --domain=rust
```

**Option 2: Manual**
1. Copy a template from `templates/` to `agents/AGENTS.<name>.md`
2. Customize the agent definition
3. Update `data/lineage.yaml`, `data/capabilities.yaml`
4. Run: `invoke update-version --agent=<name> --version=1.0.0 --changes="Initial creation"`
5. Run: `invoke validate`

### Updating an Agent
1. Edit the agent markdown file
2. Update version: `invoke update-version --agent=<name> --version=1.1.0 --changes="Description"`
3. Validate: `invoke validate`

### Using Pre-defined Swarms
Check `data/swarms.yaml` for available teams:
- **full-stack-web-team**: Backend + Frontend + DevOps
- **gcp-enterprise-deployment**: GCP FAST + GCP Engineer
- **documentation-squad**: Tech Writer + Backend (for examples)

---

## 📊 Metadata System

### Lineage Tracking (`data/lineage.yaml`)
Maps agents to their source templates:
```yaml
agents:
  - id: python-backend
    path: agents/AGENTS.python-backend.md
    lineage:
      parent_template: backend-developer
      derivation_type: implementation
```

### Capability Matrix (`data/capabilities.yaml`)
Defines what each agent can and cannot do:
```yaml
python-backend:
  can_do:
    - api_design
    - database_queries
  cannot_do:
    - ui_design
  tools_required:
    - python
    - pytest
```

### Swarm Compatibility (`data/swarms.yaml`)
Pre-configured agent teams and compatibility rules.

### Version History (`data/versions.yaml`)
Complete change log for every agent.

---

## 🧠 Cognitive Architecture

All agents follow the **Think-Act-Reflect** loop:

1. **Think (Plan)**: Create `artifacts/plan_[task].md` before complex work
2. **Act (Execute)**: Implement according to plan
3. **Reflect (Verify)**: Validate with evidence (logs, tests, screenshots)

### Artifact Protocol
Agents produce tangible outputs:
- **Planning Artifacts**: Implementation plans
- **Evidence Artifacts**: Logs and test results
- **Visual Artifacts**: Screenshots and diagrams
- **Summary Artifacts**: Walkthroughs

---

## 📖 Knowledge Base

The `knowledge/` directory contains foundational guidelines that inform all agents:

- **core-directives.md**: The "Think-Act-Reflect" cognitive loop
- **artifact-protocol.md**: How to produce evidence and plans
- **engineering-standards.md**: SOLID, DRY, testing philosophy
- **security-baseline.md**: OWASP Top 10, secrets management
- **cloud-architecture.md**: 12-Factor apps, IaC principles
- **technical-writing-guide.md**: Documentation standards

---

## 🔧 Build System

### Available Tasks
```bash
invoke --list              # Show all tasks
invoke setup               # Create venv and install deps
invoke validate            # Validate all YAML files
invoke clean               # Remove venv and caches
invoke create-agent        # Create agent from template
invoke update-version      # Update version history
```

### Reproducibility
All dependencies are pinned via:
- **Nix**: System-level tools (`flake.lock`)
- **Python**: Application dependencies (`requirements.txt`)

---

## 🎯 Agent Templates

Current templates:
- **tech-writer**: Generic technical writer
- **backend-developer**: Server-side development
- **frontend-developer**: UI/UX development
- **devops-engineer**: Infrastructure and CI/CD
- **api-designer**: RESTful API design
- **code-reviewer**: Code quality audits
- **security-auditor**: Security assessments
- **test-engineer**: Testing strategies
- **system-architect**: Architecture design
- **orchestrator-agent**: Swarm coordination

---

## 🤖 Production Agents

Current agents:
- **golang-techwriter**: Golang documentation specialist
- **python-backend**: Python/FastAPI backend developer
- **react-frontend**: React/TypeScript frontend developer
- **aws-devops**: AWS infrastructure engineer
- **gcp-engineer**: GCP cloud engineer
- **gcp-fast-engineer**: Google Cloud Foundation Fabric FAST specialist

---

## 📋 Contributing

### Adding a Template
1. Create `templates/<category>/<name>.md`
2. Follow the cognitive architecture format
3. Add to `data/lineage.yaml` under `templates`

### Adding Knowledge
1. Create `knowledge/<topic>.md`
2. Use clear, actionable guidelines
3. Reference established standards

---

## 📜 License

BSD 3-Clause License - See LICENSE file for details.

---

## 🙏 Acknowledgments

Inspired by:
- [Antigravity Workspace Template](https://github.com/study8677/antigravity-workspace-template) - Cognitive architecture patterns
- Google Gemini's "Deep Think" protocol
- The FAST (Foundation Automated Secure Toolkit) framework
