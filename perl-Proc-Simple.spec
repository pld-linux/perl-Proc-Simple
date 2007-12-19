#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Proc
%define		pnam	Simple
Summary:	Proc::Simple Perl module - launch and control background processes
Summary(pl.UTF-8):	Moduł Perla Proc::Simple - uruchamianie i sterowanie procesami w tle
Name:		perl-Proc-Simple
Version:	1.22
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	2c7d98f9c0002b607e3ba504599aa69f
Patch0:		%{name}-paths.patch
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
%patch0 -p0

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
%dir %{perl_vendorlib}/auto/Proc
%dir %{perl_vendorlib}/auto/Proc/Simple
%{perl_vendorlib}/auto/Proc/Simple/autosplit.ix
%{_mandir}/man3/*
%dir %{_examplesdir}/%{name}-%{version}
%attr(755,root,root) %{_examplesdir}/%{name}-%{version}/*
