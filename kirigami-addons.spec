#define git 20230812

%bcond_without kde5
%bcond_without kde6

Name:		kirigami-addons
Version:	0.10.0
Release:	%{?git:0.%{git}.}2
Summary:	Add-on widgets for the Kirigami library
%if 0%{?git:1}
Source0:	https://invent.kde.org/sredman/kirigami-addons/-/archive/master/kirigami-addons-master.tar.bz2
%else
Source0:	https://download.kde.org/stable/kirigami-addons/kirigami-addons-%{version}.tar.xz
%endif
Patch0:		kirigami-addons-qt-6.6.patch
License:	LGPLv2+
Group:		Applications/Productivity
BuildRequires:	cmake
BuildRequires:	ninja
BuildRequires:	cmake(ECM)
%if %{with kde5}
BuildRequires:	cmake(Qt5Core)
BuildRequires:	cmake(Qt5Gui)
BuildRequires:	cmake(Qt5Network)
BuildRequires:	cmake(Qt5Qml)
BuildRequires:	cmake(Qt5QmlModels)
BuildRequires:	cmake(Qt5Quick)
BuildRequires:	cmake(Qt5QuickControls2)
BuildRequires:	cmake(KF5Kirigami2)
BuildRequires:	cmake(KF5I18n)
%endif
%if %{with kde6}
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
%endif

%description
Add-on widgets for the Kirigami library.

%package devel
Summary:	Development files for %{name}
Group:		Development/KDE and Qt
Requires:	%{name} = %{EVRD}
%if %{with kde5}
Requires:	%{name}-kde5-devel
%endif
%if %{with kde6}
Requires:	%{name}-kde6-devel
%endif

%description devel
This package contains header files needed if you wish to build
applications based on %{name}.

%if %{with kde5}
%package kde5
Summary:	Kirigami addons for KDE 5.x
Group:		Graphical desktop/KDE
Requires:	%{name} = %{EVRD}

%description kde5
Kirigami addons for KDE 5.x

%package kde5-devel
Summary:	Development files for Kirigami addons for KDE 5.x
Group:		Development/KDE and Qt
Requires:	%{name}-kde5 = %{EVRD}

%description kde5-devel
Development files for Kirigami addons for KDE 5.x
%endif

%if %{with kde6}
%package kde6
Summary:	Kirigami addons for KDE 6.x
Group:		Graphical desktop/KDE
Requires:	%{name} = %{EVRD}
%rename kf6-kirigami-addons

%description kde6
Kirigami addons for KDE 6.x

%package kde6-devel
Summary:	Development files for Kirigami addons for KDE 6.x
Group:		Development/KDE and Qt
Requires:	%{name}-kde6 = %{EVRD}
%rename kf6-kirigami-addons-devel

%description kde6-devel
Development files for Kirigami addons for KDE 6.x
%endif

%prep
%autosetup -p1 -n %{name}-%{?git:master}%{!?git:%{version}}
%if %{with kde5}
CMAKE_BUILD_DIR=build-kde5 %cmake \
	-DBUILD_QCH:BOOL=ON \
	-DBUILD_WITH_QT6:BOOL=OFF \
	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON \
	-G Ninja
cd ..
%endif

%if %{with kde6}
CMAKE_BUILD_DIR=build-kde6 %cmake \
	-DBUILD_QCH:BOOL=ON \
	-DBUILD_WITH_QT6:BOOL=ON \
	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON \
	-G Ninja
%endif

%build
%if %{with kde5}
%ninja_build -C build-kde5
%endif

%if %{with kde6}
%ninja_build -C build-kde6
%endif

%install
%if %{with kde5}
%ninja_install -C build-kde5
%endif

%if %{with kde6}
%ninja_install -C build-kde6
%endif

%find_lang %{name}

%files -f %{name}.lang

%files devel

%if %{with kde5}
%files kde5
%{_libdir}/qt5/qml/org/kde/kirigamiaddons

%files kde5-devel
%{_libdir}/cmake/KF5KirigamiAddons
%endif

%if %{with kde6}
%files kde6
%{_qtdir}/qml/org/kde/kirigamiaddons

%files kde6-devel
%{_libdir}/cmake/KF6KirigamiAddons
%endif
