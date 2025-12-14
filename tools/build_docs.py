#!/usr/bin/env python3
"""
Generate static HTML documentation site for the Agent Knowledge System.

Usage:
    python tools/build_docs.py
"""

import yaml
from pathlib import Path
from jinja2 import Template
from datetime import datetime

PROJECT_ROOT = Path(__file__).parent.parent
DIST_DIR = PROJECT_ROOT / "dist"


HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Agent Knowledge System</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body {
            font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
            line-height: 1.6;
            color: #333;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            padding: 2rem;
        }
        .container {
            max-width: 1200px;
            margin: 0 auto;
            background: white;
            border-radius: 16px;
            box-shadow: 0 20px 60px rgba(0,0,0,0.3);
            padding: 3rem;
        }
        header {
            text-align: center;
            margin-bottom: 3rem;
        }
        h1 {
            font-size: 3rem;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            margin-bottom: 0.5rem;
        }
        .subtitle {
            color: #666;
            font-size: 1.2rem;
        }
        .stats {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 1.5rem;
            margin-bottom: 3rem;
        }
        .stat-card {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 2rem;
            border-radius: 12px;
            text-align: center;
        }
        .stat-value {
            font-size: 3rem;
            font-weight: bold;
        }
        .stat-label {
            font-size: 1rem;
            opacity: 0.9;
            margin-top: 0.5rem;
        }
        .section {
            margin-bottom: 3rem;
        }
        h2 {
            color: #764ba2;
            margin-bottom: 1.5rem;
            font-size: 2rem;
        }
        .agent-grid {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
            gap: 1.5rem;
        }
        .agent-card {
            border: 2px solid #e0e0e0;
            border-radius: 12px;
            padding: 1.5rem;
            transition: all 0.3s ease;
        }
        .agent-card:hover {
            border-color: #764ba2;
            box-shadow: 0 8px 16px rgba(118, 75, 162, 0.2);
            transform: translateY(-4px);
        }
        .agent-name {
            font-size: 1.3rem;
            font-weight: bold;
            color: #764ba2;
            margin-bottom: 0.5rem;
        }
        .agent-meta {
            font-size: 0.9rem;
            color: #666;
            margin-bottom: 0.5rem;
        }
        .agent-version {
            display: inline-block;
            background: #667eea;
            color: white;
            padding: 0.25rem 0.75rem;
            border-radius: 20px;
            font-size: 0.85rem;
            margin-top: 0.5rem;
        }
        .capabilities {
            margin-top: 1rem;
        }
        .badge {
            display: inline-block;
            background: #f0f0f0;
            padding: 0.25rem 0.75rem;
            border-radius: 20px;
            font-size: 0.8rem;
            margin: 0.25rem;
            color: #555;
        }
        .badge.can { background: #d4edda; color: #155724; }
        .badge.cannot { background: #f8d7da; color: #721c24; }
        .swarm-card {
            background: #f8f9fa;
            border-left: 4px solid #764ba2;
            padding: 1.5rem;
            border-radius: 8px;
            margin-bottom: 1.5rem;
        }
        .swarm-name {
            font-weight: bold;
            font-size: 1.2rem;
            color: #764ba2;
            margin-bottom: 0.5rem;
        }
        footer {
            text-align: center;
            margin-top: 3rem;
            padding-top: 2rem;
            border-top: 2px solid #e0e0e0;
            color: #666;
        }
    </style>
</head>
<body>
    <div class="container">
        <header>
            <h1>🤖 Agent Knowledge System</h1>
            <p class="subtitle">Production-Ready AI Agent Registry</p>
            <p style="color: #888;">Generated: {{ generated_at }}</p>
        </header>
        
        <div class="stats">
            <div class="stat-card">
                <div class="stat-value">{{ n_agents }}</div>
                <div class="stat-label">Agents</div>
            </div>
            <div class="stat-card">
                <div class="stat-value">{{ n_templates }}</div>
                <div class="stat-label">Templates</div>
            </div>
            <div class="stat-card">
                <div class="stat-value">{{ n_knowledge }}</div>
                <div class="stat-label">Knowledge Docs</div>
            </div>
            <div class="stat-card">
                <div class="stat-value">{{ n_swarms }}</div>
                <div class="stat-label">Swarms</div>
            </div>
        </div>
        
        <section class="section">
            <h2>🤖 Agents</h2>
            <div class="agent-grid">
                {% for agent in agents %}
                <div class="agent-card">
                    <div class="agent-name">{{ agent.id }}</div>
                    <div class="agent-meta">Based on: {{ agent.parent }}</div>
                    <div class="agent-meta">Type: {{ agent.derivation_type }}</div>
                    <div class="agent-version">v{{ agent.version }}</div>
                    <div class="capabilities">
                        <strong>Can Do:</strong><br>
                        {% for cap in agent.can_do[:3] %}
                        <span class="badge can">{{ cap }}</span>
                        {% endfor %}
                    </div>
                </div>
                {% endfor %}
            </div>
        </section>
        
        <section class="section">
            <h2>🌐 Swarms</h2>
            {% for swarm in swarms %}
            <div class="swarm-card">
                <div class="swarm-name">{{ swarm.name }}</div>
                <p>{{ swarm.description }}</p>
                <p><strong>Team:</strong> {{ swarm.agents }}</p>
                <p><strong>Use Cases:</strong> {{ swarm.use_cases }}</p>
            </div>
            {% endfor %}
        </section>
        
        <footer>
            <p>Built with the Agent Knowledge System</p>
            <p>BSD 3-Clause License © 2025 Enqack</p>
        </footer>
    </div>
</body>
</html>
"""


def load_yaml(filename):
    """Load a YAML file from data directory."""
    with open(PROJECT_ROOT / "data" / filename) as f:
        return yaml.safe_load(f)


def build_site():
    """Generate the static HTML site."""
    print("📚 Generating documentation site...")
    
    # Load data
    lineage = load_yaml("lineage.yaml")
    capabilities = load_yaml("capabilities.yaml")
    swarms_data = load_yaml("swarms.yaml")
    versions = load_yaml("versions.yaml")
    
    # Prepare agent data
    agents = []
    for agent in lineage["agents"]:
        agent_id = agent["id"]
        caps = capabilities["agents"].get(agent_id, {})
        version_info = versions["agents"].get(agent_id, {})
        
        agents.append({
            "id": agent_id,
            "parent": agent["lineage"]["parent_template"],
            "derivation_type": agent["lineage"]["derivation_type"],
            "version": version_info.get("current_version", "1.0.0"),
            "can_do": caps.get("can_do", []),
            "cannot_do": caps.get("cannot_do", []),
        })
    
    # Prepare swarm data
    swarms = []
    for swarm in swarms_data["swarms"]:
        swarms.append({
            "name": swarm["name"],
            "description": swarm["description"],
            "agents": ", ".join(swarm["agents"]),
            "use_cases": ", ".join(swarm["use_cases"]),
        })
   
    # Stats
    n_agents = len(lineage["agents"])
    n_templates = len(lineage["templates"])
    n_knowledge = len(list((PROJECT_ROOT / "knowledge").glob("*.md")))
    n_swarms = len(swarms_data["swarms"])
    
    # Render template
    template = Template(HTML_TEMPLATE)
    html = template.render(
        generated_at=datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        n_agents=n_agents,
        n_templates=n_templates,
        n_knowledge=n_knowledge,
        n_swarms=n_swarms,
        agents=agents,
        swarms=swarms,
    )
    
    # Write output
    DIST_DIR.mkdir(exist_ok=True)
    output_file = DIST_DIR / "index.html"
    with open(output_file, "w") as f:
        f.write(html)
    
    print(f"✅ Documentation site generated: {output_file}")
    print(f"💡 Open in browser: file://{output_file.absolute()}")


if __name__ == "__main__":
    build_site()
