
# Conditional build:
%bcond_without	tests	# do not perform "make test"

%include	/usr/lib/rpm/macros.perl
%define		pdir	Authen
%define		pnam	SASL
Summary:	Authen::PAM Perl module - SASL Authentication framework
Summary(pl):	Modu³ Perla Authen::SASL - szkielet autentykacji SASL
Name:		perl-Authen-SASL
Version:	2.06
Release:	1
Vendor:		Graham Barr <gbarr@pobox.com>
License:	GPL or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	d56d589137f7757cedc2a8cce704328c
Patch0:		%{name}-non_existent_man.patch
BuildRequires:	perl-devel >= 5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Digest-HMAC
%endif
# earlier perl-ldap contain own Authen::SASL
Conflicts:	perl-ldap < 0.26
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
SASL is a generic mechanism for authentication used by several network
protocols. Authen::SASL provides an implementation framework that all
protocols should be able to share.

%description -l pl
SASL jest ogólnym mechanizmem autentykacji wykorzystywanym przez
niektóre protoko³y sieciowe. Authen::SASL udostêpnia szkielet
implementacji, który powinien dawaæ mo¿liwo¶æ wspó³dzielenia go przez
wszystkie protoko³y.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}
%patch -p1

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}
%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog api.txt
%dir %{perl_vendorlib}/Authen/SASL
%{perl_vendorlib}/Authen/SASL.pm
%{perl_vendorlib}/Authen/SASL/*
%{_mandir}/man3/*
