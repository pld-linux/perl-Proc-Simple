%include	/usr/lib/rpm/macros.perl
%define		pdir	Proc
%define		pnam	Simple
Summary:	Proc::Simple Perl module
Summary(cs):	Modul Proc::Simple pro Perl
Summary(da):	Perlmodul Proc::Simple
Summary(de):	Proc::Simple Perl Modul
Summary(es):	Módulo de Perl Proc::Simple
Summary(fr):	Module Perl Proc::Simple
Summary(it):	Modulo di Perl Proc::Simple
Summary(ja):	Proc::Simple Perl ¥â¥¸¥å¡¼¥ë
Summary(ko):	Proc::Simple ÆÞ ¸ðÁÙ
Summary(no):	Perlmodul Proc::Simple
Summary(pl):	Modu³ Perla Proc::Simple
Summary(pt):	Módulo de Perl Proc::Simple
Summary(pt_BR):	Módulo Perl Proc::Simple
Summary(ru):	íÏÄÕÌØ ÄÌÑ Perl Proc::Simple
Summary(sv):	Proc::Simple Perlmodul
Summary(uk):	íÏÄÕÌØ ÄÌÑ Perl Proc::Simple
Summary(zh_CN):	Proc::Simple Perl Ä£¿é
Name:		perl-Proc-Simple
Version:	1.19
Release:	6
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
Patch0:		%{name}-paths.patch
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Proc::Simple - launch and control background processes.

%description -l pl
Proc::Simple - umo¿liwia uruchamianie i kontrolowanie procesów w tle.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}
%patch -p0

%build
%{__perl} Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__make} install DESTDIR=$RPM_BUILD_ROOT

cp -f eg/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%{perl_sitelib}/Proc/Simple.pm
%dir %{perl_sitelib}/auto/Proc
%dir %{perl_sitelib}/auto/Proc/Simple
%{perl_sitelib}/auto/Proc/Simple/autosplit.ix
%{_mandir}/man3/*
%dir %{_examplesdir}/%{name}-%{version}
%attr(755,root,root) %{_examplesdir}/%{name}-%{version}/*
