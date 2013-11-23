#!/usr/bin/python3
from gi.repository import Gtk, GraphGtk

def main():
    window = Gtk.Window(Gtk.WindowType.TOPLEVEL)
    window.set_default_size(800, 600)
    window.connect("destroy", Gtk.main_quit)

    graphView = GraphGtk.View()
    graphView.connect("node-selected", node_selected)
    graphView.connect("node-deselected", node_deselected)
    graphView.connect("nodes-connected", nodes_connected)
    graphView.connect("nodes-disconnected", nodes_disconnected)

    vbox = Gtk.Box()
    vbox.set_orientation(Gtk.Orientation.VERTICAL)
    window.add(vbox)

    #Build the menu
    menubar = Gtk.MenuBar()
    graph_menu = Gtk.Menu()
    graph = Gtk.MenuItem("Graph")
    graph.set_submenu(graph_menu)

    add_node = Gtk.MenuItem("Add Node")
    add_node.connect("activate", menu_item_activated, graphView)
    graph_menu.append(add_node)

    delete = Gtk.MenuItem("Delete Node")
    delete.connect("activate", menu_item_activated, graphView)
    graph_menu.append(delete)

    menubar.append(graph)

    vbox.pack_start(menubar, False, False, 0)
    vbox.pack_start(graphView, True, True, 0)

    #Show all widgets
    window.show_all()

    Gtk.main()


def menu_item_activated(menu_item, graph):
    label = menu_item.get_label()
    
    if ("Add Node" in label):
        dialog = Gtk.Dialog()
        dialog.set_modal(True)
        dialog.add_button(Gtk.STOCK_CANCEL, Gtk.ResponseType.REJECT)
        dialog.add_button(Gtk.STOCK_OK, Gtk.ResponseType.ACCEPT)

        dialog.set_default_size(350, 80)

        vbox = dialog.get_content_area()

        name_label = Gtk.Label("Name")
        name_entry = Gtk.Entry()
        vbox.pack_start(name_label, False, False, 0)
        vbox.pack_start(name_entry, False, False, 0)

        columns = Gtk.Box()
        columns.set_homogeneous(True)
        vbox.pack_start(columns, True, True, 0)

        left_column = Gtk.Box()
        left_column.set_orientation(Gtk.Orientation.VERTICAL)
        columns.pack_start(left_column, True, True, 0)
        left_column.pack_start(Gtk.Label("Inputs"), False, False, 0)

        right_column = Gtk.Box()
        right_column.set_orientation(Gtk.Orientation.VERTICAL)
        columns.pack_start(right_column, True, True, 0)
        right_column.pack_start(Gtk.Label("Outputs"), False, False, 0)

        inputs = Gtk.Box()
        inputs.set_orientation(Gtk.Orientation.VERTICAL)
        left_column.pack_start(inputs, True, True, 0)

        outputs = Gtk.Box()
        outputs.set_orientation(Gtk.Orientation.VERTICAL)
        right_column.pack_start(outputs, True, True, 0)

        add_input = Gtk.Button("Add")
        add_input.connect("clicked", button_clicked, inputs)
        left_column.pack_start(add_input, False, False, 0)

        add_output = Gtk.Button("Add")
        add_output.connect("clicked", button_clicked, outputs)
        right_column.pack_start(add_output, False, False, 0)

        vbox.show_all()

        result = dialog.run()

        if(result == Gtk.ResponseType.ACCEPT):
            node = GraphGtk.Node()
            node.set_name(name_entry.get_text())

            for entry in inputs.get_children():
                node.add_pad(entry.get_text(), False)

            for entry in outputs.get_children():
                node.add_pad(entry.get_text(), True)

            graph.add_node(node)
        dialog.close()
    elif("Delete Node" in label):
        graph.remove_selected_nodes()


def button_clicked(button, vbox):
    entry = Gtk.Entry()
    vbox.pack_start(entry, False, False, 2)
    entry.show()


def nodes_connected(view, fromNode, output, to, input):
    print("Connected pads: %s->%s" % (output, input))


def nodes_disconnected(view, fromNode, output, to, input):
    print("Disconnected pads: %s->%s" % (output, input))


def node_selected(view, node):
    print("Selected: %s" % node.get_name())


def node_deselected(view, node):
    print("Deselected: %s" % node.get_name())
    
main()
