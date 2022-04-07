# shell.nix
{ pkgs ? import <nixpkgs> { } }:
let
  unstable = import
    (fetchTarball "https://nixos.org/channels/nixos-unstable/nixexprs.tar.xz")
    { };
  my-python = unstable.python310;
  python-with-my-packages = my-python.withPackages (p:
    with p; [
      pandas
      tkinter
      xlrd
      # other python packages you want
    ]);
in pkgs.mkShell {
  buildInputs = [ python-with-my-packages pkgs.sl ];
  shellHook = ''
    echo "Dev Session"
    export PYTHONPATH=${python-with-my-packages}/${python-with-my-packages.sitePackages}
  '';
}
