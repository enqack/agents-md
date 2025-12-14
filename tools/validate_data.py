#!/usr/bin/env python3
"""
Validate all data YAML files for consistency and correctness.

Usage:
    python tools/validate_data.py
"""

import yaml
from pathlib import Path
from collections import defaultdict

PROJECT_ROOT = Path(__file__).parent.parent
DATA_DIR = PROJECT_ROOT / "data"


def load_yaml(filename):
    """Load a YAML file from data directory."""
    with open(DATA_DIR / filename) as f:
        return yaml.safe_load(f)


def validate_lineage():
    """Validate lineage.yaml."""
    print("🔍 Validating lineage.yaml...")
    lineage = load_yaml("lineage.yaml")
    
    errors = []
    
    # Check all templates exist
    for template in lineage["templates"]:
        path = PROJECT_ROOT / template["path"]
        if not path.exists():
            errors.append(f"Template file missing: {path}")
    
    # Check all agents exist
    for agent in lineage["agents"]:
        path = PROJECT_ROOT / agent["path"]
        if not path.exists():
            errors.append(f"Agent file missing: {path}")
    
    if errors:
        for err in errors:
            print(f"  ❌ {err}")
        return False
    
    print(f"  ✅ {len(lineage['templates'])} templates, {len(lineage['agents'])} agents validated")
    return True


def validate_capabilities():
    """Validate capabilities.yaml."""
    print("🔍 Validating capabilities.yaml...")
    capabilities = load_yaml("capabilities.yaml")
    lineage = load_yaml("lineage.yaml")
    
    agent_ids = {agent["id"] for agent in lineage["agents"]}
    capability_ids = set(capabilities["agents"].keys())
    
    missing = agent_ids - capability_ids
    extra = capability_ids - agent_ids
    
    errors = []
    if missing:
        errors.append(f"Missing capability definitions: {missing}")
    if extra:
        errors.append(f"Extra capability definitions: {extra}")
    
    if errors:
        for err in errors:
            print(f"  ❌ {err}")
        return False
    
    print(f"  ✅ All {len(agent_ids)} agents have capability definitions")
    return True


def validate_versions():
    """Validate versions.yaml."""
    print("🔍 Validating versions.yaml...")
    versions = load_yaml("versions.yaml")
    lineage = load_yaml("lineage.yaml")
    
    agent_ids = {agent["id"] for agent in lineage["agents"]}
    version_ids = set(versions["agents"].keys())
    
    missing = agent_ids - version_ids
    extra = version_ids - agent_ids
    
    errors = []
    if missing:
        errors.append(f"Missing version history: {missing}")
    if extra:
        errors.append(f"Extra version history: {extra}")
    
    if errors:
        for err in errors:
            print(f"  ❌ {err}")
        return False
    
    print(f"  ✅ All {len(agent_ids)} agents have version history")
    return True


def validate_swarms():
    """Validate swarms.yaml."""
    print("🔍 Validating swarms.yaml...")
    swarms = load_yaml("swarms.yaml")
    lineage = load_yaml("lineage.yaml")
    
    agent_ids = {agent["id"] for agent in lineage["agents"]}
    
    errors = []
    for swarm in swarms["swarms"]:
        for agent_id in swarm["agents"]:
            if agent_id not in agent_ids:
                errors.append(f"Swarm '{swarm['name']}' references unknown agent: {agent_id}")
    
    if errors:
        for err in errors:
            print(f"  ❌ {err}")
        return False
    
    print(f"  ✅ All {len(swarms['swarms'])} swarms are valid")
    return True


def main():
    print("=" * 60)
    print("Agent Data Validation")
    print("=" * 60)
    
    results = [
        validate_lineage(),
        validate_capabilities(),
        validate_versions(),
        validate_swarms()
    ]
    
    print("\n" + "=" * 60)
    if all(results):
        print("✅ All validations passed!")
        return 0
    else:
        print("❌ Validation failed. Please fix the errors above.")
        return 1


if __name__ == "__main__":
    exit(main())
