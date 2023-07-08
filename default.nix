{ pkgs ? import <nixpkgs> {} }:
pkgs.mkShell {
	packages = with pkgs; [ 
		zoom-us
		jupyter # jupyter-notebook
		lazygit
		(python3.withPackages (ps: with ps; [ pypdf2 regex matplotlib tensorflow keras gym ]))
	];
}
