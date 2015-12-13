#include "new_connection.h"
#include "ui_new_connection.h"

new_connection::new_connection(QWidget *parent) :
    QDialog(parent),
    ui(new Ui::new_connection)
{
    ui->setupUi(this);
}

new_connection::~new_connection()
{
    delete ui;
}
