#include "http_server_dialog.h"
#include "ui_http_server_dialog.h"

http_server_dialog::http_server_dialog(QWidget *parent) :
    QDialog(parent),
    ui(new Ui::http_server_dialog)
{
    ui->setupUi(this);
}

http_server_dialog::~http_server_dialog()
{
    delete ui;
}
