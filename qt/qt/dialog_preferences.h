#ifndef DIALOG_PREFERENCES_H
#define DIALOG_PREFERENCES_H

#include <QDialog>

namespace Ui {
class dialog_preferences;
}

class dialog_preferences : public QDialog
{
    Q_OBJECT

public:
    explicit dialog_preferences(QWidget *parent = 0);
    ~dialog_preferences();

private:
    Ui::dialog_preferences *ui;
};

#endif // DIALOG_PREFERENCES_H
