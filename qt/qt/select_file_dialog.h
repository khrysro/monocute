#ifndef SELECT_FILE_DIALOG_H
#define SELECT_FILE_DIALOG_H

#include <QDialog>

namespace Ui {
class select_file_dialog;
}

class select_file_dialog : public QDialog
{
    Q_OBJECT

public:
    explicit select_file_dialog(QWidget *parent = 0);
    ~select_file_dialog();

private:
    Ui::select_file_dialog *ui;
};

#endif // SELECT_FILE_DIALOG_H
