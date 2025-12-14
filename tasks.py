"""
Invoke tasks for Agent Knowledge System.

Usage:
    invoke --list           # List all tasks
    invoke setup            # Create venv and install deps
    invoke validate         # Validate data files
    invoke clean            # Clean build artifacts
"""

from invoke import task
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).parent


@task
def setup(c):
    """Create virtual environment and install dependencies."""
    print("🔧 Setting up development environment...")
    
    # Create venv
    if not (PROJECT_ROOT / ".venv").exists():
        print("📦 Creating virtual environment...")
        c.run("python3 -m venv .venv")
    else:
        print("✅ Virtual environment already exists")
    
    # Install dependencies
    print("📥 Installing dependencies...")
    c.run(".venv/bin/pip install -r requirements.txt")
    
    print("\n✅ Setup complete!")
    print("💡 Activate with: source .venv/bin/activate")


@task
def validate(c):
    """Validate all data YAML files."""
    print("🔍 Validating data files...")
    result = c.run("python3 tools/validate_data.py", warn=True)
    
    if result.ok:
        print("\n✅ All validations passed!")
    else:
        print("\n❌ Validation failed. See errors above.")
        sys.exit(1)


@task
def clean(c):
    """Remove virtual environment and caches."""
    print("🧹 Cleaning build artifacts...")
    
    # Remove venv
    if (PROJECT_ROOT / ".venv").exists():
        c.run("rm -rf .venv")
        print("✅ Removed .venv")
    
    # Remove Python caches
    c.run("find . -type d -name __pycache__ -exec rm -rf {} + 2>/dev/null || true")
    c.run("find . -type f -name '*.pyc' -delete 2>/dev/null || true")
    print("✅ Removed Python caches")


@task
def create_agent(c, template, name, domain=""):
    """Create a new agent from a template.
    
    Args:
        template: Template ID (e.g., backend-developer)
        name: Agent name (e.g., rust-backend)
        domain: Optional domain specialization
    """
    cmd = f"python3 tools/create_agent.py {template} {name}"
    if domain:
        cmd += f" --domain {domain}"
    
    c.run(cmd)


@task
def update_version(c, agent, version, changes):
    """Update version history for an agent.
    
    Args:
        agent: Agent name (e.g., python-backend)
        version: New version (e.g., 1.2.0)
        changes: Description of changes
    """
    c.run(f'python3 tools/update_version.py {agent} {version} "{changes}"')
