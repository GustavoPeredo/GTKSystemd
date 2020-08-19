# window.py
#
# Copyright 2020 GustavoPeredo
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
import os
import numpy
from gi.repository import Gtk, Handy

@Gtk.Template(resource_path='/org/gustavoperedo/GTKSytemd/window.ui')
class GtksystemdWindow(Gtk.ApplicationWindow):
    __gtype_name__ = 'GtksystemdWindow'

    outerTree = Gtk.Template.Child()
    cellName = Gtk.Template.Child()
    cellLoaded = Gtk.Template.Child()
    cellActive = Gtk.Template.Child()
    cellSub = Gtk.Template.Child()
    cellDescription = Gtk.Template.Child()
    startButton = Gtk.Template.Child()
    stopButton = Gtk.Template.Child()
    reloadButton = Gtk.Template.Child()
    restartButton = Gtk.Template.Child()
    killButton = Gtk.Template.Child()
    outerTreeList = Gtk.Template.Child()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        """ Defines what process is selected """

        self.select = self.outerTree.get_selection()

        """ Defines and calls what each action button does """

        self.startButton.connect("clicked", self.runAction, "start",
                                  self.select)
        self.stopButton.connect("clicked", self.runAction, "stop",
                                  self.select)
        self.reloadButton.connect("clicked", self.runAction, "reload",
                                  self.select)
        self.restartButton.connect("clicked", self.runAction, "restart",
                                  self.select)
        self.killButton.connect("clicked", self.runAction, "kill",
                                  self.select)

        """ Calls the reset function """

        self.reset()

        """ FIXME: Find a way to refresh the unit list"""

        for items in (tuple(map(tuple, self.splitSystemD("templist"))))[1:-7]:
            self.outerTreeList.append(items, )

    """ FIXME: There must be abetter way of doing this!"""
    """ Takes what is written on the tempfile and makes it readable by
        splitting the text into different rows depending on their po-
        sitions. """
    def splitSystemD(self, output):
        with open(output, 'r') as data:
            for lines in data.read().split("\n"):
                if len(lines.split("loaded")) == 2:
                    beginning_num = len(lines.split("loaded")[0])
                    last_num = len(lines.split("loaded")[-1])

                    column_locations = numpy.array([5, beginning_num + 5,
                    beginning_num + 15, beginning_num + 23, beginning_num + 31,
                    beginning_num + 31 + last_num])

                    widths = column_locations[1:] - column_locations[:-1]

                    return(numpy.genfromtxt(output, dtype=str, delimiter=widths,
                                              autostrip=True))

    """ The reset function refreshes the templist file """
    def reset(self):
        os.system('rm templist')
        os.system('systemctl list-units --all | cat >> templist')

    """ Runs a systemd action """
    def runAction(self, widget, action, process):
        model, treeiter = process.get_selected()
        if treeiter is not None:
            process = model[treeiter][0]
        os.system('systemctl ' + action + " " + process)
        self.reset()
