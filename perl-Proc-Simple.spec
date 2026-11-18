#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%define		pdir	Proc
%define		pnam	Simple
Summary:	Proc::Simple Perl module - launch and control background processes
Summary(pl.UTF-8):	Moduł Perla Proc::Simple - uruchamianie i sterowanie procesami w tle
Name:		perl-Proc-Simple
Version:	1.32
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	https://www.cpan.org/authors/id/M/MS/MSCHILLI/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	aa666815b9d9a86eff9e8a088fc30d1c
Patch0:		%{name}-paths.patch
URL:		http://search.cpan.org/dist/Proc-Simple/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Proc::Simple is the module to launch and control background processes.
It provides objects mimicing real-life processes from a user's point
of view.

%description -l pl.UTF-8
Proc::Simple to moduł umożliwiający uruchamianie i kontrolowanie
procesów w tle. Dostarcza obiekty naśladujące prawdziwe procesy z
punktu widzenia użytkownika.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}
%patch -P0 -p0

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT
cp -f eg/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%{perl_vendorlib}/Proc/Simple.pm
%{_mandir}/man3/*
%dir %{_examplesdir}/%{name}-%{version}
%attr(755,root,root) %{_examplesdir}/%{name}-%{version}/*
