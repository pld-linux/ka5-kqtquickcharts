#
# Conditional build:
%bcond_with	tests		# build with tests
%define		kdeappsver	22.08.2
%define		kframever	5.94.0
%define		qtver		5.15.2
%define		kaname		kqtquickcharts
Summary:	kqtquickcharts
Name:		ka5-%{kaname}
Version:	22.08.2
Release:	1
License:	GPL v2+/LGPL v2.1+
Group:		X11/Applications
Source0:	https://download.kde.org/stable/release-service/%{kdeappsver}/src/%{kaname}-%{version}.tar.xz
# Source0-md5:	9bdb65bf9bd40fcf7b8b74024446997e
URL:		http://www.kde.org/
BuildRequires:	Qt5Core-devel >= %{qtver}
BuildRequires:	Qt5Gui-devel
BuildRequires:	Qt5Network-devel >= 5.11.1
BuildRequires:	Qt5Qml-devel
BuildRequires:	Qt5Quick-devel
BuildRequires:	cmake >= 2.8.12
BuildRequires:	kf5-extra-cmake-modules >= %{kframever}
BuildRequires:	ninja
BuildRequires:	qt5-build >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.164
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Qt Quick plugin for beautiful and interactive charts.

%description -l pl.UTF-8
Wtyczka do Qt Quick do tworzenia pięknych i interaktywnych wykresów.

%package devel
Summary:	Header files for %{kaname} development
Summary(pl.UTF-8):	Pliki nagłówkowe dla programistów używających %{kaname}
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for %{kaname} development.

%description devel -l pl.UTF-8
Pliki nagłówkowe dla programistów używających %{kaname}.

%prep
%setup -q -n %{kaname}-%{version}

%build
install -d build
cd build
%cmake \
	-G Ninja \
	%{!?with_tests:-DBUILD_TESTING=OFF} \
	-DHTML_INSTALL_DIR=%{_kdedocdir} \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
	..
%ninja_build

%if %{with tests}
ctest
%endif


%install
rm -rf $RPM_BUILD_ROOT
%ninja_install -C build

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%dir %{_libdir}/qt5/qml/org/kde/charts
%{_libdir}/qt5/qml/org/kde/charts/BarChart.qml
%{_libdir}/qt5/qml/org/kde/charts/Label.qml
%{_libdir}/qt5/qml/org/kde/charts/LegendItem.qml
%{_libdir}/qt5/qml/org/kde/charts/LineChart.qml
%{_libdir}/qt5/qml/org/kde/charts/LineLabel.qml
%{_libdir}/qt5/qml/org/kde/charts/XYChart.qml
%attr(755,root,root) %{_libdir}/qt5/qml/org/kde/charts/libkqtquickcharts.so
%{_libdir}/qt5/qml/org/kde/charts/qmldir

%files devel
%defattr(644,root,root,755)
%{_includedir}/KF5/kqtquickcharts_version.h
%{_libdir}/cmake/KQtQuickCharts
