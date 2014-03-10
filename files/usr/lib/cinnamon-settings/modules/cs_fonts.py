#!/usr/bin/env python

from SettingsWidgets import *
from gi.repository.Gtk import SizeGroup, SizeGroupMode


class Module:
    def __init__(self, content_box):
        keywords = _("font, size, small, large")
        advanced = False
        sidePage = SidePage(_("Fonts"), "fonts.svg", keywords, advanced, content_box)
        self.sidePage = sidePage
        self.name = "fonts"
        self.category = "appear"
        self.comment = _("Configure system fonts")
        
        #Main Header Text
        title = Gtk.Label()
        title.set_markup("<span font_desc='10.5'><b>%s</b></span>" %_("Configure how your system fonts appear"))
        sidePage.add_widget(title)
        
        #Some info about the settings
        info = Gtk.Label(_("Fonts can make reading text easier, help save screen space, or simply personalize your setup."))
        sidePage.add_widget(info)
        
        sidePage.add_widget(Gtk.Separator.new(Gtk.Orientation.HORIZONTAL))
        
        size_groups = getattr(self, "size_groups", [SizeGroup(SizeGroupMode.HORIZONTAL) for x in range(2)])
        sidePage.add_widget(size_groups)
        
        size_groups[0].add_widget(Gtk.Label(_("Default font")))
        sidePage.add_widget(GSettingsFontButton("", "org.cinnamon.desktop.interface", "font-name", None))
        sidePage.add_widget(GSettingsFontButton(_("Document font"), "org.gnome.desktop.interface", "document-font-name", None))
        sidePage.add_widget(GSettingsFontButton(_("Monospace font"), "org.gnome.desktop.interface", "monospace-font-name", None))
        sidePage.add_widget(GSettingsFontButton(_("Window title font"), "org.cinnamon.desktop.wm.preferences", "titlebar-font", None))
        sidePage.add_widget(GSettingsRangeSpin(_("Text scaling factor"), "org.cinnamon.desktop.interface", "text-scaling-factor", None, adjustment_step = 0.1), True)
        sidePage.add_widget(GSettingsComboBox(_("Antialiasing"), "org.cinnamon.settings-daemon.plugins.xsettings", "antialiasing", None, [(i, i.title()) for i in ("none", "grayscale", "rgba")]), True)
        sidePage.add_widget(GSettingsComboBox(_("Hinting"), "org.cinnamon.settings-daemon.plugins.xsettings", "hinting", None, [(i, i.title()) for i in ("none", "slight", "medium", "full")]), True)
        

