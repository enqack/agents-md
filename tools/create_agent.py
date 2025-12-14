#!/usr/bin/env python3
"""
Create a new agent from a template.

Usage:
    python tools/create_agent.py <template_id> <agent_name> [--domain DOMAIN]

Example:
    python tools/create_agent.py backend-developer rust-backend --domain rust
"""

import argparse
import yaml
from pathlib import Path
from datetime import datetime

PROJECT_ROOT = Path(__file__).parent.parent


def load_lineage():
    """Load the lineage.yaml file."""
    with open(PROJECT_ROOT / "data" / "lineage.yaml") as f:
        return yaml.safe_load(f)


def find_template(template_id):
    """Find template path by ID."""
    lineage = load_lineage()
    for template in lineage["templates"]:
        if template["id"] == template_id:
            return PROJECT_ROOT / template["path"]
    raise ValueError(f"Template '{template_id}' not found")


def create_agent(template_id, agent_name, domain=None):
    """Create a new agent from a template."""
    template_path = find_template(template_id)
    agent_path = PROJECT_ROOT / "agents" / f"AGENTS.{agent_name}.md"
    
    if agent_path.exists():
        raise FileExistsError(f"Agent '{agent_name}' already exists")
    
    # Read template
    with open(template_path) as f:
        content = f.read()
    
    # Replace placeholders
    if domain:
        content = content.replace("{{DOMAIN}}", domain.title())
        content = content.replace("{{domain}}", domain)
    
    # Write agent file
    with open(agent_path, "w") as f:
        f.write(content)
    
    print(f"✅ Created agent: {agent_path}")
    print(f"\n📝 Next steps:")
    print(f"1. Edit {agent_path} to customize the agent")
    print(f"2. Run: python tools/update_version.py {agent_name} 1.0.0 'Initial creation'")
    print(f"3. Manually update data/lineage.yaml, data/capabilities.yaml")


def main():
    parser = argparse.ArgumentParser(description="Create a new agent from a template")
    parser.add_argument("template_id", help="Template ID (e.g., backend-developer)")
    parser.add_argument("agent_name", help="Agent name (e.g., rust-backend)")
    parser.add_argument("--domain", help="Domain specialization")
    
    args = parser.parse_args()
    create_agent(args.template_id, args.agent_name, args.domain)


if __name__ == "__main__":
    main()
