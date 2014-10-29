#!/usr/bin/env python
# -*- coding: utf-8 -*-

##############################################################################################################
# This script is a simple management system for series made of exercises and solution.                       #
# It is possible to make zipped series for moodle, a zip containing all series. Furthermore one can          #
# generate previews for one exercise/solution. Two handy functions are the make-workbook and the             #
# make-catalogue. The former one creaets a pdf containig all series, each one followed by its solution       #
# just like they were distributed. The latter one create a sort of index of all available exercises in       #
# the system. Each exercise is followed by its solution.                                                     #
#                                                                                                            #
# The structure for a new exercise should be created by using the make-new-exercise function.                #
# For further help, please refer to the help function of the software.                                       #
# ---------------------------------------------------------------------------------------------------------- #
#                                                                                                            #
# Author: Andreas Ruppen                                                                                     #
# License: GPL                                                                                               #
# This program is free software; you can redistribute it and/or modify                                       #
#   it under the terms of the GNU General Public License as published by                                     #
#   the Free Software Foundation; either version 2 of the License, or                                        #
#   (at your option) any later version.                                                                      #
#                                                                                                            #
#   This program is distributed in the hope that it will be useful,                                          #
#   but WITHOUT ANY WARRANTY; without even the implied warranty of                                           #
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the                                            #
#   GNU General Public License for more details.                                                             #
#                                                                                                            #
#   You should have received a copy of the GNU General Public License                                        #
#   along with this program; if not, write to the                                                            #
#   Free Software Foundation, Inc.,                                                                          #
#   59 Temple Place - Suite 330, Boston, MA  02111-1307, USA.                                                #
##############################################################################################################
import sys
import logging
import logging.config
import subprocess
if float(sys.version[:3])<3.0:
    import ConfigParser
else: 
    import configparser as ConfigParser
import argparse
from os.path import dirname, join, expanduser
    
class KeyboardSwitcher:
    """
        Created on 24 October 2014
        @author: ruppena
    """
    def __init__(self):
        """Do some initialization stuff"""
        INSTALL_DIR = dirname(__file__)
        CONFIG_DIR = '/etc/KeyboardSwitcher/'
        logging.basicConfig(level=logging.ERROR)
        logging.config.fileConfig([join(CONFIG_DIR, 'logging.conf'), expanduser('~/.logging.conf'), 'logging.conf'])
        self.__log = logging.getLogger('mylogger')

        self.__log.debug("Reading general configuration from keyboardswitcher.cfg")
        self.__ksConfig = ConfigParser.SafeConfigParser()
        self.__ksConfig.read([join(CONFIG_DIR, 'keyboardswitcher.cfg'), expanduser('~/.keyboardswitcher.cfg'), 'keyboardswitcher.cfg'])


        #you could read here parameters of the config file instead of passing them on cmd line
        #self.__baseURI = self.__ksConfig.get("Config", "baseURI")
        self.__xmodmap = self.__ksConfig.get("General", "xmodmap")
        self.__layout = "mac_internal"
        
    def main(self):
        """The main function"""
        self.__log.debug("The chosen layout is: " + self.__layout)
        self.__log.info("Clenaup old modifier keys")
        subprocess.call(self.__xmodmap + ' -e "clear control"', shell=True)
        subprocess.call(self.__xmodmap + ' -e "clear mod4"', shell=True)
        subprocess.call(self.__xmodmap + ' -e "clear mod5"', shell=True)
        subprocess.call(self.__xmodmap + ' -e "clear mod1"', shell=True)
        self.__log.info("Apply new layout")
        for option in self.__ksConfig.options(self.__layout):
            value = self.__ksConfig.get(self.__layout, option)
            key = option.replace('kc_', 'keycode ')
            argument = '-e "' + key + ' = ' + value + '"'
            self.__log.debug(argument)
            subprocess.call(self.__xmodmap + ' ' + argument, shell=True)
        self.__log.info("Define new modifier keys")
        subprocess.call(self.__xmodmap + ' -e "add mod4 = Super_L"', shell=True)
        subprocess.call(self.__xmodmap + ' -e "add mod5 = ISO_Level3_Shift"', shell=True)
        subprocess.call(self.__xmodmap + ' -e "add mod1 = Alt_L Meta_L"', shell=True)
        subprocess.call(self.__xmodmap + ' -e "add mod1 = Alt_R Meta_R"', shell=True)
        subprocess.call(self.__xmodmap + ' -e "add control = Control_L"', shell=True)
        subprocess.call(self.__xmodmap + ' -e "add control = Control_R"', shell=True)


    def print_layouts(self):
        """Shows a list of available layouts"""
        print("Following layouts are available:")
        sections = self.__ksConfig.sections()
        for section in sections:
            if section != "General":
                print("\t* "+section)

    def getArguments(self, argv):
        parser = argparse.ArgumentParser()
        parser.add_argument("layout", help="layout to apply", nargs='?', default="logitech")
        parser.add_argument("-l", "--list-layouts", help="List the available layouts",
                            required=False, action="store_true")
        args = parser.parse_args(argv)
        if args.list_layouts:
            self.print_layouts()
        else:
            self.__layout = args.layout
            self.main()

if __name__ == '__main__':
    prog = KeyboardSwitcher()
    prog.getArguments(sys.argv[1:])
