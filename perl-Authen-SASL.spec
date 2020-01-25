#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%define		pdir	Authen
%define		pnam	SASL
Summary:	Authen::SASL Perl module - SASL authentication framework
Summary(pl.UTF-8):	Moduł Perla Authen::SASL - szkielet autentykacji SASL
Name:		perl-Authen-SASL
Version:	2.1600
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Authen/%{pdir}-%{pnam}-2.16.tar.gz
# Source0-md5:	7c03a689d4c689e5a9e2f18a1c586b2f
URL:		http://search.cpan.org/dist/Authen-SASL/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Digest-HMAC
BuildRequires:	perl-Digest-MD5
BuildRequires:	perl-GSSAPI
BuildRequires:	perl-Test-Simple
%endif
# earlier perl-ldap contain own Authen::SASL
Conflicts:	perl-ldap < 0.26
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
SASL is a generic mechanism for authentication used by several network
protocols. Authen::SASL provides an implementation framework that all
protocols should be able to share.

%description -l pl.UTF-8
SASL jest ogólnym mechanizmem autentykacji wykorzystywanym przez
niektóre protokoły sieciowe. Authen::SASL udostępnia szkielet
implementacji, który powinien dawać możliwość współdzielenia go przez
wszystkie protokoły.

%prep
%setup -q -n %{pdir}-%{pnam}-2.16

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}
%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{perl_vendorlib}/Authen/SASL.pod

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes api.txt
%{perl_vendorlib}/Authen/SASL.pm
%{perl_vendorlib}/Authen/SASL
%{_mandir}/man3/Authen::SASL*.3pm*
