{ pkgs ? import <nixpkgs> {} }:
pkgs.mkShell {
	packages = with pkgs; [ 
		zoom-us
		jupyter # jupyter-notebook
		lazygit
		(python3.withPackages (ps: with ps; [matplotlib tensorflow keras]))
	];
}
