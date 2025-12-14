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
            python311
            python311Packages.pyyaml
            python311Packages.rich
            python311Packages.jinja2
            python311Packages.invoke
          ];

          shellHook = ''
            echo "🛸 Agent Knowledge System - Development Environment"
            echo ""
            echo "Available commands:"
            echo "  invoke validate     - Validate all data YAML files"
            echo "  invoke stats        - Show repository statistics"
            echo "  invoke build-docs   - Generate HTML documentation"
            echo "  invoke --list       - List all available tasks"
            echo ""
            echo "✅ All dependencies provided by Nix"
          '';
        };
      }
    );
}
