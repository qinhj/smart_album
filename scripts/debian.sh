#!/bin/bash
#
# Usage:
# $ bash debian.sh [arch [backend]]

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

  # get backend
  BACKEND=${1:-"fake"}

  # make install
  INSTALL_LOCAL=${REPO_DIR}/install
  rm -rf ${INSTALL_LOCAL} && mkdir -p ${INSTALL_LOCAL}
  pushd ${REPO_DIR}
  make install DESTDIR=${INSTALL_LOCAL} BACKEND=${BACKEND}
  popd
  # patch for unexpected `__pycache__`
  find ${INSTALL_LOCAL} -name "__pycache__" | xargs rm -rf

  # add debian resources
  debian=debian # "DEBIAN" for `dpkg -b`
  cp -rf ${REPO_DIR}/debian ${INSTALL_LOCAL}/${debian}
  eval sed -i "s/@BACKEND/${BACKEND}/g" ${INSTALL_LOCAL}/${debian}/control
  eval sed -i "s/@BACKEND/${BACKEND}/g" ${INSTALL_LOCAL}/${debian}/rules
  if [[ $BACKEND == "fake" ]]; then
    eval sed -i "s/@DEP//g" ${INSTALL_LOCAL}/${debian}/control
    eval sed -i "s/@CON/bianbu-smart-album-tiorb/g" ${INSTALL_LOCAL}/${debian}/control
  elif [[ $BACKEND == "tiorb" ]]; then
    eval sed -i "s/@DEP/tiorb,/g" ${INSTALL_LOCAL}/${debian}/control
    eval sed -i "s/@CON/bianbu-smart-album-fake/g" ${INSTALL_LOCAL}/${debian}/control
  else
    : # not supported yet
  fi

  # create debian package
  pushd ${INSTALL_LOCAL}
  dpkg-buildpackage -b -uc -us --no-pre-clean --no-post-clean # -tc
  popd
}
make_deb_via_dpkg $@ # riscv64 fake
