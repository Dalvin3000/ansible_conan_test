#include <QApplication>
#include <QWidget>
#include <QLayout>
#include <QLabel>
#include <QFileInfo>
#include <QDir>


int main(int argc, char** argv)
{
    {
        QFileInfo thisPath{ *argv };

        QApplication::addLibraryPath(thisPath.absoluteDir().absoluteFilePath("../lib"));

        QApplication app(argc, argv);

        QWidget mainWindow;

        mainWindow.setFixedSize({ 300, 150 });
        mainWindow.setStyleSheet("font-size: 16pt");

        mainWindow.setLayout(new QHBoxLayout{ &mainWindow });
        mainWindow.layout()->addItem(new QSpacerItem{0, 0, QSizePolicy::MinimumExpanding});
        mainWindow.layout()->addWidget(new QLabel{ "v0.1", &mainWindow });
        mainWindow.layout()->addItem(new QSpacerItem{ 0, 0, QSizePolicy::MinimumExpanding });

        mainWindow.show();

        app.exec();
    }

    return 0;
};

