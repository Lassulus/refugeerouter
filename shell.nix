{ pkgs ? import <nixpkgs> {} }:
let
  mach-nix = import (builtins.fetchGit {
    url = "https://github.com/DavHau/mach-nix";
    ref = "refs/tags/3.4.0";
  }) {
    pkgs = pkgs;
    # python = "python39";
  };
in
pkgs.mkShell {
  buildInputs = [
    (mach-nix.mkPython {
      requirements = builtins.readFile ./requirements.txt;
    })
    # (pkgs.python3.withPackages (pp: [
    #   pp.django_4
    #   pp.ipython
    # ]))
    (pkgs.writers.writeBashBin "init-project" ''
      # https://gist.github.com/kalafut/42bd31b2fdbf7a225da94e320d3e29ba
      # Simple creation of a single-app django project, as described in: https://zindilis.com/posts/django-anatomy-for-single-app/
      #
      # ./django_init foo
      #
      # This will result is the following flat structure:
      #
      # .
      # └── foo
      #     ├── manage.py
      #     ├── settings.py
      #     ├── urls.py
      #     ├── foo
      #     │   ├── __init__.py
      #     │   ├── admin.py
      #     │   ├── apps.py
      #     │   ├── migrations
      #     │   │   └── __init__.py
      #     │   ├── models.py
      #     │   ├── tests.py
      #     │   └── views.py
      #     └── wsgi.py
      #
      # Note: this script assumes a GNU-compatible sed is installed. On macOS you can get this easily with Homebrew.

      set -x

      prj=$1
      django-admin startproject $prj
      pushd .
      cd $prj
      mv $prj/* .
      rm __init__.py
      rm -rf $prj
      sed -i 's/'"''${prj}"'\.settings/settings/g' manage.py wsgi.py
      sed -i 's/'"''${prj}"'\.urls/urls/g' settings.py
      sed -i 's/'"''${prj}"'\.wsgi\.application/wsgi.application/g' settings.py
      sed -i '/BASE_DIR = /s/Path(__file__).resolve().parent.parent/Path(__file__).resolve().parent/' settings.py
      sed -i 's/'"''${prj}"'\.wsgi\.application/wsgi.application/g' settings.py
      python ./manage.py startapp ''${prj}
      popd
      mv $prj tmp_$prj
      mv tmp_$prj/* .
      rmdir tmp_$prj
    '')
  ];
}
