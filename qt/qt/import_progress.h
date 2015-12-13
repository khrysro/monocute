#ifndef IMPORT_PROGRESS_H
#define IMPORT_PROGRESS_H

#include <QDialog>

namespace Ui {
class import_progress;
}

class import_progress : public QDialog
{
    Q_OBJECT

public:
    explicit import_progress(QWidget *parent = 0);
    ~import_progress();

private:
    Ui::import_progress *ui;
};

#endif // IMPORT_PROGRESS_H
