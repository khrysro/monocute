#include "about_mccm.h"
#include "ui_about_mccm.h"

about_mccm::about_mccm(QWidget *parent) :
    QDialog(parent),
    ui(new Ui::about_mccm)
{
    ui->setupUi(this);
}

about_mccm::~about_mccm()
{
    delete ui;
}
