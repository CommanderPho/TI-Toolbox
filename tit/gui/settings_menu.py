#!/usr/bin/env simnibs_python
# -*- coding: utf-8 -*-

"""
Settings Menu - Gear icon menu for Help, Acknowledgments, and Contact
"""

from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import QSettings


class FloatingHelpWindow(QtWidgets.QDialog):
    """Floating window for Help content."""

    def __init__(self, parent=None):
        super(FloatingHelpWindow, self).__init__(parent)
        self.setWindowTitle("TI-Toolbox - Help")
        self.setMinimumSize(800, 600)
        self.setup_ui()

    def setup_ui(self):
        """Set up the help window UI."""
        from tit.gui.help_tab import HelpTab

        layout = QtWidgets.QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)

        # Create the help tab content
        self.help_content = HelpTab(self)
        layout.addWidget(self.help_content)

        # Add a close button at the bottom
        button_layout = QtWidgets.QHBoxLayout()
        button_layout.addStretch()
        close_btn = QtWidgets.QPushButton("Close")
        close_btn.clicked.connect(self.close)
        close_btn.setMinimumWidth(100)
        button_layout.addWidget(close_btn)
        button_layout.addStretch()
        layout.addLayout(button_layout)


class FloatingContactWindow(QtWidgets.QDialog):
    """Floating window for Contact content."""

    def __init__(self, parent=None):
        super(FloatingContactWindow, self).__init__(parent)
        self.setWindowTitle("TI-Toolbox - Contact")
        self.setMinimumSize(700, 500)
        self.setup_ui()

    def setup_ui(self):
        """Set up the contact window UI."""
        from tit.gui.contact_tab import ContactTab

        layout = QtWidgets.QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)

        # Create the contact tab content
        self.contact_content = ContactTab(self)
        layout.addWidget(self.contact_content)

        # Add a close button at the bottom
        button_layout = QtWidgets.QHBoxLayout()
        button_layout.addStretch()
        close_btn = QtWidgets.QPushButton("Close")
        close_btn.clicked.connect(self.close)
        close_btn.setMinimumWidth(100)
        button_layout.addWidget(close_btn)
        button_layout.addStretch()
        layout.addLayout(button_layout)


class FloatingAcknowledgmentsWindow(QtWidgets.QDialog):
    """Floating window for Acknowledgments content."""

    def __init__(self, parent=None):
        super(FloatingAcknowledgmentsWindow, self).__init__(parent)
        self.setWindowTitle("TI-Toolbox - Acknowledgments")
        self.setMinimumSize(700, 500)
        self.setup_ui()

    def setup_ui(self):
        """Set up the acknowledgments window UI."""
        from tit.gui.acknowledgments_tab import AcknowledgmentsTab

        layout = QtWidgets.QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)

        # Create the acknowledgments tab content
        self.acknowledgments_content = AcknowledgmentsTab(self)
        layout.addWidget(self.acknowledgments_content)

        # Add a close button at the bottom
        button_layout = QtWidgets.QHBoxLayout()
        button_layout.addStretch()
        close_btn = QtWidgets.QPushButton("Close")
        close_btn.clicked.connect(self.close)
        close_btn.setMinimumWidth(100)
        button_layout.addWidget(close_btn)
        button_layout.addStretch()
        layout.addLayout(button_layout)


class SettingsMenuButton(QtWidgets.QPushButton):
    """Gear icon button with dropdown menu for settings/info."""

    def __init__(self, parent=None):
        super(SettingsMenuButton, self).__init__(parent)
        self.parent = parent
        self.setup_ui()

    def setup_ui(self):
        """Set up the gear button and menu."""
        # Set gear icon (using Unicode gear symbol)
        self.setText("⚙")  # Gear emoji/symbol
        self.setStyleSheet(
            """
            QPushButton {
                font-size: 24px;
                border: none;
                background: transparent;
                padding: 5px;
            }
            QPushButton:hover {
                background: rgba(0, 0, 0, 0.1);
                border-radius: 3px;
            }
            QPushButton::menu-indicator {
                width: 0px;
            }
        """
        )
        self.setToolTip("Settings and Information")
        self.setCursor(QtCore.Qt.PointingHandCursor)

        # Create the dropdown menu
        self.menu = QtWidgets.QMenu(self)

        # Add menu actions
        preferences_action = self.menu.addAction("Preferences")
        preferences_action.triggered.connect(self.open_preferences)
        
        self.menu.addSeparator()
        
        help_action = self.menu.addAction("Help")
        help_action.triggered.connect(self.open_help)

        contact_action = self.menu.addAction("Contact")
        contact_action.triggered.connect(self.open_contact)

        acknowledgments_action = self.menu.addAction("Acknowledgments")
        acknowledgments_action.triggered.connect(self.open_acknowledgments)

        # Set the menu to the button
        self.setMenu(self.menu)

    def open_help(self):
        """Open the Help window."""
        help_window = FloatingHelpWindow(self.parent)
        help_window.show()

    def open_extensions(self):
        """Open the Extensions window."""
        from tit.gui.extensions import FloatingExtensionsWindow

        extensions_window = FloatingExtensionsWindow(
            self.parent, main_window=self.parent
        )
        extensions_window.show()

    def open_contact(self):
        """Open the Contact window."""
        contact_window = FloatingContactWindow(self.parent)
        contact_window.show()

    def open_acknowledgments(self):
        """Open the Acknowledgments window."""
        acknowledgments_window = FloatingAcknowledgmentsWindow(self.parent)
        acknowledgments_window.show()
    
    def open_preferences(self):
        """Open the Preferences window."""
        preferences_window = FloatingPreferencesWindow(self.parent)
        preferences_window.show()


class FloatingPreferencesWindow(QtWidgets.QDialog):
    """Floating window for Preferences."""
    
    def __init__(self, parent=None):
        super(FloatingPreferencesWindow, self).__init__(parent)
        self.setWindowTitle("TI-Toolbox - Preferences")
        self.setMinimumSize(500, 300)
        self.settings = QSettings("TI-Toolbox", "TI-Toolbox")
        self.setup_ui()
        self.load_settings()
        
    def setup_ui(self):
        """Set up the preferences window UI."""
        layout = QtWidgets.QVBoxLayout(self)
        layout.setContentsMargins(20, 20, 20, 20)
        layout.setSpacing(15)
        
        # Title
        title_label = QtWidgets.QLabel("Preferences")
        title_label.setStyleSheet("font-size: 18px; font-weight: bold;")
        layout.addWidget(title_label)
        
        # System Monitor section
        monitor_group = QtWidgets.QGroupBox("System Monitor")
        monitor_group.setStyleSheet("""
            QGroupBox {
                font-weight: bold;
                border: 1px solid #cccccc;
                border-radius: 5px;
                margin-top: 10px;
                padding-top: 10px;
            }
            QGroupBox::title {
                subcontrol-origin: margin;
                left: 10px;
                padding: 0 5px;
            }
        """)
        monitor_layout = QtWidgets.QVBoxLayout(monitor_group)
        monitor_layout.setSpacing(10)
        
        # Command history logging option
        self.command_history_cb = QtWidgets.QCheckBox("Enable command history logging")
        self.command_history_cb.setToolTip(
            "When enabled, logs all toolbox-related process commands to command_history.log in the project directory"
        )
        monitor_layout.addWidget(self.command_history_cb)
        
        # Description
        desc_label = QtWidgets.QLabel(
            "Command history logging records when toolbox processes start, including timestamp and full command line."
        )
        desc_label.setWordWrap(True)
        desc_label.setStyleSheet("color: #666666; font-size: 10px;")
        monitor_layout.addWidget(desc_label)
        
        layout.addWidget(monitor_group)
        
        layout.addStretch()
        
        # Buttons
        button_layout = QtWidgets.QHBoxLayout()
        button_layout.addStretch()
        
        self.apply_btn = QtWidgets.QPushButton("Apply")
        self.apply_btn.clicked.connect(self.apply_settings)
        self.apply_btn.setMinimumWidth(100)
        button_layout.addWidget(self.apply_btn)
        
        self.ok_btn = QtWidgets.QPushButton("OK")
        self.ok_btn.clicked.connect(self.ok_clicked)
        self.ok_btn.setMinimumWidth(100)
        button_layout.addWidget(self.ok_btn)
        
        self.cancel_btn = QtWidgets.QPushButton("Cancel")
        self.cancel_btn.clicked.connect(self.close)
        self.cancel_btn.setMinimumWidth(100)
        button_layout.addWidget(self.cancel_btn)
        
        layout.addLayout(button_layout)
    
    def load_settings(self):
        """Load settings from QSettings."""
        # Default to True (enabled) if not set
        command_history_enabled = self.settings.value("system_monitor/command_history_enabled", True, type=bool)
        self.command_history_cb.setChecked(command_history_enabled)
    
    def save_settings(self):
        """Save settings to QSettings."""
        self.settings.setValue("system_monitor/command_history_enabled", self.command_history_cb.isChecked())
        self.settings.sync()
    
    def apply_settings(self):
        """Apply settings without closing the dialog."""
        self.save_settings()
        QtWidgets.QMessageBox.information(self, "Preferences", "Settings have been saved.")
    
    def ok_clicked(self):
        """Save settings and close the dialog."""
        self.save_settings()
        self.close()


class ExtensionsButton(QtWidgets.QPushButton):
    """Extensions icon button for opening extensions window."""

    def __init__(self, parent=None):
        super(ExtensionsButton, self).__init__(parent)
        self.parent = parent
        self.setup_ui()

    def setup_ui(self):
        """Set up the extensions button."""
        # Set extensions icon (using Unicode symbol compatible with Ubuntu containers)
        self.setText(
            "◳"
        )  # Square with top right quadrant - represents extensions/modules
        self.setStyleSheet(
            """
            QPushButton {
                font-size: 18px;
                font-weight: bold;
                border: none;
                background: transparent;
                padding: 5px;
            }
            QPushButton:hover {
                background: rgba(0, 0, 0, 0.1);
                border-radius: 3px;
            }
        """
        )
        self.setToolTip("Extensions")
        self.setCursor(QtCore.Qt.PointingHandCursor)

        # Connect click to open extensions
        self.clicked.connect(self.open_extensions)

    def open_extensions(self):
        """Open the Extensions window."""
        from tit.gui.extensions import FloatingExtensionsWindow

        extensions_window = FloatingExtensionsWindow(
            self.parent, main_window=self.parent
        )
        extensions_window.show()
