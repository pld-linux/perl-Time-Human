#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%define	pdir	Time
%define	pnam	Human
Summary:	Convert localtime() format to "speaking clock" time
Summary(pl.UTF-8):	Konwersja localtime() do czasu w języku mówionym
Name:		perl-%{pdir}-%{pnam}
Version:	1.03
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Time/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	0e869154c54593305cb1366285c8cac5
URL:		http://search.cpan.org/dist/Time-Human/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module provides a "vague" rendering of the time into natural
language; it's originally intended for text-to-speech applications
and other speech-based interfaces. 

%description -l pl.UTF-8
Ten moduł udostępnia funkcję przekształcającą czas na język naturalny.
Oryginalnie została przeznaczona do aplikacji czytających tekst oraz
innych bazujących na mowie interfejsów.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

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
%doc Changes
%{perl_vendorlib}/Time/*
%{_mandir}/man3/*
