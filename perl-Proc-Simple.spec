%include	/usr/lib/rpm/macros.perl
%define	pdir	Proc
%define	pnam	Simple
Summary:	Proc-Simple perl module
Summary(pl):	Modu³ perla Proc-Simple
Name:		perl-Proc-Simple
Version:	1.19
Release:	4
License:	GPL
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
Patch0:		%{name}-paths.patch
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Proc-Simple - launch and control background processes.

%description -l pl
Proc-Simple - umo¿liwia uruchamianie i kontrolowanie procesów w tle.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}
%patch -p0

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz eg
%{perl_sitelib}/Proc/Simple.pm
%{perl_sitelib}/auto/Proc/Simple
%{_mandir}/man3/*
