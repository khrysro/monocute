#!/bin/sh
#
# Uninstall Script for Monocaffe Connections Manager
# Please run as root
#
# This script is based on the one of pyjama.
#

# Clever way of testing for root
userpriv=$(test -w \/ && echo "ok")
if [ -z $userpriv ]
    then echo "Please run this script as root / sudo"
    exit 1
fi

install_dir="/usr/share/apps/mccm"

echo "1/3 Removing from Menu"
rm -f /usr/share/pixmaps/mccm.xpm
rm -f /usr/share/applications/mccm.desktop

echo "2/3 Removing Symlinks"
rm -f /usr/bin/mccm
rm -f /usr/bin/mccm-qt

echo "3/3 Removing mccm"
rm -rf ${install_dir}
