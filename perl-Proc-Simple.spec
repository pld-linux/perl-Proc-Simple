%include	/usr/lib/rpm/macros.perl
Summary:	Proc-Simple perl module
Summary(pl):	Modu³ perla Proc-Simple
Name:		perl-Proc-Simple
Version:	1.14
Release:	1
License:	GPL
Group:		Development/Languages/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Source:		ftp://ftp.perl.org/pub/CPAN/modules/by-module/Proc/Proc-Simple-%{version}.tar.gz
Patch:		perl-Proc-Simple-paths.patch
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.005_03-14
%requires_eq	perl
Requires:	%{perl_sitearch}
BuildRoot:	/tmp/%{name}-%{version}-root

%description
Proc-Simple - launch and control background processes. 

%description -l pl
Proc-Simple - umo¿liwia uruchamianie i kontrolowanie procesów w tle.

%prep
%setup -q -n Proc-Simple-%{version}
%patch -p0

%build
perl Makefile.PL
make

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

(
  cd $RPM_BUILD_ROOT%{perl_sitearch}/auto/Proc/Simple
  sed -e "s#$RPM_BUILD_ROOT##" .packlist >.packlist.new
  mv .packlist.new .packlist
)

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man3/* \
        README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.gz eg

%{perl_sitelib}/Proc/Simple.pm
%{perl_sitelib}/auto/Proc/Simple
%{perl_sitearch}/auto/Proc/Simple

%{_mandir}/man3/*
