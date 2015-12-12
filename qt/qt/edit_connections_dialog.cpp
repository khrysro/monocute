#include "edit_connections_dialog.h"
#include "ui_edit_connections_dialog.h"

edit_connections_dialog::edit_connections_dialog(QWidget *parent) :
    QDialog(parent),
    ui(new Ui::edit_connections_dialog)
{
    ui->setupUi(this);
}

edit_connections_dialog::~edit_connections_dialog()
{
    delete ui;
}
