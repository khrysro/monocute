#!/bin/bash
#
# Creates the Structure for a deb

rm -rf /tmp/pack
mkdir -p /tmp/pack/usr/share/apps/mccm
mkdir -p /tmp/pack/DEBIAN
cp -R ../* /tmp/pack/usr/share/apps/mccm
cp debian/* /tmp/pack/DEBIAN/

cd /tmp/
dpkg -b pack mcm-0.9.3_all.deb
