#
# Conditional build:
# _without_tests - do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Authen
%define		pnam	SASL
Summary:	Authen::PAM Perl module - SASL Authentication framework
Summary(pl):	Modu� Perla Authen::SASL - szkielet autentykacji SASL
Name:		perl-Authen-SASL
Version:	2.03
Release:	1
Vendor:		Graham Barr <gbarr@pobox.com>
License:	GPL or Artistic
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
Patch0:		%{name}-non_existent_man.patch
BuildRequires:	pam-devel
BuildRequires:	perl >= 5.6
BuildRequires:	rpm-perlprov >= 3.0.3-16
# earlier perl-ldap contain own Authen::SASL
Conflicts:	perl-ldap < 0.26
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
SASL is a generic mechanism for authentication used by several network
protocols. Authen::SASL provides an implementation framework that all
protocols should be able to share.

%description -l pl
SASL jest og�lnym mechanizmem autentykacji wykorzystywanym przez
niekt�re protoko�y sieciowe. Authen::SASL udost�pnia szkielet
implementacji, kt�ry powinien dawa� mo�liwo�� wsp�dzielenia go przez
wszystkie protoko�y.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}
%patch -p1

%build
perl Makefile.PL
%{__make}
%{!?_without_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog api.txt
%dir %{perl_sitelib}/Authen/SASL
%{perl_sitelib}/Authen/SASL.pm
%{perl_sitelib}/Authen/SASL/*
%{_mandir}/man3/*
