#
# Conditional build:
%bcond_without	tests	# unit tests
#
%define		pdir	Authen
%define		pnam	SASL
Summary:	Authen::SASL Perl module - SASL authentication framework
Summary(pl.UTF-8):	Moduł Perla Authen::SASL - szkielet uwierzytelniania SASL
Name:		perl-Authen-SASL
Version:	2.2100
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	https://www.cpan.org/modules/by-authors/id/E/EH/EHUELS/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	4476f347a4ea45a7e0d3067da83ed29c
URL:		https://metacpan.org/dist/Authen-SASL
BuildRequires:	perl-ExtUtils-MakeMaker
BuildRequires:	perl-devel >= 1:5.14.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Crypt-URandom
BuildRequires:	perl-Digest-HMAC
BuildRequires:	perl-Digest-MD5
BuildRequires:	perl-GSSAPI
BuildRequires:	perl-Test-Pod >= 1.41
BuildRequires:	perl-Test-Pod-Coverage
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
SASL jest ogólnym mechanizmem uwierzytelniania wykorzystywanym przez
niektóre protokoły sieciowe. Authen::SASL udostępnia szkielet
implementacji, który powinien dawać możliwość współdzielenia go przez
wszystkie protokoły.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor

%{__make}

%if %{with tests}
%{__make} test
%endif

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
