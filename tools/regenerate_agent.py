#!/usr/bin/env python3
"""
Regenerate an agent from its parent template.

Usage:
    python tools/regenerate_agent.py <agent_name> [--domain DOMAIN]
"""

import argparse
import shutil
import yaml
from pathlib import Path

PROJECT_ROOT = Path(__file__).parent.parent


def load_lineage():
    """Load the lineage.yaml file."""
    with open(PROJECT_ROOT / "data" / "lineage.yaml") as f:
        return yaml.safe_load(f)


def find_agent_template(agent_id):
    """Find the parent template ID for an agent."""
    lineage = load_lineage()
    for agent in lineage.get("agents", []):
        if agent["id"] == agent_id:
            return agent["lineage"]["parent_template"]
    raise ValueError(f"Agent '{agent_id}' not found in lineage.yaml")


def find_template_path(template_id):
    """Find path for a template ID."""
    lineage = load_lineage()
    for template in lineage.get("templates", []):
        if template["id"] == template_id:
            return PROJECT_ROOT / template["path"]
    raise ValueError(f"Template '{template_id}' not found")


def regenerate_agent(agent_name, domain=None):
    """Regenerate an agent file from its template."""
    print(f"🔄 Regenerating agent: {agent_name}...")
    
    # 1. Resolve template
    try:
        template_id = find_agent_template(agent_name)
        template_path = find_template_path(template_id)
    except ValueError as e:
        print(f"❌ Error: {e}")
        exit(1)
    
    agent_path = PROJECT_ROOT / "agents" / f"AGENTS.{agent_name}.md"
    if not agent_path.exists():
        print(f"❌ Error: Agent file {agent_path} does not exist. Use create_agent for new agents.")
        exit(1)
        
    # 2. Backup
    from datetime import datetime
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_path = agent_path.with_suffix(f".md.{timestamp}.bak")
    shutil.copy2(agent_path, backup_path)
    print(f"📦 Backed up existing agent to {backup_path.name}")
    
    # 3. Read Template
    with open(template_path) as f:
        content = f.read()
        
    # 4. Substitute
    if domain:
        content = content.replace("{{DOMAIN}}", domain.title())
        content = content.replace("{{domain}}", domain)
        
    # 5. Write
    with open(agent_path, "w") as f:
        f.write(content)
        
    print(f"✅ Successfully regenerated {agent_name} from template '{template_id}'")


def main():
    parser = argparse.ArgumentParser(description="Regenerate an agent from its template")
    parser.add_argument("agent_name", help="Agent ID (e.g., rust-backend)")
    parser.add_argument("--domain", help="Domain specialization (if template requires it)")
    
    args = parser.parse_args()
    regenerate_agent(args.agent_name, args.domain)


if __name__ == "__main__":
    main()
