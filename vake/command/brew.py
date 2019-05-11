# 1st
import os

# 2nd
from .. import xos
from . import base

BREW = "brew"
BREWFILE = "Brewfile"


class BrewAction(base.Action):
    def kegs(self):
        path = os.path.join(os.getcwd(), xos.sysname(), BREWFILE)

        if self.logger:
            self.logger.debug("Read kegs from file: %s" % path)

        if os.path.exists(path):
            return open(path).read().splitlines()
        else:
            return []


class Install(BrewAction):
    def run(self):
        if not self.shell.available(BREW):
            self.logger.warn("Command is not available: %s" % BREW)
            return

        kegs = self.kegs()

        if not kegs:
            self.logger.info("No available kegs were found")
            return

        for keg in kegs:
            self.shell.execute([BREW, "install", keg])

        return


class Uninstall(BrewAction):
    def run(self):
        if not self.shell.available(BREW):
            self.logger.warn("Command is not available: %s" % BREW)
            return

        kegs = self.kegs()

        if not kegs:
            self.logger.info("No available kegs were found")
            return

        for keg in kegs:
            self.shell.execute([BREW, "uninstall", keg])

        return


class Status(BrewAction):
    def run(self):
        if not self.shell.available(BREW):
            self.logger.warn("Command is not available: %s" % BREW)
            return

        self.shell.execute([BREW, "tap"])
        self.shell.execute([BREW, "list"])
        return
