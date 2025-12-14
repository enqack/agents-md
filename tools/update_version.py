#!/usr/bin/env python3
"""
Update the version history for an agent.

Usage:
    python tools/update_version.py <agent_name> <new_version> <change_description>

Example:
    python tools/update_version.py python-backend 1.2.0 "Added async support"
"""

import argparse
import yaml
from pathlib import Path
from datetime import date

PROJECT_ROOT = Path(__file__).parent.parent
VERSIONS_FILE = PROJECT_ROOT / "data" / "versions.yaml"


def update_version(agent_name, new_version, changes):
    """Add a new version entry for an agent."""
    with open(VERSIONS_FILE) as f:
        data = yaml.safe_load(f)
    
    if agent_name not in data["agents"]:
        raise ValueError(f"Agent '{agent_name}' not found in versions.yaml")
    
    # Create new version entry
    new_entry = {
        "version": new_version,
        "date": str(date.today()),
        "changes": changes,
        "template_version": "unknown"  # User should update this manually
    }
    
    # Add to versions list
    data["agents"][agent_name]["versions"].append(new_entry)
    data["agents"][agent_name]["current_version"] = new_version
    
    # Write back
    with open(VERSIONS_FILE, "w") as f:
        yaml.dump(data, f, default_flow_style=False, sort_keys=False)
    
    print(f"✅ Updated {agent_name} to version {new_version}")
    print(f"📝 Don't forget to update 'template_version' in versions.yaml if applicable")


def main():
    parser = argparse.ArgumentParser(description="Update agent version history")
    parser.add_argument("agent_name", help="Agent name (e.g., python-backend)")
    parser.add_argument("new_version", help="New version (e.g., 1.2.0)")
    parser.add_argument("changes", help="Description of changes")
    
    args = parser.parse_args()
    update_version(args.agent_name, args.new_version, args.changes)


if __name__ == "__main__":
    main()
