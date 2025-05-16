{
  description = "Recover a private 2D array in a smart contract";

  inputs = { nixpkgs.url = "github:nixos/nixpkgs/nixos-unstable"; };

  outputs = { self, nixpkgs }:
    let
      system = "x86_64-linux";
      pkgs = import nixpkgs { inherit system; };

      python = pkgs.mkShell {
        nativeBuildInputs = [
          pkgs.python312
          pkgs.python312Packages.eth-abi
          pkgs.python312Packages.pycryptodome
          pkgs.python312Packages.requests
        ];
        shellHook = ''
          python3 recover2DArray.py -h
        '';
      };

      solidity = pkgs.mkShell {
        nativeBuildInputs = [ pkgs.foundry ];
        shellHook = ''
          cd contracts/
          anvil &
        '';
      };

    in {
      devShells.${system} = {
        python = python;
        solidity = solidity;

        dev = pkgs.mkShell {
          nativeBuildInputs = python.nativeBuildInputs
            ++ solidity.nativeBuildInputs;
        };

        lint = pkgs.mkShell {
          nativeBuildInputs =
            [ pkgs.nixfmt-classic pkgs.ruff pkgs.slither-analyzer pkgs.solc ];
          shellHook = ''
            nixfmt flake.nix
            ruff check recover2DArray.py
            solc-select use 0.8.28 --always-install
            slither contracts/src/Array.sol
          '';
        };
      };
    };
}
