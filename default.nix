{ pkgs ? import <nixpkgs> {} }:
pkgs.mkShell {
	packages = with pkgs; [ 
		jupyter # jupyter-notebook
		lazygit
		(python3.withPackages (ps: with ps; [matplotlib]))
	];
}
