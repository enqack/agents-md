{
  description = "Agent Knowledge System - Development Environment";

  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixos-unstable";
    flake-utils.url = "github:numtide/flake-utils";
  };

  outputs = { self, nixpkgs, flake-utils }:
    flake-utils.lib.eachDefaultSystem (system:
      let
        pkgs = nixpkgs.legacyPackages.${system};
        python = pkgs.python311;
      in
      {
        devShells.default = pkgs.mkShell {
          buildInputs = with pkgs; [
            python
            python311Packages.pip
            python311Packages.virtualenv
            python311Packages.invoke
          ];

          shellHook = ''
            echo "🛸 Agent Knowledge System - Development Environment"
            echo ""
            echo "Available commands:"
            echo "  invoke setup     - Create venv and install dependencies"
            echo "  invoke validate  - Validate all data YAML files"
            echo "  invoke clean     - Remove venv and caches"
            echo "  invoke --list    - List all available tasks"
            echo ""
            
            # Activate venv if it exists
            if [ -d .venv ]; then
              source .venv/bin/activate
              echo "✅ Virtual environment activated (.venv)"
            else
              echo "⚠️  Run 'invoke setup' to create virtual environment"
            fi
          '';
        };
      }
    );
}
