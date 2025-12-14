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
    """Remove build artifacts and caches."""
    print("🧹 Cleaning build artifacts...")
    
    # Remove dist
    if (PROJECT_ROOT / "dist").exists():
        c.run("rm -rf dist")
        print("✅ Removed dist/")
    
    # Remove Python caches
    c.run("find . -type d -name __pycache__ -exec rm -rf {} + 2>/dev/null || true")
    c.run("find . -type f -name '*.pyc' -delete 2>/dev/null || true")
    
    # Remove backup files
    c.run("find agents -name '*.bak' -delete 2>/dev/null || true")
    print("✅ Removed backup files")
    
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
def regenerate(c, agent, domain=""):
    """Regenerate an agent from its template.
    
    Args:
        agent: Agent name (e.g., rust-backend)
        domain: Optional domain specialization
    """
    cmd = f"python3 tools/regenerate_agent.py {agent}"
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


@task
def stats(c):
    """Show repository statistics and metrics."""
    import yaml
    from pathlib import Path
    from rich.console import Console
    from rich.table import Table
    from rich.panel import Panel
    
    console = Console()
    PROJECT_ROOT = Path(".")
    
    # Load data
    with open(PROJECT_ROOT / "data" / "lineage.yaml") as f:
        lineage = yaml.safe_load(f)
    with open(PROJECT_ROOT / "data" / "swarms.yaml") as f:
        swarms_data = yaml.safe_load(f)
    with open(PROJECT_ROOT / "data" / "versions.yaml") as f:
        versions = yaml.safe_load(f)
    
    # Header
    console.print("\n[bold cyan]🤖 Agent Knowledge System Statistics[/bold cyan]\n", justify="center")
    
    # Overview stats
    overview = Table(show_header=False, box=None)
    overview.add_column("Metric", style="cyan")
    overview.add_column("Value", justify="right", style="green bold")
    
    n_templates = len(lineage["templates"])
    n_agents = len(lineage["agents"])
    n_knowledge = len(list(Path("knowledge").glob("*.md")))
    n_swarms = len(swarms_data["swarms"])
    
    overview.add_row("📋 Templates", str(n_templates))
    overview.add_row("🤖 Agents", str(n_agents))
    overview.add_row("📚 Knowledge Docs", str(n_knowledge))
    overview.add_row("🌐 Swarms", str(n_swarms))
    
    console.print(Panel(overview, title="[bold]Overview[/bold]", border_style="cyan"))
    
    # Agents by category
    agents_table = Table(title="[bold]Agents by Category[/bold]", show_lines=True)
    agents_table.add_column("Agent", style="cyan")
    agents_table.add_column("Template", style="yellow")
    agents_table.add_column("Version", justify="center", style="green")
    
    for agent in lineage["agents"]:
        agent_id = agent["id"]
        parent = agent["lineage"]["parent_template"]
        ver = versions["agents"].get(agent_id, {}).get("current_version", "N/A")
        agents_table.add_row(agent_id, parent, ver)
    
    console.print("\n", agents_table)
    
    # Swarms
    swarms_table = Table(title="[bold]Pre-defined Swarms[/bold]", show_lines=True)
    swarms_table.add_column("Swarm", style="cyan")
    swarms_table.add_column("Agents", style="yellow")
    swarms_table.add_column("Use Cases", style="magenta")
    
    for swarm in swarms_data["swarms"]:
        name = swarm["name"]
        agents = ", ".join(swarm["agents"])
        use_cases = ", ".join(swarm["use_cases"][:2])  # First 2
        swarms_table.add_row(name, agents, use_cases)
    
    console.print("\n", swarms_table)
    console.print()


@task
def build_docs(c):
    """Generate static HTML documentation site."""
    print("📚 Building documentation site...")
    c.run("python3 tools/build_docs.py")

@task(name="regenerate-all")
def regenerate_all(c):
    """Regenerate ALL agents using metadata from lineage.yaml."""
    import yaml
    from pathlib import Path
    
    PROJECT_ROOT = Path(".")
    print("🔄 Starting batch regeneration of ALL agents...")
    
    with open(PROJECT_ROOT / "data" / "lineage.yaml") as f:
        lineage = yaml.safe_load(f)
        
    for agent in lineage.get("agents", []):
        agent_id = agent["id"]
        # Get domain from generation_parameters, fallback to metadata domain
        gen_params = agent.get("generation_parameters", {})
        domain = gen_params.get("domain") or agent.get("metadata", {}).get("domain")
        
        cmd = f"python3 tools/regenerate_agent.py {agent_id}"
        if domain:
            cmd += f" --domain {domain}"
            
        c.run(cmd)
        
    print("\n✅ Batch regeneration complete!")
