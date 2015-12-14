#-------------------------------------------------
#
# Project created by QtCreator 2015-12-11T13:56:47
#
#-------------------------------------------------

QT       += core gui

greaterThan(QT_MAJOR_VERSION, 4): QT += widgets

TARGET = monocute
TEMPLATE = app


SOURCES += main.cpp\
        mainwindow.cpp \
    about_mccm.cpp \
    edit_connections_dialog.cpp \
    select_file_dialog.cpp \
    http_server_dialog.cpp \
    dialog_preferences.cpp \
    import_progress.cpp \
    new_connection.cpp

HEADERS  += mainwindow.h \
    about_mccm.h \
    edit_connections_dialog.h \
    select_file_dialog.h \
    http_server_dialog.h \
    dialog_preferences.h \
    import_progress.h \
    new_connection.h

FORMS    += mainwindow.ui \
    about_mccm.ui \
    edit_connections_dialog.ui \
    select_file_dialog.ui \
    http_server_dialog.ui \
    dialog_preferences.ui \
    import_progress.ui \
    new_connection.ui

RESOURCES += \
    AppResources.qrc
