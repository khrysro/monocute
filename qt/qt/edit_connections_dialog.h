#ifndef EDIT_CONNECTIONS_DIALOG_H
#define EDIT_CONNECTIONS_DIALOG_H

#include <QDialog>

namespace Ui {
class edit_connections_dialog;
}

class edit_connections_dialog : public QDialog
{
    Q_OBJECT

public:
    explicit edit_connections_dialog(QWidget *parent = 0);
    ~edit_connections_dialog();

private:
    Ui::edit_connections_dialog *ui;
};

#endif // EDIT_CONNECTIONS_DIALOG_H
