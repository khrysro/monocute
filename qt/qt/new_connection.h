#ifndef NEW_CONNECTION_H
#define NEW_CONNECTION_H

#include <QDialog>

namespace Ui {
class new_connection;
}

class new_connection : public QDialog
{
    Q_OBJECT

public:
    explicit new_connection(QWidget *parent = 0);
    ~new_connection();

private:
    Ui::new_connection *ui;
};

#endif // NEW_CONNECTION_H
