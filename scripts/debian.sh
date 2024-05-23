#!/bin/bash
#
# Usage:
# $ bash debian.sh

set -e

REPO_DIR=$(readlink -f "$(dirname $0)/..")

# check dpkg/python3/...
function check() {
  set +e
  which $1 1>/dev/null 2>&1
  if [[ 0 -ne $? ]]; then
    echo -e "\033[5;31m[ERROR] Plz double check if '$1' is available or not!\033[0m"
    exit 1
  fi
  set -e
}

# make debian package
function make_deb_via_dpkg() {
  check dpkg-buildpackage # dpkg

  pushd ${REPO_DIR}

  # patch for unexpected `__pycache__`
  find ${REPO_DIR} -name "__pycache__" | xargs rm -rf

  # create debian package
  # Note: "--no-post-clean" requires dpkg-buildpackage version >= 1.21.0(maybe)
  # At least, for version <= 1.19.0.5 it's not available. Options:
  # -b, --build=binary          binary-only, no source files.
  # -uc, --unsigned-changes     unsigned .buildinfo and .changes file.
  # -us, --unsigned-source      unsigned source package.
  # -nc, --no-pre-clean         do not pre clean source tree (implies -b).
  dpkg-buildpackage -uc -us --no-pre-clean #--no-post-clean #-tc

  popd
}
make_deb_via_dpkg $@
