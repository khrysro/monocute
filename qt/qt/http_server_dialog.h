#ifndef HTTP_SERVER_DIALOG_H
#define HTTP_SERVER_DIALOG_H

#include <QDialog>

namespace Ui {
class http_server_dialog;
}

class http_server_dialog : public QDialog
{
    Q_OBJECT

public:
    explicit http_server_dialog(QWidget *parent = 0);
    ~http_server_dialog();

private:
    Ui::http_server_dialog *ui;
};

#endif // HTTP_SERVER_DIALOG_H
