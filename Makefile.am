SUBDIRS = graph-gtk tests

pkgconfigdir = $(libdir)/pkgconfig
pkgconfig_DATA = graph-gtk.pc

EXTRA_DIST = graph-gtk.pc.in

ACLOCAL_AMFLAGS = -I m4 ${ACLOCAL_FLAGS}
DISTCHECK_CONFIGURE_FLAGS = --enable-introspection
