#ifndef ABOUT_MCCM_H
#define ABOUT_MCCM_H

#include <QDialog>

namespace Ui {
class about_mccm;
}

class about_mccm : public QDialog
{
    Q_OBJECT

public:
    explicit about_mccm(QWidget *parent = 0);
    ~about_mccm();

private:
    Ui::about_mccm *ui;
};

#endif // ABOUT_MCCM_H
