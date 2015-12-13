#include "import_progress.h"
#include "ui_import_progress.h"

import_progress::import_progress(QWidget *parent) :
    QDialog(parent),
    ui(new Ui::import_progress)
{
    ui->setupUi(this);
}

import_progress::~import_progress()
{
    delete ui;
}
