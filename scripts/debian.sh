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
  check dpkg

  # get architecture
  ARCH=${1:-"riscv64"}
  # update architecture for Debian && Ubuntu
  if [[ "$ARCH" == "x86_64" ]]; then
    ARCH="amd64"
  fi
  # get backend
  BACKEND=${2:-"fake"}
  # get version
  VER=$(cat ${REPO_DIR}/VERSION_NUMBER)

  # make install
  INSTALL_LOCAL=${REPO_DIR}/install
  pushd ${REPO_DIR}
  make install DESTDIR=${INSTALL_LOCAL} BACKEND=${BACKEND}
  popd

  # add debian resources
  cp -rf ${REPO_DIR}/debian ${INSTALL_LOCAL}/DEBIAN
  eval sed -i "s/@BACKEND/${BACKEND}/g" ${INSTALL_LOCAL}/DEBIAN/control
  eval sed -i "s/@VERSION_NUMBER/${VER}/g" ${INSTALL_LOCAL}/DEBIAN/control
  eval sed -i "s/@ARCH/${ARCH}/g" ${INSTALL_LOCAL}/DEBIAN/control
  if [[ $BACKEND == "fake" ]]; then
    eval sed -i "s/@DEP//g" ${INSTALL_LOCAL}/DEBIAN/control
    eval sed -i "s/@CON/bianbu-smart-album-tiorb/g" ${INSTALL_LOCAL}/DEBIAN/control
  elif [[ $BACKEND == "tiorb" ]]; then
    eval sed -i "s/@DEP/tiorb,/g" ${INSTALL_LOCAL}/DEBIAN/control
    eval sed -i "s/@CON/bianbu-smart-album-fake/g" ${INSTALL_LOCAL}/DEBIAN/control
  else
    : # not supported yet
  fi

  # create debian package
  dpkg -b ${INSTALL_LOCAL} bianbu-smart-album-${BACKEND}_${VER}_${ARCH}.deb
}
make_deb_via_dpkg $@ # riscv64 fake
