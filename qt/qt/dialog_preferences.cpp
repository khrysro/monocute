#include "dialog_preferences.h"
#include "ui_dialog_preferences.h"

dialog_preferences::dialog_preferences(QWidget *parent) :
    QDialog(parent),
    ui(new Ui::dialog_preferences)
{
    ui->setupUi(this);
}

dialog_preferences::~dialog_preferences()
{
    delete ui;
}
