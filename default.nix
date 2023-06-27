{ pkgs ? import <nixpkgs> {} }:
pkgs.mkShell {
	nativeBuildInputs = with pkgs; [ 
		jupyter # jupyter-notebook
		ungoogled-chromium # zoom
		python3 
		lazygit
	];
}
