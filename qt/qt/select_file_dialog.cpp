#include "select_file_dialog.h"
#include "ui_select_file_dialog.h"

select_file_dialog::select_file_dialog(QWidget *parent) :
    QDialog(parent),
    ui(new Ui::select_file_dialog)
{
    ui->setupUi(this);
}

select_file_dialog::~select_file_dialog()
{
    delete ui;
}
