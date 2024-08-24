%define stable %(if [ "$(echo %{version} |cut -d. -f3)" -gt 50 ]; then echo -n "un"; fi; echo stable)
#define git 20230821

Name:		kirigami-addons
Version:	1.4.0
Release:	%{?git:0.%{git}.}1
Summary:	Add-on widgets for the Kirigami library
%if 0%{?git:1}
Source0:	https://invent.kde.org/libraries/kirigami-addons/-/archive/master/kirigami-addons-master.tar.bz2
%else
Source0:	https://download.kde.org/%{stable}/kirigami-addons/kirigami-addons-%{version}.tar.xz
%endif
License:	LGPLv2+
Group:		System/Libraries
BuildRequires:	cmake
BuildRequires:	ninja
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(Qt6)
BuildRequires:	cmake(Qt6Core)
BuildRequires:	cmake(Qt6DBus)
BuildRequires:	cmake(Qt6Gui)
BuildRequires:	cmake(Qt6Network)
BuildRequires:	cmake(Qt6Qml)
BuildRequires:	cmake(Qt6QmlModels)
BuildRequires:	cmake(Qt6Quick)
BuildRequires:	cmake(Qt6QuickControls2)
BuildRequires:	cmake(KF6Kirigami2)
BuildRequires:	cmake(KF6I18n)
BuildRequires:	cmake(KF6Config)
BuildRequires:	cmake(KF6CoreAddons)
BuildRequires:	cmake(KF6GuiAddons)
Suggests:	%{name}-translations = %{EVRD}
%rename %{name}-kde6
%rename kf6-kirigami-addons

%description
Add-on widgets for the Kirigami library.

%package devel
Summary:       Development files for %{name}
Group:         Development/KDE and Qt
Requires:      %{name} = %{EVRD}
%rename %{name}-kde6-devel
%rename kf6-kirigami-addons-devel

%description devel
This package contains header files needed if you wish to build
applications based on %{name}.

# Translations are shared with kirigami-addons-kde5
%package translations
Summary:	Translations for kirigami-addons
Group:		System/Libraries

%description translations
Translations for kirigami-addons

%prep
%autosetup -p1 -n %{name}-%{?git:master}%{!?git:%{version}}
%cmake \
	-DBUILD_QCH:BOOL=ON \
	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON \
	-G Ninja

%build
%ninja_build -C build

%install
%ninja_install -C build

%find_lang %{name}6

%files
%{_qtdir}/qml/org/kde/kirigamiaddons
%{_libdir}/libKirigamiAddonsStatefulApp.so*

%files translations -f %{name}6.lang

%files devel
%{_libdir}/cmake/KF6KirigamiAddons
%{_includedir}/KirigamiAddonsStatefulApp
%{_libdir}/libKirigamiAddonsStatefulApp.so
%{_datadir}/kdevappwizard/templates/kirigamiaddons6.tar.bz2
