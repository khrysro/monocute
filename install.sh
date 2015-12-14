#!/bin/sh
#
# Install Script for Monocute Connections Manager
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
mcm_shell="/usr/share/apps/mccm/bin/mccm"

echo "1/3 Copying files to ${install_dir}"
mkdir -p ${install_dir} 2>/dev/null
cp -R * ${install_dir} 2>/dev/null

echo "2/3 Creating symlinks"

ln -s ${mcm_shell}  /usr/bin/mccm
ln -s ${mcm_shell}  /usr/bin/mccm-qt

echo "3/3 Creating menu-entry for Monocute Connections Manager"
cp /usr/share/apps/mccm/qt/mccm_icon.xpm /usr/share/pixmaps/mccm.xpm
cp /usr/share/apps/mccm/qt/mccm.desktop /usr/share/applications/

echo "Done. Monocute Connections Manager is ready"
echo "Type mccm on a console or run mcm-qt from the Menu"


exit 0
