#define snapshot 20200825
#define commit a445f089cbecdc257a3ec67ddcbeb88acdb83349

Name:		kirigami-addons
Version:	0.7.2
Release:	%{?snapshot:0.%{snapshot}.}1
Summary:	Add-on widgets for the Kirigami library
%if 0%{?snapshot:1}
Source0:	https://invent.kde.org/sredman/kirigami-addons/-/archive/master/kirigami-addons-master.tar.bz2
%else
Source0:	https://download.kde.org/stable/kirigami-addons/kirigami-addons-%{version}.tar.xz
%endif
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
Add-on widgets for the Kirigami library.

%package devel
Summary:	Development files for %{name}
Group:		Development/KDE and Qt
Requires:	%{name} = %{EVRD}
Provides:	%{name}-devel = %{EVRD}

%description devel
This package contains header files needed if you wish to build
applications based on %{name}.

%prep
%autosetup -p1 -n %{name}-%{?snapshot:master}%{!?snapshot:%{version}}
%cmake_kde5 -G Ninja

%build
%ninja_build -C build

%install
%ninja_install -C build
%find_lang %{name}

%files -f %{name}.lang
%{_libdir}/qt5/qml/org/kde/kirigamiaddons

%files devel
%{_libdir}/cmake/KF5KirigamiAddons
