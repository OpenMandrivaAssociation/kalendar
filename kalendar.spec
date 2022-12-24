%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)

Name:           kalendar
Version:        22.12.0
Release:        1
Summary:        Calendar Application
Group:          Graphical desktop/KDE/Plasma5
License:        GPL-3.0
URL:            https://apps.kde.org/kalendar
Source:         https://download.kde.org/%{stable}/release-service/%{version}/src/kalendar-%{version}.tar.xz

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
BuildRequires:	cmake(KF5MailCommon)
BuildRequires:  cmake(KF5Notifications)
BuildRequires:  cmake(KF5PimCommonAkonadi)
BuildRequires:  cmake(KF5QQC2DesktopStyle)
BuildRequires:  cmake(KF5Service)
BuildRequires:  cmake(KF5WindowSystem)
BuildRequires:  cmake(KF5XmlGui)
BuildRequires:	cmake(KF5Plasma)
BuildRequires:  cmake(Qt5Core)
BuildRequires:  cmake(Qt5Gui)
BuildRequires:  cmake(Qt5Location)
BuildRequires:  cmake(Qt5Qml)
BuildRequires:  cmake(Qt5QuickControls2)
BuildRequires:  cmake(Qt5QuickTest)
BuildRequires:  cmake(Qt5Svg)
BuildRequires:	pkgconfig(gpgme)

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
%{_bindir}/kalendar*
%{_datadir}/applications/org.kde.kalendar.desktop
%{_datadir}/metainfo/org.kde.kalendar.appdata.xml
%{_datadir}/qlogging-categories5/kalendar.categories
%{_iconsdir}/hicolor/scalable/apps/org.kde.kalendar.svg
%{_libdir}/qml/org/kde/akonadi
%{_libdir}/qml/org/kde/kalendar
%{_datadir}/metainfo/org.kde.kalendar.contact.appdata.xml
%{_datadir}/plasma/plasmoids/org.kde.kalendar.contact
%{_datadir}/qlogging-categories5/akonadi.quick.categories
%{_datadir}/qlogging-categories5/kalendar.contact.categories
