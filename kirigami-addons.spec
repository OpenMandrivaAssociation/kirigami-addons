%define snapshot 20200825
%define commit a445f089cbecdc257a3ec67ddcbeb88acdb83349

Name:		kirigami-addons
Version:	0.0
Release:	%{?snapshot:0.%{snapshot}.}1
Summary:	Add-on widgets for the Kirigami library
Source0:	https://invent.kde.org/sredman/kirigami-addons/-/archive/master/kirigami-addons-master.tar.bz2
License:	LGPLv2+
Group:		Applications/Productivity
BuildRequires:	cmake
BuildRequires:	ninja
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(Qt5Core)
BuildRequires:	cmake(Qt5Gui)
BuildRequires:	cmake(Qt5Network)
BuildRequires:	cmake(Qt5Qml)
BuildRequires:	cmake(Qt5QmlModels)
BuildRequires:	cmake(Qt5Quick)
BuildRequires:	cmake(Qt5QuickControls2)
BuildRequires:	cmake(KF5Kirigami2)
BuildRequires:	cmake(KF5I18n)

%description
Add-on widgets for the Kirigami library

%prep
%autosetup -p1 -n %{name}-master
%cmake_kde5 -G Ninja

%build
%ninja_build -C build

%install
%ninja_install -C build

%files
%{_libdir}/qt5/qml/org/kde/kirigamiaddons
