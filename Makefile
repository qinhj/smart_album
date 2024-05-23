# =========================================================
#                makefile for smart album
# ---------------------------------------------------------
# @brief :	Template for GNU Makefile
# @author:	hongjie.qin@spacemit.com
# @version:	v1.0.0 2024/02/28
# ---------------------------------------------------------
# @usage:
# $ make install DESTDIR=$(pwd)/install
# =========================================================

# ========================================================================================

default: all

all:
	@echo "nothing need to do ..."

clean:
	rm -rf $(DESTDIR)

install_backend:
	mkdir -p $(DESTDIR)/usr/src/bianbu-smart-album${BACKEND}
	cp -rdf assets $(DESTDIR)/usr/src/bianbu-smart-album${BACKEND}
	cp -rdf backend $(DESTDIR)/usr/src/bianbu-smart-album${BACKEND}
	cp -rdf gui $(DESTDIR)/usr/src/bianbu-smart-album${BACKEND}
	cp -rdf resources $(DESTDIR)/usr/src/bianbu-smart-album${BACKEND}
	cp -rdf icon.ico $(DESTDIR)/usr/src/bianbu-smart-album${BACKEND}
	cp -rdf LICENSE $(DESTDIR)/usr/src/bianbu-smart-album${BACKEND}
	cp -rdf main.py $(DESTDIR)/usr/src/bianbu-smart-album${BACKEND}
	cp -rdf VERSION_NUMBER $(DESTDIR)/usr/src/bianbu-smart-album${BACKEND}

install: clean all
	mkdir -p $(DESTDIR)
	cp -rdf rootfs/* $(DESTDIR)/
	cp -rdf assets $(DESTDIR)/usr/share/bianbu-smart-album/
	make install_backend

.NOTPARALLEL: install
.PHONY: all clean install
