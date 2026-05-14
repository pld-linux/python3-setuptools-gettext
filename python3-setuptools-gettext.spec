#
# Conditional build:
%bcond_with	tests		# unit tests (needs translate-toolkit)

%define		module	setuptools_gettext
%define		egg_name	setuptools_gettext
%define		pypi_name	setuptools-gettext
Summary:	Setuptools plugin compiling .po into .mo at build time
Summary(pl.UTF-8):	Wtyczka setuptools kompilująca pliki .po do .mo na etapie budowania
Name:		python3-setuptools-gettext
Version:	0.1.16
Release:	1
License:	GPL v2+
Group:		Libraries/Python
Source0:	https://files.pythonhosted.org/packages/source/s/%{pypi_name}/%{module}-%{version}.tar.gz
# Source0-md5:	9b3da8a4f0b9bd52b4de84ae1b43e4eb
URL:		https://github.com/breezy-team/setuptools-gettext
BuildRequires:	python3-build
BuildRequires:	python3-installer
BuildRequires:	python3-modules >= 1:3.9
BuildRequires:	python3-setuptools >= 61.0
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 2.044
Requires:	gettext-tools
Requires:	python3-modules >= 1:3.9
Requires:	python3-setuptools >= 61.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
setuptools-gettext is a setuptools plugin that compiles gettext .po
files into .mo catalogs during the wheel-build step and ships the
resulting catalogs as package data. It registers distutils commands
(build_mo, clean_mo, install_mo, update_pot) and a
setuptools.finalize_distribution_options entry point so projects can
declare locale handling entirely in pyproject.toml.

%description -l pl.UTF-8
setuptools-gettext to wtyczka setuptools kompilująca pliki gettext .po
do katalogów .mo na etapie budowania paczki wheel i dołączająca je
jako dane pakietu. Rejestruje polecenia distutils (build_mo, clean_mo,
install_mo, update_pot) oraz punkt wejścia
setuptools.finalize_distribution_options, dzięki czemu obsługę
tłumaczeń projektu można opisać wyłącznie w pyproject.toml.

%prep
%setup -q -n %{module}-%{version}

%build
%py3_build_pyproject

%install
rm -rf $RPM_BUILD_ROOT
%py3_install_pyproject

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc COPYING README.md
%{py3_sitescriptdir}/%{module}
%{py3_sitescriptdir}/%{egg_name}-%{version}.dist-info
