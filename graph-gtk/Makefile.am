AM_CFLAGS = $(GTK_CFLAGS) -g
LIBS = $(GTK_LIBS)

lib_LTLIBRARIES = libgraph-gtk.la

pkginclude_HEADERS = 		graph-gtk-view.h	\
				graph-gtk-node.h	\
				graph-gtk-pad.h		\
				graph-gtk-connection.h  \
				graph-gtk-types.h

libgraph_gtk_la_SOURCES = 	graph-gtk-view.c	\
				graph-gtk-node.c	\
				graph-gtk-pad.c		\
				graph-gtk-connection.c

-include $(INTROSPECTION_MAKEFILE)
INTROSPECTION_GIRS =
INTROSPECTION_SCANNER_ARGS = --add-include-path=. \
  --identifier-prefix=GraphGtk \
  --symbol-prefix=graph_gtk --warn-all
INTROSPECTION_COMPILER_ARGS = --includedir=.


if HAVE_INTROSPECTION
  introspection_sources = $(libgraph_gtk_la_SOURCES) $(pkginclude_HEADERS)

  GraphGtk-0.1.gir: libgraph-gtk.la
  GraphGtk_0_1_gir_INCLUDES = GObject-2.0 Gtk-3.0
  GraphGtk_0_1_gir_CFLAGS = $(INCLUDES)
  GraphGtk_0_1_gir_LIBS = libgraph-gtk.la
  GraphGtk_0_1_gir_FILES = $(introspection_sources)
  INTROSPECTION_GIRS += GraphGtk-0.1.gir

  girdir = $(datadir)/gir-1.0
  gir_DATA = $(INTROSPECTION_GIRS)

  typelibdir = $(libdir)/girepository-1.0
  typelib_DATA = $(INTROSPECTION_GIRS:.gir=.typelib)

  CLEANFILES = $(gir_DATA) $(typelib_DATA)
endif
