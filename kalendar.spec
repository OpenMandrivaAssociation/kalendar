Name:           kalendar
Version:        1.0.0
Release:        1
Summary:        Calendar Application
Group:          Graphical desktop/KDE/Plasma5
License:        GPL-3.0
URL:            https://apps.kde.org/kalendar
Source:         https://download.kde.org/stable/kalendar/%{name}-%{version}.tar.xz

BuildRequires:  cmake
BuildRequires:  cmake(ECM)
BuildRequires:  cmake(KF5Akonadi)
BuildRequires:  cmake(KF5AkonadiContact)
BuildRequires:  cmake(KF5CalendarCore)
BuildRequires:  cmake(KF5CalendarSupport)
BuildRequires:  cmake(KF5ConfigWidgets)
BuildRequires:  cmake(KF5Contacts)
BuildRequires:  cmake(KF5CoreAddons)
BuildRequires:  cmake(KF5DBusAddons)
BuildRequires:  cmake(KF5EventViews)
BuildRequires:  cmake(KF5I18n)
BuildRequires:  cmake(KF5IconThemes)
BuildRequires:  cmake(KF5ItemModels)
BuildRequires:  cmake(KF5Kirigami2)
BuildRequires:  cmake(KF5Notifications)
BuildRequires:  cmake(KF5QQC2DesktopStyle)
BuildRequires:  cmake(KF5Service)
BuildRequires:  cmake(KF5WindowSystem)
BuildRequires:  cmake(KF5XmlGui)
BuildRequires:  cmake(Qt5Core)
BuildRequires:  cmake(Qt5Gui)
BuildRequires:  cmake(Qt5Location)
BuildRequires:  cmake(Qt5Qml)
BuildRequires:  cmake(Qt5QuickControls2)
BuildRequires:  cmake(Qt5QuickTest)
BuildRequires:  cmake(Qt5Svg)

Requires: kdepim-addons
Requires: kdepim-runtime
Requires: kirigami2
Requires: qt5-qtgraphicaleffects
Requires: qt5-qtlocation
Requires: qml(org.kde.kitemmodels)

%description
Kalendar is a calendar application that allows you to manage your tasks and events. 
Kalendar supports both local calendars as well as a multitude of online calendars: Nextcloud, Google® Calendar, Outlook®, Caldav, and many more.
Kalendar gives you many ways to interact with your events. 
The month view provides an overview of the entire month; the week view presents a detailed hour-by-hour overview of your week; 
and the schedule view lists all of your upcoming events so that you can easily and quickly plan ahead.
A tasks view is also available, making it possible for you to manage your tasks and subtasks with Kalendar's powerful tree view 
and its customisable filtering capabilities.
Kalendar was built with the idea to be usable on desktop, on mobile and everything in between.

%prep
%autosetup -p1

%build
%cmake

%make_build

%install
%make_install -C build

%find_lang %{name} --with-man --all-name

%files -f %{name}.lang
%{_sysconfdir}/autostart/org.kde.kalendarac.desktop
%{_bindir}/kalendar*
%{_datadir}/applications/org.kde.kalendar.desktop
%{_datadir}/dbus-1/services/org.kde.kalendarac.service
%{_datadir}/knotifications5/kalendarac.notifyrc
%{_datadir}/metainfo/org.kde.kalendar.appdata.xml
%{_datadir}/qlogging-categories5/kalendar.categories
%{_iconsdir}/hicolor/scalable/apps/org.kde.kalendar.svg
