# =========================================================
#                makefile for smart album
# ---------------------------------------------------------
# @brief :	Template for GNU Makefile
# @author:	hongjie.qin@spacemit.com
# @version:	v1.0.0 2024/02/28
# ---------------------------------------------------------
# @usage:
# $ make install DESTDIR=$(pwd)/install # BACKEND=tiorb
# =========================================================

BACKEND ?= fake

# ========================================================================================

default: install

all:
	@echo "nothing need to do ..."

clean:
	rm -rf $(DESTDIR)

install_post:
	sed -i "s/@VERSION_NUMBER/$(shell cat VERSION_NUMBER)/g" $(DESTDIR)/usr/share/*/*.json $(DESTDIR)/usr/share/*/*.desktop
	sed -i "s/@BACKEND/${BACKEND}/g" $(DESTDIR)/usr/share/*/*.json $(DESTDIR)/usr/share/*/*.desktop
#	eval "sed -i 's/app_path = os.path.abspath(os.getcwd())/app_path = \"\/usr\/src\/bianbu-smart-album-${BACKEND}\"/g'" $(shell find $(DESTDIR)/usr/src/bianbu-smart-album-${BACKEND} -name "*.py")

install: clean all
	mkdir -p $(DESTDIR)
	cp -rdf rootfs/* $(DESTDIR)/
	cp -rdf assets $(DESTDIR)/usr/share/bianbu-smart-album/
	mkdir -p $(DESTDIR)/usr/src/bianbu-smart-album-${BACKEND}
	cp -rdf assets $(DESTDIR)/usr/src/bianbu-smart-album-${BACKEND}
	cp -rdf backend $(DESTDIR)/usr/src/bianbu-smart-album-${BACKEND}
	if [ "${BACKEND}" = "fake" ]; then rm -rf $(DESTDIR)/usr/src/bianbu-smart-album-${BACKEND}/backend/tiorb; fi
	cp -rdf gui $(DESTDIR)/usr/src/bianbu-smart-album-${BACKEND}
	cp -rdf resources $(DESTDIR)/usr/src/bianbu-smart-album-${BACKEND}
	cp -rdf icon.ico $(DESTDIR)/usr/src/bianbu-smart-album-${BACKEND}
	cp -rdf LICENSE $(DESTDIR)/usr/src/bianbu-smart-album-${BACKEND}
	cp -rdf main.py $(DESTDIR)/usr/src/bianbu-smart-album-${BACKEND}
	cp -rdf VERSION_NUMBER $(DESTDIR)/usr/src/bianbu-smart-album-${BACKEND}
	make install_post

.NOTPARALLEL: install
.PHONY: all clean install
